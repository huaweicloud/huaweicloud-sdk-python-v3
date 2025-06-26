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
        r"""ListTablesStatisticRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param rate_type: **参数解释**： 查询类型，固定取值。 **约束限制**： 不涉及。 **取值范围**： skew：表倾斜率。 dirtyPage：表脏页率。 **默认取值**： 不涉及。
        :type rate_type: str
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0
        :type offset: int
        :param limit: **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 不限制。
        :type limit: int
        :param order_by: **参数解释**： 排序字段，固定取值。 **约束限制**： 不涉及。 **取值范围**： table_size：表大小。 rate：表倾斜率或脏页率。 **默认取值**： 不涉及。
        :type order_by: str
        :param sort_by: **参数解释**： 正序还是倒序排序，固定取值。 **约束限制**： 不涉及。 **取值范围**： ASC：正序。 DESC：倒序。 **默认取值**： 不涉及。
        :type sort_by: str
        :param filter: **参数解释**： 查询条件，固定取值。 **约束限制**： 不涉及。 **取值范围**： db_name：数据库名称。 schema_name：schema名称。 table_name：表名。 table_owner：所属用户。 **默认取值**： 不涉及。
        :type filter: str
        :param value: **参数解释**： 过滤条件的值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
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
        r"""Gets the cluster_id of this ListTablesStatisticRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListTablesStatisticRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListTablesStatisticRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def rate_type(self):
        r"""Gets the rate_type of this ListTablesStatisticRequest.

        **参数解释**： 查询类型，固定取值。 **约束限制**： 不涉及。 **取值范围**： skew：表倾斜率。 dirtyPage：表脏页率。 **默认取值**： 不涉及。

        :return: The rate_type of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        r"""Sets the rate_type of this ListTablesStatisticRequest.

        **参数解释**： 查询类型，固定取值。 **约束限制**： 不涉及。 **取值范围**： skew：表倾斜率。 dirtyPage：表脏页率。 **默认取值**： 不涉及。

        :param rate_type: The rate_type of this ListTablesStatisticRequest.
        :type rate_type: str
        """
        self._rate_type = rate_type

    @property
    def offset(self):
        r"""Gets the offset of this ListTablesStatisticRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :return: The offset of this ListTablesStatisticRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTablesStatisticRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :param offset: The offset of this ListTablesStatisticRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTablesStatisticRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 不限制。

        :return: The limit of this ListTablesStatisticRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTablesStatisticRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 不限制。

        :param limit: The limit of this ListTablesStatisticRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListTablesStatisticRequest.

        **参数解释**： 排序字段，固定取值。 **约束限制**： 不涉及。 **取值范围**： table_size：表大小。 rate：表倾斜率或脏页率。 **默认取值**： 不涉及。

        :return: The order_by of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListTablesStatisticRequest.

        **参数解释**： 排序字段，固定取值。 **约束限制**： 不涉及。 **取值范围**： table_size：表大小。 rate：表倾斜率或脏页率。 **默认取值**： 不涉及。

        :param order_by: The order_by of this ListTablesStatisticRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListTablesStatisticRequest.

        **参数解释**： 正序还是倒序排序，固定取值。 **约束限制**： 不涉及。 **取值范围**： ASC：正序。 DESC：倒序。 **默认取值**： 不涉及。

        :return: The sort_by of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListTablesStatisticRequest.

        **参数解释**： 正序还是倒序排序，固定取值。 **约束限制**： 不涉及。 **取值范围**： ASC：正序。 DESC：倒序。 **默认取值**： 不涉及。

        :param sort_by: The sort_by of this ListTablesStatisticRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def filter(self):
        r"""Gets the filter of this ListTablesStatisticRequest.

        **参数解释**： 查询条件，固定取值。 **约束限制**： 不涉及。 **取值范围**： db_name：数据库名称。 schema_name：schema名称。 table_name：表名。 table_owner：所属用户。 **默认取值**： 不涉及。

        :return: The filter of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListTablesStatisticRequest.

        **参数解释**： 查询条件，固定取值。 **约束限制**： 不涉及。 **取值范围**： db_name：数据库名称。 schema_name：schema名称。 table_name：表名。 table_owner：所属用户。 **默认取值**： 不涉及。

        :param filter: The filter of this ListTablesStatisticRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def value(self):
        r"""Gets the value of this ListTablesStatisticRequest.

        **参数解释**： 过滤条件的值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The value of this ListTablesStatisticRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ListTablesStatisticRequest.

        **参数解释**： 过滤条件的值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

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
