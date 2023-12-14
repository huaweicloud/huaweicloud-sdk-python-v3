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
        """ListLogicalClusterTasksRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param offset: 分页查询，偏移
        :type offset: int
        :param limit: 分页查询，每页显示的条目数量
        :type limit: int
        :param logical_cluster_name: 集群名称
        :type logical_cluster_name: str
        :param type: 类型
        :type type: str
        :param order_by: 排序字段
        :type order_by: str
        :param order: 排序：升序/降序
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
        """Gets the cluster_id of this ListLogicalClusterTasksRequest.

        集群ID

        :return: The cluster_id of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListLogicalClusterTasksRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListLogicalClusterTasksRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def offset(self):
        """Gets the offset of this ListLogicalClusterTasksRequest.

        分页查询，偏移

        :return: The offset of this ListLogicalClusterTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListLogicalClusterTasksRequest.

        分页查询，偏移

        :param offset: The offset of this ListLogicalClusterTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListLogicalClusterTasksRequest.

        分页查询，每页显示的条目数量

        :return: The limit of this ListLogicalClusterTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLogicalClusterTasksRequest.

        分页查询，每页显示的条目数量

        :param limit: The limit of this ListLogicalClusterTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this ListLogicalClusterTasksRequest.

        集群名称

        :return: The logical_cluster_name of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this ListLogicalClusterTasksRequest.

        集群名称

        :param logical_cluster_name: The logical_cluster_name of this ListLogicalClusterTasksRequest.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def type(self):
        """Gets the type of this ListLogicalClusterTasksRequest.

        类型

        :return: The type of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListLogicalClusterTasksRequest.

        类型

        :param type: The type of this ListLogicalClusterTasksRequest.
        :type type: str
        """
        self._type = type

    @property
    def order_by(self):
        """Gets the order_by of this ListLogicalClusterTasksRequest.

        排序字段

        :return: The order_by of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListLogicalClusterTasksRequest.

        排序字段

        :param order_by: The order_by of this ListLogicalClusterTasksRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        """Gets the order of this ListLogicalClusterTasksRequest.

        排序：升序/降序

        :return: The order of this ListLogicalClusterTasksRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListLogicalClusterTasksRequest.

        排序：升序/降序

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
