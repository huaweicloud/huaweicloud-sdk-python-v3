# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterRedistributionRequest:

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
        'limit': 'int',
        'offset': 'int',
        'db_name': 'str',
        'table_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'limit': 'limit',
        'offset': 'offset',
        'db_name': 'db_name',
        'table_name': 'table_name',
        'type': 'type'
    }

    def __init__(self, cluster_id=None, limit=None, offset=None, db_name=None, table_name=None, type=None):
        r"""ShowClusterRedistributionRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param limit: **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10
        :type limit: int
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0
        :type offset: int
        :param db_name: **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type db_name: str
        :param table_name: **参数解释**： 表名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type table_name: str
        :param type: **参数解释**： 类型，取值来自public.pgxc_redistb表的redistributed字段。多个可用逗号分割。 **约束限制**： 不涉及。 **取值范围**： i：重分布中； y：已完成； n：未开始； **默认取值**： null，即不过滤。
        :type type: str
        """
        
        

        self._cluster_id = None
        self._limit = None
        self._offset = None
        self._db_name = None
        self._table_name = None
        self._type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if db_name is not None:
            self.db_name = db_name
        if table_name is not None:
            self.table_name = table_name
        if type is not None:
            self.type = type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowClusterRedistributionRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ShowClusterRedistributionRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowClusterRedistributionRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ShowClusterRedistributionRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowClusterRedistributionRequest.

        **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10

        :return: The limit of this ShowClusterRedistributionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowClusterRedistributionRequest.

        **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10

        :param limit: The limit of this ShowClusterRedistributionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowClusterRedistributionRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0

        :return: The offset of this ShowClusterRedistributionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowClusterRedistributionRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0

        :param offset: The offset of this ShowClusterRedistributionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def db_name(self):
        r"""Gets the db_name of this ShowClusterRedistributionRequest.

        **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The db_name of this ShowClusterRedistributionRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ShowClusterRedistributionRequest.

        **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param db_name: The db_name of this ShowClusterRedistributionRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ShowClusterRedistributionRequest.

        **参数解释**： 表名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The table_name of this ShowClusterRedistributionRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ShowClusterRedistributionRequest.

        **参数解释**： 表名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param table_name: The table_name of this ShowClusterRedistributionRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def type(self):
        r"""Gets the type of this ShowClusterRedistributionRequest.

        **参数解释**： 类型，取值来自public.pgxc_redistb表的redistributed字段。多个可用逗号分割。 **约束限制**： 不涉及。 **取值范围**： i：重分布中； y：已完成； n：未开始； **默认取值**： null，即不过滤。

        :return: The type of this ShowClusterRedistributionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowClusterRedistributionRequest.

        **参数解释**： 类型，取值来自public.pgxc_redistb表的redistributed字段。多个可用逗号分割。 **约束限制**： 不涉及。 **取值范围**： i：重分布中； y：已完成； n：未开始； **默认取值**： null，即不过滤。

        :param type: The type of this ShowClusterRedistributionRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowClusterRedistributionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
