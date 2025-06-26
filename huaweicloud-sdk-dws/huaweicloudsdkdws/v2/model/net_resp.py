# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virtual_cluster_id': 'int',
        'ctime': 'int',
        'host_id': 'int',
        'host_name': 'str',
        'instance_name': 'str',
        'up': 'bool',
        'speed': 'int',
        'recv_packets': 'int',
        'send_packets': 'int',
        'recv_drop': 'int',
        'recv_rate': 'float',
        'send_rate': 'float',
        'io_rate': 'float',
        'interface_name': 'str'
    }

    attribute_map = {
        'virtual_cluster_id': 'virtual_cluster_id',
        'ctime': 'ctime',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'instance_name': 'instance_name',
        'up': 'up',
        'speed': 'speed',
        'recv_packets': 'recv_packets',
        'send_packets': 'send_packets',
        'recv_drop': 'recv_drop',
        'recv_rate': 'recv_rate',
        'send_rate': 'send_rate',
        'io_rate': 'io_rate',
        'interface_name': 'interface_name'
    }

    def __init__(self, virtual_cluster_id=None, ctime=None, host_id=None, host_name=None, instance_name=None, up=None, speed=None, recv_packets=None, send_packets=None, recv_drop=None, recv_rate=None, send_rate=None, io_rate=None, interface_name=None):
        r"""NetResp

        The model defined in huaweicloud sdk

        :param virtual_cluster_id: **参数解释**： 虚拟集群ID。 **取值范围**： 不涉及。
        :type virtual_cluster_id: int
        :param ctime: **参数解释**： 查询时间。 **取值范围**： 不涉及。
        :type ctime: int
        :param host_id: **参数解释**： 主机ID。 **取值范围**： 不涉及。
        :type host_id: int
        :param host_name: **参数解释**： 主机名称。 **取值范围**： 不涉及。
        :type host_name: str
        :param instance_name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type instance_name: str
        :param up: **参数解释**： 网卡状态。 **取值范围**： true：代表up。 false：代表down。
        :type up: bool
        :param speed: **参数解释**： 网卡速度(Mbps)。 **取值范围**： 不涉及。
        :type speed: int
        :param recv_packets: **参数解释**： 接收包数(个)。 **取值范围**： 不涉及。
        :type recv_packets: int
        :param send_packets: **参数解释**： 发送包数(个)。 **取值范围**： 不涉及。
        :type send_packets: int
        :param recv_drop: **参数解释**： 接收丢包数(个)。 **取值范围**： 不涉及。
        :type recv_drop: int
        :param recv_rate: **参数解释**： 接收速率(KB/s)。 **取值范围**： 不涉及。
        :type recv_rate: float
        :param send_rate: **参数解释**： 发送速率(KB/s)。 **取值范围**： 不涉及。
        :type send_rate: float
        :param io_rate: **参数解释**： 网络速率(KB/s)。 **取值范围**： 不涉及。
        :type io_rate: float
        :param interface_name: **参数解释**： 网卡名称。 **取值范围**： 不涉及。
        :type interface_name: str
        """
        
        

        self._virtual_cluster_id = None
        self._ctime = None
        self._host_id = None
        self._host_name = None
        self._instance_name = None
        self._up = None
        self._speed = None
        self._recv_packets = None
        self._send_packets = None
        self._recv_drop = None
        self._recv_rate = None
        self._send_rate = None
        self._io_rate = None
        self._interface_name = None
        self.discriminator = None

        if virtual_cluster_id is not None:
            self.virtual_cluster_id = virtual_cluster_id
        if ctime is not None:
            self.ctime = ctime
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if instance_name is not None:
            self.instance_name = instance_name
        if up is not None:
            self.up = up
        if speed is not None:
            self.speed = speed
        if recv_packets is not None:
            self.recv_packets = recv_packets
        if send_packets is not None:
            self.send_packets = send_packets
        if recv_drop is not None:
            self.recv_drop = recv_drop
        if recv_rate is not None:
            self.recv_rate = recv_rate
        if send_rate is not None:
            self.send_rate = send_rate
        if io_rate is not None:
            self.io_rate = io_rate
        if interface_name is not None:
            self.interface_name = interface_name

    @property
    def virtual_cluster_id(self):
        r"""Gets the virtual_cluster_id of this NetResp.

        **参数解释**： 虚拟集群ID。 **取值范围**： 不涉及。

        :return: The virtual_cluster_id of this NetResp.
        :rtype: int
        """
        return self._virtual_cluster_id

    @virtual_cluster_id.setter
    def virtual_cluster_id(self, virtual_cluster_id):
        r"""Sets the virtual_cluster_id of this NetResp.

        **参数解释**： 虚拟集群ID。 **取值范围**： 不涉及。

        :param virtual_cluster_id: The virtual_cluster_id of this NetResp.
        :type virtual_cluster_id: int
        """
        self._virtual_cluster_id = virtual_cluster_id

    @property
    def ctime(self):
        r"""Gets the ctime of this NetResp.

        **参数解释**： 查询时间。 **取值范围**： 不涉及。

        :return: The ctime of this NetResp.
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        r"""Sets the ctime of this NetResp.

        **参数解释**： 查询时间。 **取值范围**： 不涉及。

        :param ctime: The ctime of this NetResp.
        :type ctime: int
        """
        self._ctime = ctime

    @property
    def host_id(self):
        r"""Gets the host_id of this NetResp.

        **参数解释**： 主机ID。 **取值范围**： 不涉及。

        :return: The host_id of this NetResp.
        :rtype: int
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this NetResp.

        **参数解释**： 主机ID。 **取值范围**： 不涉及。

        :param host_id: The host_id of this NetResp.
        :type host_id: int
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this NetResp.

        **参数解释**： 主机名称。 **取值范围**： 不涉及。

        :return: The host_name of this NetResp.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this NetResp.

        **参数解释**： 主机名称。 **取值范围**： 不涉及。

        :param host_name: The host_name of this NetResp.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def instance_name(self):
        r"""Gets the instance_name of this NetResp.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The instance_name of this NetResp.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this NetResp.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param instance_name: The instance_name of this NetResp.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def up(self):
        r"""Gets the up of this NetResp.

        **参数解释**： 网卡状态。 **取值范围**： true：代表up。 false：代表down。

        :return: The up of this NetResp.
        :rtype: bool
        """
        return self._up

    @up.setter
    def up(self, up):
        r"""Sets the up of this NetResp.

        **参数解释**： 网卡状态。 **取值范围**： true：代表up。 false：代表down。

        :param up: The up of this NetResp.
        :type up: bool
        """
        self._up = up

    @property
    def speed(self):
        r"""Gets the speed of this NetResp.

        **参数解释**： 网卡速度(Mbps)。 **取值范围**： 不涉及。

        :return: The speed of this NetResp.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this NetResp.

        **参数解释**： 网卡速度(Mbps)。 **取值范围**： 不涉及。

        :param speed: The speed of this NetResp.
        :type speed: int
        """
        self._speed = speed

    @property
    def recv_packets(self):
        r"""Gets the recv_packets of this NetResp.

        **参数解释**： 接收包数(个)。 **取值范围**： 不涉及。

        :return: The recv_packets of this NetResp.
        :rtype: int
        """
        return self._recv_packets

    @recv_packets.setter
    def recv_packets(self, recv_packets):
        r"""Sets the recv_packets of this NetResp.

        **参数解释**： 接收包数(个)。 **取值范围**： 不涉及。

        :param recv_packets: The recv_packets of this NetResp.
        :type recv_packets: int
        """
        self._recv_packets = recv_packets

    @property
    def send_packets(self):
        r"""Gets the send_packets of this NetResp.

        **参数解释**： 发送包数(个)。 **取值范围**： 不涉及。

        :return: The send_packets of this NetResp.
        :rtype: int
        """
        return self._send_packets

    @send_packets.setter
    def send_packets(self, send_packets):
        r"""Sets the send_packets of this NetResp.

        **参数解释**： 发送包数(个)。 **取值范围**： 不涉及。

        :param send_packets: The send_packets of this NetResp.
        :type send_packets: int
        """
        self._send_packets = send_packets

    @property
    def recv_drop(self):
        r"""Gets the recv_drop of this NetResp.

        **参数解释**： 接收丢包数(个)。 **取值范围**： 不涉及。

        :return: The recv_drop of this NetResp.
        :rtype: int
        """
        return self._recv_drop

    @recv_drop.setter
    def recv_drop(self, recv_drop):
        r"""Sets the recv_drop of this NetResp.

        **参数解释**： 接收丢包数(个)。 **取值范围**： 不涉及。

        :param recv_drop: The recv_drop of this NetResp.
        :type recv_drop: int
        """
        self._recv_drop = recv_drop

    @property
    def recv_rate(self):
        r"""Gets the recv_rate of this NetResp.

        **参数解释**： 接收速率(KB/s)。 **取值范围**： 不涉及。

        :return: The recv_rate of this NetResp.
        :rtype: float
        """
        return self._recv_rate

    @recv_rate.setter
    def recv_rate(self, recv_rate):
        r"""Sets the recv_rate of this NetResp.

        **参数解释**： 接收速率(KB/s)。 **取值范围**： 不涉及。

        :param recv_rate: The recv_rate of this NetResp.
        :type recv_rate: float
        """
        self._recv_rate = recv_rate

    @property
    def send_rate(self):
        r"""Gets the send_rate of this NetResp.

        **参数解释**： 发送速率(KB/s)。 **取值范围**： 不涉及。

        :return: The send_rate of this NetResp.
        :rtype: float
        """
        return self._send_rate

    @send_rate.setter
    def send_rate(self, send_rate):
        r"""Sets the send_rate of this NetResp.

        **参数解释**： 发送速率(KB/s)。 **取值范围**： 不涉及。

        :param send_rate: The send_rate of this NetResp.
        :type send_rate: float
        """
        self._send_rate = send_rate

    @property
    def io_rate(self):
        r"""Gets the io_rate of this NetResp.

        **参数解释**： 网络速率(KB/s)。 **取值范围**： 不涉及。

        :return: The io_rate of this NetResp.
        :rtype: float
        """
        return self._io_rate

    @io_rate.setter
    def io_rate(self, io_rate):
        r"""Sets the io_rate of this NetResp.

        **参数解释**： 网络速率(KB/s)。 **取值范围**： 不涉及。

        :param io_rate: The io_rate of this NetResp.
        :type io_rate: float
        """
        self._io_rate = io_rate

    @property
    def interface_name(self):
        r"""Gets the interface_name of this NetResp.

        **参数解释**： 网卡名称。 **取值范围**： 不涉及。

        :return: The interface_name of this NetResp.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        r"""Sets the interface_name of this NetResp.

        **参数解释**： 网卡名称。 **取值范围**： 不涉及。

        :param interface_name: The interface_name of this NetResp.
        :type interface_name: str
        """
        self._interface_name = interface_name

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
        if not isinstance(other, NetResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
