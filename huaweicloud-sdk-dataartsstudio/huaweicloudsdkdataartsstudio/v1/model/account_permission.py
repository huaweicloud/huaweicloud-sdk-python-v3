# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountPermission:

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
        'cluster_name': 'str',
        'column_name': 'str',
        'database_name': 'str',
        'datasource_type': 'str',
        'expire_msg': 'str',
        'expire_status': 'str',
        'expire_time': 'int',
        'id': 'str',
        'instance_id': 'str',
        'member_id': 'str',
        'member_name': 'str',
        'permission_action': 'str',
        'permission_action_code': 'int',
        'project_id': 'str',
        'row_level_security': 'str',
        'row_level_security_desc': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'column_name': 'column_name',
        'database_name': 'database_name',
        'datasource_type': 'datasource_type',
        'expire_msg': 'expire_msg',
        'expire_status': 'expire_status',
        'expire_time': 'expire_time',
        'id': 'id',
        'instance_id': 'instance_id',
        'member_id': 'member_id',
        'member_name': 'member_name',
        'permission_action': 'permission_action',
        'permission_action_code': 'permission_action_code',
        'project_id': 'project_id',
        'row_level_security': 'row_level_security',
        'row_level_security_desc': 'row_level_security_desc',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, cluster_id=None, cluster_name=None, column_name=None, database_name=None, datasource_type=None, expire_msg=None, expire_status=None, expire_time=None, id=None, instance_id=None, member_id=None, member_name=None, permission_action=None, permission_action_code=None, project_id=None, row_level_security=None, row_level_security_desc=None, schema_name=None, table_name=None, workspace_id=None):
        r"""AccountPermission

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param column_name: 列名
        :type column_name: str
        :param database_name: 数据库名
        :type database_name: str
        :param datasource_type: 数据源类型,HIVE
        :type datasource_type: str
        :param expire_msg: 到期信息
        :type expire_msg: str
        :param expire_status: 权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON
        :type expire_status: str
        :param expire_time: 到期时间
        :type expire_time: int
        :param id: 权限id
        :type id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param member_id: 成员id
        :type member_id: str
        :param member_name: 成员名称
        :type member_name: str
        :param permission_action: 权限类别,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE
        :type permission_action: str
        :param permission_action_code: 权限位图
        :type permission_action_code: int
        :param project_id: 项目ID
        :type project_id: str
        :param row_level_security: 行级权限表达式
        :type row_level_security: str
        :param row_level_security_desc: 行级权限描述
        :type row_level_security_desc: str
        :param schema_name: schema名称
        :type schema_name: str
        :param table_name: 表名
        :type table_name: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._column_name = None
        self._database_name = None
        self._datasource_type = None
        self._expire_msg = None
        self._expire_status = None
        self._expire_time = None
        self._id = None
        self._instance_id = None
        self._member_id = None
        self._member_name = None
        self._permission_action = None
        self._permission_action_code = None
        self._project_id = None
        self._row_level_security = None
        self._row_level_security_desc = None
        self._schema_name = None
        self._table_name = None
        self._workspace_id = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        if column_name is not None:
            self.column_name = column_name
        if database_name is not None:
            self.database_name = database_name
        self.datasource_type = datasource_type
        if expire_msg is not None:
            self.expire_msg = expire_msg
        self.expire_status = expire_status
        if expire_time is not None:
            self.expire_time = expire_time
        self.id = id
        self.instance_id = instance_id
        if member_id is not None:
            self.member_id = member_id
        if member_name is not None:
            self.member_name = member_name
        if permission_action is not None:
            self.permission_action = permission_action
        if permission_action_code is not None:
            self.permission_action_code = permission_action_code
        self.project_id = project_id
        if row_level_security is not None:
            self.row_level_security = row_level_security
        if row_level_security_desc is not None:
            self.row_level_security_desc = row_level_security_desc
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        self.workspace_id = workspace_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this AccountPermission.

        集群id

        :return: The cluster_id of this AccountPermission.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this AccountPermission.

        集群id

        :param cluster_id: The cluster_id of this AccountPermission.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this AccountPermission.

        集群名称

        :return: The cluster_name of this AccountPermission.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this AccountPermission.

        集群名称

        :param cluster_name: The cluster_name of this AccountPermission.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def column_name(self):
        r"""Gets the column_name of this AccountPermission.

        列名

        :return: The column_name of this AccountPermission.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this AccountPermission.

        列名

        :param column_name: The column_name of this AccountPermission.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def database_name(self):
        r"""Gets the database_name of this AccountPermission.

        数据库名

        :return: The database_name of this AccountPermission.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this AccountPermission.

        数据库名

        :param database_name: The database_name of this AccountPermission.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this AccountPermission.

        数据源类型,HIVE

        :return: The datasource_type of this AccountPermission.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this AccountPermission.

        数据源类型,HIVE

        :param datasource_type: The datasource_type of this AccountPermission.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def expire_msg(self):
        r"""Gets the expire_msg of this AccountPermission.

        到期信息

        :return: The expire_msg of this AccountPermission.
        :rtype: str
        """
        return self._expire_msg

    @expire_msg.setter
    def expire_msg(self, expire_msg):
        r"""Sets the expire_msg of this AccountPermission.

        到期信息

        :param expire_msg: The expire_msg of this AccountPermission.
        :type expire_msg: str
        """
        self._expire_msg = expire_msg

    @property
    def expire_status(self):
        r"""Gets the expire_status of this AccountPermission.

        权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON

        :return: The expire_status of this AccountPermission.
        :rtype: str
        """
        return self._expire_status

    @expire_status.setter
    def expire_status(self, expire_status):
        r"""Sets the expire_status of this AccountPermission.

        权限状态,REVOKE_FAILED,TO_BE_REVOKE,INACTIVE,PERMANENTLY_ACTIVE,ACTIVE,EXPIRE_SOON

        :param expire_status: The expire_status of this AccountPermission.
        :type expire_status: str
        """
        self._expire_status = expire_status

    @property
    def expire_time(self):
        r"""Gets the expire_time of this AccountPermission.

        到期时间

        :return: The expire_time of this AccountPermission.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this AccountPermission.

        到期时间

        :param expire_time: The expire_time of this AccountPermission.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def id(self):
        r"""Gets the id of this AccountPermission.

        权限id

        :return: The id of this AccountPermission.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AccountPermission.

        权限id

        :param id: The id of this AccountPermission.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AccountPermission.

        实例id

        :return: The instance_id of this AccountPermission.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AccountPermission.

        实例id

        :param instance_id: The instance_id of this AccountPermission.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def member_id(self):
        r"""Gets the member_id of this AccountPermission.

        成员id

        :return: The member_id of this AccountPermission.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this AccountPermission.

        成员id

        :param member_id: The member_id of this AccountPermission.
        :type member_id: str
        """
        self._member_id = member_id

    @property
    def member_name(self):
        r"""Gets the member_name of this AccountPermission.

        成员名称

        :return: The member_name of this AccountPermission.
        :rtype: str
        """
        return self._member_name

    @member_name.setter
    def member_name(self, member_name):
        r"""Sets the member_name of this AccountPermission.

        成员名称

        :param member_name: The member_name of this AccountPermission.
        :type member_name: str
        """
        self._member_name = member_name

    @property
    def permission_action(self):
        r"""Gets the permission_action of this AccountPermission.

        权限类别,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE

        :return: The permission_action of this AccountPermission.
        :rtype: str
        """
        return self._permission_action

    @permission_action.setter
    def permission_action(self, permission_action):
        r"""Sets the permission_action of this AccountPermission.

        权限类别,ALL,SELECT,UPDATE,CREATE,DROP,ALTER,INDEX,LOCK,READ,WRITE

        :param permission_action: The permission_action of this AccountPermission.
        :type permission_action: str
        """
        self._permission_action = permission_action

    @property
    def permission_action_code(self):
        r"""Gets the permission_action_code of this AccountPermission.

        权限位图

        :return: The permission_action_code of this AccountPermission.
        :rtype: int
        """
        return self._permission_action_code

    @permission_action_code.setter
    def permission_action_code(self, permission_action_code):
        r"""Sets the permission_action_code of this AccountPermission.

        权限位图

        :param permission_action_code: The permission_action_code of this AccountPermission.
        :type permission_action_code: int
        """
        self._permission_action_code = permission_action_code

    @property
    def project_id(self):
        r"""Gets the project_id of this AccountPermission.

        项目ID

        :return: The project_id of this AccountPermission.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AccountPermission.

        项目ID

        :param project_id: The project_id of this AccountPermission.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def row_level_security(self):
        r"""Gets the row_level_security of this AccountPermission.

        行级权限表达式

        :return: The row_level_security of this AccountPermission.
        :rtype: str
        """
        return self._row_level_security

    @row_level_security.setter
    def row_level_security(self, row_level_security):
        r"""Sets the row_level_security of this AccountPermission.

        行级权限表达式

        :param row_level_security: The row_level_security of this AccountPermission.
        :type row_level_security: str
        """
        self._row_level_security = row_level_security

    @property
    def row_level_security_desc(self):
        r"""Gets the row_level_security_desc of this AccountPermission.

        行级权限描述

        :return: The row_level_security_desc of this AccountPermission.
        :rtype: str
        """
        return self._row_level_security_desc

    @row_level_security_desc.setter
    def row_level_security_desc(self, row_level_security_desc):
        r"""Sets the row_level_security_desc of this AccountPermission.

        行级权限描述

        :param row_level_security_desc: The row_level_security_desc of this AccountPermission.
        :type row_level_security_desc: str
        """
        self._row_level_security_desc = row_level_security_desc

    @property
    def schema_name(self):
        r"""Gets the schema_name of this AccountPermission.

        schema名称

        :return: The schema_name of this AccountPermission.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this AccountPermission.

        schema名称

        :param schema_name: The schema_name of this AccountPermission.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this AccountPermission.

        表名

        :return: The table_name of this AccountPermission.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this AccountPermission.

        表名

        :param table_name: The table_name of this AccountPermission.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AccountPermission.

        工作空间id

        :return: The workspace_id of this AccountPermission.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AccountPermission.

        工作空间id

        :param workspace_id: The workspace_id of this AccountPermission.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, AccountPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
