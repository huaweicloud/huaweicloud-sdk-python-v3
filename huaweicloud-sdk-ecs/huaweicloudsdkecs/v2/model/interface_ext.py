# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterfaceExt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'preserve_on_delete': 'bool',
        'port_state': 'str',
        'fixed_ips': 'list[FixedIp]',
        'net_id': 'str',
        'port_id': 'str',
        'mac_addr': 'str',
        'delete_on_termination': 'bool',
        'driver_mode': 'str',
        'min_rate': 'int',
        'multiqueue_num': 'int',
        'pci_address': 'str'
    }

    attribute_map = {
        'preserve_on_delete': 'preserve_on_delete',
        'port_state': 'port_state',
        'fixed_ips': 'fixed_ips',
        'net_id': 'net_id',
        'port_id': 'port_id',
        'mac_addr': 'mac_addr',
        'delete_on_termination': 'delete_on_termination',
        'driver_mode': 'driver_mode',
        'min_rate': 'min_rate',
        'multiqueue_num': 'multiqueue_num',
        'pci_address': 'pci_address'
    }

    def __init__(self, preserve_on_delete=None, port_state=None, fixed_ips=None, net_id=None, port_id=None, mac_addr=None, delete_on_termination=None, driver_mode=None, min_rate=None, multiqueue_num=None, pci_address=None):
        r"""InterfaceExt

        The model defined in huaweicloud sdk

        :param preserve_on_delete: 
        :type preserve_on_delete: bool
        :param port_state: 
        :type port_state: str
        :param fixed_ips: 
        :type fixed_ips: list[:class:`huaweicloudsdkecs.v2.FixedIp`]
        :param net_id: 
        :type net_id: str
        :param port_id: 
        :type port_id: str
        :param mac_addr: 
        :type mac_addr: str
        :param delete_on_termination: 
        :type delete_on_termination: bool
        :param driver_mode: 
        :type driver_mode: str
        :param min_rate: 
        :type min_rate: int
        :param multiqueue_num: 
        :type multiqueue_num: int
        :param pci_address: 
        :type pci_address: str
        """
        
        

        self._preserve_on_delete = None
        self._port_state = None
        self._fixed_ips = None
        self._net_id = None
        self._port_id = None
        self._mac_addr = None
        self._delete_on_termination = None
        self._driver_mode = None
        self._min_rate = None
        self._multiqueue_num = None
        self._pci_address = None
        self.discriminator = None

        if preserve_on_delete is not None:
            self.preserve_on_delete = preserve_on_delete
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
    def preserve_on_delete(self):
        r"""Gets the preserve_on_delete of this InterfaceExt.

        :return: The preserve_on_delete of this InterfaceExt.
        :rtype: bool
        """
        return self._preserve_on_delete

    @preserve_on_delete.setter
    def preserve_on_delete(self, preserve_on_delete):
        r"""Sets the preserve_on_delete of this InterfaceExt.

        :param preserve_on_delete: The preserve_on_delete of this InterfaceExt.
        :type preserve_on_delete: bool
        """
        self._preserve_on_delete = preserve_on_delete

    @property
    def port_state(self):
        r"""Gets the port_state of this InterfaceExt.

        :return: The port_state of this InterfaceExt.
        :rtype: str
        """
        return self._port_state

    @port_state.setter
    def port_state(self, port_state):
        r"""Sets the port_state of this InterfaceExt.

        :param port_state: The port_state of this InterfaceExt.
        :type port_state: str
        """
        self._port_state = port_state

    @property
    def fixed_ips(self):
        r"""Gets the fixed_ips of this InterfaceExt.

        :return: The fixed_ips of this InterfaceExt.
        :rtype: list[:class:`huaweicloudsdkecs.v2.FixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        r"""Sets the fixed_ips of this InterfaceExt.

        :param fixed_ips: The fixed_ips of this InterfaceExt.
        :type fixed_ips: list[:class:`huaweicloudsdkecs.v2.FixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def net_id(self):
        r"""Gets the net_id of this InterfaceExt.

        :return: The net_id of this InterfaceExt.
        :rtype: str
        """
        return self._net_id

    @net_id.setter
    def net_id(self, net_id):
        r"""Sets the net_id of this InterfaceExt.

        :param net_id: The net_id of this InterfaceExt.
        :type net_id: str
        """
        self._net_id = net_id

    @property
    def port_id(self):
        r"""Gets the port_id of this InterfaceExt.

        :return: The port_id of this InterfaceExt.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this InterfaceExt.

        :param port_id: The port_id of this InterfaceExt.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def mac_addr(self):
        r"""Gets the mac_addr of this InterfaceExt.

        :return: The mac_addr of this InterfaceExt.
        :rtype: str
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        r"""Sets the mac_addr of this InterfaceExt.

        :param mac_addr: The mac_addr of this InterfaceExt.
        :type mac_addr: str
        """
        self._mac_addr = mac_addr

    @property
    def delete_on_termination(self):
        r"""Gets the delete_on_termination of this InterfaceExt.

        :return: The delete_on_termination of this InterfaceExt.
        :rtype: bool
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        r"""Sets the delete_on_termination of this InterfaceExt.

        :param delete_on_termination: The delete_on_termination of this InterfaceExt.
        :type delete_on_termination: bool
        """
        self._delete_on_termination = delete_on_termination

    @property
    def driver_mode(self):
        r"""Gets the driver_mode of this InterfaceExt.

        :return: The driver_mode of this InterfaceExt.
        :rtype: str
        """
        return self._driver_mode

    @driver_mode.setter
    def driver_mode(self, driver_mode):
        r"""Sets the driver_mode of this InterfaceExt.

        :param driver_mode: The driver_mode of this InterfaceExt.
        :type driver_mode: str
        """
        self._driver_mode = driver_mode

    @property
    def min_rate(self):
        r"""Gets the min_rate of this InterfaceExt.

        :return: The min_rate of this InterfaceExt.
        :rtype: int
        """
        return self._min_rate

    @min_rate.setter
    def min_rate(self, min_rate):
        r"""Sets the min_rate of this InterfaceExt.

        :param min_rate: The min_rate of this InterfaceExt.
        :type min_rate: int
        """
        self._min_rate = min_rate

    @property
    def multiqueue_num(self):
        r"""Gets the multiqueue_num of this InterfaceExt.

        :return: The multiqueue_num of this InterfaceExt.
        :rtype: int
        """
        return self._multiqueue_num

    @multiqueue_num.setter
    def multiqueue_num(self, multiqueue_num):
        r"""Sets the multiqueue_num of this InterfaceExt.

        :param multiqueue_num: The multiqueue_num of this InterfaceExt.
        :type multiqueue_num: int
        """
        self._multiqueue_num = multiqueue_num

    @property
    def pci_address(self):
        r"""Gets the pci_address of this InterfaceExt.

        :return: The pci_address of this InterfaceExt.
        :rtype: str
        """
        return self._pci_address

    @pci_address.setter
    def pci_address(self, pci_address):
        r"""Sets the pci_address of this InterfaceExt.

        :param pci_address: The pci_address of this InterfaceExt.
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
        if not isinstance(other, InterfaceExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
