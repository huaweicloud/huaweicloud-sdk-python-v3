# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'nodes': 'list[Node]',
        'schedule': 'Schedule',
        'params': 'list[JobParam]',
        'directory': 'str',
        'downstream_jobs': 'list[JobInformation]',
        'process_type': 'str',
        'id': 'int',
        'create_time': 'int',
        'single_node_job_flag': 'bool',
        'single_node_job_type': 'str',
        'last_update_user': 'str',
        'log_path': 'str',
        'basic_config': 'BasicConfig',
        'description': 'str',
        'clean_overdue_days': 'int',
        'clean_waiting_job': 'str',
        'empty_running_job': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'nodes': 'nodes',
        'schedule': 'schedule',
        'params': 'params',
        'directory': 'directory',
        'downstream_jobs': 'downstreamJobs',
        'process_type': 'processType',
        'id': 'id',
        'create_time': 'createTime',
        'single_node_job_flag': 'singleNodeJobFlag',
        'single_node_job_type': 'singleNodeJobType',
        'last_update_user': 'lastUpdateUser',
        'log_path': 'logPath',
        'basic_config': 'basicConfig',
        'description': 'description',
        'clean_overdue_days': 'cleanOverdueDays',
        'clean_waiting_job': 'cleanWaitingJob',
        'empty_running_job': 'emptyRunningJob',
        'version': 'version'
    }

    def __init__(self, name=None, nodes=None, schedule=None, params=None, directory=None, downstream_jobs=None, process_type=None, id=None, create_time=None, single_node_job_flag=None, single_node_job_type=None, last_update_user=None, log_path=None, basic_config=None, description=None, clean_overdue_days=None, clean_waiting_job=None, empty_running_job=None, version=None):
        r"""ShowJobResponse

        The model defined in huaweicloud sdk

        :param name: 作业名称
        :type name: str
        :param nodes: 节点定义
        :type nodes: list[:class:`huaweicloudsdkdgc.v1.Node`]
        :param schedule: 
        :type schedule: :class:`huaweicloudsdkdgc.v1.Schedule`
        :param params: 作业参数定义
        :type params: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        :param directory: 作业在目录树上的路径。创建作业时如果路径目录不存在，会自动创建目录，如/dir/a/，默认在根目录/。
        :type directory: str
        :param downstream_jobs: 下游作业信息
        :type downstream_jobs: list[:class:`huaweicloudsdkdgc.v1.JobInformation`]
        :param process_type: 作业类型，REAL_TIME： 实时处理，BATCH：批处理
        :type process_type: str
        :param id: 作业Id, 用户查询作业时使用。
        :type id: int
        :param create_time: 作业创建时间.
        :type create_time: int
        :param single_node_job_flag: 是否选择单任务，默认为false
        :type single_node_job_flag: bool
        :param single_node_job_type: 单任务类型
        :type single_node_job_type: str
        :param last_update_user: 作业最后修改人
        :type last_update_user: str
        :param log_path: 作业运行日志存放的OBS路径。
        :type log_path: str
        :param basic_config: 
        :type basic_config: :class:`huaweicloudsdkdgc.v1.BasicConfig`
        :param description: 作业描述信息
        :type description: str
        :param clean_overdue_days: 设置作业的最大超时时间。
        :type clean_overdue_days: int
        :param clean_waiting_job: 清除等待的作业。
        :type clean_waiting_job: str
        :param empty_running_job: 是否空跑。
        :type empty_running_job: str
        :param version: 作业版本信息。
        :type version: str
        """
        
        super(ShowJobResponse, self).__init__()

        self._name = None
        self._nodes = None
        self._schedule = None
        self._params = None
        self._directory = None
        self._downstream_jobs = None
        self._process_type = None
        self._id = None
        self._create_time = None
        self._single_node_job_flag = None
        self._single_node_job_type = None
        self._last_update_user = None
        self._log_path = None
        self._basic_config = None
        self._description = None
        self._clean_overdue_days = None
        self._clean_waiting_job = None
        self._empty_running_job = None
        self._version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if nodes is not None:
            self.nodes = nodes
        if schedule is not None:
            self.schedule = schedule
        if params is not None:
            self.params = params
        if directory is not None:
            self.directory = directory
        if downstream_jobs is not None:
            self.downstream_jobs = downstream_jobs
        if process_type is not None:
            self.process_type = process_type
        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if single_node_job_flag is not None:
            self.single_node_job_flag = single_node_job_flag
        if single_node_job_type is not None:
            self.single_node_job_type = single_node_job_type
        if last_update_user is not None:
            self.last_update_user = last_update_user
        if log_path is not None:
            self.log_path = log_path
        if basic_config is not None:
            self.basic_config = basic_config
        if description is not None:
            self.description = description
        if clean_overdue_days is not None:
            self.clean_overdue_days = clean_overdue_days
        if clean_waiting_job is not None:
            self.clean_waiting_job = clean_waiting_job
        if empty_running_job is not None:
            self.empty_running_job = empty_running_job
        if version is not None:
            self.version = version

    @property
    def name(self):
        r"""Gets the name of this ShowJobResponse.

        作业名称

        :return: The name of this ShowJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowJobResponse.

        作业名称

        :param name: The name of this ShowJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def nodes(self):
        r"""Gets the nodes of this ShowJobResponse.

        节点定义

        :return: The nodes of this ShowJobResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.Node`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ShowJobResponse.

        节点定义

        :param nodes: The nodes of this ShowJobResponse.
        :type nodes: list[:class:`huaweicloudsdkdgc.v1.Node`]
        """
        self._nodes = nodes

    @property
    def schedule(self):
        r"""Gets the schedule of this ShowJobResponse.

        :return: The schedule of this ShowJobResponse.
        :rtype: :class:`huaweicloudsdkdgc.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this ShowJobResponse.

        :param schedule: The schedule of this ShowJobResponse.
        :type schedule: :class:`huaweicloudsdkdgc.v1.Schedule`
        """
        self._schedule = schedule

    @property
    def params(self):
        r"""Gets the params of this ShowJobResponse.

        作业参数定义

        :return: The params of this ShowJobResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ShowJobResponse.

        作业参数定义

        :param params: The params of this ShowJobResponse.
        :type params: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        self._params = params

    @property
    def directory(self):
        r"""Gets the directory of this ShowJobResponse.

        作业在目录树上的路径。创建作业时如果路径目录不存在，会自动创建目录，如/dir/a/，默认在根目录/。

        :return: The directory of this ShowJobResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this ShowJobResponse.

        作业在目录树上的路径。创建作业时如果路径目录不存在，会自动创建目录，如/dir/a/，默认在根目录/。

        :param directory: The directory of this ShowJobResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def downstream_jobs(self):
        r"""Gets the downstream_jobs of this ShowJobResponse.

        下游作业信息

        :return: The downstream_jobs of this ShowJobResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobInformation`]
        """
        return self._downstream_jobs

    @downstream_jobs.setter
    def downstream_jobs(self, downstream_jobs):
        r"""Sets the downstream_jobs of this ShowJobResponse.

        下游作业信息

        :param downstream_jobs: The downstream_jobs of this ShowJobResponse.
        :type downstream_jobs: list[:class:`huaweicloudsdkdgc.v1.JobInformation`]
        """
        self._downstream_jobs = downstream_jobs

    @property
    def process_type(self):
        r"""Gets the process_type of this ShowJobResponse.

        作业类型，REAL_TIME： 实时处理，BATCH：批处理

        :return: The process_type of this ShowJobResponse.
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        r"""Sets the process_type of this ShowJobResponse.

        作业类型，REAL_TIME： 实时处理，BATCH：批处理

        :param process_type: The process_type of this ShowJobResponse.
        :type process_type: str
        """
        self._process_type = process_type

    @property
    def id(self):
        r"""Gets the id of this ShowJobResponse.

        作业Id, 用户查询作业时使用。

        :return: The id of this ShowJobResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowJobResponse.

        作业Id, 用户查询作业时使用。

        :param id: The id of this ShowJobResponse.
        :type id: int
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowJobResponse.

        作业创建时间.

        :return: The create_time of this ShowJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowJobResponse.

        作业创建时间.

        :param create_time: The create_time of this ShowJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def single_node_job_flag(self):
        r"""Gets the single_node_job_flag of this ShowJobResponse.

        是否选择单任务，默认为false

        :return: The single_node_job_flag of this ShowJobResponse.
        :rtype: bool
        """
        return self._single_node_job_flag

    @single_node_job_flag.setter
    def single_node_job_flag(self, single_node_job_flag):
        r"""Sets the single_node_job_flag of this ShowJobResponse.

        是否选择单任务，默认为false

        :param single_node_job_flag: The single_node_job_flag of this ShowJobResponse.
        :type single_node_job_flag: bool
        """
        self._single_node_job_flag = single_node_job_flag

    @property
    def single_node_job_type(self):
        r"""Gets the single_node_job_type of this ShowJobResponse.

        单任务类型

        :return: The single_node_job_type of this ShowJobResponse.
        :rtype: str
        """
        return self._single_node_job_type

    @single_node_job_type.setter
    def single_node_job_type(self, single_node_job_type):
        r"""Sets the single_node_job_type of this ShowJobResponse.

        单任务类型

        :param single_node_job_type: The single_node_job_type of this ShowJobResponse.
        :type single_node_job_type: str
        """
        self._single_node_job_type = single_node_job_type

    @property
    def last_update_user(self):
        r"""Gets the last_update_user of this ShowJobResponse.

        作业最后修改人

        :return: The last_update_user of this ShowJobResponse.
        :rtype: str
        """
        return self._last_update_user

    @last_update_user.setter
    def last_update_user(self, last_update_user):
        r"""Sets the last_update_user of this ShowJobResponse.

        作业最后修改人

        :param last_update_user: The last_update_user of this ShowJobResponse.
        :type last_update_user: str
        """
        self._last_update_user = last_update_user

    @property
    def log_path(self):
        r"""Gets the log_path of this ShowJobResponse.

        作业运行日志存放的OBS路径。

        :return: The log_path of this ShowJobResponse.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        r"""Sets the log_path of this ShowJobResponse.

        作业运行日志存放的OBS路径。

        :param log_path: The log_path of this ShowJobResponse.
        :type log_path: str
        """
        self._log_path = log_path

    @property
    def basic_config(self):
        r"""Gets the basic_config of this ShowJobResponse.

        :return: The basic_config of this ShowJobResponse.
        :rtype: :class:`huaweicloudsdkdgc.v1.BasicConfig`
        """
        return self._basic_config

    @basic_config.setter
    def basic_config(self, basic_config):
        r"""Sets the basic_config of this ShowJobResponse.

        :param basic_config: The basic_config of this ShowJobResponse.
        :type basic_config: :class:`huaweicloudsdkdgc.v1.BasicConfig`
        """
        self._basic_config = basic_config

    @property
    def description(self):
        r"""Gets the description of this ShowJobResponse.

        作业描述信息

        :return: The description of this ShowJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowJobResponse.

        作业描述信息

        :param description: The description of this ShowJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def clean_overdue_days(self):
        r"""Gets the clean_overdue_days of this ShowJobResponse.

        设置作业的最大超时时间。

        :return: The clean_overdue_days of this ShowJobResponse.
        :rtype: int
        """
        return self._clean_overdue_days

    @clean_overdue_days.setter
    def clean_overdue_days(self, clean_overdue_days):
        r"""Sets the clean_overdue_days of this ShowJobResponse.

        设置作业的最大超时时间。

        :param clean_overdue_days: The clean_overdue_days of this ShowJobResponse.
        :type clean_overdue_days: int
        """
        self._clean_overdue_days = clean_overdue_days

    @property
    def clean_waiting_job(self):
        r"""Gets the clean_waiting_job of this ShowJobResponse.

        清除等待的作业。

        :return: The clean_waiting_job of this ShowJobResponse.
        :rtype: str
        """
        return self._clean_waiting_job

    @clean_waiting_job.setter
    def clean_waiting_job(self, clean_waiting_job):
        r"""Sets the clean_waiting_job of this ShowJobResponse.

        清除等待的作业。

        :param clean_waiting_job: The clean_waiting_job of this ShowJobResponse.
        :type clean_waiting_job: str
        """
        self._clean_waiting_job = clean_waiting_job

    @property
    def empty_running_job(self):
        r"""Gets the empty_running_job of this ShowJobResponse.

        是否空跑。

        :return: The empty_running_job of this ShowJobResponse.
        :rtype: str
        """
        return self._empty_running_job

    @empty_running_job.setter
    def empty_running_job(self, empty_running_job):
        r"""Sets the empty_running_job of this ShowJobResponse.

        是否空跑。

        :param empty_running_job: The empty_running_job of this ShowJobResponse.
        :type empty_running_job: str
        """
        self._empty_running_job = empty_running_job

    @property
    def version(self):
        r"""Gets the version of this ShowJobResponse.

        作业版本信息。

        :return: The version of this ShowJobResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowJobResponse.

        作业版本信息。

        :param version: The version of this ShowJobResponse.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
