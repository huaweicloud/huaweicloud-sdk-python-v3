# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancerTopologyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'TopologyNodes',
        'edges': 'list[TopologyEdge]',
        'labels': 'TopologyLabels'
    }

    attribute_map = {
        'nodes': 'nodes',
        'edges': 'edges',
        'labels': 'labels'
    }

    def __init__(self, nodes=None, edges=None, labels=None):
        r"""LoadBalancerTopologyResult

        The model defined in huaweicloud sdk

        :param nodes: 
        :type nodes: :class:`huaweicloudsdkelb.v3.TopologyNodes`
        :param edges: **参数解释**：拓扑边的信息
        :type edges: list[:class:`huaweicloudsdkelb.v3.TopologyEdge`]
        :param labels: 
        :type labels: :class:`huaweicloudsdkelb.v3.TopologyLabels`
        """
        
        

        self._nodes = None
        self._edges = None
        self._labels = None
        self.discriminator = None

        self.nodes = nodes
        self.edges = edges
        self.labels = labels

    @property
    def nodes(self):
        r"""Gets the nodes of this LoadBalancerTopologyResult.

        :return: The nodes of this LoadBalancerTopologyResult.
        :rtype: :class:`huaweicloudsdkelb.v3.TopologyNodes`
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this LoadBalancerTopologyResult.

        :param nodes: The nodes of this LoadBalancerTopologyResult.
        :type nodes: :class:`huaweicloudsdkelb.v3.TopologyNodes`
        """
        self._nodes = nodes

    @property
    def edges(self):
        r"""Gets the edges of this LoadBalancerTopologyResult.

        **参数解释**：拓扑边的信息

        :return: The edges of this LoadBalancerTopologyResult.
        :rtype: list[:class:`huaweicloudsdkelb.v3.TopologyEdge`]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        r"""Sets the edges of this LoadBalancerTopologyResult.

        **参数解释**：拓扑边的信息

        :param edges: The edges of this LoadBalancerTopologyResult.
        :type edges: list[:class:`huaweicloudsdkelb.v3.TopologyEdge`]
        """
        self._edges = edges

    @property
    def labels(self):
        r"""Gets the labels of this LoadBalancerTopologyResult.

        :return: The labels of this LoadBalancerTopologyResult.
        :rtype: :class:`huaweicloudsdkelb.v3.TopologyLabels`
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this LoadBalancerTopologyResult.

        :param labels: The labels of this LoadBalancerTopologyResult.
        :type labels: :class:`huaweicloudsdkelb.v3.TopologyLabels`
        """
        self._labels = labels

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
        if not isinstance(other, LoadBalancerTopologyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
