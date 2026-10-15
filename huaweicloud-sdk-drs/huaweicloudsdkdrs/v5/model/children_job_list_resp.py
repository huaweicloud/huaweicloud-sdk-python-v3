# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChildrenJobListResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'description': 'str',
        'create_time': 'str',
        'engine_type': 'str',
        'net_type': 'str',
        'charging_mode': 'str',
        'billing_tag': 'bool',
        'job_direction': 'str',
        'job_type': 'str',
        'task_type': 'str',
        'enterprise_project_id': 'str',
        'job_mode': 'str',
        'job_mode_role': 'str',
        'is_multi_az': 'bool',
        'node_role': 'str',
        'node_new_framework': 'bool',
        'job_action': 'JobActions'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'description': 'description',
        'create_time': 'create_time',
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'charging_mode': 'charging_mode',
        'billing_tag': 'billing_tag',
        'job_direction': 'job_direction',
        'job_type': 'job_type',
        'task_type': 'task_type',
        'enterprise_project_id': 'enterprise_project_id',
        'job_mode': 'job_mode',
        'job_mode_role': 'job_mode_role',
        'is_multi_az': 'is_multi_az',
        'node_role': 'node_role',
        'node_new_framework': 'node_new_framework',
        'job_action': 'job_action'
    }

    def __init__(self, id=None, name=None, status=None, description=None, create_time=None, engine_type=None, net_type=None, charging_mode=None, billing_tag=None, job_direction=None, job_type=None, task_type=None, enterprise_project_id=None, job_mode=None, job_mode_role=None, is_multi_az=None, node_role=None, node_new_framework=None, job_action=None):
        r"""ChildrenJobListResp

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: **参数解释**：  任务名称，用于标识数据复制任务。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type name: str
        :param status: **参数解释**：  任务当前运行状态。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - CHILD_TRANSFER_STARTING：子任务启动中 - CHILD_TRANSFER_STARTED：子任务迁移中 - CHILD_TRANSFER_COMPLETE：子任务迁移完成 - CHILD_TRANSFER_FAILED：子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束  **默认取值**：  不涉及
        :type status: str
        :param description: **参数解释**：  任务的描述信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type description: str
        :param create_time: 任务创建时间。
        :type create_time: str
        :param engine_type: **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及
        :type engine_type: str
        :param net_type: **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及
        :type net_type: str
        :param charging_mode: **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  不涉及。  **取值范围**：  - period：包周期 - on_demand：按需  **默认取值**：  不涉及
        :type charging_mode: str
        :param billing_tag: **参数解释**：  任务的计费模式标识，用于标识该任务当前是否处于计费状态。  **约束限制**：  不涉及。  **取值范围**：  - true：计费中 - false：不计费  **默认取值**：  不涉及
        :type billing_tag: bool
        :param job_direction: **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及
        :type job_direction: str
        :param job_type: **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及
        :type job_type: str
        :param task_type: **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  不涉及
        :type task_type: str
        :param enterprise_project_id: **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type enterprise_project_id: str
        :param job_mode: **参数解释**：  任务模式，指定数据复制任务的执行组织方式。  **约束限制**：  不涉及。  **取值范围**：  - single：单任务 - sync_child：同步子任务 - multi_to_single：多对一任务  **默认取值**：  不涉及
        :type job_mode: str
        :param job_mode_role: **参数解释**：  任务角色，指定数据复制任务在多任务场景中的角色。  **约束限制**：  不涉及。  **取值范围**：  - parent：父任务 - child：子任务 - master：主任务 - slave：备任务  **默认取值**：  不涉及
        :type job_mode_role: str
        :param is_multi_az: **参数解释**：  标识任务是否为跨可用区（AZ）部署的主备任务。  **约束限制**：  不涉及。  **取值范围**：  - true：跨AZ主备任务 - false：非跨AZ任务  **默认取值**：  不涉及
        :type is_multi_az: bool
        :param node_role: **参数解释**：  任务节点角色，标识任务在集群部署中的角色。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type node_role: str
        :param node_new_framework: **参数解释**：  标识任务是否使用新框架执行。  **约束限制**：  不涉及。  **取值范围**：  - true：使用新框架 - false：使用旧框架  **默认取值**：  不涉及
        :type node_new_framework: bool
        :param job_action: 
        :type job_action: :class:`huaweicloudsdkdrs.v5.JobActions`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._description = None
        self._create_time = None
        self._engine_type = None
        self._net_type = None
        self._charging_mode = None
        self._billing_tag = None
        self._job_direction = None
        self._job_type = None
        self._task_type = None
        self._enterprise_project_id = None
        self._job_mode = None
        self._job_mode_role = None
        self._is_multi_az = None
        self._node_role = None
        self._node_new_framework = None
        self._job_action = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.create_time = create_time
        self.engine_type = engine_type
        self.net_type = net_type
        self.charging_mode = charging_mode
        self.billing_tag = billing_tag
        self.job_direction = job_direction
        self.job_type = job_type
        self.task_type = task_type
        self.enterprise_project_id = enterprise_project_id
        self.job_mode = job_mode
        self.job_mode_role = job_mode_role
        self.is_multi_az = is_multi_az
        self.node_role = node_role
        self.node_new_framework = node_new_framework
        self.job_action = job_action

    @property
    def id(self):
        r"""Gets the id of this ChildrenJobListResp.

        任务ID。

        :return: The id of this ChildrenJobListResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChildrenJobListResp.

        任务ID。

        :param id: The id of this ChildrenJobListResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ChildrenJobListResp.

        **参数解释**：  任务名称，用于标识数据复制任务。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The name of this ChildrenJobListResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ChildrenJobListResp.

        **参数解释**：  任务名称，用于标识数据复制任务。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param name: The name of this ChildrenJobListResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ChildrenJobListResp.

        **参数解释**：  任务当前运行状态。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - CHILD_TRANSFER_STARTING：子任务启动中 - CHILD_TRANSFER_STARTED：子任务迁移中 - CHILD_TRANSFER_COMPLETE：子任务迁移完成 - CHILD_TRANSFER_FAILED：子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束  **默认取值**：  不涉及

        :return: The status of this ChildrenJobListResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ChildrenJobListResp.

        **参数解释**：  任务当前运行状态。  **约束限制**：  不涉及。  **取值范围**：  - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - CHILD_TRANSFER_STARTING：子任务启动中 - CHILD_TRANSFER_STARTED：子任务迁移中 - CHILD_TRANSFER_COMPLETE：子任务迁移完成 - CHILD_TRANSFER_FAILED：子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束  **默认取值**：  不涉及

        :param status: The status of this ChildrenJobListResp.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this ChildrenJobListResp.

        **参数解释**：  任务的描述信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The description of this ChildrenJobListResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ChildrenJobListResp.

        **参数解释**：  任务的描述信息。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param description: The description of this ChildrenJobListResp.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this ChildrenJobListResp.

        任务创建时间。

        :return: The create_time of this ChildrenJobListResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ChildrenJobListResp.

        任务创建时间。

        :param create_time: The create_time of this ChildrenJobListResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ChildrenJobListResp.

        **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及

        :return: The engine_type of this ChildrenJobListResp.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ChildrenJobListResp.

        **参数解释**：  DRS任务引擎类型。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及

        :param engine_type: The engine_type of this ChildrenJobListResp.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        r"""Gets the net_type of this ChildrenJobListResp.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :return: The net_type of this ChildrenJobListResp.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this ChildrenJobListResp.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :param net_type: The net_type of this ChildrenJobListResp.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ChildrenJobListResp.

        **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  不涉及。  **取值范围**：  - period：包周期 - on_demand：按需  **默认取值**：  不涉及

        :return: The charging_mode of this ChildrenJobListResp.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ChildrenJobListResp.

        **参数解释**：  任务的计费模式，指定数据复制任务的付费方式。  **约束限制**：  不涉及。  **取值范围**：  - period：包周期 - on_demand：按需  **默认取值**：  不涉及

        :param charging_mode: The charging_mode of this ChildrenJobListResp.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def billing_tag(self):
        r"""Gets the billing_tag of this ChildrenJobListResp.

        **参数解释**：  任务的计费模式标识，用于标识该任务当前是否处于计费状态。  **约束限制**：  不涉及。  **取值范围**：  - true：计费中 - false：不计费  **默认取值**：  不涉及

        :return: The billing_tag of this ChildrenJobListResp.
        :rtype: bool
        """
        return self._billing_tag

    @billing_tag.setter
    def billing_tag(self, billing_tag):
        r"""Sets the billing_tag of this ChildrenJobListResp.

        **参数解释**：  任务的计费模式标识，用于标识该任务当前是否处于计费状态。  **约束限制**：  不涉及。  **取值范围**：  - true：计费中 - false：不计费  **默认取值**：  不涉及

        :param billing_tag: The billing_tag of this ChildrenJobListResp.
        :type billing_tag: bool
        """
        self._billing_tag = billing_tag

    @property
    def job_direction(self):
        r"""Gets the job_direction of this ChildrenJobListResp.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :return: The job_direction of this ChildrenJobListResp.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        r"""Sets the job_direction of this ChildrenJobListResp.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :param job_direction: The job_direction of this ChildrenJobListResp.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def job_type(self):
        r"""Gets the job_type of this ChildrenJobListResp.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及

        :return: The job_type of this ChildrenJobListResp.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ChildrenJobListResp.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及

        :param job_type: The job_type of this ChildrenJobListResp.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def task_type(self):
        r"""Gets the task_type of this ChildrenJobListResp.

        **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  不涉及

        :return: The task_type of this ChildrenJobListResp.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ChildrenJobListResp.

        **参数解释**：  任务迁移模式，指定数据复制任务的执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移，仅迁移历史数据 - FULL_INCR_TRANS：全量+增量迁移，先迁移历史数据再持续同步增量 - INCR_TRANS：增量迁移，仅同步数据变更  **默认取值**：  不涉及

        :param task_type: The task_type of this ChildrenJobListResp.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ChildrenJobListResp.

        **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The enterprise_project_id of this ChildrenJobListResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ChildrenJobListResp.

        **参数解释**：  企业项目ID，用于按企业项目过滤查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param enterprise_project_id: The enterprise_project_id of this ChildrenJobListResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def job_mode(self):
        r"""Gets the job_mode of this ChildrenJobListResp.

        **参数解释**：  任务模式，指定数据复制任务的执行组织方式。  **约束限制**：  不涉及。  **取值范围**：  - single：单任务 - sync_child：同步子任务 - multi_to_single：多对一任务  **默认取值**：  不涉及

        :return: The job_mode of this ChildrenJobListResp.
        :rtype: str
        """
        return self._job_mode

    @job_mode.setter
    def job_mode(self, job_mode):
        r"""Sets the job_mode of this ChildrenJobListResp.

        **参数解释**：  任务模式，指定数据复制任务的执行组织方式。  **约束限制**：  不涉及。  **取值范围**：  - single：单任务 - sync_child：同步子任务 - multi_to_single：多对一任务  **默认取值**：  不涉及

        :param job_mode: The job_mode of this ChildrenJobListResp.
        :type job_mode: str
        """
        self._job_mode = job_mode

    @property
    def job_mode_role(self):
        r"""Gets the job_mode_role of this ChildrenJobListResp.

        **参数解释**：  任务角色，指定数据复制任务在多任务场景中的角色。  **约束限制**：  不涉及。  **取值范围**：  - parent：父任务 - child：子任务 - master：主任务 - slave：备任务  **默认取值**：  不涉及

        :return: The job_mode_role of this ChildrenJobListResp.
        :rtype: str
        """
        return self._job_mode_role

    @job_mode_role.setter
    def job_mode_role(self, job_mode_role):
        r"""Sets the job_mode_role of this ChildrenJobListResp.

        **参数解释**：  任务角色，指定数据复制任务在多任务场景中的角色。  **约束限制**：  不涉及。  **取值范围**：  - parent：父任务 - child：子任务 - master：主任务 - slave：备任务  **默认取值**：  不涉及

        :param job_mode_role: The job_mode_role of this ChildrenJobListResp.
        :type job_mode_role: str
        """
        self._job_mode_role = job_mode_role

    @property
    def is_multi_az(self):
        r"""Gets the is_multi_az of this ChildrenJobListResp.

        **参数解释**：  标识任务是否为跨可用区（AZ）部署的主备任务。  **约束限制**：  不涉及。  **取值范围**：  - true：跨AZ主备任务 - false：非跨AZ任务  **默认取值**：  不涉及

        :return: The is_multi_az of this ChildrenJobListResp.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        r"""Sets the is_multi_az of this ChildrenJobListResp.

        **参数解释**：  标识任务是否为跨可用区（AZ）部署的主备任务。  **约束限制**：  不涉及。  **取值范围**：  - true：跨AZ主备任务 - false：非跨AZ任务  **默认取值**：  不涉及

        :param is_multi_az: The is_multi_az of this ChildrenJobListResp.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

    @property
    def node_role(self):
        r"""Gets the node_role of this ChildrenJobListResp.

        **参数解释**：  任务节点角色，标识任务在集群部署中的角色。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The node_role of this ChildrenJobListResp.
        :rtype: str
        """
        return self._node_role

    @node_role.setter
    def node_role(self, node_role):
        r"""Sets the node_role of this ChildrenJobListResp.

        **参数解释**：  任务节点角色，标识任务在集群部署中的角色。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param node_role: The node_role of this ChildrenJobListResp.
        :type node_role: str
        """
        self._node_role = node_role

    @property
    def node_new_framework(self):
        r"""Gets the node_new_framework of this ChildrenJobListResp.

        **参数解释**：  标识任务是否使用新框架执行。  **约束限制**：  不涉及。  **取值范围**：  - true：使用新框架 - false：使用旧框架  **默认取值**：  不涉及

        :return: The node_new_framework of this ChildrenJobListResp.
        :rtype: bool
        """
        return self._node_new_framework

    @node_new_framework.setter
    def node_new_framework(self, node_new_framework):
        r"""Sets the node_new_framework of this ChildrenJobListResp.

        **参数解释**：  标识任务是否使用新框架执行。  **约束限制**：  不涉及。  **取值范围**：  - true：使用新框架 - false：使用旧框架  **默认取值**：  不涉及

        :param node_new_framework: The node_new_framework of this ChildrenJobListResp.
        :type node_new_framework: bool
        """
        self._node_new_framework = node_new_framework

    @property
    def job_action(self):
        r"""Gets the job_action of this ChildrenJobListResp.

        :return: The job_action of this ChildrenJobListResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobActions`
        """
        return self._job_action

    @job_action.setter
    def job_action(self, job_action):
        r"""Sets the job_action of this ChildrenJobListResp.

        :param job_action: The job_action of this ChildrenJobListResp.
        :type job_action: :class:`huaweicloudsdkdrs.v5.JobActions`
        """
        self._job_action = job_action

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
        if not isinstance(other, ChildrenJobListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
