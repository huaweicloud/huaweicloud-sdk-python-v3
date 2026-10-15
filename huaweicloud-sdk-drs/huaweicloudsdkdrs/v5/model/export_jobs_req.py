# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportJobsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'name': 'str',
        'status': 'str',
        'dbs_instance_ids': 'list[str]',
        'description': 'str',
        'create_at': 'str',
        'completed_at': 'str',
        'enterprise_project_id': 'str',
        'engine_type': 'str',
        'net_type': 'str',
        'billing_tag': 'str',
        'billing_mode': 'str',
        'public_ip': 'str',
        'instance_ip': 'str',
        'inner_ip': 'str',
        'spec_type': 'str',
        'direction': 'str',
        'task_type': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'name': 'name',
        'status': 'status',
        'dbs_instance_ids': 'dbs_instance_ids',
        'description': 'description',
        'create_at': 'create_at',
        'completed_at': 'completed_at',
        'enterprise_project_id': 'enterprise_project_id',
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'billing_tag': 'billing_tag',
        'billing_mode': 'billing_mode',
        'public_ip': 'public_ip',
        'instance_ip': 'instance_ip',
        'inner_ip': 'inner_ip',
        'spec_type': 'spec_type',
        'direction': 'direction',
        'task_type': 'task_type',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'tag': 'tag'
    }

    def __init__(self, job_type=None, name=None, status=None, dbs_instance_ids=None, description=None, create_at=None, completed_at=None, enterprise_project_id=None, engine_type=None, net_type=None, billing_tag=None, billing_mode=None, public_ip=None, instance_ip=None, inner_ip=None, spec_type=None, direction=None, task_type=None, sort_key=None, sort_dir=None, tag=None):
        r"""ExportJobsReq

        The model defined in huaweicloud sdk

        :param job_type: DRS任务的业务场景类型。用于筛选导出特定业务场景类型的任务列表。 取值： - migration 实时迁移 - sync 实时同步 - backupMigration 备份迁移 - subscription 订阅 - cloudDataGuard 实时灾备
        :type job_type: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。默认查询所有状态的任务 - 当job_type取值：migration,sync,cloudDataGuard     对应的任务状态取值如下：     CREATING：创建中。     CREATE_FAILED：创建失败。     CONFIGURATION：配置中。     STARTJOBING：启动中。     WAITING_FOR_START：等待启动中。     START_JOB_FAILED：任务启动失败。     FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。     FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。     FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。     INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。     INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。     RELEASE_RESOURCE_STARTED：结束任务中。     RELEASE_RESOURCE_FAILED：结束任务失败。     RELEASE_RESOURCE_COMPLETE：已结束。     CHANGE_JOB_STARTED：任务变更中。     CHANGE_JOB_FAILED：任务变更失败。     CHILD_TRANSFER_STARTING：子任务启动中。     CHILD_TRANSFER_STARTED：子任务迁移中。     CHILD_TRANSFER_COMPLETE：子任务迁移完成。     CHILD_TRANSFER_FAILED：子任务迁移失败。     RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。     RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。其中，异常状态可单独查询，也可以通过以下方式查询全部异常任务：CREATE_FAILED，START_JOB_FAILED，FULL_TRANSFER_FAILED，INCRE_TRANSFER_FAILED，RELEASE_RESOURCE_FAILED，CHANGE_JOB_FAILED，CHILD_TRANSFER_FAILED。 - 当job_type取值：backupMigration   对应的任务状态取值如下：     SUBSCRIPTION_STARTED：创建中。     CREATE_FAILED：创建失败。     SUBSCRIPTION_FAILED：订阅失败。     CONFIGURATION：配置中。     STARTJOBING：启动中。     REBUILD_NODE_STARTED：故障恢复。     REBUILD_NODE_FAILED：故障恢复失败。     START_JOB_FAILED：任务启动失败。 - 当job_type取值：subscription   对应的任务状态取值如下：     SUCCESS：成功。     TRANSFERRING：备份迁移中。     FAILED：失败。     PRECHECK FAILED：预检查失败。
        :type status: str
        :param dbs_instance_ids: 数据库实例ID，最大数量为10。
        :type dbs_instance_ids: list[str]
        :param description: 描述。
        :type description: str
        :param create_at: 创建时间。 当job_type取值：migration,sync,cloudDataGuard， 任务创建时间，比如\&quot;2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\&quot; 当job_type取值：backupMigration， 表示任务创建时间，比如\&quot;2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\&quot; 当job_type取值：subscription，表示消费时间点，比如\&quot;2026-05-25T13:25:46.383Z|2026-05-28T13:25:46.999Z\&quot;
        :type create_at: str
        :param completed_at: 完成时间。在job_type是backupMigration时支持该参数填写， 表示任务完成时间，比如\&quot;2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\&quot;
        :type completed_at: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param engine_type: 引擎类型。当job_type取值：migration,sync,cloudDataGuard，该参数支持填写。当job_type取值：backupMigration 时，该参数默认值是sqlserver
        :type engine_type: str
        :param net_type: 网络类型。取值： eip：公网网络。 vpc：VPC网络。 vpn：VPN、专线网络。 当job_type取值：migration,sync,cloudDataGuard，该参数支持填写。
        :type net_type: str
        :param billing_tag: 计费标识。当job_type取值：migration,sync,cloudDataGuard,subscription，该参数支持填写。取值\&quot;0\&quot;表示计费中，\&quot;1\&quot;表示未计费
        :type billing_tag: str
        :param billing_mode: 计费模式。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。取值：\&quot;1\&quot;表示包年包月，\&quot;0\&quot;表示按需计费
        :type billing_mode: str
        :param public_ip: 实例绑定的公网IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。
        :type public_ip: str
        :param instance_ip: DRS绑定的数据库实例IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。
        :type instance_ip: str
        :param inner_ip: DRS绑定的内网IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。
        :type inner_ip: str
        :param spec_type: 规格类型。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。 取值如下： 2xlarge：极大规格。 xlarge：超大规格。 high：大规格。 medium：中规格。 small：小规格。 micro：极小规格。
        :type spec_type: str
        :param direction: 数据流动方向。 当job_type取值migration,sync时支持传值。 取值： - up：入云 - down：出云 - non-dbs：自建 - multiWrite：双向同步。 当job_type取值cloudDataGuard时支持传值， 取值： - up：本云为备 - down：本云为主 - multiWrite：双主灾备
        :type direction: str
        :param task_type: 同步类型。当job_type取值migration,sync时支持传值。
        :type task_type: str
        :param sort_key: 返回结果按该关键字排序，默认为“create_time”。 当前支持排序的关键字： name status create_time net_type job_direction pay_mode
        :type sort_key: str
        :param sort_dir: 降序或升序（分别对应desc和asc，默认为“desc”）。
        :type sort_dir: str
        :param tag: 标签
        :type tag: str
        """
        
        

        self._job_type = None
        self._name = None
        self._status = None
        self._dbs_instance_ids = None
        self._description = None
        self._create_at = None
        self._completed_at = None
        self._enterprise_project_id = None
        self._engine_type = None
        self._net_type = None
        self._billing_tag = None
        self._billing_mode = None
        self._public_ip = None
        self._instance_ip = None
        self._inner_ip = None
        self._spec_type = None
        self._direction = None
        self._task_type = None
        self._sort_key = None
        self._sort_dir = None
        self._tag = None
        self.discriminator = None

        self.job_type = job_type
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if dbs_instance_ids is not None:
            self.dbs_instance_ids = dbs_instance_ids
        if description is not None:
            self.description = description
        if create_at is not None:
            self.create_at = create_at
        if completed_at is not None:
            self.completed_at = completed_at
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if engine_type is not None:
            self.engine_type = engine_type
        if net_type is not None:
            self.net_type = net_type
        if billing_tag is not None:
            self.billing_tag = billing_tag
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if public_ip is not None:
            self.public_ip = public_ip
        if instance_ip is not None:
            self.instance_ip = instance_ip
        if inner_ip is not None:
            self.inner_ip = inner_ip
        if spec_type is not None:
            self.spec_type = spec_type
        if direction is not None:
            self.direction = direction
        if task_type is not None:
            self.task_type = task_type
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if tag is not None:
            self.tag = tag

    @property
    def job_type(self):
        r"""Gets the job_type of this ExportJobsReq.

        DRS任务的业务场景类型。用于筛选导出特定业务场景类型的任务列表。 取值： - migration 实时迁移 - sync 实时同步 - backupMigration 备份迁移 - subscription 订阅 - cloudDataGuard 实时灾备

        :return: The job_type of this ExportJobsReq.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ExportJobsReq.

        DRS任务的业务场景类型。用于筛选导出特定业务场景类型的任务列表。 取值： - migration 实时迁移 - sync 实时同步 - backupMigration 备份迁移 - subscription 订阅 - cloudDataGuard 实时灾备

        :param job_type: The job_type of this ExportJobsReq.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def name(self):
        r"""Gets the name of this ExportJobsReq.

        任务名称。

        :return: The name of this ExportJobsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExportJobsReq.

        任务名称。

        :param name: The name of this ExportJobsReq.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ExportJobsReq.

        任务状态。默认查询所有状态的任务 - 当job_type取值：migration,sync,cloudDataGuard     对应的任务状态取值如下：     CREATING：创建中。     CREATE_FAILED：创建失败。     CONFIGURATION：配置中。     STARTJOBING：启动中。     WAITING_FOR_START：等待启动中。     START_JOB_FAILED：任务启动失败。     FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。     FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。     FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。     INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。     INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。     RELEASE_RESOURCE_STARTED：结束任务中。     RELEASE_RESOURCE_FAILED：结束任务失败。     RELEASE_RESOURCE_COMPLETE：已结束。     CHANGE_JOB_STARTED：任务变更中。     CHANGE_JOB_FAILED：任务变更失败。     CHILD_TRANSFER_STARTING：子任务启动中。     CHILD_TRANSFER_STARTED：子任务迁移中。     CHILD_TRANSFER_COMPLETE：子任务迁移完成。     CHILD_TRANSFER_FAILED：子任务迁移失败。     RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。     RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。其中，异常状态可单独查询，也可以通过以下方式查询全部异常任务：CREATE_FAILED，START_JOB_FAILED，FULL_TRANSFER_FAILED，INCRE_TRANSFER_FAILED，RELEASE_RESOURCE_FAILED，CHANGE_JOB_FAILED，CHILD_TRANSFER_FAILED。 - 当job_type取值：backupMigration   对应的任务状态取值如下：     SUBSCRIPTION_STARTED：创建中。     CREATE_FAILED：创建失败。     SUBSCRIPTION_FAILED：订阅失败。     CONFIGURATION：配置中。     STARTJOBING：启动中。     REBUILD_NODE_STARTED：故障恢复。     REBUILD_NODE_FAILED：故障恢复失败。     START_JOB_FAILED：任务启动失败。 - 当job_type取值：subscription   对应的任务状态取值如下：     SUCCESS：成功。     TRANSFERRING：备份迁移中。     FAILED：失败。     PRECHECK FAILED：预检查失败。

        :return: The status of this ExportJobsReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportJobsReq.

        任务状态。默认查询所有状态的任务 - 当job_type取值：migration,sync,cloudDataGuard     对应的任务状态取值如下：     CREATING：创建中。     CREATE_FAILED：创建失败。     CONFIGURATION：配置中。     STARTJOBING：启动中。     WAITING_FOR_START：等待启动中。     START_JOB_FAILED：任务启动失败。     FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。     FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。     FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。     INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。     INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。     RELEASE_RESOURCE_STARTED：结束任务中。     RELEASE_RESOURCE_FAILED：结束任务失败。     RELEASE_RESOURCE_COMPLETE：已结束。     CHANGE_JOB_STARTED：任务变更中。     CHANGE_JOB_FAILED：任务变更失败。     CHILD_TRANSFER_STARTING：子任务启动中。     CHILD_TRANSFER_STARTED：子任务迁移中。     CHILD_TRANSFER_COMPLETE：子任务迁移完成。     CHILD_TRANSFER_FAILED：子任务迁移失败。     RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。     RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。其中，异常状态可单独查询，也可以通过以下方式查询全部异常任务：CREATE_FAILED，START_JOB_FAILED，FULL_TRANSFER_FAILED，INCRE_TRANSFER_FAILED，RELEASE_RESOURCE_FAILED，CHANGE_JOB_FAILED，CHILD_TRANSFER_FAILED。 - 当job_type取值：backupMigration   对应的任务状态取值如下：     SUBSCRIPTION_STARTED：创建中。     CREATE_FAILED：创建失败。     SUBSCRIPTION_FAILED：订阅失败。     CONFIGURATION：配置中。     STARTJOBING：启动中。     REBUILD_NODE_STARTED：故障恢复。     REBUILD_NODE_FAILED：故障恢复失败。     START_JOB_FAILED：任务启动失败。 - 当job_type取值：subscription   对应的任务状态取值如下：     SUCCESS：成功。     TRANSFERRING：备份迁移中。     FAILED：失败。     PRECHECK FAILED：预检查失败。

        :param status: The status of this ExportJobsReq.
        :type status: str
        """
        self._status = status

    @property
    def dbs_instance_ids(self):
        r"""Gets the dbs_instance_ids of this ExportJobsReq.

        数据库实例ID，最大数量为10。

        :return: The dbs_instance_ids of this ExportJobsReq.
        :rtype: list[str]
        """
        return self._dbs_instance_ids

    @dbs_instance_ids.setter
    def dbs_instance_ids(self, dbs_instance_ids):
        r"""Sets the dbs_instance_ids of this ExportJobsReq.

        数据库实例ID，最大数量为10。

        :param dbs_instance_ids: The dbs_instance_ids of this ExportJobsReq.
        :type dbs_instance_ids: list[str]
        """
        self._dbs_instance_ids = dbs_instance_ids

    @property
    def description(self):
        r"""Gets the description of this ExportJobsReq.

        描述。

        :return: The description of this ExportJobsReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExportJobsReq.

        描述。

        :param description: The description of this ExportJobsReq.
        :type description: str
        """
        self._description = description

    @property
    def create_at(self):
        r"""Gets the create_at of this ExportJobsReq.

        创建时间。 当job_type取值：migration,sync,cloudDataGuard， 任务创建时间，比如\"2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\" 当job_type取值：backupMigration， 表示任务创建时间，比如\"2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\" 当job_type取值：subscription，表示消费时间点，比如\"2026-05-25T13:25:46.383Z|2026-05-28T13:25:46.999Z\"

        :return: The create_at of this ExportJobsReq.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ExportJobsReq.

        创建时间。 当job_type取值：migration,sync,cloudDataGuard， 任务创建时间，比如\"2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\" 当job_type取值：backupMigration， 表示任务创建时间，比如\"2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\" 当job_type取值：subscription，表示消费时间点，比如\"2026-05-25T13:25:46.383Z|2026-05-28T13:25:46.999Z\"

        :param create_at: The create_at of this ExportJobsReq.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def completed_at(self):
        r"""Gets the completed_at of this ExportJobsReq.

        完成时间。在job_type是backupMigration时支持该参数填写， 表示任务完成时间，比如\"2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\"

        :return: The completed_at of this ExportJobsReq.
        :rtype: str
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        r"""Sets the completed_at of this ExportJobsReq.

        完成时间。在job_type是backupMigration时支持该参数填写， 表示任务完成时间，比如\"2026-05-25T13:41:00.127Z|2026-05-28T13:41:00.999Z\"

        :param completed_at: The completed_at of this ExportJobsReq.
        :type completed_at: str
        """
        self._completed_at = completed_at

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportJobsReq.

        企业项目ID。

        :return: The enterprise_project_id of this ExportJobsReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportJobsReq.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ExportJobsReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ExportJobsReq.

        引擎类型。当job_type取值：migration,sync,cloudDataGuard，该参数支持填写。当job_type取值：backupMigration 时，该参数默认值是sqlserver

        :return: The engine_type of this ExportJobsReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ExportJobsReq.

        引擎类型。当job_type取值：migration,sync,cloudDataGuard，该参数支持填写。当job_type取值：backupMigration 时，该参数默认值是sqlserver

        :param engine_type: The engine_type of this ExportJobsReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        r"""Gets the net_type of this ExportJobsReq.

        网络类型。取值： eip：公网网络。 vpc：VPC网络。 vpn：VPN、专线网络。 当job_type取值：migration,sync,cloudDataGuard，该参数支持填写。

        :return: The net_type of this ExportJobsReq.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this ExportJobsReq.

        网络类型。取值： eip：公网网络。 vpc：VPC网络。 vpn：VPN、专线网络。 当job_type取值：migration,sync,cloudDataGuard，该参数支持填写。

        :param net_type: The net_type of this ExportJobsReq.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def billing_tag(self):
        r"""Gets the billing_tag of this ExportJobsReq.

        计费标识。当job_type取值：migration,sync,cloudDataGuard,subscription，该参数支持填写。取值\"0\"表示计费中，\"1\"表示未计费

        :return: The billing_tag of this ExportJobsReq.
        :rtype: str
        """
        return self._billing_tag

    @billing_tag.setter
    def billing_tag(self, billing_tag):
        r"""Sets the billing_tag of this ExportJobsReq.

        计费标识。当job_type取值：migration,sync,cloudDataGuard,subscription，该参数支持填写。取值\"0\"表示计费中，\"1\"表示未计费

        :param billing_tag: The billing_tag of this ExportJobsReq.
        :type billing_tag: str
        """
        self._billing_tag = billing_tag

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this ExportJobsReq.

        计费模式。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。取值：\"1\"表示包年包月，\"0\"表示按需计费

        :return: The billing_mode of this ExportJobsReq.
        :rtype: str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this ExportJobsReq.

        计费模式。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。取值：\"1\"表示包年包月，\"0\"表示按需计费

        :param billing_mode: The billing_mode of this ExportJobsReq.
        :type billing_mode: str
        """
        self._billing_mode = billing_mode

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ExportJobsReq.

        实例绑定的公网IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。

        :return: The public_ip of this ExportJobsReq.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ExportJobsReq.

        实例绑定的公网IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。

        :param public_ip: The public_ip of this ExportJobsReq.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def instance_ip(self):
        r"""Gets the instance_ip of this ExportJobsReq.

        DRS绑定的数据库实例IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。

        :return: The instance_ip of this ExportJobsReq.
        :rtype: str
        """
        return self._instance_ip

    @instance_ip.setter
    def instance_ip(self, instance_ip):
        r"""Sets the instance_ip of this ExportJobsReq.

        DRS绑定的数据库实例IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。

        :param instance_ip: The instance_ip of this ExportJobsReq.
        :type instance_ip: str
        """
        self._instance_ip = instance_ip

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this ExportJobsReq.

        DRS绑定的内网IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。

        :return: The inner_ip of this ExportJobsReq.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this ExportJobsReq.

        DRS绑定的内网IP。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。

        :param inner_ip: The inner_ip of this ExportJobsReq.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

    @property
    def spec_type(self):
        r"""Gets the spec_type of this ExportJobsReq.

        规格类型。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。 取值如下： 2xlarge：极大规格。 xlarge：超大规格。 high：大规格。 medium：中规格。 small：小规格。 micro：极小规格。

        :return: The spec_type of this ExportJobsReq.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        r"""Sets the spec_type of this ExportJobsReq.

        规格类型。当job_type取值：migration,sync,cloudDataGuard，支持该参数填写。 取值如下： 2xlarge：极大规格。 xlarge：超大规格。 high：大规格。 medium：中规格。 small：小规格。 micro：极小规格。

        :param spec_type: The spec_type of this ExportJobsReq.
        :type spec_type: str
        """
        self._spec_type = spec_type

    @property
    def direction(self):
        r"""Gets the direction of this ExportJobsReq.

        数据流动方向。 当job_type取值migration,sync时支持传值。 取值： - up：入云 - down：出云 - non-dbs：自建 - multiWrite：双向同步。 当job_type取值cloudDataGuard时支持传值， 取值： - up：本云为备 - down：本云为主 - multiWrite：双主灾备

        :return: The direction of this ExportJobsReq.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this ExportJobsReq.

        数据流动方向。 当job_type取值migration,sync时支持传值。 取值： - up：入云 - down：出云 - non-dbs：自建 - multiWrite：双向同步。 当job_type取值cloudDataGuard时支持传值， 取值： - up：本云为备 - down：本云为主 - multiWrite：双主灾备

        :param direction: The direction of this ExportJobsReq.
        :type direction: str
        """
        self._direction = direction

    @property
    def task_type(self):
        r"""Gets the task_type of this ExportJobsReq.

        同步类型。当job_type取值migration,sync时支持传值。

        :return: The task_type of this ExportJobsReq.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ExportJobsReq.

        同步类型。当job_type取值migration,sync时支持传值。

        :param task_type: The task_type of this ExportJobsReq.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ExportJobsReq.

        返回结果按该关键字排序，默认为“create_time”。 当前支持排序的关键字： name status create_time net_type job_direction pay_mode

        :return: The sort_key of this ExportJobsReq.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ExportJobsReq.

        返回结果按该关键字排序，默认为“create_time”。 当前支持排序的关键字： name status create_time net_type job_direction pay_mode

        :param sort_key: The sort_key of this ExportJobsReq.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ExportJobsReq.

        降序或升序（分别对应desc和asc，默认为“desc”）。

        :return: The sort_dir of this ExportJobsReq.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ExportJobsReq.

        降序或升序（分别对应desc和asc，默认为“desc”）。

        :param sort_dir: The sort_dir of this ExportJobsReq.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def tag(self):
        r"""Gets the tag of this ExportJobsReq.

        标签

        :return: The tag of this ExportJobsReq.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ExportJobsReq.

        标签

        :param tag: The tag of this ExportJobsReq.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ExportJobsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
