# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterfaceAttachment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'fixed_ips': 'list[ServerInterfaceFixedIp]',
        'mac_addr': 'str',
        'net_id': 'str',
        'port_id': 'str',
        'port_state': 'str',
        'delete_on_termination': 'bool',
        'driver_mode': 'str',
        'min_rate': 'int',
        'multiqueue_num': 'int',
        'pci_address': 'str'
    }

    attribute_map = {
        'fixed_ips': 'fixed_ips',
        'mac_addr': 'mac_addr',
        'net_id': 'net_id',
        'port_id': 'port_id',
        'port_state': 'port_state',
        'delete_on_termination': 'delete_on_termination',
        'driver_mode': 'driver_mode',
        'min_rate': 'min_rate',
        'multiqueue_num': 'multiqueue_num',
        'pci_address': 'pci_address'
    }

    def __init__(self, fixed_ips=None, mac_addr=None, net_id=None, port_id=None, port_state=None, delete_on_termination=None, driver_mode=None, min_rate=None, multiqueue_num=None, pci_address=None):
        """InterfaceAttachment

        The model defined in huaweicloud sdk

        :param fixed_ips: 网卡私网IP信息列表。
        :type fixed_ips: list[:class:`huaweicloudsdkecs.v2.ServerInterfaceFixedIp`]
        :param mac_addr: 网卡Mac地址信息。
        :type mac_addr: str
        :param net_id: 网卡端口所属网络ID。
        :type net_id: str
        :param port_id: 网卡端口ID。
        :type port_id: str
        :param port_state: 网卡端口状态。
        :type port_state: str
        :param delete_on_termination: 卸载网卡时，是否删除网卡。
        :type delete_on_termination: bool
        :param driver_mode: 从guest os中，网卡的驱动类型。可选值为virtio和hinic，默认为virtio
        :type driver_mode: str
        :param min_rate: 网卡带宽下限。
        :type min_rate: int
        :param multiqueue_num: 网卡多队列个数。
        :type multiqueue_num: int
        :param pci_address: 弹性网卡在Linux GuestOS里的BDF号
        :type pci_address: str
        """
        
        

        self._fixed_ips = None
        self._mac_addr = None
        self._net_id = None
        self._port_id = None
        self._port_state = None
        self._delete_on_termination = None
        self._driver_mode = None
        self._min_rate = None
        self._multiqueue_num = None
        self._pci_address = None
        self.discriminator = None

        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if mac_addr is not None:
            self.mac_addr = mac_addr
        if net_id is not None:
            self.net_id = net_id
        if port_id is not None:
            self.port_id = port_id
        if port_state is not None:
            self.port_state = port_state
        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination
        if driver_mode is not None:
            self.driver_mode = driver_mode
        if min_rate is not None:
            self.min_rate = min_rate
        if multiqueue_num is not None:
            self.multiqueue_num = multiqueue_num
        if pci_address is not None:
            self.pci_address = pci_address

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this InterfaceAttachment.

        网卡私网IP信息列表。

        :return: The fixed_ips of this InterfaceAttachment.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerInterfaceFixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this InterfaceAttachment.

        网卡私网IP信息列表。

        :param fixed_ips: The fixed_ips of this InterfaceAttachment.
        :type fixed_ips: list[:class:`huaweicloudsdkecs.v2.ServerInterfaceFixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def mac_addr(self):
        """Gets the mac_addr of this InterfaceAttachment.

        网卡Mac地址信息。

        :return: The mac_addr of this InterfaceAttachment.
        :rtype: str
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        """Sets the mac_addr of this InterfaceAttachment.

        网卡Mac地址信息。

        :param mac_addr: The mac_addr of this InterfaceAttachment.
        :type mac_addr: str
        """
        self._mac_addr = mac_addr

    @property
    def net_id(self):
        """Gets the net_id of this InterfaceAttachment.

        网卡端口所属网络ID。

        :return: The net_id of this InterfaceAttachment.
        :rtype: str
        """
        return self._net_id

    @net_id.setter
    def net_id(self, net_id):
        """Sets the net_id of this InterfaceAttachment.

        网卡端口所属网络ID。

        :param net_id: The net_id of this InterfaceAttachment.
        :type net_id: str
        """
        self._net_id = net_id

    @property
    def port_id(self):
        """Gets the port_id of this InterfaceAttachment.

        网卡端口ID。

        :return: The port_id of this InterfaceAttachment.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this InterfaceAttachment.

        网卡端口ID。

        :param port_id: The port_id of this InterfaceAttachment.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def port_state(self):
        """Gets the port_state of this InterfaceAttachment.

        网卡端口状态。

        :return: The port_state of this InterfaceAttachment.
        :rtype: str
        """
        return self._port_state

    @port_state.setter
    def port_state(self, port_state):
        """Sets the port_state of this InterfaceAttachment.

        网卡端口状态。

        :param port_state: The port_state of this InterfaceAttachment.
        :type port_state: str
        """
        self._port_state = port_state

    @property
    def delete_on_termination(self):
        """Gets the delete_on_termination of this InterfaceAttachment.

        卸载网卡时，是否删除网卡。

        :return: The delete_on_termination of this InterfaceAttachment.
        :rtype: bool
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        """Sets the delete_on_termination of this InterfaceAttachment.

        卸载网卡时，是否删除网卡。

        :param delete_on_termination: The delete_on_termination of this InterfaceAttachment.
        :type delete_on_termination: bool
        """
        self._delete_on_termination = delete_on_termination

    @property
    def driver_mode(self):
        """Gets the driver_mode of this InterfaceAttachment.

        从guest os中，网卡的驱动类型。可选值为virtio和hinic，默认为virtio

        :return: The driver_mode of this InterfaceAttachment.
        :rtype: str
        """
        return self._driver_mode

    @driver_mode.setter
    def driver_mode(self, driver_mode):
        """Sets the driver_mode of this InterfaceAttachment.

        从guest os中，网卡的驱动类型。可选值为virtio和hinic，默认为virtio

        :param driver_mode: The driver_mode of this InterfaceAttachment.
        :type driver_mode: str
        """
        self._driver_mode = driver_mode

    @property
    def min_rate(self):
        """Gets the min_rate of this InterfaceAttachment.

        网卡带宽下限。

        :return: The min_rate of this InterfaceAttachment.
        :rtype: int
        """
        return self._min_rate

    @min_rate.setter
    def min_rate(self, min_rate):
        """Sets the min_rate of this InterfaceAttachment.

        网卡带宽下限。

        :param min_rate: The min_rate of this InterfaceAttachment.
        :type min_rate: int
        """
        self._min_rate = min_rate

    @property
    def multiqueue_num(self):
        """Gets the multiqueue_num of this InterfaceAttachment.

        网卡多队列个数。

        :return: The multiqueue_num of this InterfaceAttachment.
        :rtype: int
        """
        return self._multiqueue_num

    @multiqueue_num.setter
    def multiqueue_num(self, multiqueue_num):
        """Sets the multiqueue_num of this InterfaceAttachment.

        网卡多队列个数。

        :param multiqueue_num: The multiqueue_num of this InterfaceAttachment.
        :type multiqueue_num: int
        """
        self._multiqueue_num = multiqueue_num

    @property
    def pci_address(self):
        """Gets the pci_address of this InterfaceAttachment.

        弹性网卡在Linux GuestOS里的BDF号

        :return: The pci_address of this InterfaceAttachment.
        :rtype: str
        """
        return self._pci_address

    @pci_address.setter
    def pci_address(self, pci_address):
        """Sets the pci_address of this InterfaceAttachment.

        弹性网卡在Linux GuestOS里的BDF号

        :param pci_address: The pci_address of this InterfaceAttachment.
        :type pci_address: str
        """
        self._pci_address = pci_address

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
        if not isinstance(other, InterfaceAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
