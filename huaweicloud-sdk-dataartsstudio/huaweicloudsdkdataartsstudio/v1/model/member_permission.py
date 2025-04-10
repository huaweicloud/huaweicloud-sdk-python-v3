# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_set_id': 'str',
        'permission_source': 'str',
        'permission_actions': 'str',
        'url': 'str',
        'datasource_type': 'str',
        'cluster_name': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'column_name': 'str'
    }

    attribute_map = {
        'permission_set_id': 'permission_set_id',
        'permission_source': 'permission_source',
        'permission_actions': 'permission_actions',
        'url': 'url',
        'datasource_type': 'datasource_type',
        'cluster_name': 'cluster_name',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'column_name': 'column_name'
    }

    def __init__(self, permission_set_id=None, permission_source=None, permission_actions=None, url=None, datasource_type=None, cluster_name=None, database_name=None, schema_name=None, table_name=None, column_name=None):
        r"""MemberPermission

        The model defined in huaweicloud sdk

        :param permission_set_id: 权限集ID
        :type permission_set_id: str
        :param permission_source: 权限来源：1、权限集名称。2、权限审批
        :type permission_source: str
        :param permission_actions: 权限类别,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE
        :type permission_actions: str
        :param url: Hive数据源，指定url权限的策略信息
        :type url: str
        :param datasource_type: 数据源类型
        :type datasource_type: str
        :param cluster_name: 集群名
        :type cluster_name: str
        :param database_name: 数据库名
        :type database_name: str
        :param schema_name: schema名
        :type schema_name: str
        :param table_name: 表名
        :type table_name: str
        :param column_name: 列名
        :type column_name: str
        """
        
        

        self._permission_set_id = None
        self._permission_source = None
        self._permission_actions = None
        self._url = None
        self._datasource_type = None
        self._cluster_name = None
        self._database_name = None
        self._schema_name = None
        self._table_name = None
        self._column_name = None
        self.discriminator = None

        self.permission_set_id = permission_set_id
        self.permission_source = permission_source
        self.permission_actions = permission_actions
        if url is not None:
            self.url = url
        self.datasource_type = datasource_type
        self.cluster_name = cluster_name
        self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        self.table_name = table_name
        if column_name is not None:
            self.column_name = column_name

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this MemberPermission.

        权限集ID

        :return: The permission_set_id of this MemberPermission.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this MemberPermission.

        权限集ID

        :param permission_set_id: The permission_set_id of this MemberPermission.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def permission_source(self):
        r"""Gets the permission_source of this MemberPermission.

        权限来源：1、权限集名称。2、权限审批

        :return: The permission_source of this MemberPermission.
        :rtype: str
        """
        return self._permission_source

    @permission_source.setter
    def permission_source(self, permission_source):
        r"""Sets the permission_source of this MemberPermission.

        权限来源：1、权限集名称。2、权限审批

        :param permission_source: The permission_source of this MemberPermission.
        :type permission_source: str
        """
        self._permission_source = permission_source

    @property
    def permission_actions(self):
        r"""Gets the permission_actions of this MemberPermission.

        权限类别,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE

        :return: The permission_actions of this MemberPermission.
        :rtype: str
        """
        return self._permission_actions

    @permission_actions.setter
    def permission_actions(self, permission_actions):
        r"""Sets the permission_actions of this MemberPermission.

        权限类别,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE

        :param permission_actions: The permission_actions of this MemberPermission.
        :type permission_actions: str
        """
        self._permission_actions = permission_actions

    @property
    def url(self):
        r"""Gets the url of this MemberPermission.

        Hive数据源，指定url权限的策略信息

        :return: The url of this MemberPermission.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this MemberPermission.

        Hive数据源，指定url权限的策略信息

        :param url: The url of this MemberPermission.
        :type url: str
        """
        self._url = url

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this MemberPermission.

        数据源类型

        :return: The datasource_type of this MemberPermission.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this MemberPermission.

        数据源类型

        :param datasource_type: The datasource_type of this MemberPermission.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this MemberPermission.

        集群名

        :return: The cluster_name of this MemberPermission.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this MemberPermission.

        集群名

        :param cluster_name: The cluster_name of this MemberPermission.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database_name(self):
        r"""Gets the database_name of this MemberPermission.

        数据库名

        :return: The database_name of this MemberPermission.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this MemberPermission.

        数据库名

        :param database_name: The database_name of this MemberPermission.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this MemberPermission.

        schema名

        :return: The schema_name of this MemberPermission.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this MemberPermission.

        schema名

        :param schema_name: The schema_name of this MemberPermission.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this MemberPermission.

        表名

        :return: The table_name of this MemberPermission.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this MemberPermission.

        表名

        :param table_name: The table_name of this MemberPermission.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        r"""Gets the column_name of this MemberPermission.

        列名

        :return: The column_name of this MemberPermission.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this MemberPermission.

        列名

        :param column_name: The column_name of this MemberPermission.
        :type column_name: str
        """
        self._column_name = column_name

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
        if not isinstance(other, MemberPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
