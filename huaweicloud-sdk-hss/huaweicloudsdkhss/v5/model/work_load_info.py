# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkLoadInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_name': 'str',
        'workload_name': 'str',
        'workload_id': 'str',
        'workload_type': 'str',
        'workload_status': 'str',
        'namespace_name': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'agent_version': 'str',
        'installed_pod_num': 'int',
        'not_install_num': 'int',
        'install_failed_num': 'int',
        'offline_num': 'int',
        'pod_num': 'int',
        'protect_pod_num': 'int',
        'running_job_num': 'int',
        'image_name': 'list[str]',
        'labels': 'list[LabelInfo]',
        'instance_info': 'list[ServerlessInstanceInfo]',
        'protect_status': 'str',
        'create_time': 'int',
        'last_schedule_time': 'int',
        'schedule': 'str',
        'upgradable': 'bool'
    }

    attribute_map = {
        'enterprise_project_name': 'enterprise_project_name',
        'workload_name': 'workload_name',
        'workload_id': 'workload_id',
        'workload_type': 'workload_type',
        'workload_status': 'workload_status',
        'namespace_name': 'namespace_name',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'agent_version': 'agent_version',
        'installed_pod_num': 'installed_pod_num',
        'not_install_num': 'not_install_num',
        'install_failed_num': 'install_failed_num',
        'offline_num': 'offline_num',
        'pod_num': 'pod_num',
        'protect_pod_num': 'protect_pod_num',
        'running_job_num': 'running_job_num',
        'image_name': 'image_name',
        'labels': 'labels',
        'instance_info': 'instance_info',
        'protect_status': 'protect_status',
        'create_time': 'create_time',
        'last_schedule_time': 'last_schedule_time',
        'schedule': 'schedule',
        'upgradable': 'upgradable'
    }

    def __init__(self, enterprise_project_name=None, workload_name=None, workload_id=None, workload_type=None, workload_status=None, namespace_name=None, cluster_name=None, cluster_id=None, agent_version=None, installed_pod_num=None, not_install_num=None, install_failed_num=None, offline_num=None, pod_num=None, protect_pod_num=None, running_job_num=None, image_name=None, labels=None, instance_info=None, protect_status=None, create_time=None, last_schedule_time=None, schedule=None, upgradable=None):
        r"""WorkLoadInfo

        The model defined in huaweicloud sdk

        :param enterprise_project_name: **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 
        :type enterprise_project_name: str
        :param workload_name: **参数解释**: 工作负载名称 **取值范围**: 字符长度0-65535位 
        :type workload_name: str
        :param workload_id: **参数解释**: 工作负载Id **取值范围**: 字符长度0-65535位 
        :type workload_id: str
        :param workload_type: **参数解释**: 工作负载类型 **取值范围**: 字符长度0-65535位 
        :type workload_type: str
        :param workload_status: **参数解释**: 工作负载状态 **取值范围**: 字符长度0-65535位 
        :type workload_status: str
        :param namespace_name: **参数解释**: 命名空间名称 **取值范围**: 字符长度0-256位 
        :type namespace_name: str
        :param cluster_name: **参数解释**: 所属集群名称 **取值范围**: 字符长度0-65535位 
        :type cluster_name: str
        :param cluster_id: **参数解释**: 所属集群ID **取值范围**: 字符长度0-65535位 
        :type cluster_id: str
        :param agent_version: **参数解释**: agent版本 **取值范围**: 字符长度0-65535位 
        :type agent_version: str
        :param installed_pod_num: **参数解释**: 已安装实例个数 **取值范围**: 最小值0，最大值2147483647 
        :type installed_pod_num: int
        :param not_install_num: **参数解释**: 未安装实例个数 **取值范围**: 最小值0，最大值2147483647 
        :type not_install_num: int
        :param install_failed_num: **参数解释**: 安装失败实例个数 **取值范围**: 最小值0，最大值2147483647 
        :type install_failed_num: int
        :param offline_num: **参数解释**: 离线agent个数 **取值范围**: 最小值0，最大值2147483647 
        :type offline_num: int
        :param pod_num: **参数解释**: 全部实例个数 **取值范围**: 最小值0，最大值2147483647 
        :type pod_num: int
        :param protect_pod_num: **参数解释**: 已防护实例个数 **取值范围**: 最小值0，最大值2147483647 
        :type protect_pod_num: int
        :param running_job_num: **参数解释**: 运行任务数 **取值范围**: 最小值0，最大值2147483647 
        :type running_job_num: int
        :param image_name: **参数解释**: 镜像名称列表 **取值范围**: 最小值0，最大值256 
        :type image_name: list[str]
        :param labels: **参数解释**: 标签 **取值范围**: 最小值0，最大值65535 
        :type labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        :param instance_info: **参数解释**: 实例信息 **取值范围**: 最小值0，最大值65535 
        :type instance_info: list[:class:`huaweicloudsdkhss.v5.ServerlessInstanceInfo`]
        :param protect_status: **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 
        :type protect_status: str
        :param create_time: **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type create_time: int
        :param last_schedule_time: **参数解释**: 普通任务为完成时间，定时任务类型为最近调度时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type last_schedule_time: int
        :param schedule: **参数解释**: 定时任务类型 任务触发 **取值范围**: 字符长度0-65535位 
        :type schedule: str
        :param upgradable: **参数解释**: 是否可升级 **取值范围**: - true：是。 - false：否。 
        :type upgradable: bool
        """
        
        

        self._enterprise_project_name = None
        self._workload_name = None
        self._workload_id = None
        self._workload_type = None
        self._workload_status = None
        self._namespace_name = None
        self._cluster_name = None
        self._cluster_id = None
        self._agent_version = None
        self._installed_pod_num = None
        self._not_install_num = None
        self._install_failed_num = None
        self._offline_num = None
        self._pod_num = None
        self._protect_pod_num = None
        self._running_job_num = None
        self._image_name = None
        self._labels = None
        self._instance_info = None
        self._protect_status = None
        self._create_time = None
        self._last_schedule_time = None
        self._schedule = None
        self._upgradable = None
        self.discriminator = None

        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if workload_name is not None:
            self.workload_name = workload_name
        if workload_id is not None:
            self.workload_id = workload_id
        if workload_type is not None:
            self.workload_type = workload_type
        if workload_status is not None:
            self.workload_status = workload_status
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if agent_version is not None:
            self.agent_version = agent_version
        if installed_pod_num is not None:
            self.installed_pod_num = installed_pod_num
        if not_install_num is not None:
            self.not_install_num = not_install_num
        if install_failed_num is not None:
            self.install_failed_num = install_failed_num
        if offline_num is not None:
            self.offline_num = offline_num
        if pod_num is not None:
            self.pod_num = pod_num
        if protect_pod_num is not None:
            self.protect_pod_num = protect_pod_num
        if running_job_num is not None:
            self.running_job_num = running_job_num
        if image_name is not None:
            self.image_name = image_name
        if labels is not None:
            self.labels = labels
        if instance_info is not None:
            self.instance_info = instance_info
        if protect_status is not None:
            self.protect_status = protect_status
        if create_time is not None:
            self.create_time = create_time
        if last_schedule_time is not None:
            self.last_schedule_time = last_schedule_time
        if schedule is not None:
            self.schedule = schedule
        if upgradable is not None:
            self.upgradable = upgradable

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this WorkLoadInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 

        :return: The enterprise_project_name of this WorkLoadInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this WorkLoadInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 

        :param enterprise_project_name: The enterprise_project_name of this WorkLoadInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def workload_name(self):
        r"""Gets the workload_name of this WorkLoadInfo.

        **参数解释**: 工作负载名称 **取值范围**: 字符长度0-65535位 

        :return: The workload_name of this WorkLoadInfo.
        :rtype: str
        """
        return self._workload_name

    @workload_name.setter
    def workload_name(self, workload_name):
        r"""Sets the workload_name of this WorkLoadInfo.

        **参数解释**: 工作负载名称 **取值范围**: 字符长度0-65535位 

        :param workload_name: The workload_name of this WorkLoadInfo.
        :type workload_name: str
        """
        self._workload_name = workload_name

    @property
    def workload_id(self):
        r"""Gets the workload_id of this WorkLoadInfo.

        **参数解释**: 工作负载Id **取值范围**: 字符长度0-65535位 

        :return: The workload_id of this WorkLoadInfo.
        :rtype: str
        """
        return self._workload_id

    @workload_id.setter
    def workload_id(self, workload_id):
        r"""Sets the workload_id of this WorkLoadInfo.

        **参数解释**: 工作负载Id **取值范围**: 字符长度0-65535位 

        :param workload_id: The workload_id of this WorkLoadInfo.
        :type workload_id: str
        """
        self._workload_id = workload_id

    @property
    def workload_type(self):
        r"""Gets the workload_type of this WorkLoadInfo.

        **参数解释**: 工作负载类型 **取值范围**: 字符长度0-65535位 

        :return: The workload_type of this WorkLoadInfo.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        r"""Sets the workload_type of this WorkLoadInfo.

        **参数解释**: 工作负载类型 **取值范围**: 字符长度0-65535位 

        :param workload_type: The workload_type of this WorkLoadInfo.
        :type workload_type: str
        """
        self._workload_type = workload_type

    @property
    def workload_status(self):
        r"""Gets the workload_status of this WorkLoadInfo.

        **参数解释**: 工作负载状态 **取值范围**: 字符长度0-65535位 

        :return: The workload_status of this WorkLoadInfo.
        :rtype: str
        """
        return self._workload_status

    @workload_status.setter
    def workload_status(self, workload_status):
        r"""Sets the workload_status of this WorkLoadInfo.

        **参数解释**: 工作负载状态 **取值范围**: 字符长度0-65535位 

        :param workload_status: The workload_status of this WorkLoadInfo.
        :type workload_status: str
        """
        self._workload_status = workload_status

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this WorkLoadInfo.

        **参数解释**: 命名空间名称 **取值范围**: 字符长度0-256位 

        :return: The namespace_name of this WorkLoadInfo.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this WorkLoadInfo.

        **参数解释**: 命名空间名称 **取值范围**: 字符长度0-256位 

        :param namespace_name: The namespace_name of this WorkLoadInfo.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this WorkLoadInfo.

        **参数解释**: 所属集群名称 **取值范围**: 字符长度0-65535位 

        :return: The cluster_name of this WorkLoadInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this WorkLoadInfo.

        **参数解释**: 所属集群名称 **取值范围**: 字符长度0-65535位 

        :param cluster_name: The cluster_name of this WorkLoadInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this WorkLoadInfo.

        **参数解释**: 所属集群ID **取值范围**: 字符长度0-65535位 

        :return: The cluster_id of this WorkLoadInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this WorkLoadInfo.

        **参数解释**: 所属集群ID **取值范围**: 字符长度0-65535位 

        :param cluster_id: The cluster_id of this WorkLoadInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def agent_version(self):
        r"""Gets the agent_version of this WorkLoadInfo.

        **参数解释**: agent版本 **取值范围**: 字符长度0-65535位 

        :return: The agent_version of this WorkLoadInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this WorkLoadInfo.

        **参数解释**: agent版本 **取值范围**: 字符长度0-65535位 

        :param agent_version: The agent_version of this WorkLoadInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def installed_pod_num(self):
        r"""Gets the installed_pod_num of this WorkLoadInfo.

        **参数解释**: 已安装实例个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The installed_pod_num of this WorkLoadInfo.
        :rtype: int
        """
        return self._installed_pod_num

    @installed_pod_num.setter
    def installed_pod_num(self, installed_pod_num):
        r"""Sets the installed_pod_num of this WorkLoadInfo.

        **参数解释**: 已安装实例个数 **取值范围**: 最小值0，最大值2147483647 

        :param installed_pod_num: The installed_pod_num of this WorkLoadInfo.
        :type installed_pod_num: int
        """
        self._installed_pod_num = installed_pod_num

    @property
    def not_install_num(self):
        r"""Gets the not_install_num of this WorkLoadInfo.

        **参数解释**: 未安装实例个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The not_install_num of this WorkLoadInfo.
        :rtype: int
        """
        return self._not_install_num

    @not_install_num.setter
    def not_install_num(self, not_install_num):
        r"""Sets the not_install_num of this WorkLoadInfo.

        **参数解释**: 未安装实例个数 **取值范围**: 最小值0，最大值2147483647 

        :param not_install_num: The not_install_num of this WorkLoadInfo.
        :type not_install_num: int
        """
        self._not_install_num = not_install_num

    @property
    def install_failed_num(self):
        r"""Gets the install_failed_num of this WorkLoadInfo.

        **参数解释**: 安装失败实例个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The install_failed_num of this WorkLoadInfo.
        :rtype: int
        """
        return self._install_failed_num

    @install_failed_num.setter
    def install_failed_num(self, install_failed_num):
        r"""Sets the install_failed_num of this WorkLoadInfo.

        **参数解释**: 安装失败实例个数 **取值范围**: 最小值0，最大值2147483647 

        :param install_failed_num: The install_failed_num of this WorkLoadInfo.
        :type install_failed_num: int
        """
        self._install_failed_num = install_failed_num

    @property
    def offline_num(self):
        r"""Gets the offline_num of this WorkLoadInfo.

        **参数解释**: 离线agent个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The offline_num of this WorkLoadInfo.
        :rtype: int
        """
        return self._offline_num

    @offline_num.setter
    def offline_num(self, offline_num):
        r"""Sets the offline_num of this WorkLoadInfo.

        **参数解释**: 离线agent个数 **取值范围**: 最小值0，最大值2147483647 

        :param offline_num: The offline_num of this WorkLoadInfo.
        :type offline_num: int
        """
        self._offline_num = offline_num

    @property
    def pod_num(self):
        r"""Gets the pod_num of this WorkLoadInfo.

        **参数解释**: 全部实例个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The pod_num of this WorkLoadInfo.
        :rtype: int
        """
        return self._pod_num

    @pod_num.setter
    def pod_num(self, pod_num):
        r"""Sets the pod_num of this WorkLoadInfo.

        **参数解释**: 全部实例个数 **取值范围**: 最小值0，最大值2147483647 

        :param pod_num: The pod_num of this WorkLoadInfo.
        :type pod_num: int
        """
        self._pod_num = pod_num

    @property
    def protect_pod_num(self):
        r"""Gets the protect_pod_num of this WorkLoadInfo.

        **参数解释**: 已防护实例个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The protect_pod_num of this WorkLoadInfo.
        :rtype: int
        """
        return self._protect_pod_num

    @protect_pod_num.setter
    def protect_pod_num(self, protect_pod_num):
        r"""Sets the protect_pod_num of this WorkLoadInfo.

        **参数解释**: 已防护实例个数 **取值范围**: 最小值0，最大值2147483647 

        :param protect_pod_num: The protect_pod_num of this WorkLoadInfo.
        :type protect_pod_num: int
        """
        self._protect_pod_num = protect_pod_num

    @property
    def running_job_num(self):
        r"""Gets the running_job_num of this WorkLoadInfo.

        **参数解释**: 运行任务数 **取值范围**: 最小值0，最大值2147483647 

        :return: The running_job_num of this WorkLoadInfo.
        :rtype: int
        """
        return self._running_job_num

    @running_job_num.setter
    def running_job_num(self, running_job_num):
        r"""Sets the running_job_num of this WorkLoadInfo.

        **参数解释**: 运行任务数 **取值范围**: 最小值0，最大值2147483647 

        :param running_job_num: The running_job_num of this WorkLoadInfo.
        :type running_job_num: int
        """
        self._running_job_num = running_job_num

    @property
    def image_name(self):
        r"""Gets the image_name of this WorkLoadInfo.

        **参数解释**: 镜像名称列表 **取值范围**: 最小值0，最大值256 

        :return: The image_name of this WorkLoadInfo.
        :rtype: list[str]
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this WorkLoadInfo.

        **参数解释**: 镜像名称列表 **取值范围**: 最小值0，最大值256 

        :param image_name: The image_name of this WorkLoadInfo.
        :type image_name: list[str]
        """
        self._image_name = image_name

    @property
    def labels(self):
        r"""Gets the labels of this WorkLoadInfo.

        **参数解释**: 标签 **取值范围**: 最小值0，最大值65535 

        :return: The labels of this WorkLoadInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this WorkLoadInfo.

        **参数解释**: 标签 **取值范围**: 最小值0，最大值65535 

        :param labels: The labels of this WorkLoadInfo.
        :type labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        self._labels = labels

    @property
    def instance_info(self):
        r"""Gets the instance_info of this WorkLoadInfo.

        **参数解释**: 实例信息 **取值范围**: 最小值0，最大值65535 

        :return: The instance_info of this WorkLoadInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ServerlessInstanceInfo`]
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        r"""Sets the instance_info of this WorkLoadInfo.

        **参数解释**: 实例信息 **取值范围**: 最小值0，最大值65535 

        :param instance_info: The instance_info of this WorkLoadInfo.
        :type instance_info: list[:class:`huaweicloudsdkhss.v5.ServerlessInstanceInfo`]
        """
        self._instance_info = instance_info

    @property
    def protect_status(self):
        r"""Gets the protect_status of this WorkLoadInfo.

        **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 

        :return: The protect_status of this WorkLoadInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this WorkLoadInfo.

        **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 

        :param protect_status: The protect_status of this WorkLoadInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def create_time(self):
        r"""Gets the create_time of this WorkLoadInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The create_time of this WorkLoadInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WorkLoadInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this WorkLoadInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_schedule_time(self):
        r"""Gets the last_schedule_time of this WorkLoadInfo.

        **参数解释**: 普通任务为完成时间，定时任务类型为最近调度时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The last_schedule_time of this WorkLoadInfo.
        :rtype: int
        """
        return self._last_schedule_time

    @last_schedule_time.setter
    def last_schedule_time(self, last_schedule_time):
        r"""Sets the last_schedule_time of this WorkLoadInfo.

        **参数解释**: 普通任务为完成时间，定时任务类型为最近调度时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param last_schedule_time: The last_schedule_time of this WorkLoadInfo.
        :type last_schedule_time: int
        """
        self._last_schedule_time = last_schedule_time

    @property
    def schedule(self):
        r"""Gets the schedule of this WorkLoadInfo.

        **参数解释**: 定时任务类型 任务触发 **取值范围**: 字符长度0-65535位 

        :return: The schedule of this WorkLoadInfo.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this WorkLoadInfo.

        **参数解释**: 定时任务类型 任务触发 **取值范围**: 字符长度0-65535位 

        :param schedule: The schedule of this WorkLoadInfo.
        :type schedule: str
        """
        self._schedule = schedule

    @property
    def upgradable(self):
        r"""Gets the upgradable of this WorkLoadInfo.

        **参数解释**: 是否可升级 **取值范围**: - true：是。 - false：否。 

        :return: The upgradable of this WorkLoadInfo.
        :rtype: bool
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        r"""Sets the upgradable of this WorkLoadInfo.

        **参数解释**: 是否可升级 **取值范围**: - true：是。 - false：否。 

        :param upgradable: The upgradable of this WorkLoadInfo.
        :type upgradable: bool
        """
        self._upgradable = upgradable

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
        if not isinstance(other, WorkLoadInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
