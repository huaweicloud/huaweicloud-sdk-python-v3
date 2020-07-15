# coding: utf-8

import pprint
import re

import six





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
        'port_state': 'str'
    }

    attribute_map = {
        'fixed_ips': 'fixed_ips',
        'mac_addr': 'mac_addr',
        'net_id': 'net_id',
        'port_id': 'port_id',
        'port_state': 'port_state'
    }

    def __init__(self, fixed_ips=None, mac_addr=None, net_id=None, port_id=None, port_state=None):
        """InterfaceAttachment - a model defined in huaweicloud sdk"""
        
        

        self._fixed_ips = None
        self._mac_addr = None
        self._net_id = None
        self._port_id = None
        self._port_state = None
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

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this InterfaceAttachment.

        网卡私网IP信息列表。

        :return: The fixed_ips of this InterfaceAttachment.
        :rtype: list[ServerInterfaceFixedIp]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this InterfaceAttachment.

        网卡私网IP信息列表。

        :param fixed_ips: The fixed_ips of this InterfaceAttachment.
        :type: list[ServerInterfaceFixedIp]
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._port_state = port_state

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InterfaceAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
