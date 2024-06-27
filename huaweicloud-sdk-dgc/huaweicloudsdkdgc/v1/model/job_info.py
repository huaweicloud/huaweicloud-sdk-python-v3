# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInfo:

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
        'process_type': 'str',
        'single_node_job_flag': 'bool',
        'single_node_job_type': 'str',
        'last_update_user': 'str',
        'log_path': 'str',
        'basic_config': 'BasicConfig',
        'target_status': 'str',
        'approvers': 'list[JobApprover]'
    }

    attribute_map = {
        'name': 'name',
        'nodes': 'nodes',
        'schedule': 'schedule',
        'params': 'params',
        'directory': 'directory',
        'process_type': 'processType',
        'single_node_job_flag': 'singleNodeJobFlag',
        'single_node_job_type': 'singleNodeJobType',
        'last_update_user': 'lastUpdateUser',
        'log_path': 'logPath',
        'basic_config': 'basicConfig',
        'target_status': 'targetStatus',
        'approvers': 'approvers'
    }

    def __init__(self, name=None, nodes=None, schedule=None, params=None, directory=None, process_type=None, single_node_job_flag=None, single_node_job_type=None, last_update_user=None, log_path=None, basic_config=None, target_status=None, approvers=None):
        """JobInfo

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
        :param process_type: 作业类型，REAL_TIME： 实时处理，BATCH：批处理
        :type process_type: str
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
        :param target_status: 在开启审批开关后，需要填写该字段。表示创建作业的目标状态，有三种状态：SAVED、SUBMITTED和PRODUCTION，分别表示作业创建后是保存态，提交态，生产态。
        :type target_status: str
        :param approvers: 在开启审批开关后，需要填写该字段，表示作业（或脚本）审批人。
        :type approvers: list[:class:`huaweicloudsdkdgc.v1.JobApprover`]
        """
        
        

        self._name = None
        self._nodes = None
        self._schedule = None
        self._params = None
        self._directory = None
        self._process_type = None
        self._single_node_job_flag = None
        self._single_node_job_type = None
        self._last_update_user = None
        self._log_path = None
        self._basic_config = None
        self._target_status = None
        self._approvers = None
        self.discriminator = None

        self.name = name
        self.nodes = nodes
        self.schedule = schedule
        if params is not None:
            self.params = params
        if directory is not None:
            self.directory = directory
        self.process_type = process_type
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
        if target_status is not None:
            self.target_status = target_status
        if approvers is not None:
            self.approvers = approvers

    @property
    def name(self):
        """Gets the name of this JobInfo.

        作业名称

        :return: The name of this JobInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobInfo.

        作业名称

        :param name: The name of this JobInfo.
        :type name: str
        """
        self._name = name

    @property
    def nodes(self):
        """Gets the nodes of this JobInfo.

        节点定义

        :return: The nodes of this JobInfo.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.Node`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this JobInfo.

        节点定义

        :param nodes: The nodes of this JobInfo.
        :type nodes: list[:class:`huaweicloudsdkdgc.v1.Node`]
        """
        self._nodes = nodes

    @property
    def schedule(self):
        """Gets the schedule of this JobInfo.

        :return: The schedule of this JobInfo.
        :rtype: :class:`huaweicloudsdkdgc.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this JobInfo.

        :param schedule: The schedule of this JobInfo.
        :type schedule: :class:`huaweicloudsdkdgc.v1.Schedule`
        """
        self._schedule = schedule

    @property
    def params(self):
        """Gets the params of this JobInfo.

        作业参数定义

        :return: The params of this JobInfo.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this JobInfo.

        作业参数定义

        :param params: The params of this JobInfo.
        :type params: list[:class:`huaweicloudsdkdgc.v1.JobParam`]
        """
        self._params = params

    @property
    def directory(self):
        """Gets the directory of this JobInfo.

        作业在目录树上的路径。创建作业时如果路径目录不存在，会自动创建目录，如/dir/a/，默认在根目录/。

        :return: The directory of this JobInfo.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this JobInfo.

        作业在目录树上的路径。创建作业时如果路径目录不存在，会自动创建目录，如/dir/a/，默认在根目录/。

        :param directory: The directory of this JobInfo.
        :type directory: str
        """
        self._directory = directory

    @property
    def process_type(self):
        """Gets the process_type of this JobInfo.

        作业类型，REAL_TIME： 实时处理，BATCH：批处理

        :return: The process_type of this JobInfo.
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        """Sets the process_type of this JobInfo.

        作业类型，REAL_TIME： 实时处理，BATCH：批处理

        :param process_type: The process_type of this JobInfo.
        :type process_type: str
        """
        self._process_type = process_type

    @property
    def single_node_job_flag(self):
        """Gets the single_node_job_flag of this JobInfo.

        是否选择单任务，默认为false

        :return: The single_node_job_flag of this JobInfo.
        :rtype: bool
        """
        return self._single_node_job_flag

    @single_node_job_flag.setter
    def single_node_job_flag(self, single_node_job_flag):
        """Sets the single_node_job_flag of this JobInfo.

        是否选择单任务，默认为false

        :param single_node_job_flag: The single_node_job_flag of this JobInfo.
        :type single_node_job_flag: bool
        """
        self._single_node_job_flag = single_node_job_flag

    @property
    def single_node_job_type(self):
        """Gets the single_node_job_type of this JobInfo.

        单任务类型

        :return: The single_node_job_type of this JobInfo.
        :rtype: str
        """
        return self._single_node_job_type

    @single_node_job_type.setter
    def single_node_job_type(self, single_node_job_type):
        """Sets the single_node_job_type of this JobInfo.

        单任务类型

        :param single_node_job_type: The single_node_job_type of this JobInfo.
        :type single_node_job_type: str
        """
        self._single_node_job_type = single_node_job_type

    @property
    def last_update_user(self):
        """Gets the last_update_user of this JobInfo.

        作业最后修改人

        :return: The last_update_user of this JobInfo.
        :rtype: str
        """
        return self._last_update_user

    @last_update_user.setter
    def last_update_user(self, last_update_user):
        """Sets the last_update_user of this JobInfo.

        作业最后修改人

        :param last_update_user: The last_update_user of this JobInfo.
        :type last_update_user: str
        """
        self._last_update_user = last_update_user

    @property
    def log_path(self):
        """Gets the log_path of this JobInfo.

        作业运行日志存放的OBS路径。

        :return: The log_path of this JobInfo.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        """Sets the log_path of this JobInfo.

        作业运行日志存放的OBS路径。

        :param log_path: The log_path of this JobInfo.
        :type log_path: str
        """
        self._log_path = log_path

    @property
    def basic_config(self):
        """Gets the basic_config of this JobInfo.

        :return: The basic_config of this JobInfo.
        :rtype: :class:`huaweicloudsdkdgc.v1.BasicConfig`
        """
        return self._basic_config

    @basic_config.setter
    def basic_config(self, basic_config):
        """Sets the basic_config of this JobInfo.

        :param basic_config: The basic_config of this JobInfo.
        :type basic_config: :class:`huaweicloudsdkdgc.v1.BasicConfig`
        """
        self._basic_config = basic_config

    @property
    def target_status(self):
        """Gets the target_status of this JobInfo.

        在开启审批开关后，需要填写该字段。表示创建作业的目标状态，有三种状态：SAVED、SUBMITTED和PRODUCTION，分别表示作业创建后是保存态，提交态，生产态。

        :return: The target_status of this JobInfo.
        :rtype: str
        """
        return self._target_status

    @target_status.setter
    def target_status(self, target_status):
        """Sets the target_status of this JobInfo.

        在开启审批开关后，需要填写该字段。表示创建作业的目标状态，有三种状态：SAVED、SUBMITTED和PRODUCTION，分别表示作业创建后是保存态，提交态，生产态。

        :param target_status: The target_status of this JobInfo.
        :type target_status: str
        """
        self._target_status = target_status

    @property
    def approvers(self):
        """Gets the approvers of this JobInfo.

        在开启审批开关后，需要填写该字段，表示作业（或脚本）审批人。

        :return: The approvers of this JobInfo.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobApprover`]
        """
        return self._approvers

    @approvers.setter
    def approvers(self, approvers):
        """Sets the approvers of this JobInfo.

        在开启审批开关后，需要填写该字段，表示作业（或脚本）审批人。

        :param approvers: The approvers of this JobInfo.
        :type approvers: list[:class:`huaweicloudsdkdgc.v1.JobApprover`]
        """
        self._approvers = approvers

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
        if not isinstance(other, JobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
