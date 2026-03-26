# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobRunsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'id': 'str',
        'name': 'str',
        'limit': 'int',
        'offset': 'int',
        'job_id': 'str',
        'endpoint_id': 'str',
        'version_id': 'str',
        'status': 'str',
        'type': 'str',
        'sort_by': 'str',
        'order_by': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'id': 'id',
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset',
        'job_id': 'job_id',
        'endpoint_id': 'endpoint_id',
        'version_id': 'version_id',
        'status': 'status',
        'type': 'type',
        'sort_by': 'sort_by',
        'order_by': 'order_by'
    }

    def __init__(self, workspace_id=None, id=None, name=None, limit=None, offset=None, job_id=None, endpoint_id=None, version_id=None, status=None, type=None, sort_by=None, order_by=None):
        r"""ListJobRunsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: Workspace的ID
        :type workspace_id: str
        :param id: 通过作业运行id检索
        :type id: str
        :param name: 通过名字搜索运行的作业
        :type name: str
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为10。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param job_id: 通过作业id检索
        :type job_id: str
        :param endpoint_id: 通过id检索Endpoint的参数
        :type endpoint_id: str
        :param version_id: 通过作业版本检索
        :type version_id: str
        :param status: 状态过滤，支持一种状态查询，默认查询所有；  可选值有： PENDING,CREATING,RUNNING,UPDATING,SUCCEEDED,FAILED,STOPPING,STOPPED,DELETING,DELETED
        :type status: str
        :param type: 类别，可选值如下：  - RAY_JOB: Ray Job,   - PYTHON_JOB: Python Job,   - SPARK_JOB: Spark Job
        :type type: str
        :param sort_by: 根据字段排序，可选值： - CREATE_TIME：创建时间 - DURATION: 运行时间
        :type sort_by: str
        :param order_by: 排序方式，可选值： - ASC：正序排序 - DESC: 倒序排序
        :type order_by: str
        """
        
        

        self._workspace_id = None
        self._id = None
        self._name = None
        self._limit = None
        self._offset = None
        self._job_id = None
        self._endpoint_id = None
        self._version_id = None
        self._status = None
        self._type = None
        self._sort_by = None
        self._order_by = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if job_id is not None:
            self.job_id = job_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if version_id is not None:
            self.version_id = version_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if sort_by is not None:
            self.sort_by = sort_by
        if order_by is not None:
            self.order_by = order_by

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListJobRunsRequest.

        Workspace的ID

        :return: The workspace_id of this ListJobRunsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListJobRunsRequest.

        Workspace的ID

        :param workspace_id: The workspace_id of this ListJobRunsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def id(self):
        r"""Gets the id of this ListJobRunsRequest.

        通过作业运行id检索

        :return: The id of this ListJobRunsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListJobRunsRequest.

        通过作业运行id检索

        :param id: The id of this ListJobRunsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListJobRunsRequest.

        通过名字搜索运行的作业

        :return: The name of this ListJobRunsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListJobRunsRequest.

        通过名字搜索运行的作业

        :param name: The name of this ListJobRunsRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListJobRunsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :return: The limit of this ListJobRunsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobRunsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :param limit: The limit of this ListJobRunsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListJobRunsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListJobRunsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobRunsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListJobRunsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def job_id(self):
        r"""Gets the job_id of this ListJobRunsRequest.

        通过作业id检索

        :return: The job_id of this ListJobRunsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListJobRunsRequest.

        通过作业id检索

        :param job_id: The job_id of this ListJobRunsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListJobRunsRequest.

        通过id检索Endpoint的参数

        :return: The endpoint_id of this ListJobRunsRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListJobRunsRequest.

        通过id检索Endpoint的参数

        :param endpoint_id: The endpoint_id of this ListJobRunsRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def version_id(self):
        r"""Gets the version_id of this ListJobRunsRequest.

        通过作业版本检索

        :return: The version_id of this ListJobRunsRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this ListJobRunsRequest.

        通过作业版本检索

        :param version_id: The version_id of this ListJobRunsRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def status(self):
        r"""Gets the status of this ListJobRunsRequest.

        状态过滤，支持一种状态查询，默认查询所有；  可选值有： PENDING,CREATING,RUNNING,UPDATING,SUCCEEDED,FAILED,STOPPING,STOPPED,DELETING,DELETED

        :return: The status of this ListJobRunsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListJobRunsRequest.

        状态过滤，支持一种状态查询，默认查询所有；  可选值有： PENDING,CREATING,RUNNING,UPDATING,SUCCEEDED,FAILED,STOPPING,STOPPED,DELETING,DELETED

        :param status: The status of this ListJobRunsRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListJobRunsRequest.

        类别，可选值如下：  - RAY_JOB: Ray Job,   - PYTHON_JOB: Python Job,   - SPARK_JOB: Spark Job

        :return: The type of this ListJobRunsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListJobRunsRequest.

        类别，可选值如下：  - RAY_JOB: Ray Job,   - PYTHON_JOB: Python Job,   - SPARK_JOB: Spark Job

        :param type: The type of this ListJobRunsRequest.
        :type type: str
        """
        self._type = type

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListJobRunsRequest.

        根据字段排序，可选值： - CREATE_TIME：创建时间 - DURATION: 运行时间

        :return: The sort_by of this ListJobRunsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListJobRunsRequest.

        根据字段排序，可选值： - CREATE_TIME：创建时间 - DURATION: 运行时间

        :param sort_by: The sort_by of this ListJobRunsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order_by(self):
        r"""Gets the order_by of this ListJobRunsRequest.

        排序方式，可选值： - ASC：正序排序 - DESC: 倒序排序

        :return: The order_by of this ListJobRunsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListJobRunsRequest.

        排序方式，可选值： - ASC：正序排序 - DESC: 倒序排序

        :param order_by: The order_by of this ListJobRunsRequest.
        :type order_by: str
        """
        self._order_by = order_by

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
        if not isinstance(other, ListJobRunsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
