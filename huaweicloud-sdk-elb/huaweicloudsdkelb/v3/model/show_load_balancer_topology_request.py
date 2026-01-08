# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLoadBalancerTopologyRequest:

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
        'listener_id': 'str',
        'pool_id': 'str',
        'listener_name': 'str',
        'listener_protocol': 'str',
        'listener_protocol_port': 'int',
        'pool_name': 'str'
    }

    attribute_map = {
        'loadbalancer_id': 'loadbalancer_id',
        'listener_id': 'listener_id',
        'pool_id': 'pool_id',
        'listener_name': 'listener_name',
        'listener_protocol': 'listener_protocol',
        'listener_protocol_port': 'listener_protocol_port',
        'pool_name': 'pool_name'
    }

    def __init__(self, loadbalancer_id=None, listener_id=None, pool_id=None, listener_name=None, listener_protocol=None, listener_protocol_port=None, pool_name=None):
        r"""ShowLoadBalancerTopologyRequest

        The model defined in huaweicloud sdk

        :param loadbalancer_id: **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: str
        :param listener_id: 监听器的ID。  支持多值查询，查询条件格式：*listener_id&#x3D;xxx&amp;listener_id&#x3D;xxx*。
        :type listener_id: str
        :param pool_id: 后端服务器组的ID。  支持多值查询，查询条件格式：*pool_id&#x3D;xxx&amp;pool_id&#x3D;xxx*。
        :type pool_id: str
        :param listener_name: 监听器的名称。  支持多值查询，查询条件格式：*listener_name&#x3D;xxx&amp;listener_name&#x3D;xxx*。
        :type listener_name: str
        :param listener_protocol: 监听器的协议。  支持多值查询，查询条件格式：*listener_protocol&#x3D;xxx&amp;listener_protocol&#x3D;xxx*。
        :type listener_protocol: str
        :param listener_protocol_port: 监听器的监听端口。  支持多值查询，查询条件格式：*listener_protocol_port&#x3D;xxx&amp;listener_protocol_port&#x3D;xxx*。
        :type listener_protocol_port: int
        :param pool_name: 后端服务器组的名称。  支持多值查询，查询条件格式：*pool_name&#x3D;xxx&amp;pool_name&#x3D;xxx*。
        :type pool_name: str
        """
        
        

        self._loadbalancer_id = None
        self._listener_id = None
        self._pool_id = None
        self._listener_name = None
        self._listener_protocol = None
        self._listener_protocol_port = None
        self._pool_name = None
        self.discriminator = None

        self.loadbalancer_id = loadbalancer_id
        if listener_id is not None:
            self.listener_id = listener_id
        if pool_id is not None:
            self.pool_id = pool_id
        if listener_name is not None:
            self.listener_name = listener_name
        if listener_protocol is not None:
            self.listener_protocol = listener_protocol
        if listener_protocol_port is not None:
            self.listener_protocol_port = listener_protocol_port
        if pool_name is not None:
            self.pool_name = pool_name

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ShowLoadBalancerTopologyRequest.

        **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this ShowLoadBalancerTopologyRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ShowLoadBalancerTopologyRequest.

        **参数解释**：负载均衡器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this ShowLoadBalancerTopologyRequest.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def listener_id(self):
        r"""Gets the listener_id of this ShowLoadBalancerTopologyRequest.

        监听器的ID。  支持多值查询，查询条件格式：*listener_id=xxx&listener_id=xxx*。

        :return: The listener_id of this ShowLoadBalancerTopologyRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this ShowLoadBalancerTopologyRequest.

        监听器的ID。  支持多值查询，查询条件格式：*listener_id=xxx&listener_id=xxx*。

        :param listener_id: The listener_id of this ShowLoadBalancerTopologyRequest.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ShowLoadBalancerTopologyRequest.

        后端服务器组的ID。  支持多值查询，查询条件格式：*pool_id=xxx&pool_id=xxx*。

        :return: The pool_id of this ShowLoadBalancerTopologyRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ShowLoadBalancerTopologyRequest.

        后端服务器组的ID。  支持多值查询，查询条件格式：*pool_id=xxx&pool_id=xxx*。

        :param pool_id: The pool_id of this ShowLoadBalancerTopologyRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def listener_name(self):
        r"""Gets the listener_name of this ShowLoadBalancerTopologyRequest.

        监听器的名称。  支持多值查询，查询条件格式：*listener_name=xxx&listener_name=xxx*。

        :return: The listener_name of this ShowLoadBalancerTopologyRequest.
        :rtype: str
        """
        return self._listener_name

    @listener_name.setter
    def listener_name(self, listener_name):
        r"""Sets the listener_name of this ShowLoadBalancerTopologyRequest.

        监听器的名称。  支持多值查询，查询条件格式：*listener_name=xxx&listener_name=xxx*。

        :param listener_name: The listener_name of this ShowLoadBalancerTopologyRequest.
        :type listener_name: str
        """
        self._listener_name = listener_name

    @property
    def listener_protocol(self):
        r"""Gets the listener_protocol of this ShowLoadBalancerTopologyRequest.

        监听器的协议。  支持多值查询，查询条件格式：*listener_protocol=xxx&listener_protocol=xxx*。

        :return: The listener_protocol of this ShowLoadBalancerTopologyRequest.
        :rtype: str
        """
        return self._listener_protocol

    @listener_protocol.setter
    def listener_protocol(self, listener_protocol):
        r"""Sets the listener_protocol of this ShowLoadBalancerTopologyRequest.

        监听器的协议。  支持多值查询，查询条件格式：*listener_protocol=xxx&listener_protocol=xxx*。

        :param listener_protocol: The listener_protocol of this ShowLoadBalancerTopologyRequest.
        :type listener_protocol: str
        """
        self._listener_protocol = listener_protocol

    @property
    def listener_protocol_port(self):
        r"""Gets the listener_protocol_port of this ShowLoadBalancerTopologyRequest.

        监听器的监听端口。  支持多值查询，查询条件格式：*listener_protocol_port=xxx&listener_protocol_port=xxx*。

        :return: The listener_protocol_port of this ShowLoadBalancerTopologyRequest.
        :rtype: int
        """
        return self._listener_protocol_port

    @listener_protocol_port.setter
    def listener_protocol_port(self, listener_protocol_port):
        r"""Sets the listener_protocol_port of this ShowLoadBalancerTopologyRequest.

        监听器的监听端口。  支持多值查询，查询条件格式：*listener_protocol_port=xxx&listener_protocol_port=xxx*。

        :param listener_protocol_port: The listener_protocol_port of this ShowLoadBalancerTopologyRequest.
        :type listener_protocol_port: int
        """
        self._listener_protocol_port = listener_protocol_port

    @property
    def pool_name(self):
        r"""Gets the pool_name of this ShowLoadBalancerTopologyRequest.

        后端服务器组的名称。  支持多值查询，查询条件格式：*pool_name=xxx&pool_name=xxx*。

        :return: The pool_name of this ShowLoadBalancerTopologyRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this ShowLoadBalancerTopologyRequest.

        后端服务器组的名称。  支持多值查询，查询条件格式：*pool_name=xxx&pool_name=xxx*。

        :param pool_name: The pool_name of this ShowLoadBalancerTopologyRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowLoadBalancerTopologyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
