# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskTableReferenceDetailResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'int',
        'job_name': 'str',
        'db_type': 'str',
        'data_base': 'str',
        'table_name': 'str',
        'cluster_name': 'str',
        'workspace_name': 'str',
        'workspace_id': 'str',
        'owner': 'str',
        'last_submit_time': 'int',
        'io_type': 'int',
        'is_dynamic': 'bool',
        'execute_user': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'db_type': 'db_type',
        'data_base': 'data_base',
        'table_name': 'table_name',
        'cluster_name': 'cluster_name',
        'workspace_name': 'workspace_name',
        'workspace_id': 'workspace_id',
        'owner': 'owner',
        'last_submit_time': 'last_submit_time',
        'io_type': 'io_type',
        'is_dynamic': 'is_dynamic',
        'execute_user': 'execute_user'
    }

    def __init__(self, job_id=None, job_name=None, db_type=None, data_base=None, table_name=None, cluster_name=None, workspace_name=None, workspace_id=None, owner=None, last_submit_time=None, io_type=None, is_dynamic=None, execute_user=None):
        r"""TaskTableReferenceDetailResponse

        The model defined in huaweicloud sdk

        :param job_id: 作业id。
        :type job_id: int
        :param job_name: 作业名。
        :type job_name: str
        :param db_type: 数据库类型。
        :type db_type: str
        :param data_base: 数据库名。
        :type data_base: str
        :param table_name: 数据表名。
        :type table_name: str
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param workspace_name: 作业的工作空间名。
        :type workspace_name: str
        :param workspace_id: 作业的工作空间Id。
        :type workspace_id: str
        :param owner: 作业责任人。
        :type owner: str
        :param last_submit_time: 作业最后提交时间。
        :type last_submit_time: int
        :param io_type: 作业和表的关系，0表示作业是读表，1表示作业写表。
        :type io_type: int
        :param is_dynamic: 是否是动态表。
        :type is_dynamic: bool
        :param execute_user: 作业执行用户。
        :type execute_user: str
        """
        
        

        self._job_id = None
        self._job_name = None
        self._db_type = None
        self._data_base = None
        self._table_name = None
        self._cluster_name = None
        self._workspace_name = None
        self._workspace_id = None
        self._owner = None
        self._last_submit_time = None
        self._io_type = None
        self._is_dynamic = None
        self._execute_user = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if db_type is not None:
            self.db_type = db_type
        if data_base is not None:
            self.data_base = data_base
        if table_name is not None:
            self.table_name = table_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if workspace_name is not None:
            self.workspace_name = workspace_name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if owner is not None:
            self.owner = owner
        if last_submit_time is not None:
            self.last_submit_time = last_submit_time
        if io_type is not None:
            self.io_type = io_type
        if is_dynamic is not None:
            self.is_dynamic = is_dynamic
        if execute_user is not None:
            self.execute_user = execute_user

    @property
    def job_id(self):
        r"""Gets the job_id of this TaskTableReferenceDetailResponse.

        作业id。

        :return: The job_id of this TaskTableReferenceDetailResponse.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TaskTableReferenceDetailResponse.

        作业id。

        :param job_id: The job_id of this TaskTableReferenceDetailResponse.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this TaskTableReferenceDetailResponse.

        作业名。

        :return: The job_name of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this TaskTableReferenceDetailResponse.

        作业名。

        :param job_name: The job_name of this TaskTableReferenceDetailResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def db_type(self):
        r"""Gets the db_type of this TaskTableReferenceDetailResponse.

        数据库类型。

        :return: The db_type of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this TaskTableReferenceDetailResponse.

        数据库类型。

        :param db_type: The db_type of this TaskTableReferenceDetailResponse.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def data_base(self):
        r"""Gets the data_base of this TaskTableReferenceDetailResponse.

        数据库名。

        :return: The data_base of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._data_base

    @data_base.setter
    def data_base(self, data_base):
        r"""Sets the data_base of this TaskTableReferenceDetailResponse.

        数据库名。

        :param data_base: The data_base of this TaskTableReferenceDetailResponse.
        :type data_base: str
        """
        self._data_base = data_base

    @property
    def table_name(self):
        r"""Gets the table_name of this TaskTableReferenceDetailResponse.

        数据表名。

        :return: The table_name of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this TaskTableReferenceDetailResponse.

        数据表名。

        :param table_name: The table_name of this TaskTableReferenceDetailResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this TaskTableReferenceDetailResponse.

        集群名称。

        :return: The cluster_name of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this TaskTableReferenceDetailResponse.

        集群名称。

        :param cluster_name: The cluster_name of this TaskTableReferenceDetailResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def workspace_name(self):
        r"""Gets the workspace_name of this TaskTableReferenceDetailResponse.

        作业的工作空间名。

        :return: The workspace_name of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        r"""Sets the workspace_name of this TaskTableReferenceDetailResponse.

        作业的工作空间名。

        :param workspace_name: The workspace_name of this TaskTableReferenceDetailResponse.
        :type workspace_name: str
        """
        self._workspace_name = workspace_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this TaskTableReferenceDetailResponse.

        作业的工作空间Id。

        :return: The workspace_id of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this TaskTableReferenceDetailResponse.

        作业的工作空间Id。

        :param workspace_id: The workspace_id of this TaskTableReferenceDetailResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def owner(self):
        r"""Gets the owner of this TaskTableReferenceDetailResponse.

        作业责任人。

        :return: The owner of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TaskTableReferenceDetailResponse.

        作业责任人。

        :param owner: The owner of this TaskTableReferenceDetailResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def last_submit_time(self):
        r"""Gets the last_submit_time of this TaskTableReferenceDetailResponse.

        作业最后提交时间。

        :return: The last_submit_time of this TaskTableReferenceDetailResponse.
        :rtype: int
        """
        return self._last_submit_time

    @last_submit_time.setter
    def last_submit_time(self, last_submit_time):
        r"""Sets the last_submit_time of this TaskTableReferenceDetailResponse.

        作业最后提交时间。

        :param last_submit_time: The last_submit_time of this TaskTableReferenceDetailResponse.
        :type last_submit_time: int
        """
        self._last_submit_time = last_submit_time

    @property
    def io_type(self):
        r"""Gets the io_type of this TaskTableReferenceDetailResponse.

        作业和表的关系，0表示作业是读表，1表示作业写表。

        :return: The io_type of this TaskTableReferenceDetailResponse.
        :rtype: int
        """
        return self._io_type

    @io_type.setter
    def io_type(self, io_type):
        r"""Sets the io_type of this TaskTableReferenceDetailResponse.

        作业和表的关系，0表示作业是读表，1表示作业写表。

        :param io_type: The io_type of this TaskTableReferenceDetailResponse.
        :type io_type: int
        """
        self._io_type = io_type

    @property
    def is_dynamic(self):
        r"""Gets the is_dynamic of this TaskTableReferenceDetailResponse.

        是否是动态表。

        :return: The is_dynamic of this TaskTableReferenceDetailResponse.
        :rtype: bool
        """
        return self._is_dynamic

    @is_dynamic.setter
    def is_dynamic(self, is_dynamic):
        r"""Sets the is_dynamic of this TaskTableReferenceDetailResponse.

        是否是动态表。

        :param is_dynamic: The is_dynamic of this TaskTableReferenceDetailResponse.
        :type is_dynamic: bool
        """
        self._is_dynamic = is_dynamic

    @property
    def execute_user(self):
        r"""Gets the execute_user of this TaskTableReferenceDetailResponse.

        作业执行用户。

        :return: The execute_user of this TaskTableReferenceDetailResponse.
        :rtype: str
        """
        return self._execute_user

    @execute_user.setter
    def execute_user(self, execute_user):
        r"""Sets the execute_user of this TaskTableReferenceDetailResponse.

        作业执行用户。

        :param execute_user: The execute_user of this TaskTableReferenceDetailResponse.
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
        if not isinstance(other, TaskTableReferenceDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
