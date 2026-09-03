# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryDependInstancesRespDependInstancesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'job_id': 'int',
        'job_name': 'str',
        'directory_path': 'str',
        'force_success': 'bool',
        'ignore_success': 'bool',
        'parent_instance_ids': 'list[int]',
        'plan_time': 'int',
        'running_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'status': 'str',
        'submit_time': 'int',
        'version': 'int',
        'workspace_id': 'str',
        'workspace_name': 'str',
        'avg_execute_time_ms': 'int'
    }

    attribute_map = {
        'id': 'id',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'directory_path': 'directory_path',
        'force_success': 'force_success',
        'ignore_success': 'ignore_success',
        'parent_instance_ids': 'parent_instance_ids',
        'plan_time': 'plan_time',
        'running_time': 'running_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'submit_time': 'submit_time',
        'version': 'version',
        'workspace_id': 'workspace_id',
        'workspace_name': 'workspace_name',
        'avg_execute_time_ms': 'avg_execute_time_ms'
    }

    def __init__(self, id=None, job_id=None, job_name=None, directory_path=None, force_success=None, ignore_success=None, parent_instance_ids=None, plan_time=None, running_time=None, start_time=None, end_time=None, status=None, submit_time=None, version=None, workspace_id=None, workspace_name=None, avg_execute_time_ms=None):
        r"""ShowFactoryDependInstancesRespDependInstancesInfo

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: int
        :param job_id: 作业id。
        :type job_id: int
        :param job_name: 作业名称。
        :type job_name: str
        :param directory_path: 作业路径。
        :type directory_path: str
        :param force_success: 实例是否是执行了强制成功。
        :type force_success: bool
        :param ignore_success: 实例是否是执行了忽略失败。
        :type ignore_success: bool
        :param parent_instance_ids: 依赖的上游实例ID。
        :type parent_instance_ids: list[int]
        :param plan_time: 计划开始时间。
        :type plan_time: int
        :param running_time: 运行时长，单位：毫秒。 - 当实例是运行中时，运行时长为当前时间减去开始时间； - 当实例运行结束时，运行时长为结束时间减去开始时间；
        :type running_time: int
        :param start_time: 开始时间。
        :type start_time: int
        :param end_time: 结束时间。
        :type end_time: int
        :param status: 实例状态。
        :type status: str
        :param submit_time: 提交时间。
        :type submit_time: int
        :param version: 版本号。
        :type version: int
        :param workspace_id: 所在的工作空间ID。
        :type workspace_id: str
        :param workspace_name: 所在的工作空间名称。
        :type workspace_name: str
        :param avg_execute_time_ms: 作业平均执行时长，单位：毫秒。
        :type avg_execute_time_ms: int
        """
        
        

        self._id = None
        self._job_id = None
        self._job_name = None
        self._directory_path = None
        self._force_success = None
        self._ignore_success = None
        self._parent_instance_ids = None
        self._plan_time = None
        self._running_time = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._submit_time = None
        self._version = None
        self._workspace_id = None
        self._workspace_name = None
        self._avg_execute_time_ms = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if directory_path is not None:
            self.directory_path = directory_path
        if force_success is not None:
            self.force_success = force_success
        if ignore_success is not None:
            self.ignore_success = ignore_success
        if parent_instance_ids is not None:
            self.parent_instance_ids = parent_instance_ids
        if plan_time is not None:
            self.plan_time = plan_time
        if running_time is not None:
            self.running_time = running_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if submit_time is not None:
            self.submit_time = submit_time
        if version is not None:
            self.version = version
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workspace_name is not None:
            self.workspace_name = workspace_name
        if avg_execute_time_ms is not None:
            self.avg_execute_time_ms = avg_execute_time_ms

    @property
    def id(self):
        r"""Gets the id of this ShowFactoryDependInstancesRespDependInstancesInfo.

        实例ID。

        :return: The id of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowFactoryDependInstancesRespDependInstancesInfo.

        实例ID。

        :param id: The id of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type id: int
        """
        self._id = id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowFactoryDependInstancesRespDependInstancesInfo.

        作业id。

        :return: The job_id of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowFactoryDependInstancesRespDependInstancesInfo.

        作业id。

        :param job_id: The job_id of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowFactoryDependInstancesRespDependInstancesInfo.

        作业名称。

        :return: The job_name of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowFactoryDependInstancesRespDependInstancesInfo.

        作业名称。

        :param job_name: The job_name of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def directory_path(self):
        r"""Gets the directory_path of this ShowFactoryDependInstancesRespDependInstancesInfo.

        作业路径。

        :return: The directory_path of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: str
        """
        return self._directory_path

    @directory_path.setter
    def directory_path(self, directory_path):
        r"""Sets the directory_path of this ShowFactoryDependInstancesRespDependInstancesInfo.

        作业路径。

        :param directory_path: The directory_path of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type directory_path: str
        """
        self._directory_path = directory_path

    @property
    def force_success(self):
        r"""Gets the force_success of this ShowFactoryDependInstancesRespDependInstancesInfo.

        实例是否是执行了强制成功。

        :return: The force_success of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: bool
        """
        return self._force_success

    @force_success.setter
    def force_success(self, force_success):
        r"""Sets the force_success of this ShowFactoryDependInstancesRespDependInstancesInfo.

        实例是否是执行了强制成功。

        :param force_success: The force_success of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type force_success: bool
        """
        self._force_success = force_success

    @property
    def ignore_success(self):
        r"""Gets the ignore_success of this ShowFactoryDependInstancesRespDependInstancesInfo.

        实例是否是执行了忽略失败。

        :return: The ignore_success of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: bool
        """
        return self._ignore_success

    @ignore_success.setter
    def ignore_success(self, ignore_success):
        r"""Sets the ignore_success of this ShowFactoryDependInstancesRespDependInstancesInfo.

        实例是否是执行了忽略失败。

        :param ignore_success: The ignore_success of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type ignore_success: bool
        """
        self._ignore_success = ignore_success

    @property
    def parent_instance_ids(self):
        r"""Gets the parent_instance_ids of this ShowFactoryDependInstancesRespDependInstancesInfo.

        依赖的上游实例ID。

        :return: The parent_instance_ids of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: list[int]
        """
        return self._parent_instance_ids

    @parent_instance_ids.setter
    def parent_instance_ids(self, parent_instance_ids):
        r"""Sets the parent_instance_ids of this ShowFactoryDependInstancesRespDependInstancesInfo.

        依赖的上游实例ID。

        :param parent_instance_ids: The parent_instance_ids of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type parent_instance_ids: list[int]
        """
        self._parent_instance_ids = parent_instance_ids

    @property
    def plan_time(self):
        r"""Gets the plan_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        计划开始时间。

        :return: The plan_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        r"""Sets the plan_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        计划开始时间。

        :param plan_time: The plan_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def running_time(self):
        r"""Gets the running_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        运行时长，单位：毫秒。 - 当实例是运行中时，运行时长为当前时间减去开始时间； - 当实例运行结束时，运行时长为结束时间减去开始时间；

        :return: The running_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._running_time

    @running_time.setter
    def running_time(self, running_time):
        r"""Sets the running_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        运行时长，单位：毫秒。 - 当实例是运行中时，运行时长为当前时间减去开始时间； - 当实例运行结束时，运行时长为结束时间减去开始时间；

        :param running_time: The running_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type running_time: int
        """
        self._running_time = running_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        开始时间。

        :return: The start_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        开始时间。

        :param start_time: The start_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        结束时间。

        :return: The end_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        结束时间。

        :param end_time: The end_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ShowFactoryDependInstancesRespDependInstancesInfo.

        实例状态。

        :return: The status of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowFactoryDependInstancesRespDependInstancesInfo.

        实例状态。

        :param status: The status of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type status: str
        """
        self._status = status

    @property
    def submit_time(self):
        r"""Gets the submit_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        提交时间。

        :return: The submit_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        r"""Sets the submit_time of this ShowFactoryDependInstancesRespDependInstancesInfo.

        提交时间。

        :param submit_time: The submit_time of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type submit_time: int
        """
        self._submit_time = submit_time

    @property
    def version(self):
        r"""Gets the version of this ShowFactoryDependInstancesRespDependInstancesInfo.

        版本号。

        :return: The version of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowFactoryDependInstancesRespDependInstancesInfo.

        版本号。

        :param version: The version of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type version: int
        """
        self._version = version

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowFactoryDependInstancesRespDependInstancesInfo.

        所在的工作空间ID。

        :return: The workspace_id of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowFactoryDependInstancesRespDependInstancesInfo.

        所在的工作空间ID。

        :param workspace_id: The workspace_id of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def workspace_name(self):
        r"""Gets the workspace_name of this ShowFactoryDependInstancesRespDependInstancesInfo.

        所在的工作空间名称。

        :return: The workspace_name of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        r"""Sets the workspace_name of this ShowFactoryDependInstancesRespDependInstancesInfo.

        所在的工作空间名称。

        :param workspace_name: The workspace_name of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type workspace_name: str
        """
        self._workspace_name = workspace_name

    @property
    def avg_execute_time_ms(self):
        r"""Gets the avg_execute_time_ms of this ShowFactoryDependInstancesRespDependInstancesInfo.

        作业平均执行时长，单位：毫秒。

        :return: The avg_execute_time_ms of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :rtype: int
        """
        return self._avg_execute_time_ms

    @avg_execute_time_ms.setter
    def avg_execute_time_ms(self, avg_execute_time_ms):
        r"""Sets the avg_execute_time_ms of this ShowFactoryDependInstancesRespDependInstancesInfo.

        作业平均执行时长，单位：毫秒。

        :param avg_execute_time_ms: The avg_execute_time_ms of this ShowFactoryDependInstancesRespDependInstancesInfo.
        :type avg_execute_time_ms: int
        """
        self._avg_execute_time_ms = avg_execute_time_ms

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
        if not isinstance(other, ShowFactoryDependInstancesRespDependInstancesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
