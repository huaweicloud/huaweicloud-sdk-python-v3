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
        """RedisTable

        The model defined in huaweicloud sdk

        :param table_name: 表名
        :type table_name: str
        :param id: 表唯一id
        :type id: int
        :param schema_name: schema名
        :type schema_name: str
        :param logical_cluster_name: 逻辑集群名
        :type logical_cluster_name: str
        :param size: 表大小
        :type size: int
        :param status: 重分布类型 i：重分布中； y：重分布完成； n：未开始
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
        """Gets the table_name of this RedisTable.

        表名

        :return: The table_name of this RedisTable.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this RedisTable.

        表名

        :param table_name: The table_name of this RedisTable.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def id(self):
        """Gets the id of this RedisTable.

        表唯一id

        :return: The id of this RedisTable.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RedisTable.

        表唯一id

        :param id: The id of this RedisTable.
        :type id: int
        """
        self._id = id

    @property
    def schema_name(self):
        """Gets the schema_name of this RedisTable.

        schema名

        :return: The schema_name of this RedisTable.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this RedisTable.

        schema名

        :param schema_name: The schema_name of this RedisTable.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this RedisTable.

        逻辑集群名

        :return: The logical_cluster_name of this RedisTable.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this RedisTable.

        逻辑集群名

        :param logical_cluster_name: The logical_cluster_name of this RedisTable.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def size(self):
        """Gets the size of this RedisTable.

        表大小

        :return: The size of this RedisTable.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RedisTable.

        表大小

        :param size: The size of this RedisTable.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this RedisTable.

        重分布类型 i：重分布中； y：重分布完成； n：未开始

        :return: The status of this RedisTable.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RedisTable.

        重分布类型 i：重分布中； y：重分布完成； n：未开始

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
