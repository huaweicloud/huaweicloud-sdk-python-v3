# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablesStatisticRequest:

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
        'rate_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_by': 'str',
        'sort_by': 'str',
        'filter': 'str',
        'value': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'rate_type': 'rate_type',
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by',
        'sort_by': 'sort_by',
        'filter': 'filter',
        'value': 'value'
    }

    def __init__(self, cluster_id=None, rate_type=None, offset=None, limit=None, order_by=None, sort_by=None, filter=None, value=None):
        """ListTablesStatisticRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param rate_type: 查询类型。固定取值。 skew：表倾斜率。 dirtyPage：表脏页率。
        :type rate_type: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset&gt;&#x3D;0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param order_by: 排序字段。固定取值。 table_size：表大小。rate：表倾斜率或脏页率。
        :type order_by: str
        :param sort_by: 正序还是倒叙。固定取值。 ASC：正序。DESC：倒序
        :type sort_by: str
        :param filter: 查询条件。固定取值。 db_name：数据库名称。 schema_name：schema名称。 table_name：表名。 table_owner：所属用户。
        :type filter: str
        :param value: 查询条件的取值。
        :type value: str
        """
        
        

        self._cluster_id = None
        self._rate_type = None
        self._offset = None
        self._limit = None
        self._order_by = None
        self._sort_by = None
        self._filter = None
        self._value = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.rate_type = rate_type
        self.offset = offset
        self.limit = limit
        if order_by is not None:
            self.order_by = order_by
        if sort_by is not None:
            self.sort_by = sort_by
        if filter is not None:
            self.filter = filter
        if value is not None:
            self.value = value

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListTablesStatisticRequest.

        集群ID。

        :return: The cluster_id of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListTablesStatisticRequest.

        集群ID。

        :param cluster_id: The cluster_id of this ListTablesStatisticRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def rate_type(self):
        """Gets the rate_type of this ListTablesStatisticRequest.

        查询类型。固定取值。 skew：表倾斜率。 dirtyPage：表脏页率。

        :return: The rate_type of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        """Sets the rate_type of this ListTablesStatisticRequest.

        查询类型。固定取值。 skew：表倾斜率。 dirtyPage：表脏页率。

        :param rate_type: The rate_type of this ListTablesStatisticRequest.
        :type rate_type: str
        """
        self._rate_type = rate_type

    @property
    def offset(self):
        """Gets the offset of this ListTablesStatisticRequest.

        偏移量，表示从此偏移量开始查询，offset>=0。

        :return: The offset of this ListTablesStatisticRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTablesStatisticRequest.

        偏移量，表示从此偏移量开始查询，offset>=0。

        :param offset: The offset of this ListTablesStatisticRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTablesStatisticRequest.

        每页显示的条目数量。

        :return: The limit of this ListTablesStatisticRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTablesStatisticRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListTablesStatisticRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        """Gets the order_by of this ListTablesStatisticRequest.

        排序字段。固定取值。 table_size：表大小。rate：表倾斜率或脏页率。

        :return: The order_by of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListTablesStatisticRequest.

        排序字段。固定取值。 table_size：表大小。rate：表倾斜率或脏页率。

        :param order_by: The order_by of this ListTablesStatisticRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort_by(self):
        """Gets the sort_by of this ListTablesStatisticRequest.

        正序还是倒叙。固定取值。 ASC：正序。DESC：倒序

        :return: The sort_by of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListTablesStatisticRequest.

        正序还是倒叙。固定取值。 ASC：正序。DESC：倒序

        :param sort_by: The sort_by of this ListTablesStatisticRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def filter(self):
        """Gets the filter of this ListTablesStatisticRequest.

        查询条件。固定取值。 db_name：数据库名称。 schema_name：schema名称。 table_name：表名。 table_owner：所属用户。

        :return: The filter of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListTablesStatisticRequest.

        查询条件。固定取值。 db_name：数据库名称。 schema_name：schema名称。 table_name：表名。 table_owner：所属用户。

        :param filter: The filter of this ListTablesStatisticRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def value(self):
        """Gets the value of this ListTablesStatisticRequest.

        查询条件的取值。

        :return: The value of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListTablesStatisticRequest.

        查询条件的取值。

        :param value: The value of this ListTablesStatisticRequest.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ListTablesStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
