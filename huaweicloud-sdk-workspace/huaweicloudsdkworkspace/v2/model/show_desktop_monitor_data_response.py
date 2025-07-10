# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDesktopMonitorDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_online_info': 'list[MonitorUserOnlineInfo]',
        'online_status': 'int',
        'cpu_info': 'list[Datapoints]',
        'memory_info': 'list[Datapoints]',
        'disk_util_inband': 'list[Datapoints]',
        'disk_read_bytes_rate': 'list[Datapoints]',
        'disk_write_bytes_rate': 'list[Datapoints]',
        'disk_read_requests_rate': 'list[Datapoints]',
        'disk_write_requests_rate': 'list[Datapoints]',
        'network_incoming_bytes_rate_inband': 'list[Datapoints]',
        'network_outgoing_bytes_rate_inband': 'list[Datapoints]',
        'network_incoming_bytes_aggregate_rate': 'list[Datapoints]',
        'network_outgoing_bytes_aggregate_rate': 'list[Datapoints]',
        'network_vm_connections': 'list[Datapoints]'
    }

    attribute_map = {
        'user_online_info': 'user_online_info',
        'online_status': 'online_status',
        'cpu_info': 'cpu_info',
        'memory_info': 'memory_info',
        'disk_util_inband': 'disk_util_inband',
        'disk_read_bytes_rate': 'disk_read_bytes_rate',
        'disk_write_bytes_rate': 'disk_write_bytes_rate',
        'disk_read_requests_rate': 'disk_read_requests_rate',
        'disk_write_requests_rate': 'disk_write_requests_rate',
        'network_incoming_bytes_rate_inband': 'network_incoming_bytes_rate_inband',
        'network_outgoing_bytes_rate_inband': 'network_outgoing_bytes_rate_inband',
        'network_incoming_bytes_aggregate_rate': 'network_incoming_bytes_aggregate_rate',
        'network_outgoing_bytes_aggregate_rate': 'network_outgoing_bytes_aggregate_rate',
        'network_vm_connections': 'network_vm_connections'
    }

    def __init__(self, user_online_info=None, online_status=None, cpu_info=None, memory_info=None, disk_util_inband=None, disk_read_bytes_rate=None, disk_write_bytes_rate=None, disk_read_requests_rate=None, disk_write_requests_rate=None, network_incoming_bytes_rate_inband=None, network_outgoing_bytes_rate_inband=None, network_incoming_bytes_aggregate_rate=None, network_outgoing_bytes_aggregate_rate=None, network_vm_connections=None):
        r"""ShowDesktopMonitorDataResponse

        The model defined in huaweicloud sdk

        :param user_online_info: 在线信息。
        :type user_online_info: list[:class:`huaweicloudsdkworkspace.v2.MonitorUserOnlineInfo`]
        :param online_status: 计算机登录状态，在线信息没值的情况下，查看计算机登录状态 0 未登录， 1 登录中, 2登录状态同当前。
        :type online_status: int
        :param cpu_info: cpu使用率信息。
        :type cpu_info: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param memory_info: 内存使用率信息。
        :type memory_info: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param disk_util_inband: 磁盘使用率。
        :type disk_util_inband: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param disk_read_bytes_rate: 磁盘读带宽。
        :type disk_read_bytes_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param disk_write_bytes_rate: 磁盘写带宽。
        :type disk_write_bytes_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param disk_read_requests_rate: 磁盘读IOPS。
        :type disk_read_requests_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param disk_write_requests_rate: 磁盘写IOPS。
        :type disk_write_requests_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param network_incoming_bytes_rate_inband: 带内网络流入速率。
        :type network_incoming_bytes_rate_inband: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param network_outgoing_bytes_rate_inband: 带内网络流出速率。
        :type network_outgoing_bytes_rate_inband: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param network_incoming_bytes_aggregate_rate: 带外网络流入速率。
        :type network_incoming_bytes_aggregate_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param network_outgoing_bytes_aggregate_rate: 带外网络流出速率。
        :type network_outgoing_bytes_aggregate_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        :param network_vm_connections: 网络连接数。
        :type network_vm_connections: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        
        super(ShowDesktopMonitorDataResponse, self).__init__()

        self._user_online_info = None
        self._online_status = None
        self._cpu_info = None
        self._memory_info = None
        self._disk_util_inband = None
        self._disk_read_bytes_rate = None
        self._disk_write_bytes_rate = None
        self._disk_read_requests_rate = None
        self._disk_write_requests_rate = None
        self._network_incoming_bytes_rate_inband = None
        self._network_outgoing_bytes_rate_inband = None
        self._network_incoming_bytes_aggregate_rate = None
        self._network_outgoing_bytes_aggregate_rate = None
        self._network_vm_connections = None
        self.discriminator = None

        if user_online_info is not None:
            self.user_online_info = user_online_info
        if online_status is not None:
            self.online_status = online_status
        if cpu_info is not None:
            self.cpu_info = cpu_info
        if memory_info is not None:
            self.memory_info = memory_info
        if disk_util_inband is not None:
            self.disk_util_inband = disk_util_inband
        if disk_read_bytes_rate is not None:
            self.disk_read_bytes_rate = disk_read_bytes_rate
        if disk_write_bytes_rate is not None:
            self.disk_write_bytes_rate = disk_write_bytes_rate
        if disk_read_requests_rate is not None:
            self.disk_read_requests_rate = disk_read_requests_rate
        if disk_write_requests_rate is not None:
            self.disk_write_requests_rate = disk_write_requests_rate
        if network_incoming_bytes_rate_inband is not None:
            self.network_incoming_bytes_rate_inband = network_incoming_bytes_rate_inband
        if network_outgoing_bytes_rate_inband is not None:
            self.network_outgoing_bytes_rate_inband = network_outgoing_bytes_rate_inband
        if network_incoming_bytes_aggregate_rate is not None:
            self.network_incoming_bytes_aggregate_rate = network_incoming_bytes_aggregate_rate
        if network_outgoing_bytes_aggregate_rate is not None:
            self.network_outgoing_bytes_aggregate_rate = network_outgoing_bytes_aggregate_rate
        if network_vm_connections is not None:
            self.network_vm_connections = network_vm_connections

    @property
    def user_online_info(self):
        r"""Gets the user_online_info of this ShowDesktopMonitorDataResponse.

        在线信息。

        :return: The user_online_info of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.MonitorUserOnlineInfo`]
        """
        return self._user_online_info

    @user_online_info.setter
    def user_online_info(self, user_online_info):
        r"""Sets the user_online_info of this ShowDesktopMonitorDataResponse.

        在线信息。

        :param user_online_info: The user_online_info of this ShowDesktopMonitorDataResponse.
        :type user_online_info: list[:class:`huaweicloudsdkworkspace.v2.MonitorUserOnlineInfo`]
        """
        self._user_online_info = user_online_info

    @property
    def online_status(self):
        r"""Gets the online_status of this ShowDesktopMonitorDataResponse.

        计算机登录状态，在线信息没值的情况下，查看计算机登录状态 0 未登录， 1 登录中, 2登录状态同当前。

        :return: The online_status of this ShowDesktopMonitorDataResponse.
        :rtype: int
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        r"""Sets the online_status of this ShowDesktopMonitorDataResponse.

        计算机登录状态，在线信息没值的情况下，查看计算机登录状态 0 未登录， 1 登录中, 2登录状态同当前。

        :param online_status: The online_status of this ShowDesktopMonitorDataResponse.
        :type online_status: int
        """
        self._online_status = online_status

    @property
    def cpu_info(self):
        r"""Gets the cpu_info of this ShowDesktopMonitorDataResponse.

        cpu使用率信息。

        :return: The cpu_info of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._cpu_info

    @cpu_info.setter
    def cpu_info(self, cpu_info):
        r"""Sets the cpu_info of this ShowDesktopMonitorDataResponse.

        cpu使用率信息。

        :param cpu_info: The cpu_info of this ShowDesktopMonitorDataResponse.
        :type cpu_info: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._cpu_info = cpu_info

    @property
    def memory_info(self):
        r"""Gets the memory_info of this ShowDesktopMonitorDataResponse.

        内存使用率信息。

        :return: The memory_info of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._memory_info

    @memory_info.setter
    def memory_info(self, memory_info):
        r"""Sets the memory_info of this ShowDesktopMonitorDataResponse.

        内存使用率信息。

        :param memory_info: The memory_info of this ShowDesktopMonitorDataResponse.
        :type memory_info: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._memory_info = memory_info

    @property
    def disk_util_inband(self):
        r"""Gets the disk_util_inband of this ShowDesktopMonitorDataResponse.

        磁盘使用率。

        :return: The disk_util_inband of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._disk_util_inband

    @disk_util_inband.setter
    def disk_util_inband(self, disk_util_inband):
        r"""Sets the disk_util_inband of this ShowDesktopMonitorDataResponse.

        磁盘使用率。

        :param disk_util_inband: The disk_util_inband of this ShowDesktopMonitorDataResponse.
        :type disk_util_inband: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._disk_util_inband = disk_util_inband

    @property
    def disk_read_bytes_rate(self):
        r"""Gets the disk_read_bytes_rate of this ShowDesktopMonitorDataResponse.

        磁盘读带宽。

        :return: The disk_read_bytes_rate of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._disk_read_bytes_rate

    @disk_read_bytes_rate.setter
    def disk_read_bytes_rate(self, disk_read_bytes_rate):
        r"""Sets the disk_read_bytes_rate of this ShowDesktopMonitorDataResponse.

        磁盘读带宽。

        :param disk_read_bytes_rate: The disk_read_bytes_rate of this ShowDesktopMonitorDataResponse.
        :type disk_read_bytes_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._disk_read_bytes_rate = disk_read_bytes_rate

    @property
    def disk_write_bytes_rate(self):
        r"""Gets the disk_write_bytes_rate of this ShowDesktopMonitorDataResponse.

        磁盘写带宽。

        :return: The disk_write_bytes_rate of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._disk_write_bytes_rate

    @disk_write_bytes_rate.setter
    def disk_write_bytes_rate(self, disk_write_bytes_rate):
        r"""Sets the disk_write_bytes_rate of this ShowDesktopMonitorDataResponse.

        磁盘写带宽。

        :param disk_write_bytes_rate: The disk_write_bytes_rate of this ShowDesktopMonitorDataResponse.
        :type disk_write_bytes_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._disk_write_bytes_rate = disk_write_bytes_rate

    @property
    def disk_read_requests_rate(self):
        r"""Gets the disk_read_requests_rate of this ShowDesktopMonitorDataResponse.

        磁盘读IOPS。

        :return: The disk_read_requests_rate of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._disk_read_requests_rate

    @disk_read_requests_rate.setter
    def disk_read_requests_rate(self, disk_read_requests_rate):
        r"""Sets the disk_read_requests_rate of this ShowDesktopMonitorDataResponse.

        磁盘读IOPS。

        :param disk_read_requests_rate: The disk_read_requests_rate of this ShowDesktopMonitorDataResponse.
        :type disk_read_requests_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._disk_read_requests_rate = disk_read_requests_rate

    @property
    def disk_write_requests_rate(self):
        r"""Gets the disk_write_requests_rate of this ShowDesktopMonitorDataResponse.

        磁盘写IOPS。

        :return: The disk_write_requests_rate of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._disk_write_requests_rate

    @disk_write_requests_rate.setter
    def disk_write_requests_rate(self, disk_write_requests_rate):
        r"""Sets the disk_write_requests_rate of this ShowDesktopMonitorDataResponse.

        磁盘写IOPS。

        :param disk_write_requests_rate: The disk_write_requests_rate of this ShowDesktopMonitorDataResponse.
        :type disk_write_requests_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._disk_write_requests_rate = disk_write_requests_rate

    @property
    def network_incoming_bytes_rate_inband(self):
        r"""Gets the network_incoming_bytes_rate_inband of this ShowDesktopMonitorDataResponse.

        带内网络流入速率。

        :return: The network_incoming_bytes_rate_inband of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._network_incoming_bytes_rate_inband

    @network_incoming_bytes_rate_inband.setter
    def network_incoming_bytes_rate_inband(self, network_incoming_bytes_rate_inband):
        r"""Sets the network_incoming_bytes_rate_inband of this ShowDesktopMonitorDataResponse.

        带内网络流入速率。

        :param network_incoming_bytes_rate_inband: The network_incoming_bytes_rate_inband of this ShowDesktopMonitorDataResponse.
        :type network_incoming_bytes_rate_inband: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._network_incoming_bytes_rate_inband = network_incoming_bytes_rate_inband

    @property
    def network_outgoing_bytes_rate_inband(self):
        r"""Gets the network_outgoing_bytes_rate_inband of this ShowDesktopMonitorDataResponse.

        带内网络流出速率。

        :return: The network_outgoing_bytes_rate_inband of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._network_outgoing_bytes_rate_inband

    @network_outgoing_bytes_rate_inband.setter
    def network_outgoing_bytes_rate_inband(self, network_outgoing_bytes_rate_inband):
        r"""Sets the network_outgoing_bytes_rate_inband of this ShowDesktopMonitorDataResponse.

        带内网络流出速率。

        :param network_outgoing_bytes_rate_inband: The network_outgoing_bytes_rate_inband of this ShowDesktopMonitorDataResponse.
        :type network_outgoing_bytes_rate_inband: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._network_outgoing_bytes_rate_inband = network_outgoing_bytes_rate_inband

    @property
    def network_incoming_bytes_aggregate_rate(self):
        r"""Gets the network_incoming_bytes_aggregate_rate of this ShowDesktopMonitorDataResponse.

        带外网络流入速率。

        :return: The network_incoming_bytes_aggregate_rate of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._network_incoming_bytes_aggregate_rate

    @network_incoming_bytes_aggregate_rate.setter
    def network_incoming_bytes_aggregate_rate(self, network_incoming_bytes_aggregate_rate):
        r"""Sets the network_incoming_bytes_aggregate_rate of this ShowDesktopMonitorDataResponse.

        带外网络流入速率。

        :param network_incoming_bytes_aggregate_rate: The network_incoming_bytes_aggregate_rate of this ShowDesktopMonitorDataResponse.
        :type network_incoming_bytes_aggregate_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._network_incoming_bytes_aggregate_rate = network_incoming_bytes_aggregate_rate

    @property
    def network_outgoing_bytes_aggregate_rate(self):
        r"""Gets the network_outgoing_bytes_aggregate_rate of this ShowDesktopMonitorDataResponse.

        带外网络流出速率。

        :return: The network_outgoing_bytes_aggregate_rate of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._network_outgoing_bytes_aggregate_rate

    @network_outgoing_bytes_aggregate_rate.setter
    def network_outgoing_bytes_aggregate_rate(self, network_outgoing_bytes_aggregate_rate):
        r"""Sets the network_outgoing_bytes_aggregate_rate of this ShowDesktopMonitorDataResponse.

        带外网络流出速率。

        :param network_outgoing_bytes_aggregate_rate: The network_outgoing_bytes_aggregate_rate of this ShowDesktopMonitorDataResponse.
        :type network_outgoing_bytes_aggregate_rate: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._network_outgoing_bytes_aggregate_rate = network_outgoing_bytes_aggregate_rate

    @property
    def network_vm_connections(self):
        r"""Gets the network_vm_connections of this ShowDesktopMonitorDataResponse.

        网络连接数。

        :return: The network_vm_connections of this ShowDesktopMonitorDataResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        return self._network_vm_connections

    @network_vm_connections.setter
    def network_vm_connections(self, network_vm_connections):
        r"""Sets the network_vm_connections of this ShowDesktopMonitorDataResponse.

        网络连接数。

        :param network_vm_connections: The network_vm_connections of this ShowDesktopMonitorDataResponse.
        :type network_vm_connections: list[:class:`huaweicloudsdkworkspace.v2.Datapoints`]
        """
        self._network_vm_connections = network_vm_connections

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
        if not isinstance(other, ShowDesktopMonitorDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
