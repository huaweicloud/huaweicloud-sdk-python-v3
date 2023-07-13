# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryJobResp:

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
        'parent_id': 'str',
        'name': 'str',
        'status': 'str',
        'description': 'str',
        'create_time': 'str',
        'task_type': 'str',
        'source_endpoint': 'Endpoint',
        'dmq_endpoint': 'Endpoint',
        'source_sharding': 'list[Endpoint]',
        'target_endpoint': 'Endpoint',
        'net_type': 'str',
        'failed_reason': 'str',
        'inst_info': 'InstInfo',
        'actual_start_time': 'str',
        'full_transfer_complete_time': 'str',
        'update_time': 'str',
        'job_direction': 'str',
        'db_use_type': 'str',
        'need_restart': 'bool',
        'is_target_readonly': 'bool',
        'conflict_policy': 'str',
        'filter_ddl_policy': 'str',
        'speed_limit': 'list[SpeedLimitInfo]',
        'schema_type': 'str',
        'node_num': 'str',
        'object_switch': 'bool',
        'master_job_id': 'str',
        'full_mode': 'str',
        'struct_trans': 'bool',
        'index_trans': 'bool',
        'replace_definer': 'bool',
        'migrate_user': 'bool',
        'sync_database': 'bool',
        'error_code': 'str',
        'error_message': 'str',
        'target_root_db': 'DefaultRootDb',
        'az_code': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'multi_write': 'bool',
        'support_ip_v6': 'bool',
        'inherit_id': 'str',
        'gtid': 'str',
        'alarm_notify': 'QuerySmnInfoResp',
        'incre_start_position': 'str',
        'is_multi_az': 'bool',
        'az_name': 'str',
        'master_az': 'str',
        'slave_az': 'str',
        'node_role': 'str',
        'period_order': 'PeriodOrderResp',
        'object_infos': 'list[DatabaseObjectInfo]',
        'original_job_direction': 'str',
        'data_transformation': 'GetDataTransformationResp',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parent_id',
        'name': 'name',
        'status': 'status',
        'description': 'description',
        'create_time': 'create_time',
        'task_type': 'task_type',
        'source_endpoint': 'source_endpoint',
        'dmq_endpoint': 'dmq_endpoint',
        'source_sharding': 'source_sharding',
        'target_endpoint': 'target_endpoint',
        'net_type': 'net_type',
        'failed_reason': 'failed_reason',
        'inst_info': 'inst_info',
        'actual_start_time': 'actual_start_time',
        'full_transfer_complete_time': 'full_transfer_complete_time',
        'update_time': 'update_time',
        'job_direction': 'job_direction',
        'db_use_type': 'db_use_type',
        'need_restart': 'need_restart',
        'is_target_readonly': 'is_target_readonly',
        'conflict_policy': 'conflict_policy',
        'filter_ddl_policy': 'filter_ddl_policy',
        'speed_limit': 'speed_limit',
        'schema_type': 'schema_type',
        'node_num': 'node_num',
        'object_switch': 'object_switch',
        'master_job_id': 'master_job_id',
        'full_mode': 'full_mode',
        'struct_trans': 'struct_trans',
        'index_trans': 'index_trans',
        'replace_definer': 'replace_definer',
        'migrate_user': 'migrate_user',
        'sync_database': 'sync_database',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'target_root_db': 'target_root_db',
        'az_code': 'az_code',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'multi_write': 'multi_write',
        'support_ip_v6': 'support_ip_v6',
        'inherit_id': 'inherit_id',
        'gtid': 'gtid',
        'alarm_notify': 'alarm_notify',
        'incre_start_position': 'incre_start_position',
        'is_multi_az': 'is_multi_az',
        'az_name': 'az_name',
        'master_az': 'master_az',
        'slave_az': 'slave_az',
        'node_role': 'node_role',
        'period_order': 'period_order',
        'object_infos': 'object_infos',
        'original_job_direction': 'original_job_direction',
        'data_transformation': 'data_transformation',
        'tags': 'tags'
    }

    def __init__(self, id=None, parent_id=None, name=None, status=None, description=None, create_time=None, task_type=None, source_endpoint=None, dmq_endpoint=None, source_sharding=None, target_endpoint=None, net_type=None, failed_reason=None, inst_info=None, actual_start_time=None, full_transfer_complete_time=None, update_time=None, job_direction=None, db_use_type=None, need_restart=None, is_target_readonly=None, conflict_policy=None, filter_ddl_policy=None, speed_limit=None, schema_type=None, node_num=None, object_switch=None, master_job_id=None, full_mode=None, struct_trans=None, index_trans=None, replace_definer=None, migrate_user=None, sync_database=None, error_code=None, error_message=None, target_root_db=None, az_code=None, vpc_id=None, subnet_id=None, security_group_id=None, multi_write=None, support_ip_v6=None, inherit_id=None, gtid=None, alarm_notify=None, incre_start_position=None, is_multi_az=None, az_name=None, master_az=None, slave_az=None, node_role=None, period_order=None, object_infos=None, original_job_direction=None, data_transformation=None, tags=None):
        """QueryJobResp

        The model defined in huaweicloud sdk

        :param id: 任务id
        :type id: str
        :param parent_id: 父任务id。
        :type parent_id: str
        :param name: 任务名称
        :type name: str
        :param status: 任务状态。 - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - PAUSING：已暂停 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - REBUILD_NODE_STARTED：故障恢复中 - REBUILD_NODE_FAILED：故障恢复失败 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - DELETED：已删除 - CHILD_TRANSFER_STARTING：再编辑子任务启动中 - CHILD_TRANSFER_STARTED：再编辑子任务迁移中 - CHILD_TRANSFER_COMPLETE：再编辑子任务迁移完成 - CHILD_TRANSFER_FAILED：再编辑子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：再编辑子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：再编辑子任务已结束 - NODE_UPGRADE_START：升级开始 - NODE_UPGRADE_COMPLETE：升级完成 - NODE_UPGRADE_FAILED：升级失败
        :type status: str
        :param description: 描述信息
        :type description: str
        :param create_time: 创建时间，时间戳格式。
        :type create_time: str
        :param task_type: 迁移模式
        :type task_type: str
        :param source_endpoint: 
        :type source_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param dmq_endpoint: 
        :type dmq_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param source_sharding: 物理源库信息。
        :type source_sharding: list[:class:`huaweicloudsdkdrs.v3.Endpoint`]
        :param target_endpoint: 
        :type target_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        :param net_type: 网络类型
        :type net_type: str
        :param failed_reason: 失败原因。
        :type failed_reason: str
        :param inst_info: 
        :type inst_info: :class:`huaweicloudsdkdrs.v3.InstInfo`
        :param actual_start_time: 实际启动时间，时间戳格式。
        :type actual_start_time: str
        :param full_transfer_complete_time: 全量完成时间，时间戳格式。
        :type full_transfer_complete_time: str
        :param update_time: 更新时间，时间戳格式
        :type update_time: str
        :param job_direction: 任务方向
        :type job_direction: str
        :param db_use_type: 迁移场景 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备
        :type db_use_type: str
        :param need_restart: 是否需要重启
        :type need_restart: bool
        :param is_target_readonly: 指定目标实例是否限制为只读
        :type is_target_readonly: bool
        :param conflict_policy: 冲突忽略策略 - stop：冲突失败 - overwrite：冲突覆盖 - ignore：冲突忽略
        :type conflict_policy: str
        :param filter_ddl_policy: 过滤DDL策略 - drop_database：过滤drop_database - drop_databasefilter_all：过滤所有ddl - \&quot;\&quot;：不过滤
        :type filter_ddl_policy: str
        :param speed_limit: 迁移速度限制。
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v3.SpeedLimitInfo`]
        :param schema_type: 迁移方案 - Replication-主从复制 - Tungsten-日志解析 - PGBaseBackup-PG备份
        :type schema_type: str
        :param node_num: 节点个数。
        :type node_num: str
        :param object_switch: 对象选择开关
        :type object_switch: bool
        :param master_job_id: 主任务Id。
        :type master_job_id: str
        :param full_mode: 全量快照模式。
        :type full_mode: str
        :param struct_trans: 是否迁移结构。
        :type struct_trans: bool
        :param index_trans: 否迁移索引。
        :type index_trans: bool
        :param replace_definer: 是否使用目标库的用户替换掉definer。
        :type replace_definer: bool
        :param migrate_user: 是否迁移用户。
        :type migrate_user: bool
        :param sync_database: 是否库级同步。
        :type sync_database: bool
        :param error_code: 错误码
        :type error_code: str
        :param error_message: 错误信息。
        :type error_message: str
        :param target_root_db: 
        :type target_root_db: :class:`huaweicloudsdkdrs.v3.DefaultRootDb`
        :param az_code: node所在AZ
        :type az_code: str
        :param vpc_id: node所在VPC
        :type vpc_id: str
        :param subnet_id: node所在子网
        :type subnet_id: str
        :param security_group_id: node所在安全组
        :type security_group_id: str
        :param multi_write: 是否多主灾备任务,双主灾备时有值为true
        :type multi_write: bool
        :param support_ip_v6: 是否支持IPV6
        :type support_ip_v6: bool
        :param inherit_id: 继承的任务ID，Oracle_Mrskafka链路时使用。
        :type inherit_id: str
        :param gtid: 断点的GTID集合
        :type gtid: str
        :param alarm_notify: 
        :type alarm_notify: :class:`huaweicloudsdkdrs.v3.QuerySmnInfoResp`
        :param incre_start_position: 增量任务启动位点
        :type incre_start_position: str
        :param is_multi_az: 是否是主备任务。
        :type is_multi_az: bool
        :param az_name: node所在节点AZ名称。
        :type az_name: str
        :param master_az: 主备任务主AZ。
        :type master_az: str
        :param slave_az: 主备任务备AZ。
        :type slave_az: str
        :param node_role: 任务主备角色。
        :type node_role: str
        :param period_order: 
        :type period_order: :class:`huaweicloudsdkdrs.v3.PeriodOrderResp`
        :param object_infos: 已同步对象信息。
        :type object_infos: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectInfo`]
        :param original_job_direction: 初始任务方向。 取值： - up：入云，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。
        :type original_job_direction: str
        :param data_transformation: 
        :type data_transformation: :class:`huaweicloudsdkdrs.v3.GetDataTransformationResp`
        :param tags: DRS任务标签
        :type tags: list[:class:`huaweicloudsdkdrs.v3.Tag`]
        """
        
        

        self._id = None
        self._parent_id = None
        self._name = None
        self._status = None
        self._description = None
        self._create_time = None
        self._task_type = None
        self._source_endpoint = None
        self._dmq_endpoint = None
        self._source_sharding = None
        self._target_endpoint = None
        self._net_type = None
        self._failed_reason = None
        self._inst_info = None
        self._actual_start_time = None
        self._full_transfer_complete_time = None
        self._update_time = None
        self._job_direction = None
        self._db_use_type = None
        self._need_restart = None
        self._is_target_readonly = None
        self._conflict_policy = None
        self._filter_ddl_policy = None
        self._speed_limit = None
        self._schema_type = None
        self._node_num = None
        self._object_switch = None
        self._master_job_id = None
        self._full_mode = None
        self._struct_trans = None
        self._index_trans = None
        self._replace_definer = None
        self._migrate_user = None
        self._sync_database = None
        self._error_code = None
        self._error_message = None
        self._target_root_db = None
        self._az_code = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._multi_write = None
        self._support_ip_v6 = None
        self._inherit_id = None
        self._gtid = None
        self._alarm_notify = None
        self._incre_start_position = None
        self._is_multi_az = None
        self._az_name = None
        self._master_az = None
        self._slave_az = None
        self._node_role = None
        self._period_order = None
        self._object_infos = None
        self._original_job_direction = None
        self._data_transformation = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if task_type is not None:
            self.task_type = task_type
        if source_endpoint is not None:
            self.source_endpoint = source_endpoint
        if dmq_endpoint is not None:
            self.dmq_endpoint = dmq_endpoint
        if source_sharding is not None:
            self.source_sharding = source_sharding
        if target_endpoint is not None:
            self.target_endpoint = target_endpoint
        if net_type is not None:
            self.net_type = net_type
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if inst_info is not None:
            self.inst_info = inst_info
        if actual_start_time is not None:
            self.actual_start_time = actual_start_time
        if full_transfer_complete_time is not None:
            self.full_transfer_complete_time = full_transfer_complete_time
        if update_time is not None:
            self.update_time = update_time
        if job_direction is not None:
            self.job_direction = job_direction
        if db_use_type is not None:
            self.db_use_type = db_use_type
        if need_restart is not None:
            self.need_restart = need_restart
        if is_target_readonly is not None:
            self.is_target_readonly = is_target_readonly
        if conflict_policy is not None:
            self.conflict_policy = conflict_policy
        if filter_ddl_policy is not None:
            self.filter_ddl_policy = filter_ddl_policy
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if schema_type is not None:
            self.schema_type = schema_type
        if node_num is not None:
            self.node_num = node_num
        if object_switch is not None:
            self.object_switch = object_switch
        if master_job_id is not None:
            self.master_job_id = master_job_id
        if full_mode is not None:
            self.full_mode = full_mode
        if struct_trans is not None:
            self.struct_trans = struct_trans
        if index_trans is not None:
            self.index_trans = index_trans
        if replace_definer is not None:
            self.replace_definer = replace_definer
        if migrate_user is not None:
            self.migrate_user = migrate_user
        if sync_database is not None:
            self.sync_database = sync_database
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if target_root_db is not None:
            self.target_root_db = target_root_db
        if az_code is not None:
            self.az_code = az_code
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if multi_write is not None:
            self.multi_write = multi_write
        if support_ip_v6 is not None:
            self.support_ip_v6 = support_ip_v6
        if inherit_id is not None:
            self.inherit_id = inherit_id
        if gtid is not None:
            self.gtid = gtid
        if alarm_notify is not None:
            self.alarm_notify = alarm_notify
        if incre_start_position is not None:
            self.incre_start_position = incre_start_position
        if is_multi_az is not None:
            self.is_multi_az = is_multi_az
        if az_name is not None:
            self.az_name = az_name
        if master_az is not None:
            self.master_az = master_az
        if slave_az is not None:
            self.slave_az = slave_az
        if node_role is not None:
            self.node_role = node_role
        if period_order is not None:
            self.period_order = period_order
        if object_infos is not None:
            self.object_infos = object_infos
        if original_job_direction is not None:
            self.original_job_direction = original_job_direction
        if data_transformation is not None:
            self.data_transformation = data_transformation
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this QueryJobResp.

        任务id

        :return: The id of this QueryJobResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryJobResp.

        任务id

        :param id: The id of this QueryJobResp.
        :type id: str
        """
        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this QueryJobResp.

        父任务id。

        :return: The parent_id of this QueryJobResp.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this QueryJobResp.

        父任务id。

        :param parent_id: The parent_id of this QueryJobResp.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this QueryJobResp.

        任务名称

        :return: The name of this QueryJobResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryJobResp.

        任务名称

        :param name: The name of this QueryJobResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this QueryJobResp.

        任务状态。 - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - PAUSING：已暂停 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - REBUILD_NODE_STARTED：故障恢复中 - REBUILD_NODE_FAILED：故障恢复失败 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - DELETED：已删除 - CHILD_TRANSFER_STARTING：再编辑子任务启动中 - CHILD_TRANSFER_STARTED：再编辑子任务迁移中 - CHILD_TRANSFER_COMPLETE：再编辑子任务迁移完成 - CHILD_TRANSFER_FAILED：再编辑子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：再编辑子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：再编辑子任务已结束 - NODE_UPGRADE_START：升级开始 - NODE_UPGRADE_COMPLETE：升级完成 - NODE_UPGRADE_FAILED：升级失败

        :return: The status of this QueryJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryJobResp.

        任务状态。 - CREATING：创建中 - CREATE_FAILED：创建失败 - CONFIGURATION：配置中 - STARTJOBING：启动中 - WAITING_FOR_START：等待启动中 - START_JOB_FAILED：启动失败 - PAUSING：已暂停 - FULL_TRANSFER_STARTED：全量开始，灾备场景下为初始化 - FULL_TRANSFER_FAILED：全量失败，灾备场景下为初始化失败 - FULL_TRANSFER_COMPLETE：全量完成，灾备场景下为初始化完成 - INCRE_TRANSFER_STARTED：增量开始，灾备场景下为灾备中 - INCRE_TRANSFER_FAILED：增量失败，灾备场景下为灾备异常 - RELEASE_RESOURCE_STARTED：结束任务中 - RELEASE_RESOURCE_FAILED：结束任务失败 - RELEASE_RESOURCE_COMPLETE：已结束 - REBUILD_NODE_STARTED：故障恢复中 - REBUILD_NODE_FAILED：故障恢复失败 - CHANGE_JOB_STARTED：任务变更中 - CHANGE_JOB_FAILED：任务变更失败 - DELETED：已删除 - CHILD_TRANSFER_STARTING：再编辑子任务启动中 - CHILD_TRANSFER_STARTED：再编辑子任务迁移中 - CHILD_TRANSFER_COMPLETE：再编辑子任务迁移完成 - CHILD_TRANSFER_FAILED：再编辑子任务迁移失败 - RELEASE_CHILD_TRANSFER_STARTED：再编辑子任务结束中 - RELEASE_CHILD_TRANSFER_COMPLETE：再编辑子任务已结束 - NODE_UPGRADE_START：升级开始 - NODE_UPGRADE_COMPLETE：升级完成 - NODE_UPGRADE_FAILED：升级失败

        :param status: The status of this QueryJobResp.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this QueryJobResp.

        描述信息

        :return: The description of this QueryJobResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryJobResp.

        描述信息

        :param description: The description of this QueryJobResp.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this QueryJobResp.

        创建时间，时间戳格式。

        :return: The create_time of this QueryJobResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryJobResp.

        创建时间，时间戳格式。

        :param create_time: The create_time of this QueryJobResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def task_type(self):
        """Gets the task_type of this QueryJobResp.

        迁移模式

        :return: The task_type of this QueryJobResp.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this QueryJobResp.

        迁移模式

        :param task_type: The task_type of this QueryJobResp.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def source_endpoint(self):
        """Gets the source_endpoint of this QueryJobResp.

        :return: The source_endpoint of this QueryJobResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """Sets the source_endpoint of this QueryJobResp.

        :param source_endpoint: The source_endpoint of this QueryJobResp.
        :type source_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._source_endpoint = source_endpoint

    @property
    def dmq_endpoint(self):
        """Gets the dmq_endpoint of this QueryJobResp.

        :return: The dmq_endpoint of this QueryJobResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._dmq_endpoint

    @dmq_endpoint.setter
    def dmq_endpoint(self, dmq_endpoint):
        """Sets the dmq_endpoint of this QueryJobResp.

        :param dmq_endpoint: The dmq_endpoint of this QueryJobResp.
        :type dmq_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._dmq_endpoint = dmq_endpoint

    @property
    def source_sharding(self):
        """Gets the source_sharding of this QueryJobResp.

        物理源库信息。

        :return: The source_sharding of this QueryJobResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.Endpoint`]
        """
        return self._source_sharding

    @source_sharding.setter
    def source_sharding(self, source_sharding):
        """Sets the source_sharding of this QueryJobResp.

        物理源库信息。

        :param source_sharding: The source_sharding of this QueryJobResp.
        :type source_sharding: list[:class:`huaweicloudsdkdrs.v3.Endpoint`]
        """
        self._source_sharding = source_sharding

    @property
    def target_endpoint(self):
        """Gets the target_endpoint of this QueryJobResp.

        :return: The target_endpoint of this QueryJobResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        """Sets the target_endpoint of this QueryJobResp.

        :param target_endpoint: The target_endpoint of this QueryJobResp.
        :type target_endpoint: :class:`huaweicloudsdkdrs.v3.Endpoint`
        """
        self._target_endpoint = target_endpoint

    @property
    def net_type(self):
        """Gets the net_type of this QueryJobResp.

        网络类型

        :return: The net_type of this QueryJobResp.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this QueryJobResp.

        网络类型

        :param net_type: The net_type of this QueryJobResp.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def failed_reason(self):
        """Gets the failed_reason of this QueryJobResp.

        失败原因。

        :return: The failed_reason of this QueryJobResp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this QueryJobResp.

        失败原因。

        :param failed_reason: The failed_reason of this QueryJobResp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def inst_info(self):
        """Gets the inst_info of this QueryJobResp.

        :return: The inst_info of this QueryJobResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.InstInfo`
        """
        return self._inst_info

    @inst_info.setter
    def inst_info(self, inst_info):
        """Sets the inst_info of this QueryJobResp.

        :param inst_info: The inst_info of this QueryJobResp.
        :type inst_info: :class:`huaweicloudsdkdrs.v3.InstInfo`
        """
        self._inst_info = inst_info

    @property
    def actual_start_time(self):
        """Gets the actual_start_time of this QueryJobResp.

        实际启动时间，时间戳格式。

        :return: The actual_start_time of this QueryJobResp.
        :rtype: str
        """
        return self._actual_start_time

    @actual_start_time.setter
    def actual_start_time(self, actual_start_time):
        """Sets the actual_start_time of this QueryJobResp.

        实际启动时间，时间戳格式。

        :param actual_start_time: The actual_start_time of this QueryJobResp.
        :type actual_start_time: str
        """
        self._actual_start_time = actual_start_time

    @property
    def full_transfer_complete_time(self):
        """Gets the full_transfer_complete_time of this QueryJobResp.

        全量完成时间，时间戳格式。

        :return: The full_transfer_complete_time of this QueryJobResp.
        :rtype: str
        """
        return self._full_transfer_complete_time

    @full_transfer_complete_time.setter
    def full_transfer_complete_time(self, full_transfer_complete_time):
        """Sets the full_transfer_complete_time of this QueryJobResp.

        全量完成时间，时间戳格式。

        :param full_transfer_complete_time: The full_transfer_complete_time of this QueryJobResp.
        :type full_transfer_complete_time: str
        """
        self._full_transfer_complete_time = full_transfer_complete_time

    @property
    def update_time(self):
        """Gets the update_time of this QueryJobResp.

        更新时间，时间戳格式

        :return: The update_time of this QueryJobResp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this QueryJobResp.

        更新时间，时间戳格式

        :param update_time: The update_time of this QueryJobResp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def job_direction(self):
        """Gets the job_direction of this QueryJobResp.

        任务方向

        :return: The job_direction of this QueryJobResp.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this QueryJobResp.

        任务方向

        :param job_direction: The job_direction of this QueryJobResp.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def db_use_type(self):
        """Gets the db_use_type of this QueryJobResp.

        迁移场景 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备

        :return: The db_use_type of this QueryJobResp.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        """Sets the db_use_type of this QueryJobResp.

        迁移场景 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备

        :param db_use_type: The db_use_type of this QueryJobResp.
        :type db_use_type: str
        """
        self._db_use_type = db_use_type

    @property
    def need_restart(self):
        """Gets the need_restart of this QueryJobResp.

        是否需要重启

        :return: The need_restart of this QueryJobResp.
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        """Sets the need_restart of this QueryJobResp.

        是否需要重启

        :param need_restart: The need_restart of this QueryJobResp.
        :type need_restart: bool
        """
        self._need_restart = need_restart

    @property
    def is_target_readonly(self):
        """Gets the is_target_readonly of this QueryJobResp.

        指定目标实例是否限制为只读

        :return: The is_target_readonly of this QueryJobResp.
        :rtype: bool
        """
        return self._is_target_readonly

    @is_target_readonly.setter
    def is_target_readonly(self, is_target_readonly):
        """Sets the is_target_readonly of this QueryJobResp.

        指定目标实例是否限制为只读

        :param is_target_readonly: The is_target_readonly of this QueryJobResp.
        :type is_target_readonly: bool
        """
        self._is_target_readonly = is_target_readonly

    @property
    def conflict_policy(self):
        """Gets the conflict_policy of this QueryJobResp.

        冲突忽略策略 - stop：冲突失败 - overwrite：冲突覆盖 - ignore：冲突忽略

        :return: The conflict_policy of this QueryJobResp.
        :rtype: str
        """
        return self._conflict_policy

    @conflict_policy.setter
    def conflict_policy(self, conflict_policy):
        """Sets the conflict_policy of this QueryJobResp.

        冲突忽略策略 - stop：冲突失败 - overwrite：冲突覆盖 - ignore：冲突忽略

        :param conflict_policy: The conflict_policy of this QueryJobResp.
        :type conflict_policy: str
        """
        self._conflict_policy = conflict_policy

    @property
    def filter_ddl_policy(self):
        """Gets the filter_ddl_policy of this QueryJobResp.

        过滤DDL策略 - drop_database：过滤drop_database - drop_databasefilter_all：过滤所有ddl - \"\"：不过滤

        :return: The filter_ddl_policy of this QueryJobResp.
        :rtype: str
        """
        return self._filter_ddl_policy

    @filter_ddl_policy.setter
    def filter_ddl_policy(self, filter_ddl_policy):
        """Sets the filter_ddl_policy of this QueryJobResp.

        过滤DDL策略 - drop_database：过滤drop_database - drop_databasefilter_all：过滤所有ddl - \"\"：不过滤

        :param filter_ddl_policy: The filter_ddl_policy of this QueryJobResp.
        :type filter_ddl_policy: str
        """
        self._filter_ddl_policy = filter_ddl_policy

    @property
    def speed_limit(self):
        """Gets the speed_limit of this QueryJobResp.

        迁移速度限制。

        :return: The speed_limit of this QueryJobResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.SpeedLimitInfo`]
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this QueryJobResp.

        迁移速度限制。

        :param speed_limit: The speed_limit of this QueryJobResp.
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v3.SpeedLimitInfo`]
        """
        self._speed_limit = speed_limit

    @property
    def schema_type(self):
        """Gets the schema_type of this QueryJobResp.

        迁移方案 - Replication-主从复制 - Tungsten-日志解析 - PGBaseBackup-PG备份

        :return: The schema_type of this QueryJobResp.
        :rtype: str
        """
        return self._schema_type

    @schema_type.setter
    def schema_type(self, schema_type):
        """Sets the schema_type of this QueryJobResp.

        迁移方案 - Replication-主从复制 - Tungsten-日志解析 - PGBaseBackup-PG备份

        :param schema_type: The schema_type of this QueryJobResp.
        :type schema_type: str
        """
        self._schema_type = schema_type

    @property
    def node_num(self):
        """Gets the node_num of this QueryJobResp.

        节点个数。

        :return: The node_num of this QueryJobResp.
        :rtype: str
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this QueryJobResp.

        节点个数。

        :param node_num: The node_num of this QueryJobResp.
        :type node_num: str
        """
        self._node_num = node_num

    @property
    def object_switch(self):
        """Gets the object_switch of this QueryJobResp.

        对象选择开关

        :return: The object_switch of this QueryJobResp.
        :rtype: bool
        """
        return self._object_switch

    @object_switch.setter
    def object_switch(self, object_switch):
        """Sets the object_switch of this QueryJobResp.

        对象选择开关

        :param object_switch: The object_switch of this QueryJobResp.
        :type object_switch: bool
        """
        self._object_switch = object_switch

    @property
    def master_job_id(self):
        """Gets the master_job_id of this QueryJobResp.

        主任务Id。

        :return: The master_job_id of this QueryJobResp.
        :rtype: str
        """
        return self._master_job_id

    @master_job_id.setter
    def master_job_id(self, master_job_id):
        """Sets the master_job_id of this QueryJobResp.

        主任务Id。

        :param master_job_id: The master_job_id of this QueryJobResp.
        :type master_job_id: str
        """
        self._master_job_id = master_job_id

    @property
    def full_mode(self):
        """Gets the full_mode of this QueryJobResp.

        全量快照模式。

        :return: The full_mode of this QueryJobResp.
        :rtype: str
        """
        return self._full_mode

    @full_mode.setter
    def full_mode(self, full_mode):
        """Sets the full_mode of this QueryJobResp.

        全量快照模式。

        :param full_mode: The full_mode of this QueryJobResp.
        :type full_mode: str
        """
        self._full_mode = full_mode

    @property
    def struct_trans(self):
        """Gets the struct_trans of this QueryJobResp.

        是否迁移结构。

        :return: The struct_trans of this QueryJobResp.
        :rtype: bool
        """
        return self._struct_trans

    @struct_trans.setter
    def struct_trans(self, struct_trans):
        """Sets the struct_trans of this QueryJobResp.

        是否迁移结构。

        :param struct_trans: The struct_trans of this QueryJobResp.
        :type struct_trans: bool
        """
        self._struct_trans = struct_trans

    @property
    def index_trans(self):
        """Gets the index_trans of this QueryJobResp.

        否迁移索引。

        :return: The index_trans of this QueryJobResp.
        :rtype: bool
        """
        return self._index_trans

    @index_trans.setter
    def index_trans(self, index_trans):
        """Sets the index_trans of this QueryJobResp.

        否迁移索引。

        :param index_trans: The index_trans of this QueryJobResp.
        :type index_trans: bool
        """
        self._index_trans = index_trans

    @property
    def replace_definer(self):
        """Gets the replace_definer of this QueryJobResp.

        是否使用目标库的用户替换掉definer。

        :return: The replace_definer of this QueryJobResp.
        :rtype: bool
        """
        return self._replace_definer

    @replace_definer.setter
    def replace_definer(self, replace_definer):
        """Sets the replace_definer of this QueryJobResp.

        是否使用目标库的用户替换掉definer。

        :param replace_definer: The replace_definer of this QueryJobResp.
        :type replace_definer: bool
        """
        self._replace_definer = replace_definer

    @property
    def migrate_user(self):
        """Gets the migrate_user of this QueryJobResp.

        是否迁移用户。

        :return: The migrate_user of this QueryJobResp.
        :rtype: bool
        """
        return self._migrate_user

    @migrate_user.setter
    def migrate_user(self, migrate_user):
        """Sets the migrate_user of this QueryJobResp.

        是否迁移用户。

        :param migrate_user: The migrate_user of this QueryJobResp.
        :type migrate_user: bool
        """
        self._migrate_user = migrate_user

    @property
    def sync_database(self):
        """Gets the sync_database of this QueryJobResp.

        是否库级同步。

        :return: The sync_database of this QueryJobResp.
        :rtype: bool
        """
        return self._sync_database

    @sync_database.setter
    def sync_database(self, sync_database):
        """Sets the sync_database of this QueryJobResp.

        是否库级同步。

        :param sync_database: The sync_database of this QueryJobResp.
        :type sync_database: bool
        """
        self._sync_database = sync_database

    @property
    def error_code(self):
        """Gets the error_code of this QueryJobResp.

        错误码

        :return: The error_code of this QueryJobResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QueryJobResp.

        错误码

        :param error_code: The error_code of this QueryJobResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this QueryJobResp.

        错误信息。

        :return: The error_message of this QueryJobResp.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this QueryJobResp.

        错误信息。

        :param error_message: The error_message of this QueryJobResp.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def target_root_db(self):
        """Gets the target_root_db of this QueryJobResp.

        :return: The target_root_db of this QueryJobResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.DefaultRootDb`
        """
        return self._target_root_db

    @target_root_db.setter
    def target_root_db(self, target_root_db):
        """Sets the target_root_db of this QueryJobResp.

        :param target_root_db: The target_root_db of this QueryJobResp.
        :type target_root_db: :class:`huaweicloudsdkdrs.v3.DefaultRootDb`
        """
        self._target_root_db = target_root_db

    @property
    def az_code(self):
        """Gets the az_code of this QueryJobResp.

        node所在AZ

        :return: The az_code of this QueryJobResp.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this QueryJobResp.

        node所在AZ

        :param az_code: The az_code of this QueryJobResp.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def vpc_id(self):
        """Gets the vpc_id of this QueryJobResp.

        node所在VPC

        :return: The vpc_id of this QueryJobResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this QueryJobResp.

        node所在VPC

        :param vpc_id: The vpc_id of this QueryJobResp.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this QueryJobResp.

        node所在子网

        :return: The subnet_id of this QueryJobResp.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this QueryJobResp.

        node所在子网

        :param subnet_id: The subnet_id of this QueryJobResp.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this QueryJobResp.

        node所在安全组

        :return: The security_group_id of this QueryJobResp.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this QueryJobResp.

        node所在安全组

        :param security_group_id: The security_group_id of this QueryJobResp.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def multi_write(self):
        """Gets the multi_write of this QueryJobResp.

        是否多主灾备任务,双主灾备时有值为true

        :return: The multi_write of this QueryJobResp.
        :rtype: bool
        """
        return self._multi_write

    @multi_write.setter
    def multi_write(self, multi_write):
        """Sets the multi_write of this QueryJobResp.

        是否多主灾备任务,双主灾备时有值为true

        :param multi_write: The multi_write of this QueryJobResp.
        :type multi_write: bool
        """
        self._multi_write = multi_write

    @property
    def support_ip_v6(self):
        """Gets the support_ip_v6 of this QueryJobResp.

        是否支持IPV6

        :return: The support_ip_v6 of this QueryJobResp.
        :rtype: bool
        """
        return self._support_ip_v6

    @support_ip_v6.setter
    def support_ip_v6(self, support_ip_v6):
        """Sets the support_ip_v6 of this QueryJobResp.

        是否支持IPV6

        :param support_ip_v6: The support_ip_v6 of this QueryJobResp.
        :type support_ip_v6: bool
        """
        self._support_ip_v6 = support_ip_v6

    @property
    def inherit_id(self):
        """Gets the inherit_id of this QueryJobResp.

        继承的任务ID，Oracle_Mrskafka链路时使用。

        :return: The inherit_id of this QueryJobResp.
        :rtype: str
        """
        return self._inherit_id

    @inherit_id.setter
    def inherit_id(self, inherit_id):
        """Sets the inherit_id of this QueryJobResp.

        继承的任务ID，Oracle_Mrskafka链路时使用。

        :param inherit_id: The inherit_id of this QueryJobResp.
        :type inherit_id: str
        """
        self._inherit_id = inherit_id

    @property
    def gtid(self):
        """Gets the gtid of this QueryJobResp.

        断点的GTID集合

        :return: The gtid of this QueryJobResp.
        :rtype: str
        """
        return self._gtid

    @gtid.setter
    def gtid(self, gtid):
        """Sets the gtid of this QueryJobResp.

        断点的GTID集合

        :param gtid: The gtid of this QueryJobResp.
        :type gtid: str
        """
        self._gtid = gtid

    @property
    def alarm_notify(self):
        """Gets the alarm_notify of this QueryJobResp.

        :return: The alarm_notify of this QueryJobResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.QuerySmnInfoResp`
        """
        return self._alarm_notify

    @alarm_notify.setter
    def alarm_notify(self, alarm_notify):
        """Sets the alarm_notify of this QueryJobResp.

        :param alarm_notify: The alarm_notify of this QueryJobResp.
        :type alarm_notify: :class:`huaweicloudsdkdrs.v3.QuerySmnInfoResp`
        """
        self._alarm_notify = alarm_notify

    @property
    def incre_start_position(self):
        """Gets the incre_start_position of this QueryJobResp.

        增量任务启动位点

        :return: The incre_start_position of this QueryJobResp.
        :rtype: str
        """
        return self._incre_start_position

    @incre_start_position.setter
    def incre_start_position(self, incre_start_position):
        """Sets the incre_start_position of this QueryJobResp.

        增量任务启动位点

        :param incre_start_position: The incre_start_position of this QueryJobResp.
        :type incre_start_position: str
        """
        self._incre_start_position = incre_start_position

    @property
    def is_multi_az(self):
        """Gets the is_multi_az of this QueryJobResp.

        是否是主备任务。

        :return: The is_multi_az of this QueryJobResp.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        """Sets the is_multi_az of this QueryJobResp.

        是否是主备任务。

        :param is_multi_az: The is_multi_az of this QueryJobResp.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

    @property
    def az_name(self):
        """Gets the az_name of this QueryJobResp.

        node所在节点AZ名称。

        :return: The az_name of this QueryJobResp.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        """Sets the az_name of this QueryJobResp.

        node所在节点AZ名称。

        :param az_name: The az_name of this QueryJobResp.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def master_az(self):
        """Gets the master_az of this QueryJobResp.

        主备任务主AZ。

        :return: The master_az of this QueryJobResp.
        :rtype: str
        """
        return self._master_az

    @master_az.setter
    def master_az(self, master_az):
        """Sets the master_az of this QueryJobResp.

        主备任务主AZ。

        :param master_az: The master_az of this QueryJobResp.
        :type master_az: str
        """
        self._master_az = master_az

    @property
    def slave_az(self):
        """Gets the slave_az of this QueryJobResp.

        主备任务备AZ。

        :return: The slave_az of this QueryJobResp.
        :rtype: str
        """
        return self._slave_az

    @slave_az.setter
    def slave_az(self, slave_az):
        """Sets the slave_az of this QueryJobResp.

        主备任务备AZ。

        :param slave_az: The slave_az of this QueryJobResp.
        :type slave_az: str
        """
        self._slave_az = slave_az

    @property
    def node_role(self):
        """Gets the node_role of this QueryJobResp.

        任务主备角色。

        :return: The node_role of this QueryJobResp.
        :rtype: str
        """
        return self._node_role

    @node_role.setter
    def node_role(self, node_role):
        """Sets the node_role of this QueryJobResp.

        任务主备角色。

        :param node_role: The node_role of this QueryJobResp.
        :type node_role: str
        """
        self._node_role = node_role

    @property
    def period_order(self):
        """Gets the period_order of this QueryJobResp.

        :return: The period_order of this QueryJobResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.PeriodOrderResp`
        """
        return self._period_order

    @period_order.setter
    def period_order(self, period_order):
        """Sets the period_order of this QueryJobResp.

        :param period_order: The period_order of this QueryJobResp.
        :type period_order: :class:`huaweicloudsdkdrs.v3.PeriodOrderResp`
        """
        self._period_order = period_order

    @property
    def object_infos(self):
        """Gets the object_infos of this QueryJobResp.

        已同步对象信息。

        :return: The object_infos of this QueryJobResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectInfo`]
        """
        return self._object_infos

    @object_infos.setter
    def object_infos(self, object_infos):
        """Sets the object_infos of this QueryJobResp.

        已同步对象信息。

        :param object_infos: The object_infos of this QueryJobResp.
        :type object_infos: list[:class:`huaweicloudsdkdrs.v3.DatabaseObjectInfo`]
        """
        self._object_infos = object_infos

    @property
    def original_job_direction(self):
        """Gets the original_job_direction of this QueryJobResp.

        初始任务方向。 取值： - up：入云，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。

        :return: The original_job_direction of this QueryJobResp.
        :rtype: str
        """
        return self._original_job_direction

    @original_job_direction.setter
    def original_job_direction(self, original_job_direction):
        """Sets the original_job_direction of this QueryJobResp.

        初始任务方向。 取值： - up：入云，灾备场景时对应本云为备。 - down：出云，灾备场景时对应本云为主。 - non-dbs：自建。

        :param original_job_direction: The original_job_direction of this QueryJobResp.
        :type original_job_direction: str
        """
        self._original_job_direction = original_job_direction

    @property
    def data_transformation(self):
        """Gets the data_transformation of this QueryJobResp.

        :return: The data_transformation of this QueryJobResp.
        :rtype: :class:`huaweicloudsdkdrs.v3.GetDataTransformationResp`
        """
        return self._data_transformation

    @data_transformation.setter
    def data_transformation(self, data_transformation):
        """Sets the data_transformation of this QueryJobResp.

        :param data_transformation: The data_transformation of this QueryJobResp.
        :type data_transformation: :class:`huaweicloudsdkdrs.v3.GetDataTransformationResp`
        """
        self._data_transformation = data_transformation

    @property
    def tags(self):
        """Gets the tags of this QueryJobResp.

        DRS任务标签

        :return: The tags of this QueryJobResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueryJobResp.

        DRS任务标签

        :param tags: The tags of this QueryJobResp.
        :type tags: list[:class:`huaweicloudsdkdrs.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, QueryJobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
