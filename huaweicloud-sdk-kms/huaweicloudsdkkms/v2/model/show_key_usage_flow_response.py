# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKeyUsageFlowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[ShowKeyUsageFlowResponseBodyNodes]',
        'edges': 'list[ShowKeyUsageFlowResponseBodyEdges]'
    }

    attribute_map = {
        'nodes': 'nodes',
        'edges': 'edges'
    }

    def __init__(self, nodes=None, edges=None):
        r"""ShowKeyUsageFlowResponse

        The model defined in huaweicloud sdk

        :param nodes: **参数解释：** 使用流图节点列表，当前固定包含一个元素，元素内按类型分组展示各类节点 **取值范围：** 不涉及
        :type nodes: list[:class:`huaweicloudsdkkms.v2.ShowKeyUsageFlowResponseBodyNodes`]
        :param edges: **参数解释：** 使用流关系边列表，表示起点节点到策略节点、策略节点到密钥节点的使用流关系 **取值范围：** 不涉及
        :type edges: list[:class:`huaweicloudsdkkms.v2.ShowKeyUsageFlowResponseBodyEdges`]
        """
        
        super().__init__()

        self._nodes = None
        self._edges = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if edges is not None:
            self.edges = edges

    @property
    def nodes(self):
        r"""Gets the nodes of this ShowKeyUsageFlowResponse.

        **参数解释：** 使用流图节点列表，当前固定包含一个元素，元素内按类型分组展示各类节点 **取值范围：** 不涉及

        :return: The nodes of this ShowKeyUsageFlowResponse.
        :rtype: list[:class:`huaweicloudsdkkms.v2.ShowKeyUsageFlowResponseBodyNodes`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ShowKeyUsageFlowResponse.

        **参数解释：** 使用流图节点列表，当前固定包含一个元素，元素内按类型分组展示各类节点 **取值范围：** 不涉及

        :param nodes: The nodes of this ShowKeyUsageFlowResponse.
        :type nodes: list[:class:`huaweicloudsdkkms.v2.ShowKeyUsageFlowResponseBodyNodes`]
        """
        self._nodes = nodes

    @property
    def edges(self):
        r"""Gets the edges of this ShowKeyUsageFlowResponse.

        **参数解释：** 使用流关系边列表，表示起点节点到策略节点、策略节点到密钥节点的使用流关系 **取值范围：** 不涉及

        :return: The edges of this ShowKeyUsageFlowResponse.
        :rtype: list[:class:`huaweicloudsdkkms.v2.ShowKeyUsageFlowResponseBodyEdges`]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        r"""Sets the edges of this ShowKeyUsageFlowResponse.

        **参数解释：** 使用流关系边列表，表示起点节点到策略节点、策略节点到密钥节点的使用流关系 **取值范围：** 不涉及

        :param edges: The edges of this ShowKeyUsageFlowResponse.
        :type edges: list[:class:`huaweicloudsdkkms.v2.ShowKeyUsageFlowResponseBodyEdges`]
        """
        self._edges = edges

    def to_dict(self):
        import warnings
        warnings.warn("ShowKeyUsageFlowResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowKeyUsageFlowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
