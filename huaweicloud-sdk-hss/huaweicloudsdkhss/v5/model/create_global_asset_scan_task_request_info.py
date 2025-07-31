# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalAssetScanTaskRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_ids': 'list[str]',
        'server_group': 'list[str]',
        'all_hosts': 'bool'
    }

    attribute_map = {
        'host_ids': 'host_ids',
        'server_group': 'server_group',
        'all_hosts': 'all_hosts'
    }

    def __init__(self, host_ids=None, server_group=None, all_hosts=None):
        r"""CreateGlobalAssetScanTaskRequestInfo

        The model defined in huaweicloud sdk

        :param host_ids: 下发任务的主机列表
        :type host_ids: list[str]
        :param server_group: 下发任务的主机组列表
        :type server_group: list[str]
        :param all_hosts: 下发全部主机的扫描
        :type all_hosts: bool
        """
        
        

        self._host_ids = None
        self._server_group = None
        self._all_hosts = None
        self.discriminator = None

        if host_ids is not None:
            self.host_ids = host_ids
        if server_group is not None:
            self.server_group = server_group
        self.all_hosts = all_hosts

    @property
    def host_ids(self):
        r"""Gets the host_ids of this CreateGlobalAssetScanTaskRequestInfo.

        下发任务的主机列表

        :return: The host_ids of this CreateGlobalAssetScanTaskRequestInfo.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this CreateGlobalAssetScanTaskRequestInfo.

        下发任务的主机列表

        :param host_ids: The host_ids of this CreateGlobalAssetScanTaskRequestInfo.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def server_group(self):
        r"""Gets the server_group of this CreateGlobalAssetScanTaskRequestInfo.

        下发任务的主机组列表

        :return: The server_group of this CreateGlobalAssetScanTaskRequestInfo.
        :rtype: list[str]
        """
        return self._server_group

    @server_group.setter
    def server_group(self, server_group):
        r"""Sets the server_group of this CreateGlobalAssetScanTaskRequestInfo.

        下发任务的主机组列表

        :param server_group: The server_group of this CreateGlobalAssetScanTaskRequestInfo.
        :type server_group: list[str]
        """
        self._server_group = server_group

    @property
    def all_hosts(self):
        r"""Gets the all_hosts of this CreateGlobalAssetScanTaskRequestInfo.

        下发全部主机的扫描

        :return: The all_hosts of this CreateGlobalAssetScanTaskRequestInfo.
        :rtype: bool
        """
        return self._all_hosts

    @all_hosts.setter
    def all_hosts(self, all_hosts):
        r"""Sets the all_hosts of this CreateGlobalAssetScanTaskRequestInfo.

        下发全部主机的扫描

        :param all_hosts: The all_hosts of this CreateGlobalAssetScanTaskRequestInfo.
        :type all_hosts: bool
        """
        self._all_hosts = all_hosts

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
        if not isinstance(other, CreateGlobalAssetScanTaskRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
