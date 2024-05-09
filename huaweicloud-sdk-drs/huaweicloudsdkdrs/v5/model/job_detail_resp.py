# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobDetailResp:

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
        'status': 'str',
        'create_time': 'str',
        'total_count': 'int',
        'master_job_id': 'str',
        'base_info': 'JobBaseInfo',
        'source_endpoint': 'list[JobEndpointInfo]',
        'target_endpoint': 'list[JobEndpointInfo]',
        'alarm_notify': 'AlarmNotifyConfig',
        'speed_limit': 'list[SpeedLimitInfo]',
        'user_migration': 'UserMigrationInfo',
        'policy_config': 'PolicyConfig',
        'db_param': 'DbParamInfo',
        'tuning_params': 'TuningParamInfo',
        'period_order': 'PeriodOrderInfo',
        'node_info': 'JobNodeInfo',
        'logs': 'list[TaskLogInfo]',
        'network_results': 'list[QueryNetworkResult]',
        'precheck_result': 'QueryPreCheckResult',
        'progress_info': 'JobProgressInfo',
        'migration_object_progress_info': 'QueryMigrationObjectProgressInfo',
        'metrics': 'QueryMetricResult',
        'compare_result': 'CompareResultInfo',
        'support_import_file_resp': 'SupportImportFileResult',
        'instance_features': 'dict(str, str)',
        'task_version': 'str',
        'connection_management': 'ConnectionManagement',
        'public_ip_list': 'list[PublicIpConfig]',
        'bind_public_ip_state': 'str',
        'children': 'list[FailedToBindEipChildInfo]',
        'is_writable': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'create_time': 'create_time',
        'total_count': 'total_count',
        'master_job_id': 'master_job_id',
        'base_info': 'base_info',
        'source_endpoint': 'source_endpoint',
        'target_endpoint': 'target_endpoint',
        'alarm_notify': 'alarm_notify',
        'speed_limit': 'speed_limit',
        'user_migration': 'user_migration',
        'policy_config': 'policy_config',
        'db_param': 'db_param',
        'tuning_params': 'tuning_params',
        'period_order': 'period_order',
        'node_info': 'node_info',
        'logs': 'logs',
        'network_results': 'network_results',
        'precheck_result': 'precheck_result',
        'progress_info': 'progress_info',
        'migration_object_progress_info': 'migration_object_progress_info',
        'metrics': 'metrics',
        'compare_result': 'compare_result',
        'support_import_file_resp': 'support_import_file_resp',
        'instance_features': 'instance_features',
        'task_version': 'task_version',
        'connection_management': 'connection_management',
        'public_ip_list': 'public_ip_list',
        'bind_public_ip_state': 'bind_public_ip_state',
        'children': 'children',
        'is_writable': 'is_writable'
    }

    def __init__(self, id=None, status=None, create_time=None, total_count=None, master_job_id=None, base_info=None, source_endpoint=None, target_endpoint=None, alarm_notify=None, speed_limit=None, user_migration=None, policy_config=None, db_param=None, tuning_params=None, period_order=None, node_info=None, logs=None, network_results=None, precheck_result=None, progress_info=None, migration_object_progress_info=None, metrics=None, compare_result=None, support_import_file_resp=None, instance_features=None, task_version=None, connection_management=None, public_ip_list=None, bind_public_ip_state=None, children=None, is_writable=None):
        """JobDetailResp

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param status: 任务状态。
        :type status: str
        :param create_time: 任务创建时间。
        :type create_time: str
        :param total_count: 列表中的项目总数，与分页无关。
        :type total_count: int
        :param master_job_id: 多任务主节点的任务ID。
        :type master_job_id: str
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        :param source_endpoint: 任务源数据库信息体。
        :type source_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        :param target_endpoint: 任务目标数据库信息体。
        :type target_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        :param alarm_notify: 
        :type alarm_notify: :class:`huaweicloudsdkdrs.v5.AlarmNotifyConfig`
        :param speed_limit: 限速信息体。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。  - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v5.SpeedLimitInfo`]
        :param user_migration: 
        :type user_migration: :class:`huaweicloudsdkdrs.v5.UserMigrationInfo`
        :param policy_config: 
        :type policy_config: :class:`huaweicloudsdkdrs.v5.PolicyConfig`
        :param db_param: 
        :type db_param: :class:`huaweicloudsdkdrs.v5.DbParamInfo`
        :param tuning_params: 
        :type tuning_params: :class:`huaweicloudsdkdrs.v5.TuningParamInfo`
        :param period_order: 
        :type period_order: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        :param node_info: 
        :type node_info: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        :param logs: 日志查询结果信息体。
        :type logs: list[:class:`huaweicloudsdkdrs.v5.TaskLogInfo`]
        :param network_results: 网络打通测试结果信息体。
        :type network_results: list[:class:`huaweicloudsdkdrs.v5.QueryNetworkResult`]
        :param precheck_result: 
        :type precheck_result: :class:`huaweicloudsdkdrs.v5.QueryPreCheckResult`
        :param progress_info: 
        :type progress_info: :class:`huaweicloudsdkdrs.v5.JobProgressInfo`
        :param migration_object_progress_info: 
        :type migration_object_progress_info: :class:`huaweicloudsdkdrs.v5.QueryMigrationObjectProgressInfo`
        :param metrics: 
        :type metrics: :class:`huaweicloudsdkdrs.v5.QueryMetricResult`
        :param compare_result: 
        :type compare_result: :class:`huaweicloudsdkdrs.v5.CompareResultInfo`
        :param support_import_file_resp: 
        :type support_import_file_resp: :class:`huaweicloudsdkdrs.v5.SupportImportFileResult`
        :param instance_features: 由开关和版本共同控制的任务级别的功能列表。
        :type instance_features: dict(str, str)
        :param task_version: 任务版本。
        :type task_version: str
        :param connection_management: 
        :type connection_management: :class:`huaweicloudsdkdrs.v5.ConnectionManagement`
        :param public_ip_list: 指定公网IP的信息
        :type public_ip_list: list[:class:`huaweicloudsdkdrs.v5.PublicIpConfig`]
        :param bind_public_ip_state: 是否成功绑定公网IP
        :type bind_public_ip_state: str
        :param children: 多任务时，存在子任务绑定失败时，返回子任务的信息
        :type children: list[:class:`huaweicloudsdkdrs.v5.FailedToBindEipChildInfo`]
        :param is_writable: 解除目标库只读操作后，目标库解除只读是否成功。 - pending：目标库解除操作进行中。 - success：目标库解除只读操作成功。
        :type is_writable: str
        """
        
        

        self._id = None
        self._status = None
        self._create_time = None
        self._total_count = None
        self._master_job_id = None
        self._base_info = None
        self._source_endpoint = None
        self._target_endpoint = None
        self._alarm_notify = None
        self._speed_limit = None
        self._user_migration = None
        self._policy_config = None
        self._db_param = None
        self._tuning_params = None
        self._period_order = None
        self._node_info = None
        self._logs = None
        self._network_results = None
        self._precheck_result = None
        self._progress_info = None
        self._migration_object_progress_info = None
        self._metrics = None
        self._compare_result = None
        self._support_import_file_resp = None
        self._instance_features = None
        self._task_version = None
        self._connection_management = None
        self._public_ip_list = None
        self._bind_public_ip_state = None
        self._children = None
        self._is_writable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if total_count is not None:
            self.total_count = total_count
        if master_job_id is not None:
            self.master_job_id = master_job_id
        if base_info is not None:
            self.base_info = base_info
        if source_endpoint is not None:
            self.source_endpoint = source_endpoint
        if target_endpoint is not None:
            self.target_endpoint = target_endpoint
        if alarm_notify is not None:
            self.alarm_notify = alarm_notify
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if user_migration is not None:
            self.user_migration = user_migration
        if policy_config is not None:
            self.policy_config = policy_config
        if db_param is not None:
            self.db_param = db_param
        if tuning_params is not None:
            self.tuning_params = tuning_params
        if period_order is not None:
            self.period_order = period_order
        if node_info is not None:
            self.node_info = node_info
        if logs is not None:
            self.logs = logs
        if network_results is not None:
            self.network_results = network_results
        if precheck_result is not None:
            self.precheck_result = precheck_result
        if progress_info is not None:
            self.progress_info = progress_info
        if migration_object_progress_info is not None:
            self.migration_object_progress_info = migration_object_progress_info
        if metrics is not None:
            self.metrics = metrics
        if compare_result is not None:
            self.compare_result = compare_result
        if support_import_file_resp is not None:
            self.support_import_file_resp = support_import_file_resp
        if instance_features is not None:
            self.instance_features = instance_features
        if task_version is not None:
            self.task_version = task_version
        if connection_management is not None:
            self.connection_management = connection_management
        if public_ip_list is not None:
            self.public_ip_list = public_ip_list
        if bind_public_ip_state is not None:
            self.bind_public_ip_state = bind_public_ip_state
        if children is not None:
            self.children = children
        if is_writable is not None:
            self.is_writable = is_writable

    @property
    def id(self):
        """Gets the id of this JobDetailResp.

        任务ID。

        :return: The id of this JobDetailResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobDetailResp.

        任务ID。

        :param id: The id of this JobDetailResp.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this JobDetailResp.

        任务状态。

        :return: The status of this JobDetailResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobDetailResp.

        任务状态。

        :param status: The status of this JobDetailResp.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this JobDetailResp.

        任务创建时间。

        :return: The create_time of this JobDetailResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this JobDetailResp.

        任务创建时间。

        :param create_time: The create_time of this JobDetailResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def total_count(self):
        """Gets the total_count of this JobDetailResp.

        列表中的项目总数，与分页无关。

        :return: The total_count of this JobDetailResp.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this JobDetailResp.

        列表中的项目总数，与分页无关。

        :param total_count: The total_count of this JobDetailResp.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def master_job_id(self):
        """Gets the master_job_id of this JobDetailResp.

        多任务主节点的任务ID。

        :return: The master_job_id of this JobDetailResp.
        :rtype: str
        """
        return self._master_job_id

    @master_job_id.setter
    def master_job_id(self, master_job_id):
        """Sets the master_job_id of this JobDetailResp.

        多任务主节点的任务ID。

        :param master_job_id: The master_job_id of this JobDetailResp.
        :type master_job_id: str
        """
        self._master_job_id = master_job_id

    @property
    def base_info(self):
        """Gets the base_info of this JobDetailResp.

        :return: The base_info of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        """Sets the base_info of this JobDetailResp.

        :param base_info: The base_info of this JobDetailResp.
        :type base_info: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        """
        self._base_info = base_info

    @property
    def source_endpoint(self):
        """Gets the source_endpoint of this JobDetailResp.

        任务源数据库信息体。

        :return: The source_endpoint of this JobDetailResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """Sets the source_endpoint of this JobDetailResp.

        任务源数据库信息体。

        :param source_endpoint: The source_endpoint of this JobDetailResp.
        :type source_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._source_endpoint = source_endpoint

    @property
    def target_endpoint(self):
        """Gets the target_endpoint of this JobDetailResp.

        任务目标数据库信息体。

        :return: The target_endpoint of this JobDetailResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        """Sets the target_endpoint of this JobDetailResp.

        任务目标数据库信息体。

        :param target_endpoint: The target_endpoint of this JobDetailResp.
        :type target_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._target_endpoint = target_endpoint

    @property
    def alarm_notify(self):
        """Gets the alarm_notify of this JobDetailResp.

        :return: The alarm_notify of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.AlarmNotifyConfig`
        """
        return self._alarm_notify

    @alarm_notify.setter
    def alarm_notify(self, alarm_notify):
        """Sets the alarm_notify of this JobDetailResp.

        :param alarm_notify: The alarm_notify of this JobDetailResp.
        :type alarm_notify: :class:`huaweicloudsdkdrs.v5.AlarmNotifyConfig`
        """
        self._alarm_notify = alarm_notify

    @property
    def speed_limit(self):
        """Gets the speed_limit of this JobDetailResp.

        限速信息体。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。  - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。

        :return: The speed_limit of this JobDetailResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.SpeedLimitInfo`]
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this JobDetailResp.

        限速信息体。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。  - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。

        :param speed_limit: The speed_limit of this JobDetailResp.
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v5.SpeedLimitInfo`]
        """
        self._speed_limit = speed_limit

    @property
    def user_migration(self):
        """Gets the user_migration of this JobDetailResp.

        :return: The user_migration of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.UserMigrationInfo`
        """
        return self._user_migration

    @user_migration.setter
    def user_migration(self, user_migration):
        """Sets the user_migration of this JobDetailResp.

        :param user_migration: The user_migration of this JobDetailResp.
        :type user_migration: :class:`huaweicloudsdkdrs.v5.UserMigrationInfo`
        """
        self._user_migration = user_migration

    @property
    def policy_config(self):
        """Gets the policy_config of this JobDetailResp.

        :return: The policy_config of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.PolicyConfig`
        """
        return self._policy_config

    @policy_config.setter
    def policy_config(self, policy_config):
        """Sets the policy_config of this JobDetailResp.

        :param policy_config: The policy_config of this JobDetailResp.
        :type policy_config: :class:`huaweicloudsdkdrs.v5.PolicyConfig`
        """
        self._policy_config = policy_config

    @property
    def db_param(self):
        """Gets the db_param of this JobDetailResp.

        :return: The db_param of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.DbParamInfo`
        """
        return self._db_param

    @db_param.setter
    def db_param(self, db_param):
        """Sets the db_param of this JobDetailResp.

        :param db_param: The db_param of this JobDetailResp.
        :type db_param: :class:`huaweicloudsdkdrs.v5.DbParamInfo`
        """
        self._db_param = db_param

    @property
    def tuning_params(self):
        """Gets the tuning_params of this JobDetailResp.

        :return: The tuning_params of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.TuningParamInfo`
        """
        return self._tuning_params

    @tuning_params.setter
    def tuning_params(self, tuning_params):
        """Sets the tuning_params of this JobDetailResp.

        :param tuning_params: The tuning_params of this JobDetailResp.
        :type tuning_params: :class:`huaweicloudsdkdrs.v5.TuningParamInfo`
        """
        self._tuning_params = tuning_params

    @property
    def period_order(self):
        """Gets the period_order of this JobDetailResp.

        :return: The period_order of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        """
        return self._period_order

    @period_order.setter
    def period_order(self, period_order):
        """Sets the period_order of this JobDetailResp.

        :param period_order: The period_order of this JobDetailResp.
        :type period_order: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        """
        self._period_order = period_order

    @property
    def node_info(self):
        """Gets the node_info of this JobDetailResp.

        :return: The node_info of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """Sets the node_info of this JobDetailResp.

        :param node_info: The node_info of this JobDetailResp.
        :type node_info: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        self._node_info = node_info

    @property
    def logs(self):
        """Gets the logs of this JobDetailResp.

        日志查询结果信息体。

        :return: The logs of this JobDetailResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.TaskLogInfo`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this JobDetailResp.

        日志查询结果信息体。

        :param logs: The logs of this JobDetailResp.
        :type logs: list[:class:`huaweicloudsdkdrs.v5.TaskLogInfo`]
        """
        self._logs = logs

    @property
    def network_results(self):
        """Gets the network_results of this JobDetailResp.

        网络打通测试结果信息体。

        :return: The network_results of this JobDetailResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.QueryNetworkResult`]
        """
        return self._network_results

    @network_results.setter
    def network_results(self, network_results):
        """Sets the network_results of this JobDetailResp.

        网络打通测试结果信息体。

        :param network_results: The network_results of this JobDetailResp.
        :type network_results: list[:class:`huaweicloudsdkdrs.v5.QueryNetworkResult`]
        """
        self._network_results = network_results

    @property
    def precheck_result(self):
        """Gets the precheck_result of this JobDetailResp.

        :return: The precheck_result of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.QueryPreCheckResult`
        """
        return self._precheck_result

    @precheck_result.setter
    def precheck_result(self, precheck_result):
        """Sets the precheck_result of this JobDetailResp.

        :param precheck_result: The precheck_result of this JobDetailResp.
        :type precheck_result: :class:`huaweicloudsdkdrs.v5.QueryPreCheckResult`
        """
        self._precheck_result = precheck_result

    @property
    def progress_info(self):
        """Gets the progress_info of this JobDetailResp.

        :return: The progress_info of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobProgressInfo`
        """
        return self._progress_info

    @progress_info.setter
    def progress_info(self, progress_info):
        """Sets the progress_info of this JobDetailResp.

        :param progress_info: The progress_info of this JobDetailResp.
        :type progress_info: :class:`huaweicloudsdkdrs.v5.JobProgressInfo`
        """
        self._progress_info = progress_info

    @property
    def migration_object_progress_info(self):
        """Gets the migration_object_progress_info of this JobDetailResp.

        :return: The migration_object_progress_info of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.QueryMigrationObjectProgressInfo`
        """
        return self._migration_object_progress_info

    @migration_object_progress_info.setter
    def migration_object_progress_info(self, migration_object_progress_info):
        """Sets the migration_object_progress_info of this JobDetailResp.

        :param migration_object_progress_info: The migration_object_progress_info of this JobDetailResp.
        :type migration_object_progress_info: :class:`huaweicloudsdkdrs.v5.QueryMigrationObjectProgressInfo`
        """
        self._migration_object_progress_info = migration_object_progress_info

    @property
    def metrics(self):
        """Gets the metrics of this JobDetailResp.

        :return: The metrics of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.QueryMetricResult`
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this JobDetailResp.

        :param metrics: The metrics of this JobDetailResp.
        :type metrics: :class:`huaweicloudsdkdrs.v5.QueryMetricResult`
        """
        self._metrics = metrics

    @property
    def compare_result(self):
        """Gets the compare_result of this JobDetailResp.

        :return: The compare_result of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.CompareResultInfo`
        """
        return self._compare_result

    @compare_result.setter
    def compare_result(self, compare_result):
        """Sets the compare_result of this JobDetailResp.

        :param compare_result: The compare_result of this JobDetailResp.
        :type compare_result: :class:`huaweicloudsdkdrs.v5.CompareResultInfo`
        """
        self._compare_result = compare_result

    @property
    def support_import_file_resp(self):
        """Gets the support_import_file_resp of this JobDetailResp.

        :return: The support_import_file_resp of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.SupportImportFileResult`
        """
        return self._support_import_file_resp

    @support_import_file_resp.setter
    def support_import_file_resp(self, support_import_file_resp):
        """Sets the support_import_file_resp of this JobDetailResp.

        :param support_import_file_resp: The support_import_file_resp of this JobDetailResp.
        :type support_import_file_resp: :class:`huaweicloudsdkdrs.v5.SupportImportFileResult`
        """
        self._support_import_file_resp = support_import_file_resp

    @property
    def instance_features(self):
        """Gets the instance_features of this JobDetailResp.

        由开关和版本共同控制的任务级别的功能列表。

        :return: The instance_features of this JobDetailResp.
        :rtype: dict(str, str)
        """
        return self._instance_features

    @instance_features.setter
    def instance_features(self, instance_features):
        """Sets the instance_features of this JobDetailResp.

        由开关和版本共同控制的任务级别的功能列表。

        :param instance_features: The instance_features of this JobDetailResp.
        :type instance_features: dict(str, str)
        """
        self._instance_features = instance_features

    @property
    def task_version(self):
        """Gets the task_version of this JobDetailResp.

        任务版本。

        :return: The task_version of this JobDetailResp.
        :rtype: str
        """
        return self._task_version

    @task_version.setter
    def task_version(self, task_version):
        """Sets the task_version of this JobDetailResp.

        任务版本。

        :param task_version: The task_version of this JobDetailResp.
        :type task_version: str
        """
        self._task_version = task_version

    @property
    def connection_management(self):
        """Gets the connection_management of this JobDetailResp.

        :return: The connection_management of this JobDetailResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.ConnectionManagement`
        """
        return self._connection_management

    @connection_management.setter
    def connection_management(self, connection_management):
        """Sets the connection_management of this JobDetailResp.

        :param connection_management: The connection_management of this JobDetailResp.
        :type connection_management: :class:`huaweicloudsdkdrs.v5.ConnectionManagement`
        """
        self._connection_management = connection_management

    @property
    def public_ip_list(self):
        """Gets the public_ip_list of this JobDetailResp.

        指定公网IP的信息

        :return: The public_ip_list of this JobDetailResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.PublicIpConfig`]
        """
        return self._public_ip_list

    @public_ip_list.setter
    def public_ip_list(self, public_ip_list):
        """Sets the public_ip_list of this JobDetailResp.

        指定公网IP的信息

        :param public_ip_list: The public_ip_list of this JobDetailResp.
        :type public_ip_list: list[:class:`huaweicloudsdkdrs.v5.PublicIpConfig`]
        """
        self._public_ip_list = public_ip_list

    @property
    def bind_public_ip_state(self):
        """Gets the bind_public_ip_state of this JobDetailResp.

        是否成功绑定公网IP

        :return: The bind_public_ip_state of this JobDetailResp.
        :rtype: str
        """
        return self._bind_public_ip_state

    @bind_public_ip_state.setter
    def bind_public_ip_state(self, bind_public_ip_state):
        """Sets the bind_public_ip_state of this JobDetailResp.

        是否成功绑定公网IP

        :param bind_public_ip_state: The bind_public_ip_state of this JobDetailResp.
        :type bind_public_ip_state: str
        """
        self._bind_public_ip_state = bind_public_ip_state

    @property
    def children(self):
        """Gets the children of this JobDetailResp.

        多任务时，存在子任务绑定失败时，返回子任务的信息

        :return: The children of this JobDetailResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.FailedToBindEipChildInfo`]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this JobDetailResp.

        多任务时，存在子任务绑定失败时，返回子任务的信息

        :param children: The children of this JobDetailResp.
        :type children: list[:class:`huaweicloudsdkdrs.v5.FailedToBindEipChildInfo`]
        """
        self._children = children

    @property
    def is_writable(self):
        """Gets the is_writable of this JobDetailResp.

        解除目标库只读操作后，目标库解除只读是否成功。 - pending：目标库解除操作进行中。 - success：目标库解除只读操作成功。

        :return: The is_writable of this JobDetailResp.
        :rtype: str
        """
        return self._is_writable

    @is_writable.setter
    def is_writable(self, is_writable):
        """Sets the is_writable of this JobDetailResp.

        解除目标库只读操作后，目标库解除只读是否成功。 - pending：目标库解除操作进行中。 - success：目标库解除只读操作成功。

        :param is_writable: The is_writable of this JobDetailResp.
        :type is_writable: str
        """
        self._is_writable = is_writable

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
        if not isinstance(other, JobDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
