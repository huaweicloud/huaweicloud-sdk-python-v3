# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceNodesInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_count': 'int',
        'nodes': 'list[NodesInfoResp]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_count': 'node_count',
        'nodes': 'nodes'
    }

    def __init__(self, instance_id=None, node_count=None, nodes=None):
        r"""InstanceNodesInfoResp

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param node_count: 当前实例节点总数
        :type node_count: int
        :param nodes: 节点详情。
        :type nodes: list[:class:`huaweicloudsdkdcs.v2.NodesInfoResp`]
        """
        
        

        self._instance_id = None
        self._node_count = None
        self._nodes = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if node_count is not None:
            self.node_count = node_count
        if nodes is not None:
            self.nodes = nodes

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceNodesInfoResp.

        实例ID

        :return: The instance_id of this InstanceNodesInfoResp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceNodesInfoResp.

        实例ID

        :param instance_id: The instance_id of this InstanceNodesInfoResp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_count(self):
        r"""Gets the node_count of this InstanceNodesInfoResp.

        当前实例节点总数

        :return: The node_count of this InstanceNodesInfoResp.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        r"""Sets the node_count of this InstanceNodesInfoResp.

        当前实例节点总数

        :param node_count: The node_count of this InstanceNodesInfoResp.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def nodes(self):
        r"""Gets the nodes of this InstanceNodesInfoResp.

        节点详情。

        :return: The nodes of this InstanceNodesInfoResp.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.NodesInfoResp`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this InstanceNodesInfoResp.

        节点详情。

        :param nodes: The nodes of this InstanceNodesInfoResp.
        :type nodes: list[:class:`huaweicloudsdkdcs.v2.NodesInfoResp`]
        """
        self._nodes = nodes

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
        if not isinstance(other, InstanceNodesInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
