# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionSetPermissionCreateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_id': 'str',
        'permission_type': 'str',
        'permission_actions': 'list[str]',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'datasource_type': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'namespace': 'str',
        'table_name': 'str',
        'column_name': 'str',
        'row_level_security': 'str',
        'url': 'str'
    }

    attribute_map = {
        'dw_id': 'dw_id',
        'permission_type': 'permission_type',
        'permission_actions': 'permission_actions',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'datasource_type': 'datasource_type',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'namespace': 'namespace',
        'table_name': 'table_name',
        'column_name': 'column_name',
        'row_level_security': 'row_level_security',
        'url': 'url'
    }

    def __init__(self, dw_id=None, permission_type=None, permission_actions=None, cluster_id=None, cluster_name=None, datasource_type=None, database_name=None, schema_name=None, namespace=None, table_name=None, column_name=None, row_level_security=None, url=None):
        """PermissionSetPermissionCreateDTO

        The model defined in huaweicloud sdk

        :param dw_id: 数据连接id
        :type dw_id: str
        :param permission_type: 权限类型, DENY, ALLOW
        :type permission_type: str
        :param permission_actions: 权限操作列表
        :type permission_actions: list[str]
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param datasource_type: 数据源类型, HIVE
        :type datasource_type: str
        :param database_name: 数据库名称
        :type database_name: str
        :param schema_name: 模式名称
        :type schema_name: str
        :param namespace: 命名空间。无效参数，待下线。
        :type namespace: str
        :param table_name: 表名称
        :type table_name: str
        :param column_name: 列名称
        :type column_name: str
        :param row_level_security: 行级策略。无效参数，待下线。
        :type row_level_security: str
        :param url: url路径名称, MRS存算分离或者HIVE指定location场景下使用。
        :type url: str
        """
        
        

        self._dw_id = None
        self._permission_type = None
        self._permission_actions = None
        self._cluster_id = None
        self._cluster_name = None
        self._datasource_type = None
        self._database_name = None
        self._schema_name = None
        self._namespace = None
        self._table_name = None
        self._column_name = None
        self._row_level_security = None
        self._url = None
        self.discriminator = None

        if dw_id is not None:
            self.dw_id = dw_id
        if permission_type is not None:
            self.permission_type = permission_type
        if permission_actions is not None:
            self.permission_actions = permission_actions
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if database_name is not None:
            self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        if namespace is not None:
            self.namespace = namespace
        if table_name is not None:
            self.table_name = table_name
        if column_name is not None:
            self.column_name = column_name
        if row_level_security is not None:
            self.row_level_security = row_level_security
        if url is not None:
            self.url = url

    @property
    def dw_id(self):
        """Gets the dw_id of this PermissionSetPermissionCreateDTO.

        数据连接id

        :return: The dw_id of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        """Sets the dw_id of this PermissionSetPermissionCreateDTO.

        数据连接id

        :param dw_id: The dw_id of this PermissionSetPermissionCreateDTO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def permission_type(self):
        """Gets the permission_type of this PermissionSetPermissionCreateDTO.

        权限类型, DENY, ALLOW

        :return: The permission_type of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this PermissionSetPermissionCreateDTO.

        权限类型, DENY, ALLOW

        :param permission_type: The permission_type of this PermissionSetPermissionCreateDTO.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def permission_actions(self):
        """Gets the permission_actions of this PermissionSetPermissionCreateDTO.

        权限操作列表

        :return: The permission_actions of this PermissionSetPermissionCreateDTO.
        :rtype: list[str]
        """
        return self._permission_actions

    @permission_actions.setter
    def permission_actions(self, permission_actions):
        """Sets the permission_actions of this PermissionSetPermissionCreateDTO.

        权限操作列表

        :param permission_actions: The permission_actions of this PermissionSetPermissionCreateDTO.
        :type permission_actions: list[str]
        """
        self._permission_actions = permission_actions

    @property
    def cluster_id(self):
        """Gets the cluster_id of this PermissionSetPermissionCreateDTO.

        集群id

        :return: The cluster_id of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this PermissionSetPermissionCreateDTO.

        集群id

        :param cluster_id: The cluster_id of this PermissionSetPermissionCreateDTO.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this PermissionSetPermissionCreateDTO.

        集群名称

        :return: The cluster_name of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this PermissionSetPermissionCreateDTO.

        集群名称

        :param cluster_name: The cluster_name of this PermissionSetPermissionCreateDTO.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def datasource_type(self):
        """Gets the datasource_type of this PermissionSetPermissionCreateDTO.

        数据源类型, HIVE

        :return: The datasource_type of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this PermissionSetPermissionCreateDTO.

        数据源类型, HIVE

        :param datasource_type: The datasource_type of this PermissionSetPermissionCreateDTO.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def database_name(self):
        """Gets the database_name of this PermissionSetPermissionCreateDTO.

        数据库名称

        :return: The database_name of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this PermissionSetPermissionCreateDTO.

        数据库名称

        :param database_name: The database_name of this PermissionSetPermissionCreateDTO.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        """Gets the schema_name of this PermissionSetPermissionCreateDTO.

        模式名称

        :return: The schema_name of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this PermissionSetPermissionCreateDTO.

        模式名称

        :param schema_name: The schema_name of this PermissionSetPermissionCreateDTO.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def namespace(self):
        """Gets the namespace of this PermissionSetPermissionCreateDTO.

        命名空间。无效参数，待下线。

        :return: The namespace of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this PermissionSetPermissionCreateDTO.

        命名空间。无效参数，待下线。

        :param namespace: The namespace of this PermissionSetPermissionCreateDTO.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def table_name(self):
        """Gets the table_name of this PermissionSetPermissionCreateDTO.

        表名称

        :return: The table_name of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this PermissionSetPermissionCreateDTO.

        表名称

        :param table_name: The table_name of this PermissionSetPermissionCreateDTO.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        """Gets the column_name of this PermissionSetPermissionCreateDTO.

        列名称

        :return: The column_name of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this PermissionSetPermissionCreateDTO.

        列名称

        :param column_name: The column_name of this PermissionSetPermissionCreateDTO.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def row_level_security(self):
        """Gets the row_level_security of this PermissionSetPermissionCreateDTO.

        行级策略。无效参数，待下线。

        :return: The row_level_security of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._row_level_security

    @row_level_security.setter
    def row_level_security(self, row_level_security):
        """Sets the row_level_security of this PermissionSetPermissionCreateDTO.

        行级策略。无效参数，待下线。

        :param row_level_security: The row_level_security of this PermissionSetPermissionCreateDTO.
        :type row_level_security: str
        """
        self._row_level_security = row_level_security

    @property
    def url(self):
        """Gets the url of this PermissionSetPermissionCreateDTO.

        url路径名称, MRS存算分离或者HIVE指定location场景下使用。

        :return: The url of this PermissionSetPermissionCreateDTO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PermissionSetPermissionCreateDTO.

        url路径名称, MRS存算分离或者HIVE指定location场景下使用。

        :param url: The url of this PermissionSetPermissionCreateDTO.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, PermissionSetPermissionCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
