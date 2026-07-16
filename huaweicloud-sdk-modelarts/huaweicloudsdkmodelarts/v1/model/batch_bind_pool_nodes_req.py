# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBindPoolNodesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[BindNodeItem]',
        'drain': 'bool'
    }

    attribute_map = {
        'nodes': 'nodes',
        'drain': 'drain'
    }

    def __init__(self, nodes=None, drain=None):
        r"""BatchBindPoolNodesReq

        The model defined in huaweicloud sdk

        :param nodes: **参数解释**：需要进行换绑的节点列表。 **约束限制**：不涉及。
        :type nodes: list[:class:`huaweicloudsdkmodelarts.v1.BindNodeItem`]
        :param drain: **参数解释**：是否对换绑的节点进行排水。 **约束限制**：不涉及。 **取值范围**： - true：排水 - false：不排水 **默认取值**：不涉及。
        :type drain: bool
        """
        
        

        self._nodes = None
        self._drain = None
        self.discriminator = None

        self.nodes = nodes
        if drain is not None:
            self.drain = drain

    @property
    def nodes(self):
        r"""Gets the nodes of this BatchBindPoolNodesReq.

        **参数解释**：需要进行换绑的节点列表。 **约束限制**：不涉及。

        :return: The nodes of this BatchBindPoolNodesReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.BindNodeItem`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this BatchBindPoolNodesReq.

        **参数解释**：需要进行换绑的节点列表。 **约束限制**：不涉及。

        :param nodes: The nodes of this BatchBindPoolNodesReq.
        :type nodes: list[:class:`huaweicloudsdkmodelarts.v1.BindNodeItem`]
        """
        self._nodes = nodes

    @property
    def drain(self):
        r"""Gets the drain of this BatchBindPoolNodesReq.

        **参数解释**：是否对换绑的节点进行排水。 **约束限制**：不涉及。 **取值范围**： - true：排水 - false：不排水 **默认取值**：不涉及。

        :return: The drain of this BatchBindPoolNodesReq.
        :rtype: bool
        """
        return self._drain

    @drain.setter
    def drain(self, drain):
        r"""Sets the drain of this BatchBindPoolNodesReq.

        **参数解释**：是否对换绑的节点进行排水。 **约束限制**：不涉及。 **取值范围**： - true：排水 - false：不排水 **默认取值**：不涉及。

        :param drain: The drain of this BatchBindPoolNodesReq.
        :type drain: bool
        """
        self._drain = drain

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
        if not isinstance(other, BatchBindPoolNodesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
