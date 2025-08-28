# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LocalPort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'ip_address': 'str',
        'ipv6_address': 'str',
        'type': 'str',
        'virsubnet_id': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'ip_address': 'ip_address',
        'ipv6_address': 'ipv6_address',
        'type': 'type',
        'virsubnet_id': 'virsubnet_id'
    }

    def __init__(self, port_id=None, ip_address=None, ipv6_address=None, type=None, virsubnet_id=None):
        r"""LocalPort

        The model defined in huaweicloud sdk

        :param port_id: **参数解释**：负载均衡器占用的端口ID。  **取值范围**：不涉及
        :type port_id: str
        :param ip_address: **参数解释**：负载均衡器占用的私有IPv4地址。  **取值范围**：不涉及
        :type ip_address: str
        :param ipv6_address: **参数解释**：负载均衡器占用的IPv6地址。  **取值范围**：不涉及
        :type ipv6_address: str
        :param type: **参数解释**：子网端口类型。  **取值范围**： - l4_hc：四层dnat转发时健康检查使用的地址。 - l4 四层fullnat 转发时健康检查及业务转发使用的地址。 - l7 七层健康检查及业务转发使用的地址。
        :type type: str
        :param virsubnet_id: **参数解释**：子网端口所在下联面子网网络ID。  **取值范围**：不涉及
        :type virsubnet_id: str
        """
        
        

        self._port_id = None
        self._ip_address = None
        self._ipv6_address = None
        self._type = None
        self._virsubnet_id = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if type is not None:
            self.type = type
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id

    @property
    def port_id(self):
        r"""Gets the port_id of this LocalPort.

        **参数解释**：负载均衡器占用的端口ID。  **取值范围**：不涉及

        :return: The port_id of this LocalPort.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this LocalPort.

        **参数解释**：负载均衡器占用的端口ID。  **取值范围**：不涉及

        :param port_id: The port_id of this LocalPort.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this LocalPort.

        **参数解释**：负载均衡器占用的私有IPv4地址。  **取值范围**：不涉及

        :return: The ip_address of this LocalPort.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this LocalPort.

        **参数解释**：负载均衡器占用的私有IPv4地址。  **取值范围**：不涉及

        :param ip_address: The ip_address of this LocalPort.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ipv6_address(self):
        r"""Gets the ipv6_address of this LocalPort.

        **参数解释**：负载均衡器占用的IPv6地址。  **取值范围**：不涉及

        :return: The ipv6_address of this LocalPort.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        r"""Sets the ipv6_address of this LocalPort.

        **参数解释**：负载均衡器占用的IPv6地址。  **取值范围**：不涉及

        :param ipv6_address: The ipv6_address of this LocalPort.
        :type ipv6_address: str
        """
        self._ipv6_address = ipv6_address

    @property
    def type(self):
        r"""Gets the type of this LocalPort.

        **参数解释**：子网端口类型。  **取值范围**： - l4_hc：四层dnat转发时健康检查使用的地址。 - l4 四层fullnat 转发时健康检查及业务转发使用的地址。 - l7 七层健康检查及业务转发使用的地址。

        :return: The type of this LocalPort.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LocalPort.

        **参数解释**：子网端口类型。  **取值范围**： - l4_hc：四层dnat转发时健康检查使用的地址。 - l4 四层fullnat 转发时健康检查及业务转发使用的地址。 - l7 七层健康检查及业务转发使用的地址。

        :param type: The type of this LocalPort.
        :type type: str
        """
        self._type = type

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this LocalPort.

        **参数解释**：子网端口所在下联面子网网络ID。  **取值范围**：不涉及

        :return: The virsubnet_id of this LocalPort.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this LocalPort.

        **参数解释**：子网端口所在下联面子网网络ID。  **取值范围**：不涉及

        :param virsubnet_id: The virsubnet_id of this LocalPort.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

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
        if not isinstance(other, LocalPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
