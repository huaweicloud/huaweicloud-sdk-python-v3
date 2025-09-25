# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReadonlyNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[ListReadonlyNodesResult]',
        'max_readonly_node_num': 'int'
    }

    attribute_map = {
        'nodes': 'nodes',
        'max_readonly_node_num': 'max_readonly_node_num'
    }

    def __init__(self, nodes=None, max_readonly_node_num=None):
        r"""ListReadonlyNodesResponse

        The model defined in huaweicloud sdk

        :param nodes: **参数解释**: 只读节点列表。 **约束限制**: 不涉及。
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListReadonlyNodesResult`]
        :param max_readonly_node_num: **参数解释**: 数据库名称。 **取值范围**: 不涉及。
        :type max_readonly_node_num: int
        """
        
        super(ListReadonlyNodesResponse, self).__init__()

        self._nodes = None
        self._max_readonly_node_num = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if max_readonly_node_num is not None:
            self.max_readonly_node_num = max_readonly_node_num

    @property
    def nodes(self):
        r"""Gets the nodes of this ListReadonlyNodesResponse.

        **参数解释**: 只读节点列表。 **约束限制**: 不涉及。

        :return: The nodes of this ListReadonlyNodesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListReadonlyNodesResult`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ListReadonlyNodesResponse.

        **参数解释**: 只读节点列表。 **约束限制**: 不涉及。

        :param nodes: The nodes of this ListReadonlyNodesResponse.
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListReadonlyNodesResult`]
        """
        self._nodes = nodes

    @property
    def max_readonly_node_num(self):
        r"""Gets the max_readonly_node_num of this ListReadonlyNodesResponse.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :return: The max_readonly_node_num of this ListReadonlyNodesResponse.
        :rtype: int
        """
        return self._max_readonly_node_num

    @max_readonly_node_num.setter
    def max_readonly_node_num(self, max_readonly_node_num):
        r"""Sets the max_readonly_node_num of this ListReadonlyNodesResponse.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :param max_readonly_node_num: The max_readonly_node_num of this ListReadonlyNodesResponse.
        :type max_readonly_node_num: int
        """
        self._max_readonly_node_num = max_readonly_node_num

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
        if not isinstance(other, ListReadonlyNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
