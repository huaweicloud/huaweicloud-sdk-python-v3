# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogicalClusterTasksRequest:

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
        'offset': 'int',
        'limit': 'int',
        'logical_cluster_name': 'str',
        'type': 'str',
        'order_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'offset': 'offset',
        'limit': 'limit',
        'logical_cluster_name': 'logical_cluster_name',
        'type': 'type',
        'order_by': 'order_by',
        'order': 'order'
    }

    def __init__(self, cluster_id=None, offset=None, limit=None, logical_cluster_name=None, type=None, order_by=None, order=None):
        r"""ListLogicalClusterTasksRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0
        :type offset: int
        :param limit: **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10
        :type limit: int
        :param logical_cluster_name: **参数解释**： 集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type logical_cluster_name: str
        :param type: **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type type: str
        :param order_by: **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type order_by: str
        :param order: **参数解释**： 排序：升序/降序。 **约束限制**： 不涉及。 **取值范围**： ASC：表示按升序排序。 DESC：表示按降序排序。 **默认取值**： 不涉及。
        :type order: str
        """
        
        

        self._cluster_id = None
        self._offset = None
        self._limit = None
        self._logical_cluster_name = None
        self._type = None
        self._order_by = None
        self._order = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if type is not None:
            self.type = type
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListLogicalClusterTasksRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListLogicalClusterTasksRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListLogicalClusterTasksRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def offset(self):
        r"""Gets the offset of this ListLogicalClusterTasksRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :return: The offset of this ListLogicalClusterTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLogicalClusterTasksRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :param offset: The offset of this ListLogicalClusterTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLogicalClusterTasksRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10

        :return: The limit of this ListLogicalClusterTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLogicalClusterTasksRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10

        :param limit: The limit of this ListLogicalClusterTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this ListLogicalClusterTasksRequest.

        **参数解释**： 集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The logical_cluster_name of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this ListLogicalClusterTasksRequest.

        **参数解释**： 集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param logical_cluster_name: The logical_cluster_name of this ListLogicalClusterTasksRequest.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def type(self):
        r"""Gets the type of this ListLogicalClusterTasksRequest.

        **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The type of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListLogicalClusterTasksRequest.

        **参数解释**： 类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param type: The type of this ListLogicalClusterTasksRequest.
        :type type: str
        """
        self._type = type

    @property
    def order_by(self):
        r"""Gets the order_by of this ListLogicalClusterTasksRequest.

        **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The order_by of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListLogicalClusterTasksRequest.

        **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param order_by: The order_by of this ListLogicalClusterTasksRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ListLogicalClusterTasksRequest.

        **参数解释**： 排序：升序/降序。 **约束限制**： 不涉及。 **取值范围**： ASC：表示按升序排序。 DESC：表示按降序排序。 **默认取值**： 不涉及。

        :return: The order of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListLogicalClusterTasksRequest.

        **参数解释**： 排序：升序/降序。 **约束限制**： 不涉及。 **取值范围**： ASC：表示按升序排序。 DESC：表示按降序排序。 **默认取值**： 不涉及。

        :param order: The order of this ListLogicalClusterTasksRequest.
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
        if not isinstance(other, ListLogicalClusterTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
