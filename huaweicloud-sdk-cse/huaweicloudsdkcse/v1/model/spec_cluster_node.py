# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpecClusterNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_nodes': 'list[ClusterNode]'
    }

    attribute_map = {
        'cluster_nodes': 'cluster_nodes'
    }

    def __init__(self, cluster_nodes=None):
        """SpecClusterNode

        The model defined in huaweicloud sdk

        :param cluster_nodes: CCE节点信息。
        :type cluster_nodes: list[:class:`huaweicloudsdkcse.v1.ClusterNode`]
        """
        
        

        self._cluster_nodes = None
        self.discriminator = None

        if cluster_nodes is not None:
            self.cluster_nodes = cluster_nodes

    @property
    def cluster_nodes(self):
        """Gets the cluster_nodes of this SpecClusterNode.

        CCE节点信息。

        :return: The cluster_nodes of this SpecClusterNode.
        :rtype: list[:class:`huaweicloudsdkcse.v1.ClusterNode`]
        """
        return self._cluster_nodes

    @cluster_nodes.setter
    def cluster_nodes(self, cluster_nodes):
        """Sets the cluster_nodes of this SpecClusterNode.

        CCE节点信息。

        :param cluster_nodes: The cluster_nodes of this SpecClusterNode.
        :type cluster_nodes: list[:class:`huaweicloudsdkcse.v1.ClusterNode`]
        """
        self._cluster_nodes = cluster_nodes

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
        if not isinstance(other, SpecClusterNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
