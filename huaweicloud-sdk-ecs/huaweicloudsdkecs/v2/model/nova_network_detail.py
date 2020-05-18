# coding: utf-8

import pprint
import re

import six


class NovaNetworkDetail(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'label': 'str',
        'broadcast': 'str',
        'cidr': 'str',
        'cidr_v6': 'str',
        'dns1': 'str',
        'dns2': 'str',
        'gateway': 'str',
        'gateway_v6': 'str',
        'netmask': 'str',
        'netmask_v6': 'str',
        'bridge': 'str'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'broadcast': 'broadcast',
        'cidr': 'cidr',
        'cidr_v6': 'cidr_v6',
        'dns1': 'dns1',
        'dns2': 'dns2',
        'gateway': 'gateway',
        'gateway_v6': 'gateway_v6',
        'netmask': 'netmask',
        'netmask_v6': 'netmask_v6',
        'bridge': 'bridge'
    }

    def __init__(self, id=None, label=None, broadcast=None, cidr=None, cidr_v6=None, dns1=None, dns2=None, gateway=None, gateway_v6=None, netmask=None, netmask_v6=None, bridge=None):  # noqa: E501
        """NovaNetworkDetail - a model defined in huaweicloud sdk"""

        self._id = None
        self._label = None
        self._broadcast = None
        self._cidr = None
        self._cidr_v6 = None
        self._dns1 = None
        self._dns2 = None
        self._gateway = None
        self._gateway_v6 = None
        self._netmask = None
        self._netmask_v6 = None
        self._bridge = None
        self.discriminator = None

        self.id = id
        self.label = label
        self.broadcast = broadcast
        self.cidr = cidr
        self.cidr_v6 = cidr_v6
        self.dns1 = dns1
        self.dns2 = dns2
        self.gateway = gateway
        self.gateway_v6 = gateway_v6
        self.netmask = netmask
        self.netmask_v6 = netmask_v6
        if bridge is not None:
            self.bridge = bridge

    @property
    def id(self):
        """Gets the id of this NovaNetworkDetail.

        网络的ID

        :return: The id of this NovaNetworkDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaNetworkDetail.

        网络的ID

        :param id: The id of this NovaNetworkDetail.
        :type: str
        """
        self._id = id

    @property
    def label(self):
        """Gets the label of this NovaNetworkDetail.

        网络的名字

        :return: The label of this NovaNetworkDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this NovaNetworkDetail.

        网络的名字

        :param label: The label of this NovaNetworkDetail.
        :type: str
        """
        self._label = label

    @property
    def broadcast(self):
        """Gets the broadcast of this NovaNetworkDetail.

        固定为null

        :return: The broadcast of this NovaNetworkDetail.
        :rtype: str
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        """Sets the broadcast of this NovaNetworkDetail.

        固定为null

        :param broadcast: The broadcast of this NovaNetworkDetail.
        :type: str
        """
        self._broadcast = broadcast

    @property
    def cidr(self):
        """Gets the cidr of this NovaNetworkDetail.

        固定为null

        :return: The cidr of this NovaNetworkDetail.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this NovaNetworkDetail.

        固定为null

        :param cidr: The cidr of this NovaNetworkDetail.
        :type: str
        """
        self._cidr = cidr

    @property
    def cidr_v6(self):
        """Gets the cidr_v6 of this NovaNetworkDetail.

        固定为null

        :return: The cidr_v6 of this NovaNetworkDetail.
        :rtype: str
        """
        return self._cidr_v6

    @cidr_v6.setter
    def cidr_v6(self, cidr_v6):
        """Sets the cidr_v6 of this NovaNetworkDetail.

        固定为null

        :param cidr_v6: The cidr_v6 of this NovaNetworkDetail.
        :type: str
        """
        self._cidr_v6 = cidr_v6

    @property
    def dns1(self):
        """Gets the dns1 of this NovaNetworkDetail.

        固定为null

        :return: The dns1 of this NovaNetworkDetail.
        :rtype: str
        """
        return self._dns1

    @dns1.setter
    def dns1(self, dns1):
        """Sets the dns1 of this NovaNetworkDetail.

        固定为null

        :param dns1: The dns1 of this NovaNetworkDetail.
        :type: str
        """
        self._dns1 = dns1

    @property
    def dns2(self):
        """Gets the dns2 of this NovaNetworkDetail.

        固定为null

        :return: The dns2 of this NovaNetworkDetail.
        :rtype: str
        """
        return self._dns2

    @dns2.setter
    def dns2(self, dns2):
        """Sets the dns2 of this NovaNetworkDetail.

        固定为null

        :param dns2: The dns2 of this NovaNetworkDetail.
        :type: str
        """
        self._dns2 = dns2

    @property
    def gateway(self):
        """Gets the gateway of this NovaNetworkDetail.

        固定为null

        :return: The gateway of this NovaNetworkDetail.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this NovaNetworkDetail.

        固定为null

        :param gateway: The gateway of this NovaNetworkDetail.
        :type: str
        """
        self._gateway = gateway

    @property
    def gateway_v6(self):
        """Gets the gateway_v6 of this NovaNetworkDetail.

        固定为null

        :return: The gateway_v6 of this NovaNetworkDetail.
        :rtype: str
        """
        return self._gateway_v6

    @gateway_v6.setter
    def gateway_v6(self, gateway_v6):
        """Sets the gateway_v6 of this NovaNetworkDetail.

        固定为null

        :param gateway_v6: The gateway_v6 of this NovaNetworkDetail.
        :type: str
        """
        self._gateway_v6 = gateway_v6

    @property
    def netmask(self):
        """Gets the netmask of this NovaNetworkDetail.

        固定为null

        :return: The netmask of this NovaNetworkDetail.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this NovaNetworkDetail.

        固定为null

        :param netmask: The netmask of this NovaNetworkDetail.
        :type: str
        """
        self._netmask = netmask

    @property
    def netmask_v6(self):
        """Gets the netmask_v6 of this NovaNetworkDetail.

        固定为null

        :return: The netmask_v6 of this NovaNetworkDetail.
        :rtype: str
        """
        return self._netmask_v6

    @netmask_v6.setter
    def netmask_v6(self, netmask_v6):
        """Sets the netmask_v6 of this NovaNetworkDetail.

        固定为null

        :param netmask_v6: The netmask_v6 of this NovaNetworkDetail.
        :type: str
        """
        self._netmask_v6 = netmask_v6

    @property
    def bridge(self):
        """Gets the bridge of this NovaNetworkDetail.

        固定为null，UUID格式。

        :return: The bridge of this NovaNetworkDetail.
        :rtype: str
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this NovaNetworkDetail.

        固定为null，UUID格式。

        :param bridge: The bridge of this NovaNetworkDetail.
        :type: str
        """
        self._bridge = bridge

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
        if not isinstance(other, NovaNetworkDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
