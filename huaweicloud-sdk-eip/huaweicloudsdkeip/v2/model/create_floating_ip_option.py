# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFloatingIpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'floating_ip_address': 'str',
        'floating_network_id': 'str',
        'port_id': 'str',
        'fixed_ip_address': 'str'
    }

    attribute_map = {
        'floating_ip_address': 'floating_ip_address',
        'floating_network_id': 'floating_network_id',
        'port_id': 'port_id',
        'fixed_ip_address': 'fixed_ip_address'
    }

    def __init__(self, floating_ip_address=None, floating_network_id=None, port_id=None, fixed_ip_address=None):
        r"""CreateFloatingIpOption

        The model defined in huaweicloud sdk

        :param floating_ip_address: 浮动IP地址。
        :type floating_ip_address: str
        :param floating_network_id: 外部网络的id。只能使用固定的外网，外部网络的信息请通过GET /v2.0/networks?router:external&#x3D;True或GET /v2.0/networks?name&#x3D;{floating_network}或neutron net-external-list方式查询。
        :type floating_network_id: str
        :param port_id: 端口id
        :type port_id: str
        :param fixed_ip_address: 关联端口的私有IP地址。
        :type fixed_ip_address: str
        """
        
        

        self._floating_ip_address = None
        self._floating_network_id = None
        self._port_id = None
        self._fixed_ip_address = None
        self.discriminator = None

        if floating_ip_address is not None:
            self.floating_ip_address = floating_ip_address
        self.floating_network_id = floating_network_id
        if port_id is not None:
            self.port_id = port_id
        if fixed_ip_address is not None:
            self.fixed_ip_address = fixed_ip_address

    @property
    def floating_ip_address(self):
        r"""Gets the floating_ip_address of this CreateFloatingIpOption.

        浮动IP地址。

        :return: The floating_ip_address of this CreateFloatingIpOption.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        r"""Sets the floating_ip_address of this CreateFloatingIpOption.

        浮动IP地址。

        :param floating_ip_address: The floating_ip_address of this CreateFloatingIpOption.
        :type floating_ip_address: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def floating_network_id(self):
        r"""Gets the floating_network_id of this CreateFloatingIpOption.

        外部网络的id。只能使用固定的外网，外部网络的信息请通过GET /v2.0/networks?router:external=True或GET /v2.0/networks?name={floating_network}或neutron net-external-list方式查询。

        :return: The floating_network_id of this CreateFloatingIpOption.
        :rtype: str
        """
        return self._floating_network_id

    @floating_network_id.setter
    def floating_network_id(self, floating_network_id):
        r"""Sets the floating_network_id of this CreateFloatingIpOption.

        外部网络的id。只能使用固定的外网，外部网络的信息请通过GET /v2.0/networks?router:external=True或GET /v2.0/networks?name={floating_network}或neutron net-external-list方式查询。

        :param floating_network_id: The floating_network_id of this CreateFloatingIpOption.
        :type floating_network_id: str
        """
        self._floating_network_id = floating_network_id

    @property
    def port_id(self):
        r"""Gets the port_id of this CreateFloatingIpOption.

        端口id

        :return: The port_id of this CreateFloatingIpOption.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this CreateFloatingIpOption.

        端口id

        :param port_id: The port_id of this CreateFloatingIpOption.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def fixed_ip_address(self):
        r"""Gets the fixed_ip_address of this CreateFloatingIpOption.

        关联端口的私有IP地址。

        :return: The fixed_ip_address of this CreateFloatingIpOption.
        :rtype: str
        """
        return self._fixed_ip_address

    @fixed_ip_address.setter
    def fixed_ip_address(self, fixed_ip_address):
        r"""Sets the fixed_ip_address of this CreateFloatingIpOption.

        关联端口的私有IP地址。

        :param fixed_ip_address: The fixed_ip_address of this CreateFloatingIpOption.
        :type fixed_ip_address: str
        """
        self._fixed_ip_address = fixed_ip_address

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
        if not isinstance(other, CreateFloatingIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
