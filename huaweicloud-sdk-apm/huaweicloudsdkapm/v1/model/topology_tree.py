# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopologyTree:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tree': 'list[TreeNode]'
    }

    attribute_map = {
        'tree': 'tree'
    }

    def __init__(self, tree=None):
        r"""TopologyTree

        The model defined in huaweicloud sdk

        :param tree: 拓扑树节点。
        :type tree: list[:class:`huaweicloudsdkapm.v1.TreeNode`]
        """
        
        

        self._tree = None
        self.discriminator = None

        if tree is not None:
            self.tree = tree

    @property
    def tree(self):
        r"""Gets the tree of this TopologyTree.

        拓扑树节点。

        :return: The tree of this TopologyTree.
        :rtype: list[:class:`huaweicloudsdkapm.v1.TreeNode`]
        """
        return self._tree

    @tree.setter
    def tree(self, tree):
        r"""Sets the tree of this TopologyTree.

        拓扑树节点。

        :param tree: The tree of this TopologyTree.
        :type tree: list[:class:`huaweicloudsdkapm.v1.TreeNode`]
        """
        self._tree = tree

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
        if not isinstance(other, TopologyTree):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
