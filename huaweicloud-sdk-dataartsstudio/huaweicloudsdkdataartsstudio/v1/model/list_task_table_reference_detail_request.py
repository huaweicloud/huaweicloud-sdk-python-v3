# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskTableReferenceDetailRequest:

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
        'x_project_id': 'str',
        'table_name': 'str',
        'db_type': 'str',
        'data_base_name': 'str',
        'cluster_name': 'str',
        'io_type': 'int',
        'offset': 'int',
        'limit': 'int',
        'workspace_name': 'str',
        'owner': 'str',
        'execute_user': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'table_name': 'table_name',
        'db_type': 'db_type',
        'data_base_name': 'data_base_name',
        'cluster_name': 'cluster_name',
        'io_type': 'io_type',
        'offset': 'offset',
        'limit': 'limit',
        'workspace_name': 'workspace_name',
        'owner': 'owner',
        'execute_user': 'execute_user'
    }

    def __init__(self, workspace=None, x_project_id=None, table_name=None, db_type=None, data_base_name=None, cluster_name=None, io_type=None, offset=None, limit=None, workspace_name=None, owner=None, execute_user=None):
        r"""ListTaskTableReferenceDetailRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param table_name: 表名。
        :type table_name: str
        :param db_type: 数据库类型，仅支持DLI，HIVE，SPARK。
        :type db_type: str
        :param data_base_name: 数据库名称。
        :type data_base_name: str
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param io_type: 输入输出类型： - 0: 读表 - 1: 写表
        :type io_type: int
        :param offset: 分页的起始页，取值范围大于等于0。默认值: 0。
        :type offset: int
        :param limit: 分页返回结果，指定每页最大记录数。默认值: 20。
        :type limit: int
        :param workspace_name: 工作空间名称。
        :type workspace_name: str
        :param owner: 作业责任人。
        :type owner: str
        :param execute_user: 作业执行用户。
        :type execute_user: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._table_name = None
        self._db_type = None
        self._data_base_name = None
        self._cluster_name = None
        self._io_type = None
        self._offset = None
        self._limit = None
        self._workspace_name = None
        self._owner = None
        self._execute_user = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.table_name = table_name
        self.db_type = db_type
        if data_base_name is not None:
            self.data_base_name = data_base_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if io_type is not None:
            self.io_type = io_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if workspace_name is not None:
            self.workspace_name = workspace_name
        if owner is not None:
            self.owner = owner
        if execute_user is not None:
            self.execute_user = execute_user

    @property
    def workspace(self):
        r"""Gets the workspace of this ListTaskTableReferenceDetailRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListTaskTableReferenceDetailRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListTaskTableReferenceDetailRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListTaskTableReferenceDetailRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListTaskTableReferenceDetailRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListTaskTableReferenceDetailRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def table_name(self):
        r"""Gets the table_name of this ListTaskTableReferenceDetailRequest.

        表名。

        :return: The table_name of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListTaskTableReferenceDetailRequest.

        表名。

        :param table_name: The table_name of this ListTaskTableReferenceDetailRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def db_type(self):
        r"""Gets the db_type of this ListTaskTableReferenceDetailRequest.

        数据库类型，仅支持DLI，HIVE，SPARK。

        :return: The db_type of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this ListTaskTableReferenceDetailRequest.

        数据库类型，仅支持DLI，HIVE，SPARK。

        :param db_type: The db_type of this ListTaskTableReferenceDetailRequest.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def data_base_name(self):
        r"""Gets the data_base_name of this ListTaskTableReferenceDetailRequest.

        数据库名称。

        :return: The data_base_name of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._data_base_name

    @data_base_name.setter
    def data_base_name(self, data_base_name):
        r"""Sets the data_base_name of this ListTaskTableReferenceDetailRequest.

        数据库名称。

        :param data_base_name: The data_base_name of this ListTaskTableReferenceDetailRequest.
        :type data_base_name: str
        """
        self._data_base_name = data_base_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListTaskTableReferenceDetailRequest.

        集群名称。

        :return: The cluster_name of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListTaskTableReferenceDetailRequest.

        集群名称。

        :param cluster_name: The cluster_name of this ListTaskTableReferenceDetailRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def io_type(self):
        r"""Gets the io_type of this ListTaskTableReferenceDetailRequest.

        输入输出类型： - 0: 读表 - 1: 写表

        :return: The io_type of this ListTaskTableReferenceDetailRequest.
        :rtype: int
        """
        return self._io_type

    @io_type.setter
    def io_type(self, io_type):
        r"""Sets the io_type of this ListTaskTableReferenceDetailRequest.

        输入输出类型： - 0: 读表 - 1: 写表

        :param io_type: The io_type of this ListTaskTableReferenceDetailRequest.
        :type io_type: int
        """
        self._io_type = io_type

    @property
    def offset(self):
        r"""Gets the offset of this ListTaskTableReferenceDetailRequest.

        分页的起始页，取值范围大于等于0。默认值: 0。

        :return: The offset of this ListTaskTableReferenceDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTaskTableReferenceDetailRequest.

        分页的起始页，取值范围大于等于0。默认值: 0。

        :param offset: The offset of this ListTaskTableReferenceDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTaskTableReferenceDetailRequest.

        分页返回结果，指定每页最大记录数。默认值: 20。

        :return: The limit of this ListTaskTableReferenceDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTaskTableReferenceDetailRequest.

        分页返回结果，指定每页最大记录数。默认值: 20。

        :param limit: The limit of this ListTaskTableReferenceDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def workspace_name(self):
        r"""Gets the workspace_name of this ListTaskTableReferenceDetailRequest.

        工作空间名称。

        :return: The workspace_name of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        r"""Sets the workspace_name of this ListTaskTableReferenceDetailRequest.

        工作空间名称。

        :param workspace_name: The workspace_name of this ListTaskTableReferenceDetailRequest.
        :type workspace_name: str
        """
        self._workspace_name = workspace_name

    @property
    def owner(self):
        r"""Gets the owner of this ListTaskTableReferenceDetailRequest.

        作业责任人。

        :return: The owner of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ListTaskTableReferenceDetailRequest.

        作业责任人。

        :param owner: The owner of this ListTaskTableReferenceDetailRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def execute_user(self):
        r"""Gets the execute_user of this ListTaskTableReferenceDetailRequest.

        作业执行用户。

        :return: The execute_user of this ListTaskTableReferenceDetailRequest.
        :rtype: str
        """
        return self._execute_user

    @execute_user.setter
    def execute_user(self, execute_user):
        r"""Sets the execute_user of this ListTaskTableReferenceDetailRequest.

        作业执行用户。

        :param execute_user: The execute_user of this ListTaskTableReferenceDetailRequest.
        :type execute_user: str
        """
        self._execute_user = execute_user

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTaskTableReferenceDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
