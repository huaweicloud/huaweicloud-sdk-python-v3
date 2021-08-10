# coding: utf-8

import re
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
        'alarm_notify': 'str',
        'incre_start_position': 'str'
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
        'incre_start_position': 'incre_start_position'
    }

    def __init__(self, id=None, parent_id=None, name=None, status=None, description=None, create_time=None, task_type=None, source_endpoint=None, dmq_endpoint=None, source_sharding=None, target_endpoint=None, net_type=None, failed_reason=None, inst_info=None, actual_start_time=None, full_transfer_complete_time=None, update_time=None, job_direction=None, db_use_type=None, need_restart=None, is_target_readonly=None, conflict_policy=None, filter_ddl_policy=None, speed_limit=None, schema_type=None, node_num=None, object_switch=None, master_job_id=None, full_mode=None, struct_trans=None, index_trans=None, replace_definer=None, migrate_user=None, sync_database=None, error_code=None, error_message=None, target_root_db=None, az_code=None, vpc_id=None, subnet_id=None, security_group_id=None, multi_write=None, support_ip_v6=None, inherit_id=None, gtid=None, alarm_notify=None, incre_start_position=None):
        """QueryJobResp - a model defined in huaweicloud sdk"""
        
        

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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this QueryJobResp.

        任务状态

        :return: The status of this QueryJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryJobResp.

        任务状态

        :param status: The status of this QueryJobResp.
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._task_type = task_type

    @property
    def source_endpoint(self):
        """Gets the source_endpoint of this QueryJobResp.


        :return: The source_endpoint of this QueryJobResp.
        :rtype: Endpoint
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """Sets the source_endpoint of this QueryJobResp.


        :param source_endpoint: The source_endpoint of this QueryJobResp.
        :type: Endpoint
        """
        self._source_endpoint = source_endpoint

    @property
    def dmq_endpoint(self):
        """Gets the dmq_endpoint of this QueryJobResp.


        :return: The dmq_endpoint of this QueryJobResp.
        :rtype: Endpoint
        """
        return self._dmq_endpoint

    @dmq_endpoint.setter
    def dmq_endpoint(self, dmq_endpoint):
        """Sets the dmq_endpoint of this QueryJobResp.


        :param dmq_endpoint: The dmq_endpoint of this QueryJobResp.
        :type: Endpoint
        """
        self._dmq_endpoint = dmq_endpoint

    @property
    def source_sharding(self):
        """Gets the source_sharding of this QueryJobResp.

        物理源库信息。

        :return: The source_sharding of this QueryJobResp.
        :rtype: list[Endpoint]
        """
        return self._source_sharding

    @source_sharding.setter
    def source_sharding(self, source_sharding):
        """Sets the source_sharding of this QueryJobResp.

        物理源库信息。

        :param source_sharding: The source_sharding of this QueryJobResp.
        :type: list[Endpoint]
        """
        self._source_sharding = source_sharding

    @property
    def target_endpoint(self):
        """Gets the target_endpoint of this QueryJobResp.


        :return: The target_endpoint of this QueryJobResp.
        :rtype: Endpoint
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        """Sets the target_endpoint of this QueryJobResp.


        :param target_endpoint: The target_endpoint of this QueryJobResp.
        :type: Endpoint
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
        :type: str
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
        :type: str
        """
        self._failed_reason = failed_reason

    @property
    def inst_info(self):
        """Gets the inst_info of this QueryJobResp.


        :return: The inst_info of this QueryJobResp.
        :rtype: InstInfo
        """
        return self._inst_info

    @inst_info.setter
    def inst_info(self, inst_info):
        """Sets the inst_info of this QueryJobResp.


        :param inst_info: The inst_info of this QueryJobResp.
        :type: InstInfo
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: bool
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
        :type: bool
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
        :type: str
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
        :type: str
        """
        self._filter_ddl_policy = filter_ddl_policy

    @property
    def speed_limit(self):
        """Gets the speed_limit of this QueryJobResp.

        迁移速度限制。

        :return: The speed_limit of this QueryJobResp.
        :rtype: list[SpeedLimitInfo]
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this QueryJobResp.

        迁移速度限制。

        :param speed_limit: The speed_limit of this QueryJobResp.
        :type: list[SpeedLimitInfo]
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
        :type: str
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
        :type: str
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
        :type: bool
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
        :type: str
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
        :type: str
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
        :type: bool
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
        :type: bool
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
        :type: bool
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
        :type: bool
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
        :type: bool
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
        :type: str
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
        :type: str
        """
        self._error_message = error_message

    @property
    def target_root_db(self):
        """Gets the target_root_db of this QueryJobResp.


        :return: The target_root_db of this QueryJobResp.
        :rtype: DefaultRootDb
        """
        return self._target_root_db

    @target_root_db.setter
    def target_root_db(self, target_root_db):
        """Sets the target_root_db of this QueryJobResp.


        :param target_root_db: The target_root_db of this QueryJobResp.
        :type: DefaultRootDb
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: bool
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
        :type: bool
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
        :type: str
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
        :type: str
        """
        self._gtid = gtid

    @property
    def alarm_notify(self):
        """Gets the alarm_notify of this QueryJobResp.

        获取异常通知设置信息。

        :return: The alarm_notify of this QueryJobResp.
        :rtype: str
        """
        return self._alarm_notify

    @alarm_notify.setter
    def alarm_notify(self, alarm_notify):
        """Sets the alarm_notify of this QueryJobResp.

        获取异常通知设置信息。

        :param alarm_notify: The alarm_notify of this QueryJobResp.
        :type: str
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
        :type: str
        """
        self._incre_start_position = incre_start_position

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
