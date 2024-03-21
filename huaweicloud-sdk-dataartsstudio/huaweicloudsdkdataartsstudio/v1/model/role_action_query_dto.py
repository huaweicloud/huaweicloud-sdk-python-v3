# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleActionQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_permission_set_id': 'str',
        'cluster_id': 'str',
        'datasource_type': 'str',
        'database_names': 'list[str]',
        'schemas': 'list[str]',
        'table_names': 'list[str]',
        'column_names': 'list[str]'
    }

    attribute_map = {
        'parent_permission_set_id': 'parent_permission_set_id',
        'cluster_id': 'cluster_id',
        'datasource_type': 'datasource_type',
        'database_names': 'database_names',
        'schemas': 'schemas',
        'table_names': 'table_names',
        'column_names': 'column_names'
    }

    def __init__(self, parent_permission_set_id=None, cluster_id=None, datasource_type=None, database_names=None, schemas=None, table_names=None, column_names=None):
        """RoleActionQueryDTO

        The model defined in huaweicloud sdk

        :param parent_permission_set_id: 父权限集id
        :type parent_permission_set_id: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param datasource_type: 数据源类型, HIVE
        :type datasource_type: str
        :param database_names: 目前批量授权只支持单库下的多表授权，或同一集群下个多库授权，区分这两类可通过 传参中tables是否为空来判断
        :type database_names: list[str]
        :param schemas: dws权限涉及 schema，预留字段，在做DWS批量授权时应保持单schema下的批量授权，或者对单库下schema批量授权
        :type schemas: list[str]
        :param table_names: 数据表列表
        :type table_names: list[str]
        :param column_names: 数据字段列表
        :type column_names: list[str]
        """
        
        

        self._parent_permission_set_id = None
        self._cluster_id = None
        self._datasource_type = None
        self._database_names = None
        self._schemas = None
        self._table_names = None
        self._column_names = None
        self.discriminator = None

        self.parent_permission_set_id = parent_permission_set_id
        self.cluster_id = cluster_id
        self.datasource_type = datasource_type
        self.database_names = database_names
        if schemas is not None:
            self.schemas = schemas
        if table_names is not None:
            self.table_names = table_names
        if column_names is not None:
            self.column_names = column_names

    @property
    def parent_permission_set_id(self):
        """Gets the parent_permission_set_id of this RoleActionQueryDTO.

        父权限集id

        :return: The parent_permission_set_id of this RoleActionQueryDTO.
        :rtype: str
        """
        return self._parent_permission_set_id

    @parent_permission_set_id.setter
    def parent_permission_set_id(self, parent_permission_set_id):
        """Sets the parent_permission_set_id of this RoleActionQueryDTO.

        父权限集id

        :param parent_permission_set_id: The parent_permission_set_id of this RoleActionQueryDTO.
        :type parent_permission_set_id: str
        """
        self._parent_permission_set_id = parent_permission_set_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this RoleActionQueryDTO.

        集群id

        :return: The cluster_id of this RoleActionQueryDTO.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this RoleActionQueryDTO.

        集群id

        :param cluster_id: The cluster_id of this RoleActionQueryDTO.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def datasource_type(self):
        """Gets the datasource_type of this RoleActionQueryDTO.

        数据源类型, HIVE

        :return: The datasource_type of this RoleActionQueryDTO.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this RoleActionQueryDTO.

        数据源类型, HIVE

        :param datasource_type: The datasource_type of this RoleActionQueryDTO.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def database_names(self):
        """Gets the database_names of this RoleActionQueryDTO.

        目前批量授权只支持单库下的多表授权，或同一集群下个多库授权，区分这两类可通过 传参中tables是否为空来判断

        :return: The database_names of this RoleActionQueryDTO.
        :rtype: list[str]
        """
        return self._database_names

    @database_names.setter
    def database_names(self, database_names):
        """Sets the database_names of this RoleActionQueryDTO.

        目前批量授权只支持单库下的多表授权，或同一集群下个多库授权，区分这两类可通过 传参中tables是否为空来判断

        :param database_names: The database_names of this RoleActionQueryDTO.
        :type database_names: list[str]
        """
        self._database_names = database_names

    @property
    def schemas(self):
        """Gets the schemas of this RoleActionQueryDTO.

        dws权限涉及 schema，预留字段，在做DWS批量授权时应保持单schema下的批量授权，或者对单库下schema批量授权

        :return: The schemas of this RoleActionQueryDTO.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this RoleActionQueryDTO.

        dws权限涉及 schema，预留字段，在做DWS批量授权时应保持单schema下的批量授权，或者对单库下schema批量授权

        :param schemas: The schemas of this RoleActionQueryDTO.
        :type schemas: list[str]
        """
        self._schemas = schemas

    @property
    def table_names(self):
        """Gets the table_names of this RoleActionQueryDTO.

        数据表列表

        :return: The table_names of this RoleActionQueryDTO.
        :rtype: list[str]
        """
        return self._table_names

    @table_names.setter
    def table_names(self, table_names):
        """Sets the table_names of this RoleActionQueryDTO.

        数据表列表

        :param table_names: The table_names of this RoleActionQueryDTO.
        :type table_names: list[str]
        """
        self._table_names = table_names

    @property
    def column_names(self):
        """Gets the column_names of this RoleActionQueryDTO.

        数据字段列表

        :return: The column_names of this RoleActionQueryDTO.
        :rtype: list[str]
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """Sets the column_names of this RoleActionQueryDTO.

        数据字段列表

        :param column_names: The column_names of this RoleActionQueryDTO.
        :type column_names: list[str]
        """
        self._column_names = column_names

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
        if not isinstance(other, RoleActionQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
