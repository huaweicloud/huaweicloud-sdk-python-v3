# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterfaceAttachments:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_state': 'str',
        'fixed_ips': 'list[FixedIps]',
        'net_id': 'str',
        'port_id': 'str',
        'mac_addr': 'str',
        'driver_mode': 'str',
        'pci_address': 'str'
    }

    attribute_map = {
        'port_state': 'port_state',
        'fixed_ips': 'fixed_ips',
        'net_id': 'net_id',
        'port_id': 'port_id',
        'mac_addr': 'mac_addr',
        'driver_mode': 'driver_mode',
        'pci_address': 'pci_address'
    }

    def __init__(self, port_state=None, fixed_ips=None, net_id=None, port_id=None, mac_addr=None, driver_mode=None, pci_address=None):
        r"""InterfaceAttachments

        The model defined in huaweicloud sdk

        :param port_state: 网卡端口状态。取值为：ACTIVE、BUILD、DOWN
        :type port_state: str
        :param fixed_ips: 网卡私网IP信息列表，详情请参见表3 fixed_ips字段数据结构说明。
        :type fixed_ips: list[:class:`huaweicloudsdkbms.v1.FixedIps`]
        :param net_id: 网卡端口所属子网的网络ID（network_id）。
        :type net_id: str
        :param port_id: 网卡端口ID。
        :type port_id: str
        :param mac_addr: 网卡Mac地址信息
        :type mac_addr: str
        :param driver_mode: 从guest os中，网卡的驱动类型
        :type driver_mode: str
        :param pci_address: 弹性网卡在Linux GuestOS里的BDF号
        :type pci_address: str
        """
        
        

        self._port_state = None
        self._fixed_ips = None
        self._net_id = None
        self._port_id = None
        self._mac_addr = None
        self._driver_mode = None
        self._pci_address = None
        self.discriminator = None

        if port_state is not None:
            self.port_state = port_state
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if net_id is not None:
            self.net_id = net_id
        if port_id is not None:
            self.port_id = port_id
        if mac_addr is not None:
            self.mac_addr = mac_addr
        if driver_mode is not None:
            self.driver_mode = driver_mode
        if pci_address is not None:
            self.pci_address = pci_address

    @property
    def port_state(self):
        r"""Gets the port_state of this InterfaceAttachments.

        网卡端口状态。取值为：ACTIVE、BUILD、DOWN

        :return: The port_state of this InterfaceAttachments.
        :rtype: str
        """
        return self._port_state

    @port_state.setter
    def port_state(self, port_state):
        r"""Sets the port_state of this InterfaceAttachments.

        网卡端口状态。取值为：ACTIVE、BUILD、DOWN

        :param port_state: The port_state of this InterfaceAttachments.
        :type port_state: str
        """
        self._port_state = port_state

    @property
    def fixed_ips(self):
        r"""Gets the fixed_ips of this InterfaceAttachments.

        网卡私网IP信息列表，详情请参见表3 fixed_ips字段数据结构说明。

        :return: The fixed_ips of this InterfaceAttachments.
        :rtype: list[:class:`huaweicloudsdkbms.v1.FixedIps`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        r"""Sets the fixed_ips of this InterfaceAttachments.

        网卡私网IP信息列表，详情请参见表3 fixed_ips字段数据结构说明。

        :param fixed_ips: The fixed_ips of this InterfaceAttachments.
        :type fixed_ips: list[:class:`huaweicloudsdkbms.v1.FixedIps`]
        """
        self._fixed_ips = fixed_ips

    @property
    def net_id(self):
        r"""Gets the net_id of this InterfaceAttachments.

        网卡端口所属子网的网络ID（network_id）。

        :return: The net_id of this InterfaceAttachments.
        :rtype: str
        """
        return self._net_id

    @net_id.setter
    def net_id(self, net_id):
        r"""Sets the net_id of this InterfaceAttachments.

        网卡端口所属子网的网络ID（network_id）。

        :param net_id: The net_id of this InterfaceAttachments.
        :type net_id: str
        """
        self._net_id = net_id

    @property
    def port_id(self):
        r"""Gets the port_id of this InterfaceAttachments.

        网卡端口ID。

        :return: The port_id of this InterfaceAttachments.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this InterfaceAttachments.

        网卡端口ID。

        :param port_id: The port_id of this InterfaceAttachments.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def mac_addr(self):
        r"""Gets the mac_addr of this InterfaceAttachments.

        网卡Mac地址信息

        :return: The mac_addr of this InterfaceAttachments.
        :rtype: str
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        r"""Sets the mac_addr of this InterfaceAttachments.

        网卡Mac地址信息

        :param mac_addr: The mac_addr of this InterfaceAttachments.
        :type mac_addr: str
        """
        self._mac_addr = mac_addr

    @property
    def driver_mode(self):
        r"""Gets the driver_mode of this InterfaceAttachments.

        从guest os中，网卡的驱动类型

        :return: The driver_mode of this InterfaceAttachments.
        :rtype: str
        """
        return self._driver_mode

    @driver_mode.setter
    def driver_mode(self, driver_mode):
        r"""Sets the driver_mode of this InterfaceAttachments.

        从guest os中，网卡的驱动类型

        :param driver_mode: The driver_mode of this InterfaceAttachments.
        :type driver_mode: str
        """
        self._driver_mode = driver_mode

    @property
    def pci_address(self):
        r"""Gets the pci_address of this InterfaceAttachments.

        弹性网卡在Linux GuestOS里的BDF号

        :return: The pci_address of this InterfaceAttachments.
        :rtype: str
        """
        return self._pci_address

    @pci_address.setter
    def pci_address(self, pci_address):
        r"""Sets the pci_address of this InterfaceAttachments.

        弹性网卡在Linux GuestOS里的BDF号

        :param pci_address: The pci_address of this InterfaceAttachments.
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
        if not isinstance(other, InterfaceAttachments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
