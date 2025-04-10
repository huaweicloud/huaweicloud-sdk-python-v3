# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'node_group': 'str',
        'limit': 'int',
        'offset': 'int',
        'node_name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'query_node_detail': 'bool',
        'query_ecs_detail': 'bool',
        'internal_ip': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'node_group': 'node_group',
        'limit': 'limit',
        'offset': 'offset',
        'node_name': 'node_name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'query_node_detail': 'query_node_detail',
        'query_ecs_detail': 'query_ecs_detail',
        'internal_ip': 'internal_ip'
    }

    def __init__(self, cluster_id=None, node_group=None, limit=None, offset=None, node_name=None, sort_key=None, sort_dir=None, query_node_detail=None, query_ecs_detail=None, internal_ip=None):
        r"""ListNodesRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param node_group: 要查询的节点组名称。
        :type node_group: str
        :param limit: 返回结果中每页显示条数。缺省值：10。
        :type limit: int
        :param offset: 表示作业列表从该偏移量开始查询。缺省值：1。
        :type offset: int
        :param node_name: 指定节点名称，支持模糊搜索。
        :type node_name: str
        :param sort_key: 排序键，支持对节点名称排序。
        :type sort_key: str
        :param sort_dir: 列表排序方式，desc为降序，asc为升序。
        :type sort_dir: str
        :param query_node_detail: 是否查询节点详情。该字段设为true时可能会影响接口性能。
        :type query_node_detail: bool
        :param query_ecs_detail: 是否查询ECS详情信息，会涉及对ECS接口调用。
        :type query_ecs_detail: bool
        :param internal_ip: 指定内网IP。
        :type internal_ip: str
        """
        
        

        self._cluster_id = None
        self._node_group = None
        self._limit = None
        self._offset = None
        self._node_name = None
        self._sort_key = None
        self._sort_dir = None
        self._query_node_detail = None
        self._query_ecs_detail = None
        self._internal_ip = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if node_group is not None:
            self.node_group = node_group
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if node_name is not None:
            self.node_name = node_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if query_node_detail is not None:
            self.query_node_detail = query_node_detail
        if query_ecs_detail is not None:
            self.query_ecs_detail = query_ecs_detail
        if internal_ip is not None:
            self.internal_ip = internal_ip

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListNodesRequest.

        集群ID。

        :return: The cluster_id of this ListNodesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListNodesRequest.

        集群ID。

        :param cluster_id: The cluster_id of this ListNodesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def node_group(self):
        r"""Gets the node_group of this ListNodesRequest.

        要查询的节点组名称。

        :return: The node_group of this ListNodesRequest.
        :rtype: str
        """
        return self._node_group

    @node_group.setter
    def node_group(self, node_group):
        r"""Sets the node_group of this ListNodesRequest.

        要查询的节点组名称。

        :param node_group: The node_group of this ListNodesRequest.
        :type node_group: str
        """
        self._node_group = node_group

    @property
    def limit(self):
        r"""Gets the limit of this ListNodesRequest.

        返回结果中每页显示条数。缺省值：10。

        :return: The limit of this ListNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNodesRequest.

        返回结果中每页显示条数。缺省值：10。

        :param limit: The limit of this ListNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListNodesRequest.

        表示作业列表从该偏移量开始查询。缺省值：1。

        :return: The offset of this ListNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNodesRequest.

        表示作业列表从该偏移量开始查询。缺省值：1。

        :param offset: The offset of this ListNodesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def node_name(self):
        r"""Gets the node_name of this ListNodesRequest.

        指定节点名称，支持模糊搜索。

        :return: The node_name of this ListNodesRequest.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ListNodesRequest.

        指定节点名称，支持模糊搜索。

        :param node_name: The node_name of this ListNodesRequest.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListNodesRequest.

        排序键，支持对节点名称排序。

        :return: The sort_key of this ListNodesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListNodesRequest.

        排序键，支持对节点名称排序。

        :param sort_key: The sort_key of this ListNodesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListNodesRequest.

        列表排序方式，desc为降序，asc为升序。

        :return: The sort_dir of this ListNodesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListNodesRequest.

        列表排序方式，desc为降序，asc为升序。

        :param sort_dir: The sort_dir of this ListNodesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def query_node_detail(self):
        r"""Gets the query_node_detail of this ListNodesRequest.

        是否查询节点详情。该字段设为true时可能会影响接口性能。

        :return: The query_node_detail of this ListNodesRequest.
        :rtype: bool
        """
        return self._query_node_detail

    @query_node_detail.setter
    def query_node_detail(self, query_node_detail):
        r"""Sets the query_node_detail of this ListNodesRequest.

        是否查询节点详情。该字段设为true时可能会影响接口性能。

        :param query_node_detail: The query_node_detail of this ListNodesRequest.
        :type query_node_detail: bool
        """
        self._query_node_detail = query_node_detail

    @property
    def query_ecs_detail(self):
        r"""Gets the query_ecs_detail of this ListNodesRequest.

        是否查询ECS详情信息，会涉及对ECS接口调用。

        :return: The query_ecs_detail of this ListNodesRequest.
        :rtype: bool
        """
        return self._query_ecs_detail

    @query_ecs_detail.setter
    def query_ecs_detail(self, query_ecs_detail):
        r"""Sets the query_ecs_detail of this ListNodesRequest.

        是否查询ECS详情信息，会涉及对ECS接口调用。

        :param query_ecs_detail: The query_ecs_detail of this ListNodesRequest.
        :type query_ecs_detail: bool
        """
        self._query_ecs_detail = query_ecs_detail

    @property
    def internal_ip(self):
        r"""Gets the internal_ip of this ListNodesRequest.

        指定内网IP。

        :return: The internal_ip of this ListNodesRequest.
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        r"""Sets the internal_ip of this ListNodesRequest.

        指定内网IP。

        :param internal_ip: The internal_ip of this ListNodesRequest.
        :type internal_ip: str
        """
        self._internal_ip = internal_ip

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
        if not isinstance(other, ListNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
