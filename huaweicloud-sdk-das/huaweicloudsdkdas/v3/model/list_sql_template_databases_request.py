# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlTemplateDatabasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'operation': 'str',
        'keyword': 'str',
        'sort': 'str',
        'asc': 'bool',
        'size': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'operation': 'operation',
        'keyword': 'keyword',
        'sort': 'sort',
        'asc': 'asc',
        'size': 'size'
    }

    def __init__(self, instance_id=None, node_id=None, start_at=None, end_at=None, operation=None, keyword=None, sort=None, asc=None, size=None):
        r"""ListSqlTemplateDatabasesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，实例的唯一标识
        :type instance_id: str
        :param node_id: 节点ID，实例节点的唯一标识
        :type node_id: str
        :param start_at: 开始时间，Unix timestamp，单位：毫秒
        :type start_at: int
        :param end_at: 结束时间，Unix timestamp，单位：毫秒
        :type end_at: int
        :param operation: 操作类型，可组合，用逗号分隔
        :type operation: str
        :param keyword: 关键字
        :type keyword: str
        :param sort: 排序字段，取值范围：executeNum（执行次数）、totalCost（总耗时）、avgCost（平均耗时）、totalScan（总扫描行数）、avgScan（平均扫描行数）
        :type sort: str
        :param asc: 排序顺序，true（正序）、false（逆序）
        :type asc: bool
        :param size: 数量，默认30
        :type size: int
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._start_at = None
        self._end_at = None
        self._operation = None
        self._keyword = None
        self._sort = None
        self._asc = None
        self._size = None
        self.discriminator = None

        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        self.start_at = start_at
        self.end_at = end_at
        if operation is not None:
            self.operation = operation
        if keyword is not None:
            self.keyword = keyword
        if sort is not None:
            self.sort = sort
        if asc is not None:
            self.asc = asc
        if size is not None:
            self.size = size

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSqlTemplateDatabasesRequest.

        实例ID，实例的唯一标识

        :return: The instance_id of this ListSqlTemplateDatabasesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSqlTemplateDatabasesRequest.

        实例ID，实例的唯一标识

        :param instance_id: The instance_id of this ListSqlTemplateDatabasesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListSqlTemplateDatabasesRequest.

        节点ID，实例节点的唯一标识

        :return: The node_id of this ListSqlTemplateDatabasesRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListSqlTemplateDatabasesRequest.

        节点ID，实例节点的唯一标识

        :param node_id: The node_id of this ListSqlTemplateDatabasesRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def start_at(self):
        r"""Gets the start_at of this ListSqlTemplateDatabasesRequest.

        开始时间，Unix timestamp，单位：毫秒

        :return: The start_at of this ListSqlTemplateDatabasesRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListSqlTemplateDatabasesRequest.

        开始时间，Unix timestamp，单位：毫秒

        :param start_at: The start_at of this ListSqlTemplateDatabasesRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListSqlTemplateDatabasesRequest.

        结束时间，Unix timestamp，单位：毫秒

        :return: The end_at of this ListSqlTemplateDatabasesRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListSqlTemplateDatabasesRequest.

        结束时间，Unix timestamp，单位：毫秒

        :param end_at: The end_at of this ListSqlTemplateDatabasesRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def operation(self):
        r"""Gets the operation of this ListSqlTemplateDatabasesRequest.

        操作类型，可组合，用逗号分隔

        :return: The operation of this ListSqlTemplateDatabasesRequest.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ListSqlTemplateDatabasesRequest.

        操作类型，可组合，用逗号分隔

        :param operation: The operation of this ListSqlTemplateDatabasesRequest.
        :type operation: str
        """
        self._operation = operation

    @property
    def keyword(self):
        r"""Gets the keyword of this ListSqlTemplateDatabasesRequest.

        关键字

        :return: The keyword of this ListSqlTemplateDatabasesRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListSqlTemplateDatabasesRequest.

        关键字

        :param keyword: The keyword of this ListSqlTemplateDatabasesRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def sort(self):
        r"""Gets the sort of this ListSqlTemplateDatabasesRequest.

        排序字段，取值范围：executeNum（执行次数）、totalCost（总耗时）、avgCost（平均耗时）、totalScan（总扫描行数）、avgScan（平均扫描行数）

        :return: The sort of this ListSqlTemplateDatabasesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListSqlTemplateDatabasesRequest.

        排序字段，取值范围：executeNum（执行次数）、totalCost（总耗时）、avgCost（平均耗时）、totalScan（总扫描行数）、avgScan（平均扫描行数）

        :param sort: The sort of this ListSqlTemplateDatabasesRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def asc(self):
        r"""Gets the asc of this ListSqlTemplateDatabasesRequest.

        排序顺序，true（正序）、false（逆序）

        :return: The asc of this ListSqlTemplateDatabasesRequest.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this ListSqlTemplateDatabasesRequest.

        排序顺序，true（正序）、false（逆序）

        :param asc: The asc of this ListSqlTemplateDatabasesRequest.
        :type asc: bool
        """
        self._asc = asc

    @property
    def size(self):
        r"""Gets the size of this ListSqlTemplateDatabasesRequest.

        数量，默认30

        :return: The size of this ListSqlTemplateDatabasesRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListSqlTemplateDatabasesRequest.

        数量，默认30

        :param size: The size of this ListSqlTemplateDatabasesRequest.
        :type size: int
        """
        self._size = size

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSqlTemplateDatabasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
