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
        'nodes': 'list[NodeList]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'nodes': 'nodes',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, nodes=None, offset=None, limit=None, total=None):
        r"""ListNodesResponse

        The model defined in huaweicloud sdk

        :param nodes: DDM实例节点信息列表的集合。
        :type nodes: list[:class:`huaweicloudsdkddm.v1.NodeList`]
        :param offset: 分页参数: 起始值。
        :type offset: int
        :param limit: 分页参数：每页多少条。
        :type limit: int
        :param total: DDM实例节点个数。
        :type total: int
        """
        
        super(ListNodesResponse, self).__init__()

        self._nodes = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def nodes(self):
        r"""Gets the nodes of this ListNodesResponse.

        DDM实例节点信息列表的集合。

        :return: The nodes of this ListNodesResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.NodeList`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ListNodesResponse.

        DDM实例节点信息列表的集合。

        :param nodes: The nodes of this ListNodesResponse.
        :type nodes: list[:class:`huaweicloudsdkddm.v1.NodeList`]
        """
        self._nodes = nodes

    @property
    def offset(self):
        r"""Gets the offset of this ListNodesResponse.

        分页参数: 起始值。

        :return: The offset of this ListNodesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNodesResponse.

        分页参数: 起始值。

        :param offset: The offset of this ListNodesResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListNodesResponse.

        分页参数：每页多少条。

        :return: The limit of this ListNodesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNodesResponse.

        分页参数：每页多少条。

        :param limit: The limit of this ListNodesResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ListNodesResponse.

        DDM实例节点个数。

        :return: The total of this ListNodesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListNodesResponse.

        DDM实例节点个数。

        :param total: The total of this ListNodesResponse.
        :type total: int
        """
        self._total = total

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
