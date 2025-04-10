# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosePermissionDetail:

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
        'task_id': 'str',
        'user_name': 'str',
        'permission_type': 'str',
        'permission_action': 'str',
        'permission_source': 'str',
        'datasource_type': 'str',
        'cluster_name': 'str',
        'database': 'str',
        'schema': 'str',
        'table': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_id': 'task_id',
        'user_name': 'user_name',
        'permission_type': 'permission_type',
        'permission_action': 'permission_action',
        'permission_source': 'permission_source',
        'datasource_type': 'datasource_type',
        'cluster_name': 'cluster_name',
        'database': 'database',
        'schema': 'schema',
        'table': 'table',
        'remark': 'remark'
    }

    def __init__(self, id=None, task_id=None, user_name=None, permission_type=None, permission_action=None, permission_source=None, datasource_type=None, cluster_name=None, database=None, schema=None, table=None, remark=None):
        r"""DiagnosePermissionDetail

        The model defined in huaweicloud sdk

        :param id: 权限配置编号。
        :type id: str
        :param task_id: 诊断任务id。
        :type task_id: str
        :param user_name: 用户名。
        :type user_name: str
        :param permission_type: 权限类型。
        :type permission_type: str
        :param permission_action: 权限操作。
        :type permission_action: str
        :param permission_source: 权限来源。
        :type permission_source: str
        :param datasource_type: 数据源类型。
        :type datasource_type: str
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param database: 数据库名。
        :type database: str
        :param schema: schema名。
        :type schema: str
        :param table: 表名。
        :type table: str
        :param remark: 备注。
        :type remark: str
        """
        
        

        self._id = None
        self._task_id = None
        self._user_name = None
        self._permission_type = None
        self._permission_action = None
        self._permission_source = None
        self._datasource_type = None
        self._cluster_name = None
        self._database = None
        self._schema = None
        self._table = None
        self._remark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_id is not None:
            self.task_id = task_id
        if user_name is not None:
            self.user_name = user_name
        if permission_type is not None:
            self.permission_type = permission_type
        if permission_action is not None:
            self.permission_action = permission_action
        if permission_source is not None:
            self.permission_source = permission_source
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if database is not None:
            self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        r"""Gets the id of this DiagnosePermissionDetail.

        权限配置编号。

        :return: The id of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DiagnosePermissionDetail.

        权限配置编号。

        :param id: The id of this DiagnosePermissionDetail.
        :type id: str
        """
        self._id = id

    @property
    def task_id(self):
        r"""Gets the task_id of this DiagnosePermissionDetail.

        诊断任务id。

        :return: The task_id of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DiagnosePermissionDetail.

        诊断任务id。

        :param task_id: The task_id of this DiagnosePermissionDetail.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def user_name(self):
        r"""Gets the user_name of this DiagnosePermissionDetail.

        用户名。

        :return: The user_name of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DiagnosePermissionDetail.

        用户名。

        :param user_name: The user_name of this DiagnosePermissionDetail.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def permission_type(self):
        r"""Gets the permission_type of this DiagnosePermissionDetail.

        权限类型。

        :return: The permission_type of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this DiagnosePermissionDetail.

        权限类型。

        :param permission_type: The permission_type of this DiagnosePermissionDetail.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def permission_action(self):
        r"""Gets the permission_action of this DiagnosePermissionDetail.

        权限操作。

        :return: The permission_action of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._permission_action

    @permission_action.setter
    def permission_action(self, permission_action):
        r"""Sets the permission_action of this DiagnosePermissionDetail.

        权限操作。

        :param permission_action: The permission_action of this DiagnosePermissionDetail.
        :type permission_action: str
        """
        self._permission_action = permission_action

    @property
    def permission_source(self):
        r"""Gets the permission_source of this DiagnosePermissionDetail.

        权限来源。

        :return: The permission_source of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._permission_source

    @permission_source.setter
    def permission_source(self, permission_source):
        r"""Sets the permission_source of this DiagnosePermissionDetail.

        权限来源。

        :param permission_source: The permission_source of this DiagnosePermissionDetail.
        :type permission_source: str
        """
        self._permission_source = permission_source

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this DiagnosePermissionDetail.

        数据源类型。

        :return: The datasource_type of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this DiagnosePermissionDetail.

        数据源类型。

        :param datasource_type: The datasource_type of this DiagnosePermissionDetail.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this DiagnosePermissionDetail.

        集群名称。

        :return: The cluster_name of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this DiagnosePermissionDetail.

        集群名称。

        :param cluster_name: The cluster_name of this DiagnosePermissionDetail.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database(self):
        r"""Gets the database of this DiagnosePermissionDetail.

        数据库名。

        :return: The database of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this DiagnosePermissionDetail.

        数据库名。

        :param database: The database of this DiagnosePermissionDetail.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        r"""Gets the schema of this DiagnosePermissionDetail.

        schema名。

        :return: The schema of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this DiagnosePermissionDetail.

        schema名。

        :param schema: The schema of this DiagnosePermissionDetail.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        r"""Gets the table of this DiagnosePermissionDetail.

        表名。

        :return: The table of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this DiagnosePermissionDetail.

        表名。

        :param table: The table of this DiagnosePermissionDetail.
        :type table: str
        """
        self._table = table

    @property
    def remark(self):
        r"""Gets the remark of this DiagnosePermissionDetail.

        备注。

        :return: The remark of this DiagnosePermissionDetail.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this DiagnosePermissionDetail.

        备注。

        :param remark: The remark of this DiagnosePermissionDetail.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, DiagnosePermissionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
