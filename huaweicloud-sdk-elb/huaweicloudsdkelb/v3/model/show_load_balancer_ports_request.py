# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLoadBalancerPortsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancer_id': 'str',
        'port_id': 'list[str]',
        'ip_address': 'list[str]',
        'ipv6_address': 'list[str]',
        'type': 'list[str]',
        'virsubnet_id': 'list[str]'
    }

    attribute_map = {
        'loadbalancer_id': 'loadbalancer_id',
        'port_id': 'port_id',
        'ip_address': 'ip_address',
        'ipv6_address': 'ipv6_address',
        'type': 'type',
        'virsubnet_id': 'virsubnet_id'
    }

    def __init__(self, loadbalancer_id=None, port_id=None, ip_address=None, ipv6_address=None, type=None, virsubnet_id=None):
        r"""ShowLoadBalancerPortsRequest

        The model defined in huaweicloud sdk

        :param loadbalancer_id: **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: str
        :param port_id: **参数解释**：负载均衡器占用的端口ID。  支持多值查询，查询条件格式：*port_id&#x3D;xxx&amp;port_id&#x3D;xxx*。
        :type port_id: list[str]
        :param ip_address: **参数解释**：负载均衡器占用的私有IPv4地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*ip_address&#x3D;xxx&amp;ip_address&#x3D;xxx*。
        :type ip_address: list[str]
        :param ipv6_address: **参数解释**：负载均衡器占用的IPv6地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*ipv6_address&#x3D;xxx&amp;ipv6_address&#x3D;xxx*。
        :type ipv6_address: list[str]
        :param type: **参数解释**：子网端口类型。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*type&#x3D;xxx&amp;type&#x3D;xxx*。
        :type type: list[str]
        :param virsubnet_id: **参数解释**：子网端口所在下联面子网网络ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*virsubnet_id&#x3D;xxx&amp;virsubnet_id&#x3D;xxx*。
        :type virsubnet_id: list[str]
        """
        
        

        self._loadbalancer_id = None
        self._port_id = None
        self._ip_address = None
        self._ipv6_address = None
        self._type = None
        self._virsubnet_id = None
        self.discriminator = None

        self.loadbalancer_id = loadbalancer_id
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
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ShowLoadBalancerPortsRequest.

        **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this ShowLoadBalancerPortsRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ShowLoadBalancerPortsRequest.

        **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this ShowLoadBalancerPortsRequest.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def port_id(self):
        r"""Gets the port_id of this ShowLoadBalancerPortsRequest.

        **参数解释**：负载均衡器占用的端口ID。  支持多值查询，查询条件格式：*port_id=xxx&port_id=xxx*。

        :return: The port_id of this ShowLoadBalancerPortsRequest.
        :rtype: list[str]
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this ShowLoadBalancerPortsRequest.

        **参数解释**：负载均衡器占用的端口ID。  支持多值查询，查询条件格式：*port_id=xxx&port_id=xxx*。

        :param port_id: The port_id of this ShowLoadBalancerPortsRequest.
        :type port_id: list[str]
        """
        self._port_id = port_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ShowLoadBalancerPortsRequest.

        **参数解释**：负载均衡器占用的私有IPv4地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*ip_address=xxx&ip_address=xxx*。

        :return: The ip_address of this ShowLoadBalancerPortsRequest.
        :rtype: list[str]
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ShowLoadBalancerPortsRequest.

        **参数解释**：负载均衡器占用的私有IPv4地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*ip_address=xxx&ip_address=xxx*。

        :param ip_address: The ip_address of this ShowLoadBalancerPortsRequest.
        :type ip_address: list[str]
        """
        self._ip_address = ip_address

    @property
    def ipv6_address(self):
        r"""Gets the ipv6_address of this ShowLoadBalancerPortsRequest.

        **参数解释**：负载均衡器占用的IPv6地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*ipv6_address=xxx&ipv6_address=xxx*。

        :return: The ipv6_address of this ShowLoadBalancerPortsRequest.
        :rtype: list[str]
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        r"""Sets the ipv6_address of this ShowLoadBalancerPortsRequest.

        **参数解释**：负载均衡器占用的IPv6地址。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*ipv6_address=xxx&ipv6_address=xxx*。

        :param ipv6_address: The ipv6_address of this ShowLoadBalancerPortsRequest.
        :type ipv6_address: list[str]
        """
        self._ipv6_address = ipv6_address

    @property
    def type(self):
        r"""Gets the type of this ShowLoadBalancerPortsRequest.

        **参数解释**：子网端口类型。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*type=xxx&type=xxx*。

        :return: The type of this ShowLoadBalancerPortsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowLoadBalancerPortsRequest.

        **参数解释**：子网端口类型。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*type=xxx&type=xxx*。

        :param type: The type of this ShowLoadBalancerPortsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this ShowLoadBalancerPortsRequest.

        **参数解释**：子网端口所在下联面子网网络ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*virsubnet_id=xxx&virsubnet_id=xxx*。

        :return: The virsubnet_id of this ShowLoadBalancerPortsRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this ShowLoadBalancerPortsRequest.

        **参数解释**：子网端口所在下联面子网网络ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  支持多值查询，查询条件格式：*virsubnet_id=xxx&virsubnet_id=xxx*。

        :param virsubnet_id: The virsubnet_id of this ShowLoadBalancerPortsRequest.
        :type virsubnet_id: list[str]
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
        if not isinstance(other, ShowLoadBalancerPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
