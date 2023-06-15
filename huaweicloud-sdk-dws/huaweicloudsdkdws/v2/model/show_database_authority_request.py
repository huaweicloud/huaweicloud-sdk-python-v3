# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatabaseAuthorityRequest:

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
        'name': 'list[str]',
        'database': 'str',
        'schema': 'str',
        'table': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'type': 'type',
        'name': 'name',
        'database': 'database',
        'schema': 'schema',
        'table': 'table'
    }

    def __init__(self, cluster_id=None, type=None, name=None, database=None, schema=None, table=None):
        """ShowDatabaseAuthorityRequest

        The model defined in huaweicloud sdk

        :param cluster_id: cluster_id
        :type cluster_id: str
        :param type: 对象类型 [DATABASE | SCHEMA | TABLE | VIEW | COLUMN| FUNCTION|| SEQUENCE| NODEGROUP]
        :type type: str
        :param name: 对象名称
        :type name: list[str]
        :param database: 数据库名
        :type database: str
        :param schema: 模式名，对象类型为TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE时必选
        :type schema: str
        :param table: 表名，对象类型为COLUMN时必选
        :type table: str
        """
        
        

        self._cluster_id = None
        self._type = None
        self._name = None
        self._database = None
        self._schema = None
        self._table = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.type = type
        self.name = name
        self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowDatabaseAuthorityRequest.

        cluster_id

        :return: The cluster_id of this ShowDatabaseAuthorityRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowDatabaseAuthorityRequest.

        cluster_id

        :param cluster_id: The cluster_id of this ShowDatabaseAuthorityRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def type(self):
        """Gets the type of this ShowDatabaseAuthorityRequest.

        对象类型 [DATABASE | SCHEMA | TABLE | VIEW | COLUMN| FUNCTION|| SEQUENCE| NODEGROUP]

        :return: The type of this ShowDatabaseAuthorityRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowDatabaseAuthorityRequest.

        对象类型 [DATABASE | SCHEMA | TABLE | VIEW | COLUMN| FUNCTION|| SEQUENCE| NODEGROUP]

        :param type: The type of this ShowDatabaseAuthorityRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ShowDatabaseAuthorityRequest.

        对象名称

        :return: The name of this ShowDatabaseAuthorityRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDatabaseAuthorityRequest.

        对象名称

        :param name: The name of this ShowDatabaseAuthorityRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def database(self):
        """Gets the database of this ShowDatabaseAuthorityRequest.

        数据库名

        :return: The database of this ShowDatabaseAuthorityRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ShowDatabaseAuthorityRequest.

        数据库名

        :param database: The database of this ShowDatabaseAuthorityRequest.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        """Gets the schema of this ShowDatabaseAuthorityRequest.

        模式名，对象类型为TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE时必选

        :return: The schema of this ShowDatabaseAuthorityRequest.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ShowDatabaseAuthorityRequest.

        模式名，对象类型为TABLE、VIEW、COLUMN、FUNCTION、SEQUENCE时必选

        :param schema: The schema of this ShowDatabaseAuthorityRequest.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        """Gets the table of this ShowDatabaseAuthorityRequest.

        表名，对象类型为COLUMN时必选

        :return: The table of this ShowDatabaseAuthorityRequest.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this ShowDatabaseAuthorityRequest.

        表名，对象类型为COLUMN时必选

        :param table: The table of this ShowDatabaseAuthorityRequest.
        :type table: str
        """
        self._table = table

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
        if not isinstance(other, ShowDatabaseAuthorityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
