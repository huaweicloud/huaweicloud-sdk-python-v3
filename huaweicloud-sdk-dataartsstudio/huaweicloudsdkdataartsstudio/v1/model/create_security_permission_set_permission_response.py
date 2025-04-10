# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityPermissionSetPermissionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'permission_set_id': 'str',
        'project_id': 'str',
        'instance_id': 'str',
        'permission_type': 'str',
        'permission_action': 'str',
        'permission_actions': 'list[str]',
        'permission_action_code': 'int',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'datasource_type': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'namespace': 'str',
        'table_name': 'str',
        'column_name': 'str',
        'row_level_security': 'str',
        'sync_status': 'str',
        'sync_msg': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permission_set_id': 'permission_set_id',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'permission_type': 'permission_type',
        'permission_action': 'permission_action',
        'permission_actions': 'permission_actions',
        'permission_action_code': 'permission_action_code',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'datasource_type': 'datasource_type',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'namespace': 'namespace',
        'table_name': 'table_name',
        'column_name': 'column_name',
        'row_level_security': 'row_level_security',
        'sync_status': 'sync_status',
        'sync_msg': 'sync_msg',
        'url': 'url'
    }

    def __init__(self, id=None, permission_set_id=None, project_id=None, instance_id=None, permission_type=None, permission_action=None, permission_actions=None, permission_action_code=None, cluster_id=None, cluster_name=None, datasource_type=None, database_name=None, schema_name=None, namespace=None, table_name=None, column_name=None, row_level_security=None, sync_status=None, sync_msg=None, url=None):
        r"""CreateSecurityPermissionSetPermissionResponse

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param permission_set_id: 权限集id
        :type permission_set_id: str
        :param project_id: 项目id
        :type project_id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param permission_type: 权限类型, DENY, ALLOW
        :type permission_type: str
        :param permission_action: 权限操作列表
        :type permission_action: str
        :param permission_actions: 权限操作列表
        :type permission_actions: list[str]
        :param permission_action_code: 权限操作编码, 位图
        :type permission_action_code: int
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
        :param namespace: 命名空间
        :type namespace: str
        :param table_name: 表名称
        :type table_name: str
        :param column_name: 列名称
        :type column_name: str
        :param row_level_security: 行级策略
        :type row_level_security: str
        :param sync_status: 同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL
        :type sync_status: str
        :param sync_msg: 同步信息
        :type sync_msg: str
        :param url: url路径名称。
        :type url: str
        """
        
        super(CreateSecurityPermissionSetPermissionResponse, self).__init__()

        self._id = None
        self._permission_set_id = None
        self._project_id = None
        self._instance_id = None
        self._permission_type = None
        self._permission_action = None
        self._permission_actions = None
        self._permission_action_code = None
        self._cluster_id = None
        self._cluster_name = None
        self._datasource_type = None
        self._database_name = None
        self._schema_name = None
        self._namespace = None
        self._table_name = None
        self._column_name = None
        self._row_level_security = None
        self._sync_status = None
        self._sync_msg = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if permission_type is not None:
            self.permission_type = permission_type
        if permission_action is not None:
            self.permission_action = permission_action
        if permission_actions is not None:
            self.permission_actions = permission_actions
        if permission_action_code is not None:
            self.permission_action_code = permission_action_code
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
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_msg is not None:
            self.sync_msg = sync_msg
        if url is not None:
            self.url = url

    @property
    def id(self):
        r"""Gets the id of this CreateSecurityPermissionSetPermissionResponse.

        id

        :return: The id of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSecurityPermissionSetPermissionResponse.

        id

        :param id: The id of this CreateSecurityPermissionSetPermissionResponse.
        :type id: str
        """
        self._id = id

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this CreateSecurityPermissionSetPermissionResponse.

        权限集id

        :return: The permission_set_id of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this CreateSecurityPermissionSetPermissionResponse.

        权限集id

        :param permission_set_id: The permission_set_id of this CreateSecurityPermissionSetPermissionResponse.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateSecurityPermissionSetPermissionResponse.

        项目id

        :return: The project_id of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateSecurityPermissionSetPermissionResponse.

        项目id

        :param project_id: The project_id of this CreateSecurityPermissionSetPermissionResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateSecurityPermissionSetPermissionResponse.

        实例id

        :return: The instance_id of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateSecurityPermissionSetPermissionResponse.

        实例id

        :param instance_id: The instance_id of this CreateSecurityPermissionSetPermissionResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def permission_type(self):
        r"""Gets the permission_type of this CreateSecurityPermissionSetPermissionResponse.

        权限类型, DENY, ALLOW

        :return: The permission_type of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this CreateSecurityPermissionSetPermissionResponse.

        权限类型, DENY, ALLOW

        :param permission_type: The permission_type of this CreateSecurityPermissionSetPermissionResponse.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def permission_action(self):
        r"""Gets the permission_action of this CreateSecurityPermissionSetPermissionResponse.

        权限操作列表

        :return: The permission_action of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._permission_action

    @permission_action.setter
    def permission_action(self, permission_action):
        r"""Sets the permission_action of this CreateSecurityPermissionSetPermissionResponse.

        权限操作列表

        :param permission_action: The permission_action of this CreateSecurityPermissionSetPermissionResponse.
        :type permission_action: str
        """
        self._permission_action = permission_action

    @property
    def permission_actions(self):
        r"""Gets the permission_actions of this CreateSecurityPermissionSetPermissionResponse.

        权限操作列表

        :return: The permission_actions of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: list[str]
        """
        return self._permission_actions

    @permission_actions.setter
    def permission_actions(self, permission_actions):
        r"""Sets the permission_actions of this CreateSecurityPermissionSetPermissionResponse.

        权限操作列表

        :param permission_actions: The permission_actions of this CreateSecurityPermissionSetPermissionResponse.
        :type permission_actions: list[str]
        """
        self._permission_actions = permission_actions

    @property
    def permission_action_code(self):
        r"""Gets the permission_action_code of this CreateSecurityPermissionSetPermissionResponse.

        权限操作编码, 位图

        :return: The permission_action_code of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: int
        """
        return self._permission_action_code

    @permission_action_code.setter
    def permission_action_code(self, permission_action_code):
        r"""Sets the permission_action_code of this CreateSecurityPermissionSetPermissionResponse.

        权限操作编码, 位图

        :param permission_action_code: The permission_action_code of this CreateSecurityPermissionSetPermissionResponse.
        :type permission_action_code: int
        """
        self._permission_action_code = permission_action_code

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateSecurityPermissionSetPermissionResponse.

        集群id

        :return: The cluster_id of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateSecurityPermissionSetPermissionResponse.

        集群id

        :param cluster_id: The cluster_id of this CreateSecurityPermissionSetPermissionResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CreateSecurityPermissionSetPermissionResponse.

        集群名称

        :return: The cluster_name of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CreateSecurityPermissionSetPermissionResponse.

        集群名称

        :param cluster_name: The cluster_name of this CreateSecurityPermissionSetPermissionResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this CreateSecurityPermissionSetPermissionResponse.

        数据源类型, HIVE

        :return: The datasource_type of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this CreateSecurityPermissionSetPermissionResponse.

        数据源类型, HIVE

        :param datasource_type: The datasource_type of this CreateSecurityPermissionSetPermissionResponse.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def database_name(self):
        r"""Gets the database_name of this CreateSecurityPermissionSetPermissionResponse.

        数据库名称

        :return: The database_name of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this CreateSecurityPermissionSetPermissionResponse.

        数据库名称

        :param database_name: The database_name of this CreateSecurityPermissionSetPermissionResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this CreateSecurityPermissionSetPermissionResponse.

        模式名称

        :return: The schema_name of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this CreateSecurityPermissionSetPermissionResponse.

        模式名称

        :param schema_name: The schema_name of this CreateSecurityPermissionSetPermissionResponse.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateSecurityPermissionSetPermissionResponse.

        命名空间

        :return: The namespace of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateSecurityPermissionSetPermissionResponse.

        命名空间

        :param namespace: The namespace of this CreateSecurityPermissionSetPermissionResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def table_name(self):
        r"""Gets the table_name of this CreateSecurityPermissionSetPermissionResponse.

        表名称

        :return: The table_name of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this CreateSecurityPermissionSetPermissionResponse.

        表名称

        :param table_name: The table_name of this CreateSecurityPermissionSetPermissionResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def column_name(self):
        r"""Gets the column_name of this CreateSecurityPermissionSetPermissionResponse.

        列名称

        :return: The column_name of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this CreateSecurityPermissionSetPermissionResponse.

        列名称

        :param column_name: The column_name of this CreateSecurityPermissionSetPermissionResponse.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def row_level_security(self):
        r"""Gets the row_level_security of this CreateSecurityPermissionSetPermissionResponse.

        行级策略

        :return: The row_level_security of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._row_level_security

    @row_level_security.setter
    def row_level_security(self, row_level_security):
        r"""Sets the row_level_security of this CreateSecurityPermissionSetPermissionResponse.

        行级策略

        :param row_level_security: The row_level_security of this CreateSecurityPermissionSetPermissionResponse.
        :type row_level_security: str
        """
        self._row_level_security = row_level_security

    @property
    def sync_status(self):
        r"""Gets the sync_status of this CreateSecurityPermissionSetPermissionResponse.

        同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL

        :return: The sync_status of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this CreateSecurityPermissionSetPermissionResponse.

        同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL

        :param sync_status: The sync_status of this CreateSecurityPermissionSetPermissionResponse.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def sync_msg(self):
        r"""Gets the sync_msg of this CreateSecurityPermissionSetPermissionResponse.

        同步信息

        :return: The sync_msg of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._sync_msg

    @sync_msg.setter
    def sync_msg(self, sync_msg):
        r"""Sets the sync_msg of this CreateSecurityPermissionSetPermissionResponse.

        同步信息

        :param sync_msg: The sync_msg of this CreateSecurityPermissionSetPermissionResponse.
        :type sync_msg: str
        """
        self._sync_msg = sync_msg

    @property
    def url(self):
        r"""Gets the url of this CreateSecurityPermissionSetPermissionResponse.

        url路径名称。

        :return: The url of this CreateSecurityPermissionSetPermissionResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateSecurityPermissionSetPermissionResponse.

        url路径名称。

        :param url: The url of this CreateSecurityPermissionSetPermissionResponse.
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
        if not isinstance(other, CreateSecurityPermissionSetPermissionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
