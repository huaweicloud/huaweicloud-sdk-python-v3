# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityMemberTablePermissionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'feature': 'str',
        'limit': 'int',
        'offset': 'int',
        'datasource_type': 'str',
        'cluster_name': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'fuzzy_table_name': 'str',
        'workspace_ids': 'list[str]',
        'workspace': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'feature': 'feature',
        'limit': 'limit',
        'offset': 'offset',
        'datasource_type': 'datasource_type',
        'cluster_name': 'cluster_name',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'fuzzy_table_name': 'fuzzy_table_name',
        'workspace_ids': 'workspace_ids',
        'workspace': 'workspace'
    }

    def __init__(self, user_id=None, feature=None, limit=None, offset=None, datasource_type=None, cluster_name=None, database_name=None, schema_name=None, table_name=None, fuzzy_table_name=None, workspace_ids=None, workspace=None):
        r"""ListSecurityMemberTablePermissionRequest

        The model defined in huaweicloud sdk

        :param user_id: IAM用户id
        :type user_id: str
        :param feature: 权限清单场景类型，PERMISSION_LIST
        :type feature: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param datasource_type: 数据源类型,hive,dws[,dli](tag:nohcs)
        :type datasource_type: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param database_name: 数据库名称
        :type database_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param table_name: 表名称
        :type table_name: str
        :param fuzzy_table_name: 表名（模糊匹配）
        :type fuzzy_table_name: str
        :param workspace_ids: 工作空间id列表
        :type workspace_ids: list[str]
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        """
        
        

        self._user_id = None
        self._feature = None
        self._limit = None
        self._offset = None
        self._datasource_type = None
        self._cluster_name = None
        self._database_name = None
        self._schema_name = None
        self._table_name = None
        self._fuzzy_table_name = None
        self._workspace_ids = None
        self._workspace = None
        self.discriminator = None

        self.user_id = user_id
        if feature is not None:
            self.feature = feature
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if database_name is not None:
            self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if fuzzy_table_name is not None:
            self.fuzzy_table_name = fuzzy_table_name
        if workspace_ids is not None:
            self.workspace_ids = workspace_ids
        self.workspace = workspace

    @property
    def user_id(self):
        r"""Gets the user_id of this ListSecurityMemberTablePermissionRequest.

        IAM用户id

        :return: The user_id of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListSecurityMemberTablePermissionRequest.

        IAM用户id

        :param user_id: The user_id of this ListSecurityMemberTablePermissionRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def feature(self):
        r"""Gets the feature of this ListSecurityMemberTablePermissionRequest.

        权限清单场景类型，PERMISSION_LIST

        :return: The feature of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this ListSecurityMemberTablePermissionRequest.

        权限清单场景类型，PERMISSION_LIST

        :param feature: The feature of this ListSecurityMemberTablePermissionRequest.
        :type feature: str
        """
        self._feature = feature

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityMemberTablePermissionRequest.

        limit

        :return: The limit of this ListSecurityMemberTablePermissionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityMemberTablePermissionRequest.

        limit

        :param limit: The limit of this ListSecurityMemberTablePermissionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityMemberTablePermissionRequest.

        offset

        :return: The offset of this ListSecurityMemberTablePermissionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityMemberTablePermissionRequest.

        offset

        :param offset: The offset of this ListSecurityMemberTablePermissionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this ListSecurityMemberTablePermissionRequest.

        数据源类型,hive,dws[,dli](tag:nohcs)

        :return: The datasource_type of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this ListSecurityMemberTablePermissionRequest.

        数据源类型,hive,dws[,dli](tag:nohcs)

        :param datasource_type: The datasource_type of this ListSecurityMemberTablePermissionRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListSecurityMemberTablePermissionRequest.

        集群名称

        :return: The cluster_name of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListSecurityMemberTablePermissionRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListSecurityMemberTablePermissionRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListSecurityMemberTablePermissionRequest.

        数据库名称

        :return: The database_name of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListSecurityMemberTablePermissionRequest.

        数据库名称

        :param database_name: The database_name of this ListSecurityMemberTablePermissionRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ListSecurityMemberTablePermissionRequest.

        schema名称

        :return: The schema_name of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ListSecurityMemberTablePermissionRequest.

        schema名称

        :param schema_name: The schema_name of this ListSecurityMemberTablePermissionRequest.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListSecurityMemberTablePermissionRequest.

        表名称

        :return: The table_name of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListSecurityMemberTablePermissionRequest.

        表名称

        :param table_name: The table_name of this ListSecurityMemberTablePermissionRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def fuzzy_table_name(self):
        r"""Gets the fuzzy_table_name of this ListSecurityMemberTablePermissionRequest.

        表名（模糊匹配）

        :return: The fuzzy_table_name of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._fuzzy_table_name

    @fuzzy_table_name.setter
    def fuzzy_table_name(self, fuzzy_table_name):
        r"""Sets the fuzzy_table_name of this ListSecurityMemberTablePermissionRequest.

        表名（模糊匹配）

        :param fuzzy_table_name: The fuzzy_table_name of this ListSecurityMemberTablePermissionRequest.
        :type fuzzy_table_name: str
        """
        self._fuzzy_table_name = fuzzy_table_name

    @property
    def workspace_ids(self):
        r"""Gets the workspace_ids of this ListSecurityMemberTablePermissionRequest.

        工作空间id列表

        :return: The workspace_ids of this ListSecurityMemberTablePermissionRequest.
        :rtype: list[str]
        """
        return self._workspace_ids

    @workspace_ids.setter
    def workspace_ids(self, workspace_ids):
        r"""Sets the workspace_ids of this ListSecurityMemberTablePermissionRequest.

        工作空间id列表

        :param workspace_ids: The workspace_ids of this ListSecurityMemberTablePermissionRequest.
        :type workspace_ids: list[str]
        """
        self._workspace_ids = workspace_ids

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityMemberTablePermissionRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityMemberTablePermissionRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityMemberTablePermissionRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityMemberTablePermissionRequest.
        :type workspace: str
        """
        self._workspace = workspace

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
        if not isinstance(other, ListSecurityMemberTablePermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
