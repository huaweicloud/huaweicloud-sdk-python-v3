# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityPermissionSetPermissionsRequest:

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
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'permission_type': 'str',
        'permission_action': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'datasource_type': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'column_name': 'str',
        'sync_status': 'str',
        'order_by': 'str',
        'order_by_asc': 'bool'
    }

    attribute_map = {
        'permission_set_id': 'permission_set_id',
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'permission_type': 'permission_type',
        'permission_action': 'permission_action',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'datasource_type': 'datasource_type',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'column_name': 'column_name',
        'sync_status': 'sync_status',
        'order_by': 'order_by',
        'order_by_asc': 'order_by_asc'
    }

    def __init__(self, permission_set_id=None, workspace=None, limit=None, offset=None, permission_type=None, permission_action=None, cluster_id=None, cluster_name=None, datasource_type=None, database_name=None, table_name=None, column_name=None, sync_status=None, order_by=None, order_by_asc=None):
        r"""ListSecurityPermissionSetPermissionsRequest

        The model defined in huaweicloud sdk

        :param permission_set_id: 权限集id
        :type permission_set_id: str
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param permission_type: 权限类型,DENY,ALLOW
        :type permission_type: str
        :param permission_action: 权限操作,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE
        :type permission_action: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param datasource_type: 数据源类型,HIVE
        :type datasource_type: str
        :param database_name: 数据库名称
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param column_name: 列名称
        :type column_name: str
        :param sync_status: 同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL
        :type sync_status: str
        :param order_by: 排序参数, CLUSTER_NAME, DATABASE_NAME
        :type order_by: str
        :param order_by_asc: 是否升序（仅指定排序参数时有效）
        :type order_by_asc: bool
        """
        
        

        self._permission_set_id = None
        self._workspace = None
        self._limit = None
        self._offset = None
        self._permission_type = None
        self._permission_action = None
        self._cluster_id = None
        self._cluster_name = None
        self._datasource_type = None
        self._database_name = None
        self._table_name = None
        self._column_name = None
        self._sync_status = None
        self._order_by = None
        self._order_by_asc = None
        self.discriminator = None

        self.permission_set_id = permission_set_id
        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if permission_type is not None:
            self.permission_type = permission_type
        if permission_action is not None:
            self.permission_action = permission_action
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if column_name is not None:
            self.column_name = column_name
        if sync_status is not None:
            self.sync_status = sync_status
        if order_by is not None:
            self.order_by = order_by
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this ListSecurityPermissionSetPermissionsRequest.

        权限集id

        :return: The permission_set_id of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this ListSecurityPermissionSetPermissionsRequest.

        权限集id

        :param permission_set_id: The permission_set_id of this ListSecurityPermissionSetPermissionsRequest.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityPermissionSetPermissionsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityPermissionSetPermissionsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityPermissionSetPermissionsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityPermissionSetPermissionsRequest.

        limit

        :return: The limit of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityPermissionSetPermissionsRequest.

        limit

        :param limit: The limit of this ListSecurityPermissionSetPermissionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityPermissionSetPermissionsRequest.

        offset

        :return: The offset of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityPermissionSetPermissionsRequest.

        offset

        :param offset: The offset of this ListSecurityPermissionSetPermissionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def permission_type(self):
        r"""Gets the permission_type of this ListSecurityPermissionSetPermissionsRequest.

        权限类型,DENY,ALLOW

        :return: The permission_type of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this ListSecurityPermissionSetPermissionsRequest.

        权限类型,DENY,ALLOW

        :param permission_type: The permission_type of this ListSecurityPermissionSetPermissionsRequest.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def permission_action(self):
        r"""Gets the permission_action of this ListSecurityPermissionSetPermissionsRequest.

        权限操作,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE

        :return: The permission_action of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._permission_action

    @permission_action.setter
    def permission_action(self, permission_action):
        r"""Sets the permission_action of this ListSecurityPermissionSetPermissionsRequest.

        权限操作,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE

        :param permission_action: The permission_action of this ListSecurityPermissionSetPermissionsRequest.
        :type permission_action: str
        """
        self._permission_action = permission_action

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListSecurityPermissionSetPermissionsRequest.

        集群id

        :return: The cluster_id of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListSecurityPermissionSetPermissionsRequest.

        集群id

        :param cluster_id: The cluster_id of this ListSecurityPermissionSetPermissionsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListSecurityPermissionSetPermissionsRequest.

        集群名称

        :return: The cluster_name of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListSecurityPermissionSetPermissionsRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListSecurityPermissionSetPermissionsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this ListSecurityPermissionSetPermissionsRequest.

        数据源类型,HIVE

        :return: The datasource_type of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this ListSecurityPermissionSetPermissionsRequest.

        数据源类型,HIVE

        :param datasource_type: The datasource_type of this ListSecurityPermissionSetPermissionsRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def database_name(self):
        r"""Gets the database_name of this ListSecurityPermissionSetPermissionsRequest.

        数据库名称

        :return: The database_name of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListSecurityPermissionSetPermissionsRequest.

        数据库名称

        :param database_name: The database_name of this ListSecurityPermissionSetPermissionsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListSecurityPermissionSetPermissionsRequest.

        表名称

        :return: The table_name of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListSecurityPermissionSetPermissionsRequest.

        表名称

        :param table_name: The table_name of this ListSecurityPermissionSetPermissionsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        r"""Gets the column_name of this ListSecurityPermissionSetPermissionsRequest.

        列名称

        :return: The column_name of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this ListSecurityPermissionSetPermissionsRequest.

        列名称

        :param column_name: The column_name of this ListSecurityPermissionSetPermissionsRequest.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def sync_status(self):
        r"""Gets the sync_status of this ListSecurityPermissionSetPermissionsRequest.

        同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL

        :return: The sync_status of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this ListSecurityPermissionSetPermissionsRequest.

        同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL

        :param sync_status: The sync_status of this ListSecurityPermissionSetPermissionsRequest.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityPermissionSetPermissionsRequest.

        排序参数, CLUSTER_NAME, DATABASE_NAME

        :return: The order_by of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityPermissionSetPermissionsRequest.

        排序参数, CLUSTER_NAME, DATABASE_NAME

        :param order_by: The order_by of this ListSecurityPermissionSetPermissionsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_asc(self):
        r"""Gets the order_by_asc of this ListSecurityPermissionSetPermissionsRequest.

        是否升序（仅指定排序参数时有效）

        :return: The order_by_asc of this ListSecurityPermissionSetPermissionsRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        r"""Sets the order_by_asc of this ListSecurityPermissionSetPermissionsRequest.

        是否升序（仅指定排序参数时有效）

        :param order_by_asc: The order_by_asc of this ListSecurityPermissionSetPermissionsRequest.
        :type order_by_asc: bool
        """
        self._order_by_asc = order_by_asc

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
        if not isinstance(other, ListSecurityPermissionSetPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
