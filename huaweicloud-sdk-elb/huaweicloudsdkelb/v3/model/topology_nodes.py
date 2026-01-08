# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopologyNodes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'loadbalancers': 'list[LoadBalancerNode]',
        'eips': 'list[EipNode]',
        'listeners': 'list[ListenerNode]',
        'pools': 'list[PoolNode]'
    }

    attribute_map = {
        'loadbalancers': 'loadbalancers',
        'eips': 'eips',
        'listeners': 'listeners',
        'pools': 'pools'
    }

    def __init__(self, loadbalancers=None, eips=None, listeners=None, pools=None):
        r"""TopologyNodes

        The model defined in huaweicloud sdk

        :param loadbalancers: **取值范围**：拓扑LB节点信息。
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerNode`]
        :param eips: **取值范围**：拓扑EIP节点信息。
        :type eips: list[:class:`huaweicloudsdkelb.v3.EipNode`]
        :param listeners: **取值范围**：拓扑监听器节点信息。
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerNode`]
        :param pools: **取值范围**：拓扑后端服务器组节点信息。
        :type pools: list[:class:`huaweicloudsdkelb.v3.PoolNode`]
        """
        
        

        self._loadbalancers = None
        self._eips = None
        self._listeners = None
        self._pools = None
        self.discriminator = None

        self.loadbalancers = loadbalancers
        self.eips = eips
        self.listeners = listeners
        self.pools = pools

    @property
    def loadbalancers(self):
        r"""Gets the loadbalancers of this TopologyNodes.

        **取值范围**：拓扑LB节点信息。

        :return: The loadbalancers of this TopologyNodes.
        :rtype: list[:class:`huaweicloudsdkelb.v3.LoadBalancerNode`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        r"""Sets the loadbalancers of this TopologyNodes.

        **取值范围**：拓扑LB节点信息。

        :param loadbalancers: The loadbalancers of this TopologyNodes.
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.LoadBalancerNode`]
        """
        self._loadbalancers = loadbalancers

    @property
    def eips(self):
        r"""Gets the eips of this TopologyNodes.

        **取值范围**：拓扑EIP节点信息。

        :return: The eips of this TopologyNodes.
        :rtype: list[:class:`huaweicloudsdkelb.v3.EipNode`]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        r"""Sets the eips of this TopologyNodes.

        **取值范围**：拓扑EIP节点信息。

        :param eips: The eips of this TopologyNodes.
        :type eips: list[:class:`huaweicloudsdkelb.v3.EipNode`]
        """
        self._eips = eips

    @property
    def listeners(self):
        r"""Gets the listeners of this TopologyNodes.

        **取值范围**：拓扑监听器节点信息。

        :return: The listeners of this TopologyNodes.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListenerNode`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this TopologyNodes.

        **取值范围**：拓扑监听器节点信息。

        :param listeners: The listeners of this TopologyNodes.
        :type listeners: list[:class:`huaweicloudsdkelb.v3.ListenerNode`]
        """
        self._listeners = listeners

    @property
    def pools(self):
        r"""Gets the pools of this TopologyNodes.

        **取值范围**：拓扑后端服务器组节点信息。

        :return: The pools of this TopologyNodes.
        :rtype: list[:class:`huaweicloudsdkelb.v3.PoolNode`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        r"""Sets the pools of this TopologyNodes.

        **取值范围**：拓扑后端服务器组节点信息。

        :param pools: The pools of this TopologyNodes.
        :type pools: list[:class:`huaweicloudsdkelb.v3.PoolNode`]
        """
        self._pools = pools

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
        if not isinstance(other, TopologyNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
