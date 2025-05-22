# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_list': 'list[ClusterNodeInfo]',
        'count': 'int',
        'failed_count': 'int'
    }

    attribute_map = {
        'node_list': 'node_list',
        'count': 'count',
        'failed_count': 'failed_count'
    }

    def __init__(self, node_list=None, count=None, failed_count=None):
        r"""ListClusterNodesResponse

        The model defined in huaweicloud sdk

        :param node_list: **参数解释**： 集群节点列表。 **取值范围**： 不涉及。
        :type node_list: list[:class:`huaweicloudsdkdws.v2.ClusterNodeInfo`]
        :param count: **参数解释**： 集群节点总数。 **取值范围**： 大于0的整数。
        :type count: int
        :param failed_count: **参数解释**： 逻辑集群节点失败总数。一般为0。 **取值范围**： 大于等于0的整数。
        :type failed_count: int
        """
        
        super(ListClusterNodesResponse, self).__init__()

        self._node_list = None
        self._count = None
        self._failed_count = None
        self.discriminator = None

        if node_list is not None:
            self.node_list = node_list
        if count is not None:
            self.count = count
        if failed_count is not None:
            self.failed_count = failed_count

    @property
    def node_list(self):
        r"""Gets the node_list of this ListClusterNodesResponse.

        **参数解释**： 集群节点列表。 **取值范围**： 不涉及。

        :return: The node_list of this ListClusterNodesResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ClusterNodeInfo`]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this ListClusterNodesResponse.

        **参数解释**： 集群节点列表。 **取值范围**： 不涉及。

        :param node_list: The node_list of this ListClusterNodesResponse.
        :type node_list: list[:class:`huaweicloudsdkdws.v2.ClusterNodeInfo`]
        """
        self._node_list = node_list

    @property
    def count(self):
        r"""Gets the count of this ListClusterNodesResponse.

        **参数解释**： 集群节点总数。 **取值范围**： 大于0的整数。

        :return: The count of this ListClusterNodesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListClusterNodesResponse.

        **参数解释**： 集群节点总数。 **取值范围**： 大于0的整数。

        :param count: The count of this ListClusterNodesResponse.
        :type count: int
        """
        self._count = count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this ListClusterNodesResponse.

        **参数解释**： 逻辑集群节点失败总数。一般为0。 **取值范围**： 大于等于0的整数。

        :return: The failed_count of this ListClusterNodesResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this ListClusterNodesResponse.

        **参数解释**： 逻辑集群节点失败总数。一般为0。 **取值范围**： 大于等于0的整数。

        :param failed_count: The failed_count of this ListClusterNodesResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

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
        if not isinstance(other, ListClusterNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
