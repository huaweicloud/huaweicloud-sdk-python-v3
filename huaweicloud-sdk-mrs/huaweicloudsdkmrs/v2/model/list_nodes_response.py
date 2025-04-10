# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[ClusterNode]',
        'node_total': 'int'
    }

    attribute_map = {
        'nodes': 'nodes',
        'node_total': 'node_total'
    }

    def __init__(self, nodes=None, node_total=None):
        r"""ListNodesResponse

        The model defined in huaweicloud sdk

        :param nodes: 节点列表。
        :type nodes: list[:class:`huaweicloudsdkmrs.v2.ClusterNode`]
        :param node_total: 节点数。
        :type node_total: int
        """
        
        super(ListNodesResponse, self).__init__()

        self._nodes = None
        self._node_total = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if node_total is not None:
            self.node_total = node_total

    @property
    def nodes(self):
        r"""Gets the nodes of this ListNodesResponse.

        节点列表。

        :return: The nodes of this ListNodesResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.ClusterNode`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ListNodesResponse.

        节点列表。

        :param nodes: The nodes of this ListNodesResponse.
        :type nodes: list[:class:`huaweicloudsdkmrs.v2.ClusterNode`]
        """
        self._nodes = nodes

    @property
    def node_total(self):
        r"""Gets the node_total of this ListNodesResponse.

        节点数。

        :return: The node_total of this ListNodesResponse.
        :rtype: int
        """
        return self._node_total

    @node_total.setter
    def node_total(self, node_total):
        r"""Sets the node_total of this ListNodesResponse.

        节点数。

        :param node_total: The node_total of this ListNodesResponse.
        :type node_total: int
        """
        self._node_total = node_total

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
        if not isinstance(other, ListNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
