# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterNodesRequest:

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
        'deleted': 'str',
        'node_ids': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'filter_by': 'str',
        'filter': 'str',
        'order_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'deleted': 'deleted',
        'node_ids': 'node_ids',
        'offset': 'offset',
        'limit': 'limit',
        'filter_by': 'filter_by',
        'filter': 'filter',
        'order_by': 'order_by',
        'order': 'order'
    }

    def __init__(self, cluster_id=None, deleted=None, node_ids=None, offset=None, limit=None, filter_by=None, filter=None, order_by=None, order=None):
        """ListClusterNodesRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param deleted: 是否被删除，true/false
        :type deleted: str
        :param node_ids: 节点ID列表
        :type node_ids: list[str]
        :param offset: 分页查询，偏移
        :type offset: int
        :param limit: 分页查询，每页显示的条目数量
        :type limit: int
        :param filter_by: 过滤字段
        :type filter_by: str
        :param filter: 过滤字段内容
        :type filter: str
        :param order_by: 排序字段
        :type order_by: str
        :param order: 排序：升序/降序
        :type order: str
        """
        
        

        self._cluster_id = None
        self._deleted = None
        self._node_ids = None
        self._offset = None
        self._limit = None
        self._filter_by = None
        self._filter = None
        self._order_by = None
        self._order = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if deleted is not None:
            self.deleted = deleted
        if node_ids is not None:
            self.node_ids = node_ids
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if filter_by is not None:
            self.filter_by = filter_by
        if filter is not None:
            self.filter = filter
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListClusterNodesRequest.

        集群ID

        :return: The cluster_id of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListClusterNodesRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListClusterNodesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def deleted(self):
        """Gets the deleted of this ListClusterNodesRequest.

        是否被删除，true/false

        :return: The deleted of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ListClusterNodesRequest.

        是否被删除，true/false

        :param deleted: The deleted of this ListClusterNodesRequest.
        :type deleted: str
        """
        self._deleted = deleted

    @property
    def node_ids(self):
        """Gets the node_ids of this ListClusterNodesRequest.

        节点ID列表

        :return: The node_ids of this ListClusterNodesRequest.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this ListClusterNodesRequest.

        节点ID列表

        :param node_ids: The node_ids of this ListClusterNodesRequest.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def offset(self):
        """Gets the offset of this ListClusterNodesRequest.

        分页查询，偏移

        :return: The offset of this ListClusterNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListClusterNodesRequest.

        分页查询，偏移

        :param offset: The offset of this ListClusterNodesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListClusterNodesRequest.

        分页查询，每页显示的条目数量

        :return: The limit of this ListClusterNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListClusterNodesRequest.

        分页查询，每页显示的条目数量

        :param limit: The limit of this ListClusterNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def filter_by(self):
        """Gets the filter_by of this ListClusterNodesRequest.

        过滤字段

        :return: The filter_by of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._filter_by

    @filter_by.setter
    def filter_by(self, filter_by):
        """Sets the filter_by of this ListClusterNodesRequest.

        过滤字段

        :param filter_by: The filter_by of this ListClusterNodesRequest.
        :type filter_by: str
        """
        self._filter_by = filter_by

    @property
    def filter(self):
        """Gets the filter of this ListClusterNodesRequest.

        过滤字段内容

        :return: The filter of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListClusterNodesRequest.

        过滤字段内容

        :param filter: The filter of this ListClusterNodesRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def order_by(self):
        """Gets the order_by of this ListClusterNodesRequest.

        排序字段

        :return: The order_by of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListClusterNodesRequest.

        排序字段

        :param order_by: The order_by of this ListClusterNodesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        """Gets the order of this ListClusterNodesRequest.

        排序：升序/降序

        :return: The order of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListClusterNodesRequest.

        排序：升序/降序

        :param order: The order of this ListClusterNodesRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListClusterNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
