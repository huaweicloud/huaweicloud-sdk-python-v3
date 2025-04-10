# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInfoRequest:

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
        'log_path': 'str',
        'directory': 'str',
        'process_type': 'str',
        'single_node_job_flag': 'bool',
        'single_node_job_type': 'str',
        'create_user': 'str',
        'owner': 'str',
        'priority': 'str',
        'last_update_user': 'str',
        'target_status': 'str',
        'approvers': 'list[Approver]',
        'basic_config': 'BasicInfo'
    }

    attribute_map = {
        'name': 'name',
        'nodes': 'nodes',
        'schedule': 'schedule',
        'params': 'params',
        'log_path': 'log_path',
        'directory': 'directory',
        'process_type': 'process_type',
        'single_node_job_flag': 'single_node_job_flag',
        'single_node_job_type': 'single_node_job_type',
        'create_user': 'create_user',
        'owner': 'owner',
        'priority': 'priority',
        'last_update_user': 'last_update_user',
        'target_status': 'target_status',
        'approvers': 'approvers',
        'basic_config': 'basic_config'
    }

    def __init__(self, name=None, nodes=None, schedule=None, params=None, log_path=None, directory=None, process_type=None, single_node_job_flag=None, single_node_job_type=None, create_user=None, owner=None, priority=None, last_update_user=None, target_status=None, approvers=None, basic_config=None):
        r"""JobInfoRequest

        The model defined in huaweicloud sdk

        :param name: 作业名称，只能包含六种字符：英文字母、数字、中文、中划线、下划线和点号。作业名称不能重复。
        :type name: str
        :param nodes: 节点清单
        :type nodes: list[:class:`huaweicloudsdkdataartsstudio.v1.Node`]
        :param schedule: 
        :type schedule: :class:`huaweicloudsdkdataartsstudio.v1.Schedule`
        :param params: 作业参数清单
        :type params: list[:class:`huaweicloudsdkdataartsstudio.v1.JobParam`]
        :param log_path: 日志路径
        :type log_path: str
        :param directory: 目录路径
        :type directory: str
        :param process_type: 作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理
        :type process_type: str
        :param single_node_job_flag: 是否选择单任务，默认为false
        :type single_node_job_flag: bool
        :param single_node_job_type: 单任务类型
        :type single_node_job_type: str
        :param create_user: 创建用户
        :type create_user: str
        :param owner: 责任人
        :type owner: str
        :param priority: 优先级
        :type priority: str
        :param last_update_user: 作业最后修改人
        :type last_update_user: str
        :param target_status: 在开启审批开关后，需要填写该字段。表示创建作业的目标状态。  - SAVED: 保存态，表示作业仅保存，无法调度运行，需要提交并审核通过后才能运行。  - SUBMITTED: 提交态，表示作业保存后会自动提交，需要审核通过才能运行。  - PRODUCTION: 生产态，表示作业跳过审批环节，创建后可以直接运行。注意：只有工作空间的管理员用户才能创建生产态的作业。
        :type target_status: str
        :param approvers: 作业审批人
        :type approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.Approver`]
        :param basic_config: 
        :type basic_config: :class:`huaweicloudsdkdataartsstudio.v1.BasicInfo`
        """
        
        

        self._name = None
        self._nodes = None
        self._schedule = None
        self._params = None
        self._log_path = None
        self._directory = None
        self._process_type = None
        self._single_node_job_flag = None
        self._single_node_job_type = None
        self._create_user = None
        self._owner = None
        self._priority = None
        self._last_update_user = None
        self._target_status = None
        self._approvers = None
        self._basic_config = None
        self.discriminator = None

        self.name = name
        self.nodes = nodes
        self.schedule = schedule
        if params is not None:
            self.params = params
        if log_path is not None:
            self.log_path = log_path
        if directory is not None:
            self.directory = directory
        self.process_type = process_type
        if single_node_job_flag is not None:
            self.single_node_job_flag = single_node_job_flag
        if single_node_job_type is not None:
            self.single_node_job_type = single_node_job_type
        if create_user is not None:
            self.create_user = create_user
        if owner is not None:
            self.owner = owner
        if priority is not None:
            self.priority = priority
        if last_update_user is not None:
            self.last_update_user = last_update_user
        if target_status is not None:
            self.target_status = target_status
        if approvers is not None:
            self.approvers = approvers
        if basic_config is not None:
            self.basic_config = basic_config

    @property
    def name(self):
        r"""Gets the name of this JobInfoRequest.

        作业名称，只能包含六种字符：英文字母、数字、中文、中划线、下划线和点号。作业名称不能重复。

        :return: The name of this JobInfoRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobInfoRequest.

        作业名称，只能包含六种字符：英文字母、数字、中文、中划线、下划线和点号。作业名称不能重复。

        :param name: The name of this JobInfoRequest.
        :type name: str
        """
        self._name = name

    @property
    def nodes(self):
        r"""Gets the nodes of this JobInfoRequest.

        节点清单

        :return: The nodes of this JobInfoRequest.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Node`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this JobInfoRequest.

        节点清单

        :param nodes: The nodes of this JobInfoRequest.
        :type nodes: list[:class:`huaweicloudsdkdataartsstudio.v1.Node`]
        """
        self._nodes = nodes

    @property
    def schedule(self):
        r"""Gets the schedule of this JobInfoRequest.

        :return: The schedule of this JobInfoRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this JobInfoRequest.

        :param schedule: The schedule of this JobInfoRequest.
        :type schedule: :class:`huaweicloudsdkdataartsstudio.v1.Schedule`
        """
        self._schedule = schedule

    @property
    def params(self):
        r"""Gets the params of this JobInfoRequest.

        作业参数清单

        :return: The params of this JobInfoRequest.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.JobParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this JobInfoRequest.

        作业参数清单

        :param params: The params of this JobInfoRequest.
        :type params: list[:class:`huaweicloudsdkdataartsstudio.v1.JobParam`]
        """
        self._params = params

    @property
    def log_path(self):
        r"""Gets the log_path of this JobInfoRequest.

        日志路径

        :return: The log_path of this JobInfoRequest.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        r"""Sets the log_path of this JobInfoRequest.

        日志路径

        :param log_path: The log_path of this JobInfoRequest.
        :type log_path: str
        """
        self._log_path = log_path

    @property
    def directory(self):
        r"""Gets the directory of this JobInfoRequest.

        目录路径

        :return: The directory of this JobInfoRequest.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this JobInfoRequest.

        目录路径

        :param directory: The directory of this JobInfoRequest.
        :type directory: str
        """
        self._directory = directory

    @property
    def process_type(self):
        r"""Gets the process_type of this JobInfoRequest.

        作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理

        :return: The process_type of this JobInfoRequest.
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        r"""Sets the process_type of this JobInfoRequest.

        作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理

        :param process_type: The process_type of this JobInfoRequest.
        :type process_type: str
        """
        self._process_type = process_type

    @property
    def single_node_job_flag(self):
        r"""Gets the single_node_job_flag of this JobInfoRequest.

        是否选择单任务，默认为false

        :return: The single_node_job_flag of this JobInfoRequest.
        :rtype: bool
        """
        return self._single_node_job_flag

    @single_node_job_flag.setter
    def single_node_job_flag(self, single_node_job_flag):
        r"""Sets the single_node_job_flag of this JobInfoRequest.

        是否选择单任务，默认为false

        :param single_node_job_flag: The single_node_job_flag of this JobInfoRequest.
        :type single_node_job_flag: bool
        """
        self._single_node_job_flag = single_node_job_flag

    @property
    def single_node_job_type(self):
        r"""Gets the single_node_job_type of this JobInfoRequest.

        单任务类型

        :return: The single_node_job_type of this JobInfoRequest.
        :rtype: str
        """
        return self._single_node_job_type

    @single_node_job_type.setter
    def single_node_job_type(self, single_node_job_type):
        r"""Sets the single_node_job_type of this JobInfoRequest.

        单任务类型

        :param single_node_job_type: The single_node_job_type of this JobInfoRequest.
        :type single_node_job_type: str
        """
        self._single_node_job_type = single_node_job_type

    @property
    def create_user(self):
        r"""Gets the create_user of this JobInfoRequest.

        创建用户

        :return: The create_user of this JobInfoRequest.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this JobInfoRequest.

        创建用户

        :param create_user: The create_user of this JobInfoRequest.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def owner(self):
        r"""Gets the owner of this JobInfoRequest.

        责任人

        :return: The owner of this JobInfoRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this JobInfoRequest.

        责任人

        :param owner: The owner of this JobInfoRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def priority(self):
        r"""Gets the priority of this JobInfoRequest.

        优先级

        :return: The priority of this JobInfoRequest.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this JobInfoRequest.

        优先级

        :param priority: The priority of this JobInfoRequest.
        :type priority: str
        """
        self._priority = priority

    @property
    def last_update_user(self):
        r"""Gets the last_update_user of this JobInfoRequest.

        作业最后修改人

        :return: The last_update_user of this JobInfoRequest.
        :rtype: str
        """
        return self._last_update_user

    @last_update_user.setter
    def last_update_user(self, last_update_user):
        r"""Sets the last_update_user of this JobInfoRequest.

        作业最后修改人

        :param last_update_user: The last_update_user of this JobInfoRequest.
        :type last_update_user: str
        """
        self._last_update_user = last_update_user

    @property
    def target_status(self):
        r"""Gets the target_status of this JobInfoRequest.

        在开启审批开关后，需要填写该字段。表示创建作业的目标状态。  - SAVED: 保存态，表示作业仅保存，无法调度运行，需要提交并审核通过后才能运行。  - SUBMITTED: 提交态，表示作业保存后会自动提交，需要审核通过才能运行。  - PRODUCTION: 生产态，表示作业跳过审批环节，创建后可以直接运行。注意：只有工作空间的管理员用户才能创建生产态的作业。

        :return: The target_status of this JobInfoRequest.
        :rtype: str
        """
        return self._target_status

    @target_status.setter
    def target_status(self, target_status):
        r"""Sets the target_status of this JobInfoRequest.

        在开启审批开关后，需要填写该字段。表示创建作业的目标状态。  - SAVED: 保存态，表示作业仅保存，无法调度运行，需要提交并审核通过后才能运行。  - SUBMITTED: 提交态，表示作业保存后会自动提交，需要审核通过才能运行。  - PRODUCTION: 生产态，表示作业跳过审批环节，创建后可以直接运行。注意：只有工作空间的管理员用户才能创建生产态的作业。

        :param target_status: The target_status of this JobInfoRequest.
        :type target_status: str
        """
        self._target_status = target_status

    @property
    def approvers(self):
        r"""Gets the approvers of this JobInfoRequest.

        作业审批人

        :return: The approvers of this JobInfoRequest.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Approver`]
        """
        return self._approvers

    @approvers.setter
    def approvers(self, approvers):
        r"""Sets the approvers of this JobInfoRequest.

        作业审批人

        :param approvers: The approvers of this JobInfoRequest.
        :type approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.Approver`]
        """
        self._approvers = approvers

    @property
    def basic_config(self):
        r"""Gets the basic_config of this JobInfoRequest.

        :return: The basic_config of this JobInfoRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BasicInfo`
        """
        return self._basic_config

    @basic_config.setter
    def basic_config(self, basic_config):
        r"""Sets the basic_config of this JobInfoRequest.

        :param basic_config: The basic_config of this JobInfoRequest.
        :type basic_config: :class:`huaweicloudsdkdataartsstudio.v1.BasicInfo`
        """
        self._basic_config = basic_config

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
        if not isinstance(other, JobInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
