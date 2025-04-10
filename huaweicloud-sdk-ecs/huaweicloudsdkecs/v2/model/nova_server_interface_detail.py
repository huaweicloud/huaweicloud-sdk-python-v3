# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaServerInterfaceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fixed_ips': 'list[NovaServerInterfaceFixedIp]',
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
        r"""NovaServerInterfaceDetail

        The model defined in huaweicloud sdk

        :param fixed_ips: 网卡私网IP信息列表。
        :type fixed_ips: list[:class:`huaweicloudsdkecs.v2.NovaServerInterfaceFixedIp`]
        :param mac_addr: 网卡Mac地址信息。
        :type mac_addr: str
        :param net_id: 网卡端口所属网络ID。
        :type net_id: str
        :param port_id: 网卡端口ID。
        :type port_id: str
        :param port_state: 网卡端口状态。
        :type port_state: str
        """
        
        

        self._fixed_ips = None
        self._mac_addr = None
        self._net_id = None
        self._port_id = None
        self._port_state = None
        self.discriminator = None

        self.fixed_ips = fixed_ips
        self.mac_addr = mac_addr
        self.net_id = net_id
        self.port_id = port_id
        self.port_state = port_state

    @property
    def fixed_ips(self):
        r"""Gets the fixed_ips of this NovaServerInterfaceDetail.

        网卡私网IP信息列表。

        :return: The fixed_ips of this NovaServerInterfaceDetail.
        :rtype: list[:class:`huaweicloudsdkecs.v2.NovaServerInterfaceFixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        r"""Sets the fixed_ips of this NovaServerInterfaceDetail.

        网卡私网IP信息列表。

        :param fixed_ips: The fixed_ips of this NovaServerInterfaceDetail.
        :type fixed_ips: list[:class:`huaweicloudsdkecs.v2.NovaServerInterfaceFixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def mac_addr(self):
        r"""Gets the mac_addr of this NovaServerInterfaceDetail.

        网卡Mac地址信息。

        :return: The mac_addr of this NovaServerInterfaceDetail.
        :rtype: str
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        r"""Sets the mac_addr of this NovaServerInterfaceDetail.

        网卡Mac地址信息。

        :param mac_addr: The mac_addr of this NovaServerInterfaceDetail.
        :type mac_addr: str
        """
        self._mac_addr = mac_addr

    @property
    def net_id(self):
        r"""Gets the net_id of this NovaServerInterfaceDetail.

        网卡端口所属网络ID。

        :return: The net_id of this NovaServerInterfaceDetail.
        :rtype: str
        """
        return self._net_id

    @net_id.setter
    def net_id(self, net_id):
        r"""Sets the net_id of this NovaServerInterfaceDetail.

        网卡端口所属网络ID。

        :param net_id: The net_id of this NovaServerInterfaceDetail.
        :type net_id: str
        """
        self._net_id = net_id

    @property
    def port_id(self):
        r"""Gets the port_id of this NovaServerInterfaceDetail.

        网卡端口ID。

        :return: The port_id of this NovaServerInterfaceDetail.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this NovaServerInterfaceDetail.

        网卡端口ID。

        :param port_id: The port_id of this NovaServerInterfaceDetail.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def port_state(self):
        r"""Gets the port_state of this NovaServerInterfaceDetail.

        网卡端口状态。

        :return: The port_state of this NovaServerInterfaceDetail.
        :rtype: str
        """
        return self._port_state

    @port_state.setter
    def port_state(self, port_state):
        r"""Sets the port_state of this NovaServerInterfaceDetail.

        网卡端口状态。

        :param port_state: The port_state of this NovaServerInterfaceDetail.
        :type port_state: str
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
        if not isinstance(other, NovaServerInterfaceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
