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
        'node_ids': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'filter_by': 'str',
        'filter': 'str',
        'order_by': 'str',
        'order': 'str',
        'deleted': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'node_ids': 'node_ids',
        'offset': 'offset',
        'limit': 'limit',
        'filter_by': 'filter_by',
        'filter': 'filter',
        'order_by': 'order_by',
        'order': 'order',
        'deleted': 'deleted'
    }

    def __init__(self, cluster_id=None, node_ids=None, offset=None, limit=None, filter_by=None, filter=None, order_by=None, order=None, deleted=None):
        r"""ListClusterNodesRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param node_ids: **参数解释**： 节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type node_ids: list[str]
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0
        :type offset: int
        :param limit: **参数解释**： 分页查询，每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100
        :type limit: int
        :param filter_by: **参数解释**： 过滤字段。 **约束限制**： 不涉及。 **取值范围**： instCreateType：根据资源状态过滤 status：根据节点状态过滤 **默认取值**： null
        :type filter_by: str
        :param filter: **参数解释**： 过滤字段内容。 **约束限制**： 不涉及。 **取值范围**： 当根据资源状态过滤时，可选如下值： - ALL：全部 - INST：已使用 - NODE：空虚 当根据节点状态过滤时，可选如下值： - ALL：全部 - CREATING：创建中 - FREE：空闲 - ACTIVE：可用 - FAILED：不可用 - UNKNOWN：未知 - CREATE_FAILED：创建失败 - DELETING：删除中 - DELETE_FAILED：删除失败 **默认取值**： null
        :type filter: str
        :param order_by: **参数解释**： 排序字段。默认无序返回。 **约束限制**： 不涉及。 **取值范围**： name：根据名称过滤 **默认取值**： null
        :type order_by: str
        :param order: **参数解释**： 排序：升序/降序。 **约束限制**： 不涉及。 **取值范围**： asc：升序 desc：降序 **默认取值**： null
        :type order: str
        :param deleted: **参数解释**： 是否被删除，字段已废弃。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type deleted: str
        """
        
        

        self._cluster_id = None
        self._node_ids = None
        self._offset = None
        self._limit = None
        self._filter_by = None
        self._filter = None
        self._order_by = None
        self._order = None
        self._deleted = None
        self.discriminator = None

        self.cluster_id = cluster_id
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
        if deleted is not None:
            self.deleted = deleted

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListClusterNodesRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListClusterNodesRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListClusterNodesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ListClusterNodesRequest.

        **参数解释**： 节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The node_ids of this ListClusterNodesRequest.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ListClusterNodesRequest.

        **参数解释**： 节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param node_ids: The node_ids of this ListClusterNodesRequest.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def offset(self):
        r"""Gets the offset of this ListClusterNodesRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :return: The offset of this ListClusterNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListClusterNodesRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :param offset: The offset of this ListClusterNodesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListClusterNodesRequest.

        **参数解释**： 分页查询，每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100

        :return: The limit of this ListClusterNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListClusterNodesRequest.

        **参数解释**： 分页查询，每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100

        :param limit: The limit of this ListClusterNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def filter_by(self):
        r"""Gets the filter_by of this ListClusterNodesRequest.

        **参数解释**： 过滤字段。 **约束限制**： 不涉及。 **取值范围**： instCreateType：根据资源状态过滤 status：根据节点状态过滤 **默认取值**： null

        :return: The filter_by of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._filter_by

    @filter_by.setter
    def filter_by(self, filter_by):
        r"""Sets the filter_by of this ListClusterNodesRequest.

        **参数解释**： 过滤字段。 **约束限制**： 不涉及。 **取值范围**： instCreateType：根据资源状态过滤 status：根据节点状态过滤 **默认取值**： null

        :param filter_by: The filter_by of this ListClusterNodesRequest.
        :type filter_by: str
        """
        self._filter_by = filter_by

    @property
    def filter(self):
        r"""Gets the filter of this ListClusterNodesRequest.

        **参数解释**： 过滤字段内容。 **约束限制**： 不涉及。 **取值范围**： 当根据资源状态过滤时，可选如下值： - ALL：全部 - INST：已使用 - NODE：空虚 当根据节点状态过滤时，可选如下值： - ALL：全部 - CREATING：创建中 - FREE：空闲 - ACTIVE：可用 - FAILED：不可用 - UNKNOWN：未知 - CREATE_FAILED：创建失败 - DELETING：删除中 - DELETE_FAILED：删除失败 **默认取值**： null

        :return: The filter of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListClusterNodesRequest.

        **参数解释**： 过滤字段内容。 **约束限制**： 不涉及。 **取值范围**： 当根据资源状态过滤时，可选如下值： - ALL：全部 - INST：已使用 - NODE：空虚 当根据节点状态过滤时，可选如下值： - ALL：全部 - CREATING：创建中 - FREE：空闲 - ACTIVE：可用 - FAILED：不可用 - UNKNOWN：未知 - CREATE_FAILED：创建失败 - DELETING：删除中 - DELETE_FAILED：删除失败 **默认取值**： null

        :param filter: The filter of this ListClusterNodesRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def order_by(self):
        r"""Gets the order_by of this ListClusterNodesRequest.

        **参数解释**： 排序字段。默认无序返回。 **约束限制**： 不涉及。 **取值范围**： name：根据名称过滤 **默认取值**： null

        :return: The order_by of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListClusterNodesRequest.

        **参数解释**： 排序字段。默认无序返回。 **约束限制**： 不涉及。 **取值范围**： name：根据名称过滤 **默认取值**： null

        :param order_by: The order_by of this ListClusterNodesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ListClusterNodesRequest.

        **参数解释**： 排序：升序/降序。 **约束限制**： 不涉及。 **取值范围**： asc：升序 desc：降序 **默认取值**： null

        :return: The order of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListClusterNodesRequest.

        **参数解释**： 排序：升序/降序。 **约束限制**： 不涉及。 **取值范围**： asc：升序 desc：降序 **默认取值**： null

        :param order: The order of this ListClusterNodesRequest.
        :type order: str
        """
        self._order = order

    @property
    def deleted(self):
        r"""Gets the deleted of this ListClusterNodesRequest.

        **参数解释**： 是否被删除，字段已废弃。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The deleted of this ListClusterNodesRequest.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this ListClusterNodesRequest.

        **参数解释**： 是否被删除，字段已废弃。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param deleted: The deleted of this ListClusterNodesRequest.
        :type deleted: str
        """
        self._deleted = deleted

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
