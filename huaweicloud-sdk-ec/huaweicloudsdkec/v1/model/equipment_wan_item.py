# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EquipmentWanItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interface_name': 'str',
        'ip_type': 'str',
        'ip_address': 'str',
        'gateway_ip_address': 'str',
        'uplink_bandwidth_size': 'int',
        'priority': 'str',
        'nat_outbound': 'bool',
        'tunnel_bandwidth_size': 'int'
    }

    attribute_map = {
        'interface_name': 'interface_name',
        'ip_type': 'ip_type',
        'ip_address': 'ip_address',
        'gateway_ip_address': 'gateway_ip_address',
        'uplink_bandwidth_size': 'uplink_bandwidth_size',
        'priority': 'priority',
        'nat_outbound': 'nat_outbound',
        'tunnel_bandwidth_size': 'tunnel_bandwidth_size'
    }

    def __init__(self, interface_name=None, ip_type=None, ip_address=None, gateway_ip_address=None, uplink_bandwidth_size=None, priority=None, nat_outbound=None, tunnel_bandwidth_size=None):
        """EquipmentWanItem

        The model defined in huaweicloud sdk

        :param interface_name: 接口名字
        :type interface_name: str
        :param ip_type: IP类型
        :type ip_type: str
        :param ip_address: IPv4地址
        :type ip_address: str
        :param gateway_ip_address: 网关IP
        :type gateway_ip_address: str
        :param uplink_bandwidth_size: 最大上行带宽
        :type uplink_bandwidth_size: int
        :param priority: 优先级
        :type priority: str
        :param nat_outbound: 是否使能本地上网
        :type nat_outbound: bool
        :param tunnel_bandwidth_size: 最大上云带宽
        :type tunnel_bandwidth_size: int
        """
        
        

        self._interface_name = None
        self._ip_type = None
        self._ip_address = None
        self._gateway_ip_address = None
        self._uplink_bandwidth_size = None
        self._priority = None
        self._nat_outbound = None
        self._tunnel_bandwidth_size = None
        self.discriminator = None

        self.interface_name = interface_name
        if ip_type is not None:
            self.ip_type = ip_type
        if ip_address is not None:
            self.ip_address = ip_address
        if gateway_ip_address is not None:
            self.gateway_ip_address = gateway_ip_address
        if uplink_bandwidth_size is not None:
            self.uplink_bandwidth_size = uplink_bandwidth_size
        self.priority = priority
        if nat_outbound is not None:
            self.nat_outbound = nat_outbound
        if tunnel_bandwidth_size is not None:
            self.tunnel_bandwidth_size = tunnel_bandwidth_size

    @property
    def interface_name(self):
        """Gets the interface_name of this EquipmentWanItem.

        接口名字

        :return: The interface_name of this EquipmentWanItem.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this EquipmentWanItem.

        接口名字

        :param interface_name: The interface_name of this EquipmentWanItem.
        :type interface_name: str
        """
        self._interface_name = interface_name

    @property
    def ip_type(self):
        """Gets the ip_type of this EquipmentWanItem.

        IP类型

        :return: The ip_type of this EquipmentWanItem.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        """Sets the ip_type of this EquipmentWanItem.

        IP类型

        :param ip_type: The ip_type of this EquipmentWanItem.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def ip_address(self):
        """Gets the ip_address of this EquipmentWanItem.

        IPv4地址

        :return: The ip_address of this EquipmentWanItem.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this EquipmentWanItem.

        IPv4地址

        :param ip_address: The ip_address of this EquipmentWanItem.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def gateway_ip_address(self):
        """Gets the gateway_ip_address of this EquipmentWanItem.

        网关IP

        :return: The gateway_ip_address of this EquipmentWanItem.
        :rtype: str
        """
        return self._gateway_ip_address

    @gateway_ip_address.setter
    def gateway_ip_address(self, gateway_ip_address):
        """Sets the gateway_ip_address of this EquipmentWanItem.

        网关IP

        :param gateway_ip_address: The gateway_ip_address of this EquipmentWanItem.
        :type gateway_ip_address: str
        """
        self._gateway_ip_address = gateway_ip_address

    @property
    def uplink_bandwidth_size(self):
        """Gets the uplink_bandwidth_size of this EquipmentWanItem.

        最大上行带宽

        :return: The uplink_bandwidth_size of this EquipmentWanItem.
        :rtype: int
        """
        return self._uplink_bandwidth_size

    @uplink_bandwidth_size.setter
    def uplink_bandwidth_size(self, uplink_bandwidth_size):
        """Sets the uplink_bandwidth_size of this EquipmentWanItem.

        最大上行带宽

        :param uplink_bandwidth_size: The uplink_bandwidth_size of this EquipmentWanItem.
        :type uplink_bandwidth_size: int
        """
        self._uplink_bandwidth_size = uplink_bandwidth_size

    @property
    def priority(self):
        """Gets the priority of this EquipmentWanItem.

        优先级

        :return: The priority of this EquipmentWanItem.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this EquipmentWanItem.

        优先级

        :param priority: The priority of this EquipmentWanItem.
        :type priority: str
        """
        self._priority = priority

    @property
    def nat_outbound(self):
        """Gets the nat_outbound of this EquipmentWanItem.

        是否使能本地上网

        :return: The nat_outbound of this EquipmentWanItem.
        :rtype: bool
        """
        return self._nat_outbound

    @nat_outbound.setter
    def nat_outbound(self, nat_outbound):
        """Sets the nat_outbound of this EquipmentWanItem.

        是否使能本地上网

        :param nat_outbound: The nat_outbound of this EquipmentWanItem.
        :type nat_outbound: bool
        """
        self._nat_outbound = nat_outbound

    @property
    def tunnel_bandwidth_size(self):
        """Gets the tunnel_bandwidth_size of this EquipmentWanItem.

        最大上云带宽

        :return: The tunnel_bandwidth_size of this EquipmentWanItem.
        :rtype: int
        """
        return self._tunnel_bandwidth_size

    @tunnel_bandwidth_size.setter
    def tunnel_bandwidth_size(self, tunnel_bandwidth_size):
        """Sets the tunnel_bandwidth_size of this EquipmentWanItem.

        最大上云带宽

        :param tunnel_bandwidth_size: The tunnel_bandwidth_size of this EquipmentWanItem.
        :type tunnel_bandwidth_size: int
        """
        self._tunnel_bandwidth_size = tunnel_bandwidth_size

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
        if not isinstance(other, EquipmentWanItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
