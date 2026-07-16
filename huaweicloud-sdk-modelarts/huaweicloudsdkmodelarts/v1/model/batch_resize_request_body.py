# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResizeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[ResizeNodeInfo]',
        'source': 'NodeResizeParams',
        'target': 'NodeResizeParams'
    }

    attribute_map = {
        'nodes': 'nodes',
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, nodes=None, source=None, target=None):
        r"""BatchResizeRequestBody

        The model defined in huaweicloud sdk

        :param nodes: **参数解释**：扩缩容的超节点批次信息。 **约束限制**：单次最多50个超节点。
        :type nodes: list[:class:`huaweicloudsdkmodelarts.v1.ResizeNodeInfo`]
        :param source: 
        :type source: :class:`huaweicloudsdkmodelarts.v1.NodeResizeParams`
        :param target: 
        :type target: :class:`huaweicloudsdkmodelarts.v1.NodeResizeParams`
        """
        
        

        self._nodes = None
        self._source = None
        self._target = None
        self.discriminator = None

        self.nodes = nodes
        self.source = source
        self.target = target

    @property
    def nodes(self):
        r"""Gets the nodes of this BatchResizeRequestBody.

        **参数解释**：扩缩容的超节点批次信息。 **约束限制**：单次最多50个超节点。

        :return: The nodes of this BatchResizeRequestBody.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ResizeNodeInfo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this BatchResizeRequestBody.

        **参数解释**：扩缩容的超节点批次信息。 **约束限制**：单次最多50个超节点。

        :param nodes: The nodes of this BatchResizeRequestBody.
        :type nodes: list[:class:`huaweicloudsdkmodelarts.v1.ResizeNodeInfo`]
        """
        self._nodes = nodes

    @property
    def source(self):
        r"""Gets the source of this BatchResizeRequestBody.

        :return: The source of this BatchResizeRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeResizeParams`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this BatchResizeRequestBody.

        :param source: The source of this BatchResizeRequestBody.
        :type source: :class:`huaweicloudsdkmodelarts.v1.NodeResizeParams`
        """
        self._source = source

    @property
    def target(self):
        r"""Gets the target of this BatchResizeRequestBody.

        :return: The target of this BatchResizeRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeResizeParams`
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this BatchResizeRequestBody.

        :param target: The target of this BatchResizeRequestBody.
        :type target: :class:`huaweicloudsdkmodelarts.v1.NodeResizeParams`
        """
        self._target = target

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
        if not isinstance(other, BatchResizeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
