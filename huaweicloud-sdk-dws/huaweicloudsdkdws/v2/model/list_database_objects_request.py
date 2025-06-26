# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseObjectsRequest:

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
        'type': 'str',
        'name': 'str',
        'database': 'str',
        'schema': 'str',
        'table': 'str',
        'offset': 'int',
        'limit': 'int',
        'is_fine_grained_disaster': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'type': 'type',
        'name': 'name',
        'database': 'database',
        'schema': 'schema',
        'table': 'table',
        'offset': 'offset',
        'limit': 'limit',
        'is_fine_grained_disaster': 'is_fine_grained_disaster'
    }

    def __init__(self, cluster_id=None, type=None, name=None, database=None, schema=None, table=None, offset=None, limit=None, is_fine_grained_disaster=None):
        r"""ListDatabaseObjectsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param type: **参数解释**： 对象类型。 **约束限制**： 不涉及。 **取值范围**： DATABASE、SCHEMA、TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE、NODEGROUP **默认取值**： null
        :type type: str
        :param name: **参数解释**： 对象名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param database: **参数解释**： 数据库名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type database: str
        :param schema: **参数解释**： 模式名。 **约束限制**： 当对象类型为TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE时必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type schema: str
        :param table: **参数解释**： 表名。 **约束限制**： 对象类型为COLUMN时必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type table: str
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0
        :type offset: int
        :param limit: **参数解释**： 分页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 1000
        :type limit: int
        :param is_fine_grained_disaster: **参数解释**： 是否细粒度容灾。 **约束限制**： 不涉及。 **取值范围**： true|false **默认取值**： 不涉及。
        :type is_fine_grained_disaster: str
        """
        
        

        self._cluster_id = None
        self._type = None
        self._name = None
        self._database = None
        self._schema = None
        self._table = None
        self._offset = None
        self._limit = None
        self._is_fine_grained_disaster = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.type = type
        if name is not None:
            self.name = name
        if database is not None:
            self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if is_fine_grained_disaster is not None:
            self.is_fine_grained_disaster = is_fine_grained_disaster

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListDatabaseObjectsRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListDatabaseObjectsRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListDatabaseObjectsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def type(self):
        r"""Gets the type of this ListDatabaseObjectsRequest.

        **参数解释**： 对象类型。 **约束限制**： 不涉及。 **取值范围**： DATABASE、SCHEMA、TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE、NODEGROUP **默认取值**： null

        :return: The type of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDatabaseObjectsRequest.

        **参数解释**： 对象类型。 **约束限制**： 不涉及。 **取值范围**： DATABASE、SCHEMA、TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE、NODEGROUP **默认取值**： null

        :param type: The type of this ListDatabaseObjectsRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ListDatabaseObjectsRequest.

        **参数解释**： 对象名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDatabaseObjectsRequest.

        **参数解释**： 对象名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this ListDatabaseObjectsRequest.
        :type name: str
        """
        self._name = name

    @property
    def database(self):
        r"""Gets the database of this ListDatabaseObjectsRequest.

        **参数解释**： 数据库名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The database of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ListDatabaseObjectsRequest.

        **参数解释**： 数据库名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param database: The database of this ListDatabaseObjectsRequest.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        r"""Gets the schema of this ListDatabaseObjectsRequest.

        **参数解释**： 模式名。 **约束限制**： 当对象类型为TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE时必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The schema of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ListDatabaseObjectsRequest.

        **参数解释**： 模式名。 **约束限制**： 当对象类型为TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE时必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param schema: The schema of this ListDatabaseObjectsRequest.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        r"""Gets the table of this ListDatabaseObjectsRequest.

        **参数解释**： 表名。 **约束限制**： 对象类型为COLUMN时必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The table of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this ListDatabaseObjectsRequest.

        **参数解释**： 表名。 **约束限制**： 对象类型为COLUMN时必选。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param table: The table of this ListDatabaseObjectsRequest.
        :type table: str
        """
        self._table = table

    @property
    def offset(self):
        r"""Gets the offset of this ListDatabaseObjectsRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :return: The offset of this ListDatabaseObjectsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDatabaseObjectsRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :param offset: The offset of this ListDatabaseObjectsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDatabaseObjectsRequest.

        **参数解释**： 分页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 1000

        :return: The limit of this ListDatabaseObjectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDatabaseObjectsRequest.

        **参数解释**： 分页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 1000

        :param limit: The limit of this ListDatabaseObjectsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def is_fine_grained_disaster(self):
        r"""Gets the is_fine_grained_disaster of this ListDatabaseObjectsRequest.

        **参数解释**： 是否细粒度容灾。 **约束限制**： 不涉及。 **取值范围**： true|false **默认取值**： 不涉及。

        :return: The is_fine_grained_disaster of this ListDatabaseObjectsRequest.
        :rtype: str
        """
        return self._is_fine_grained_disaster

    @is_fine_grained_disaster.setter
    def is_fine_grained_disaster(self, is_fine_grained_disaster):
        r"""Sets the is_fine_grained_disaster of this ListDatabaseObjectsRequest.

        **参数解释**： 是否细粒度容灾。 **约束限制**： 不涉及。 **取值范围**： true|false **默认取值**： 不涉及。

        :param is_fine_grained_disaster: The is_fine_grained_disaster of this ListDatabaseObjectsRequest.
        :type is_fine_grained_disaster: str
        """
        self._is_fine_grained_disaster = is_fine_grained_disaster

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
        if not isinstance(other, ListDatabaseObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
