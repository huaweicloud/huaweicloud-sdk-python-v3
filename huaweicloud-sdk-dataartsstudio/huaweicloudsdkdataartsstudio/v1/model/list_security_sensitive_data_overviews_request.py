# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecuritySensitiveDataOverviewsRequest:

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
        'datasource': 'str',
        'cluster_name': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'datasource': 'datasource',
        'cluster_name': 'cluster_name',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name'
    }

    def __init__(self, workspace=None, datasource=None, cluster_name=None, database_name=None, schema_name=None, table_name=None):
        """ListSecuritySensitiveDataOverviewsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param datasource: 数据源类型,HIVE数据源,DWS数据源,DLI数据源
        :type datasource: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param database_name: 数据库名称
        :type database_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param table_name: 表名称
        :type table_name: str
        """
        
        

        self._workspace = None
        self._datasource = None
        self._cluster_name = None
        self._database_name = None
        self._schema_name = None
        self._table_name = None
        self.discriminator = None

        self.workspace = workspace
        if datasource is not None:
            self.datasource = datasource
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if database_name is not None:
            self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name

    @property
    def workspace(self):
        """Gets the workspace of this ListSecuritySensitiveDataOverviewsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecuritySensitiveDataOverviewsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListSecuritySensitiveDataOverviewsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecuritySensitiveDataOverviewsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def datasource(self):
        """Gets the datasource of this ListSecuritySensitiveDataOverviewsRequest.

        数据源类型,HIVE数据源,DWS数据源,DLI数据源

        :return: The datasource of this ListSecuritySensitiveDataOverviewsRequest.
        :rtype: str
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this ListSecuritySensitiveDataOverviewsRequest.

        数据源类型,HIVE数据源,DWS数据源,DLI数据源

        :param datasource: The datasource of this ListSecuritySensitiveDataOverviewsRequest.
        :type datasource: str
        """
        self._datasource = datasource

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ListSecuritySensitiveDataOverviewsRequest.

        集群名称

        :return: The cluster_name of this ListSecuritySensitiveDataOverviewsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ListSecuritySensitiveDataOverviewsRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListSecuritySensitiveDataOverviewsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database_name(self):
        """Gets the database_name of this ListSecuritySensitiveDataOverviewsRequest.

        数据库名称

        :return: The database_name of this ListSecuritySensitiveDataOverviewsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListSecuritySensitiveDataOverviewsRequest.

        数据库名称

        :param database_name: The database_name of this ListSecuritySensitiveDataOverviewsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        """Gets the schema_name of this ListSecuritySensitiveDataOverviewsRequest.

        schema名称

        :return: The schema_name of this ListSecuritySensitiveDataOverviewsRequest.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this ListSecuritySensitiveDataOverviewsRequest.

        schema名称

        :param schema_name: The schema_name of this ListSecuritySensitiveDataOverviewsRequest.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this ListSecuritySensitiveDataOverviewsRequest.

        表名称

        :return: The table_name of this ListSecuritySensitiveDataOverviewsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ListSecuritySensitiveDataOverviewsRequest.

        表名称

        :param table_name: The table_name of this ListSecuritySensitiveDataOverviewsRequest.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, ListSecuritySensitiveDataOverviewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
