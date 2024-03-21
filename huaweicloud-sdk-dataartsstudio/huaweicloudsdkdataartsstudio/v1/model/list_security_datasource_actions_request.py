# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDatasourceActionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'parent_permission_set_id': 'str',
        'cluster_id': 'str',
        'datasource_type': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'column_name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'parent_permission_set_id': 'parent_permission_set_id',
        'cluster_id': 'cluster_id',
        'datasource_type': 'datasource_type',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'column_name': 'column_name',
        'url': 'url'
    }

    def __init__(self, workspace=None, parent_permission_set_id=None, cluster_id=None, datasource_type=None, database_name=None, schema_name=None, table_name=None, column_name=None, url=None):
        """ListSecurityDatasourceActionsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param parent_permission_set_id: 父权限集ID。获取方法请参见[查询权限集列表](ListSecurityPermissionSets.xml) 注意： * 当该值为0时，则所有库表均支持查询 * 当该值为父权限集ID时，则基于父权限集中的权限查询
        :type parent_permission_set_id: str
        :param cluster_id: 集群ID，获取方法请参见[查询单个数据连接信息](ShowDataconnection.xml) * 查询Hive和DWS数据源操作信息时该数值为必填项，当数据源为DLI时无需填写
        :type cluster_id: str
        :param datasource_type: 数据源类型 * HIVE数据源 * DWS数据源 * DLI数据源
        :type datasource_type: str
        :param database_name: 数据库名 &#x60;注意：该值作为查询关键字时，不能与url同时存在，需要指定其一进行查询&#x60;
        :type database_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param table_name: 数据表名称
        :type table_name: str
        :param column_name: 数据字段名称
        :type column_name: str
        :param url: url路径名称 &#x60;注意：该值作为查询关键字时，不能与database_name同时存在，需要指定其一进行查询&#x60;
        :type url: str
        """
        
        

        self._workspace = None
        self._parent_permission_set_id = None
        self._cluster_id = None
        self._datasource_type = None
        self._database_name = None
        self._schema_name = None
        self._table_name = None
        self._column_name = None
        self._url = None
        self.discriminator = None

        self.workspace = workspace
        self.parent_permission_set_id = parent_permission_set_id
        self.cluster_id = cluster_id
        self.datasource_type = datasource_type
        if database_name is not None:
            self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if column_name is not None:
            self.column_name = column_name
        if url is not None:
            self.url = url

    @property
    def workspace(self):
        """Gets the workspace of this ListSecurityDatasourceActionsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListSecurityDatasourceActionsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityDatasourceActionsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def parent_permission_set_id(self):
        """Gets the parent_permission_set_id of this ListSecurityDatasourceActionsRequest.

        父权限集ID。获取方法请参见[查询权限集列表](ListSecurityPermissionSets.xml) 注意： * 当该值为0时，则所有库表均支持查询 * 当该值为父权限集ID时，则基于父权限集中的权限查询

        :return: The parent_permission_set_id of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._parent_permission_set_id

    @parent_permission_set_id.setter
    def parent_permission_set_id(self, parent_permission_set_id):
        """Sets the parent_permission_set_id of this ListSecurityDatasourceActionsRequest.

        父权限集ID。获取方法请参见[查询权限集列表](ListSecurityPermissionSets.xml) 注意： * 当该值为0时，则所有库表均支持查询 * 当该值为父权限集ID时，则基于父权限集中的权限查询

        :param parent_permission_set_id: The parent_permission_set_id of this ListSecurityDatasourceActionsRequest.
        :type parent_permission_set_id: str
        """
        self._parent_permission_set_id = parent_permission_set_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListSecurityDatasourceActionsRequest.

        集群ID，获取方法请参见[查询单个数据连接信息](ShowDataconnection.xml) * 查询Hive和DWS数据源操作信息时该数值为必填项，当数据源为DLI时无需填写

        :return: The cluster_id of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListSecurityDatasourceActionsRequest.

        集群ID，获取方法请参见[查询单个数据连接信息](ShowDataconnection.xml) * 查询Hive和DWS数据源操作信息时该数值为必填项，当数据源为DLI时无需填写

        :param cluster_id: The cluster_id of this ListSecurityDatasourceActionsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def datasource_type(self):
        """Gets the datasource_type of this ListSecurityDatasourceActionsRequest.

        数据源类型 * HIVE数据源 * DWS数据源 * DLI数据源

        :return: The datasource_type of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this ListSecurityDatasourceActionsRequest.

        数据源类型 * HIVE数据源 * DWS数据源 * DLI数据源

        :param datasource_type: The datasource_type of this ListSecurityDatasourceActionsRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def database_name(self):
        """Gets the database_name of this ListSecurityDatasourceActionsRequest.

        数据库名 `注意：该值作为查询关键字时，不能与url同时存在，需要指定其一进行查询`

        :return: The database_name of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListSecurityDatasourceActionsRequest.

        数据库名 `注意：该值作为查询关键字时，不能与url同时存在，需要指定其一进行查询`

        :param database_name: The database_name of this ListSecurityDatasourceActionsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        """Gets the schema_name of this ListSecurityDatasourceActionsRequest.

        schema名称

        :return: The schema_name of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this ListSecurityDatasourceActionsRequest.

        schema名称

        :param schema_name: The schema_name of this ListSecurityDatasourceActionsRequest.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this ListSecurityDatasourceActionsRequest.

        数据表名称

        :return: The table_name of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ListSecurityDatasourceActionsRequest.

        数据表名称

        :param table_name: The table_name of this ListSecurityDatasourceActionsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        """Gets the column_name of this ListSecurityDatasourceActionsRequest.

        数据字段名称

        :return: The column_name of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ListSecurityDatasourceActionsRequest.

        数据字段名称

        :param column_name: The column_name of this ListSecurityDatasourceActionsRequest.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def url(self):
        """Gets the url of this ListSecurityDatasourceActionsRequest.

        url路径名称 `注意：该值作为查询关键字时，不能与database_name同时存在，需要指定其一进行查询`

        :return: The url of this ListSecurityDatasourceActionsRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ListSecurityDatasourceActionsRequest.

        url路径名称 `注意：该值作为查询关键字时，不能与database_name同时存在，需要指定其一进行查询`

        :param url: The url of this ListSecurityDatasourceActionsRequest.
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
        if not isinstance(other, ListSecurityDatasourceActionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
