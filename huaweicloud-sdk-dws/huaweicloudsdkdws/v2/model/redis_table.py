# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisTable:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'id': 'int',
        'schema_name': 'str',
        'logical_cluster_name': 'str',
        'size': 'int',
        'status': 'str'
    }

    attribute_map = {
        'table_name': 'table_name',
        'id': 'id',
        'schema_name': 'schema_name',
        'logical_cluster_name': 'logical_cluster_name',
        'size': 'size',
        'status': 'status'
    }

    def __init__(self, table_name=None, id=None, schema_name=None, logical_cluster_name=None, size=None, status=None):
        r"""RedisTable

        The model defined in huaweicloud sdk

        :param table_name: **参数解释**： 表名。 **取值范围**： 不涉及。
        :type table_name: str
        :param id: **参数解释**： 表唯一id。 **取值范围**： 不涉及。
        :type id: int
        :param schema_name: **参数解释**： schema名。 **取值范围**： 不涉及。
        :type schema_name: str
        :param logical_cluster_name: **参数解释**： 逻辑集群名。 **取值范围**： 不涉及。
        :type logical_cluster_name: str
        :param size: **参数解释**： 表大小。 **取值范围**： 不涉及。
        :type size: int
        :param status: **参数解释**： 重分布类型。 **取值范围**： i：重分布中； y：重分布完成； n：未开始。
        :type status: str
        """
        
        

        self._table_name = None
        self._id = None
        self._schema_name = None
        self._logical_cluster_name = None
        self._size = None
        self._status = None
        self.discriminator = None

        if table_name is not None:
            self.table_name = table_name
        if id is not None:
            self.id = id
        if schema_name is not None:
            self.schema_name = schema_name
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status

    @property
    def table_name(self):
        r"""Gets the table_name of this RedisTable.

        **参数解释**： 表名。 **取值范围**： 不涉及。

        :return: The table_name of this RedisTable.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this RedisTable.

        **参数解释**： 表名。 **取值范围**： 不涉及。

        :param table_name: The table_name of this RedisTable.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def id(self):
        r"""Gets the id of this RedisTable.

        **参数解释**： 表唯一id。 **取值范围**： 不涉及。

        :return: The id of this RedisTable.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RedisTable.

        **参数解释**： 表唯一id。 **取值范围**： 不涉及。

        :param id: The id of this RedisTable.
        :type id: int
        """
        self._id = id

    @property
    def schema_name(self):
        r"""Gets the schema_name of this RedisTable.

        **参数解释**： schema名。 **取值范围**： 不涉及。

        :return: The schema_name of this RedisTable.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this RedisTable.

        **参数解释**： schema名。 **取值范围**： 不涉及。

        :param schema_name: The schema_name of this RedisTable.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def logical_cluster_name(self):
        r"""Gets the logical_cluster_name of this RedisTable.

        **参数解释**： 逻辑集群名。 **取值范围**： 不涉及。

        :return: The logical_cluster_name of this RedisTable.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        r"""Sets the logical_cluster_name of this RedisTable.

        **参数解释**： 逻辑集群名。 **取值范围**： 不涉及。

        :param logical_cluster_name: The logical_cluster_name of this RedisTable.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def size(self):
        r"""Gets the size of this RedisTable.

        **参数解释**： 表大小。 **取值范围**： 不涉及。

        :return: The size of this RedisTable.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RedisTable.

        **参数解释**： 表大小。 **取值范围**： 不涉及。

        :param size: The size of this RedisTable.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this RedisTable.

        **参数解释**： 重分布类型。 **取值范围**： i：重分布中； y：重分布完成； n：未开始。

        :return: The status of this RedisTable.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RedisTable.

        **参数解释**： 重分布类型。 **取值范围**： i：重分布中； y：重分布完成； n：未开始。

        :param status: The status of this RedisTable.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, RedisTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
