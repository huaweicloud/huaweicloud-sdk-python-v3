# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlinkSqlJobRequestBody:

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
        'desc': 'str',
        'queue_name': 'str',
        'sql_body': 'str',
        'run_mode': 'str',
        'cu_number': 'int',
        'parallel_number': 'int',
        'checkpoint_enabled': 'bool',
        'checkpoint_mode': 'int',
        'checkpoint_interval': 'int',
        'obs_bucket': 'str',
        'log_enabled': 'bool',
        'smn_topic': 'str',
        'restart_when_exception': 'bool',
        'idle_state_retention': 'int',
        'edge_group_ids': 'list[str]',
        'dirty_data_strategy': 'str',
        'udf_jar_url': 'str',
        'manager_cu_number': 'int',
        'tm_cus': 'int',
        'tm_slot_num': 'int',
        'resume_checkpoint': 'bool',
        'resume_max_num': 'int',
        'runtime_config': 'str',
        'operator_config': 'str',
        'static_estimator_config': 'str',
        'flink_version': 'str',
        'execution_agency_urn': 'str',
        'resource_config_version': 'str',
        'resource_config': 'ResourceConfig'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'queue_name': 'queue_name',
        'sql_body': 'sql_body',
        'run_mode': 'run_mode',
        'cu_number': 'cu_number',
        'parallel_number': 'parallel_number',
        'checkpoint_enabled': 'checkpoint_enabled',
        'checkpoint_mode': 'checkpoint_mode',
        'checkpoint_interval': 'checkpoint_interval',
        'obs_bucket': 'obs_bucket',
        'log_enabled': 'log_enabled',
        'smn_topic': 'smn_topic',
        'restart_when_exception': 'restart_when_exception',
        'idle_state_retention': 'idle_state_retention',
        'edge_group_ids': 'edge_group_ids',
        'dirty_data_strategy': 'dirty_data_strategy',
        'udf_jar_url': 'udf_jar_url',
        'manager_cu_number': 'manager_cu_number',
        'tm_cus': 'tm_cus',
        'tm_slot_num': 'tm_slot_num',
        'resume_checkpoint': 'resume_checkpoint',
        'resume_max_num': 'resume_max_num',
        'runtime_config': 'runtime_config',
        'operator_config': 'operator_config',
        'static_estimator_config': 'static_estimator_config',
        'flink_version': 'flink_version',
        'execution_agency_urn': 'execution_agency_urn',
        'resource_config_version': 'resource_config_version',
        'resource_config': 'resource_config'
    }

    def __init__(self, name=None, desc=None, queue_name=None, sql_body=None, run_mode=None, cu_number=None, parallel_number=None, checkpoint_enabled=None, checkpoint_mode=None, checkpoint_interval=None, obs_bucket=None, log_enabled=None, smn_topic=None, restart_when_exception=None, idle_state_retention=None, edge_group_ids=None, dirty_data_strategy=None, udf_jar_url=None, manager_cu_number=None, tm_cus=None, tm_slot_num=None, resume_checkpoint=None, resume_max_num=None, runtime_config=None, operator_config=None, static_estimator_config=None, flink_version=None, execution_agency_urn=None, resource_config_version=None, resource_config=None):
        r"""UpdateFlinkSqlJobRequestBody

        The model defined in huaweicloud sdk

        :param name: 作业名称。长度限制：0-57个字符。
        :type name: str
        :param desc: 作业描述。长度限制：0-2048个字符。
        :type desc: str
        :param queue_name: 队列名称。长度限制：1-128个字符。
        :type queue_name: str
        :param sql_body: Stream SQL语句。长度限制：0-1024*1024个字符。
        :type sql_body: str
        :param run_mode: 作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 默认值为shared_cluster。
        :type run_mode: str
        :param cu_number: 用户为作业选择的CU数量。默认值为2。
        :type cu_number: int
        :param parallel_number: 用户设置的作业并行数目。默认值为1。
        :type parallel_number: int
        :param checkpoint_enabled: 是否开启作业自动快照功能。 开启：true; 关闭：false; 默认：false.
        :type checkpoint_enabled: bool
        :param checkpoint_mode: 快照模式： 1表示ExactlyOnce：数据只被消费一次。 2表示AtLeastOnce：数据至少被消费一次。 默认值为1。
        :type checkpoint_mode: int
        :param checkpoint_interval: 快照时间间隔, 单位为秒，默认值为10。
        :type checkpoint_interval: int
        :param obs_bucket: 当checkpoint_enabled为true时，该参数是用户授权保存快照的OBS路径。当log_enabled 为true时，该参数是用户授权保存作业日志的OBS路径。
        :type obs_bucket: str
        :param log_enabled: 是否开启作业的日志上传到用户的OBS功能，默认为false。
        :type log_enabled: bool
        :param smn_topic: 当作业异常时，向该SMN主题推送告警信息。
        :type smn_topic: str
        :param restart_when_exception: 是否开启作业异常自动重启，默认为false。
        :type restart_when_exception: bool
        :param idle_state_retention: 空闲状态过期周期，单位为秒，默认值为3600。
        :type idle_state_retention: int
        :param edge_group_ids: 边缘计算组ID列表。
        :type edge_group_ids: list[str]
        :param dirty_data_strategy: 作业脏数据策略。 “2”：保存； “1”：抛出异常； “0”：忽略； 默认值为“0”。
        :type dirty_data_strategy: str
        :param udf_jar_url: 用户自定义UDF文件，在后续作业中可以调用插入Jar包中的自定义函数。 UDF Jar包的管理方式： 上传OBS管理UDF Jar包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理UDF Jar包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理&gt;程序包管理”中创建程序包。 Flink1.15版本不再支持DLI管理UDF Jar包。
        :type udf_jar_url: str
        :param manager_cu_number: 用户为作业选择的管理单元（jobmanager）CU数量，默认值为“1”。
        :type manager_cu_number: int
        :param tm_cus: 每个taskmanager的CU数，默认值为“1”。
        :type tm_cus: int
        :param tm_slot_num: 每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。
        :type tm_slot_num: int
        :param resume_checkpoint: 异常重启是否从checkpoint恢复。
        :type resume_checkpoint: bool
        :param resume_max_num: 异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。
        :type resume_max_num: int
        :param runtime_config: Flink作业运行时自定义优化参数。
        :type runtime_config: str
        :param operator_config: 算子的并行度配置。
        :type operator_config: str
        :param static_estimator_config: 每个算子的流量/命中率配置，json格式的字符串。例如： {\&quot;operator_list\&quot;:[   {\&quot;id\&quot;:\&quot;0a448493b4782967b150582570326227\&quot;,\&quot;rate_factor\&quot;:0.55},   {\&quot;id\&quot;:\&quot;6d2677a0ecc3fd8df0b72ec675edf8f4\&quot;,\&quot;rate_factor\&quot;:1},   {\&quot;id\&quot;:\&quot;ea632d67b7d595e5b851708ae9ad79d6\&quot;,\&quot;rate_factor\&quot;:0.55},   {\&quot;id\&quot;:\&quot;bc764cd8ddf7a0cff126f51c16239658\&quot;,\&quot;output_rate\&quot;:2000} ]}
        :type static_estimator_config: str
        :param flink_version: Flink版本。当前只支持1.10和1.12。
        :type flink_version: str
        :param execution_agency_urn: 授权给DLI的委托名。Flink1.15版本时支持配置该参数。
        :type execution_agency_urn: str
        :param resource_config_version: 资源配置版本。可选值 \&quot;v1\&quot; ,\&quot;v2\&quot;.默认为“v1”。v2版本对比于v1模版不支持设置CU数量，支持直接设置Job Manager Memory和Task Manager Memory。v1：适用于Flink 1.12、Flink 1.13、Flink 1.15。v2：适用于Flink 1.13、Flink 1.15、Flink 1.17。优先推荐使用V2版本的参数设置。
        :type resource_config_version: str
        :param resource_config: 
        :type resource_config: :class:`huaweicloudsdkdli.v1.ResourceConfig`
        """
        
        

        self._name = None
        self._desc = None
        self._queue_name = None
        self._sql_body = None
        self._run_mode = None
        self._cu_number = None
        self._parallel_number = None
        self._checkpoint_enabled = None
        self._checkpoint_mode = None
        self._checkpoint_interval = None
        self._obs_bucket = None
        self._log_enabled = None
        self._smn_topic = None
        self._restart_when_exception = None
        self._idle_state_retention = None
        self._edge_group_ids = None
        self._dirty_data_strategy = None
        self._udf_jar_url = None
        self._manager_cu_number = None
        self._tm_cus = None
        self._tm_slot_num = None
        self._resume_checkpoint = None
        self._resume_max_num = None
        self._runtime_config = None
        self._operator_config = None
        self._static_estimator_config = None
        self._flink_version = None
        self._execution_agency_urn = None
        self._resource_config_version = None
        self._resource_config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if queue_name is not None:
            self.queue_name = queue_name
        if sql_body is not None:
            self.sql_body = sql_body
        if run_mode is not None:
            self.run_mode = run_mode
        if cu_number is not None:
            self.cu_number = cu_number
        if parallel_number is not None:
            self.parallel_number = parallel_number
        if checkpoint_enabled is not None:
            self.checkpoint_enabled = checkpoint_enabled
        if checkpoint_mode is not None:
            self.checkpoint_mode = checkpoint_mode
        if checkpoint_interval is not None:
            self.checkpoint_interval = checkpoint_interval
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if log_enabled is not None:
            self.log_enabled = log_enabled
        if smn_topic is not None:
            self.smn_topic = smn_topic
        if restart_when_exception is not None:
            self.restart_when_exception = restart_when_exception
        if idle_state_retention is not None:
            self.idle_state_retention = idle_state_retention
        if edge_group_ids is not None:
            self.edge_group_ids = edge_group_ids
        if dirty_data_strategy is not None:
            self.dirty_data_strategy = dirty_data_strategy
        if udf_jar_url is not None:
            self.udf_jar_url = udf_jar_url
        if manager_cu_number is not None:
            self.manager_cu_number = manager_cu_number
        if tm_cus is not None:
            self.tm_cus = tm_cus
        if tm_slot_num is not None:
            self.tm_slot_num = tm_slot_num
        if resume_checkpoint is not None:
            self.resume_checkpoint = resume_checkpoint
        if resume_max_num is not None:
            self.resume_max_num = resume_max_num
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if operator_config is not None:
            self.operator_config = operator_config
        if static_estimator_config is not None:
            self.static_estimator_config = static_estimator_config
        if flink_version is not None:
            self.flink_version = flink_version
        if execution_agency_urn is not None:
            self.execution_agency_urn = execution_agency_urn
        if resource_config_version is not None:
            self.resource_config_version = resource_config_version
        if resource_config is not None:
            self.resource_config = resource_config

    @property
    def name(self):
        r"""Gets the name of this UpdateFlinkSqlJobRequestBody.

        作业名称。长度限制：0-57个字符。

        :return: The name of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateFlinkSqlJobRequestBody.

        作业名称。长度限制：0-57个字符。

        :param name: The name of this UpdateFlinkSqlJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this UpdateFlinkSqlJobRequestBody.

        作业描述。长度限制：0-2048个字符。

        :return: The desc of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this UpdateFlinkSqlJobRequestBody.

        作业描述。长度限制：0-2048个字符。

        :param desc: The desc of this UpdateFlinkSqlJobRequestBody.
        :type desc: str
        """
        self._desc = desc

    @property
    def queue_name(self):
        r"""Gets the queue_name of this UpdateFlinkSqlJobRequestBody.

        队列名称。长度限制：1-128个字符。

        :return: The queue_name of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this UpdateFlinkSqlJobRequestBody.

        队列名称。长度限制：1-128个字符。

        :param queue_name: The queue_name of this UpdateFlinkSqlJobRequestBody.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def sql_body(self):
        r"""Gets the sql_body of this UpdateFlinkSqlJobRequestBody.

        Stream SQL语句。长度限制：0-1024*1024个字符。

        :return: The sql_body of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        r"""Sets the sql_body of this UpdateFlinkSqlJobRequestBody.

        Stream SQL语句。长度限制：0-1024*1024个字符。

        :param sql_body: The sql_body of this UpdateFlinkSqlJobRequestBody.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def run_mode(self):
        r"""Gets the run_mode of this UpdateFlinkSqlJobRequestBody.

        作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 默认值为shared_cluster。

        :return: The run_mode of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._run_mode

    @run_mode.setter
    def run_mode(self, run_mode):
        r"""Sets the run_mode of this UpdateFlinkSqlJobRequestBody.

        作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 默认值为shared_cluster。

        :param run_mode: The run_mode of this UpdateFlinkSqlJobRequestBody.
        :type run_mode: str
        """
        self._run_mode = run_mode

    @property
    def cu_number(self):
        r"""Gets the cu_number of this UpdateFlinkSqlJobRequestBody.

        用户为作业选择的CU数量。默认值为2。

        :return: The cu_number of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._cu_number

    @cu_number.setter
    def cu_number(self, cu_number):
        r"""Sets the cu_number of this UpdateFlinkSqlJobRequestBody.

        用户为作业选择的CU数量。默认值为2。

        :param cu_number: The cu_number of this UpdateFlinkSqlJobRequestBody.
        :type cu_number: int
        """
        self._cu_number = cu_number

    @property
    def parallel_number(self):
        r"""Gets the parallel_number of this UpdateFlinkSqlJobRequestBody.

        用户设置的作业并行数目。默认值为1。

        :return: The parallel_number of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        r"""Sets the parallel_number of this UpdateFlinkSqlJobRequestBody.

        用户设置的作业并行数目。默认值为1。

        :param parallel_number: The parallel_number of this UpdateFlinkSqlJobRequestBody.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def checkpoint_enabled(self):
        r"""Gets the checkpoint_enabled of this UpdateFlinkSqlJobRequestBody.

        是否开启作业自动快照功能。 开启：true; 关闭：false; 默认：false.

        :return: The checkpoint_enabled of this UpdateFlinkSqlJobRequestBody.
        :rtype: bool
        """
        return self._checkpoint_enabled

    @checkpoint_enabled.setter
    def checkpoint_enabled(self, checkpoint_enabled):
        r"""Sets the checkpoint_enabled of this UpdateFlinkSqlJobRequestBody.

        是否开启作业自动快照功能。 开启：true; 关闭：false; 默认：false.

        :param checkpoint_enabled: The checkpoint_enabled of this UpdateFlinkSqlJobRequestBody.
        :type checkpoint_enabled: bool
        """
        self._checkpoint_enabled = checkpoint_enabled

    @property
    def checkpoint_mode(self):
        r"""Gets the checkpoint_mode of this UpdateFlinkSqlJobRequestBody.

        快照模式： 1表示ExactlyOnce：数据只被消费一次。 2表示AtLeastOnce：数据至少被消费一次。 默认值为1。

        :return: The checkpoint_mode of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._checkpoint_mode

    @checkpoint_mode.setter
    def checkpoint_mode(self, checkpoint_mode):
        r"""Sets the checkpoint_mode of this UpdateFlinkSqlJobRequestBody.

        快照模式： 1表示ExactlyOnce：数据只被消费一次。 2表示AtLeastOnce：数据至少被消费一次。 默认值为1。

        :param checkpoint_mode: The checkpoint_mode of this UpdateFlinkSqlJobRequestBody.
        :type checkpoint_mode: int
        """
        self._checkpoint_mode = checkpoint_mode

    @property
    def checkpoint_interval(self):
        r"""Gets the checkpoint_interval of this UpdateFlinkSqlJobRequestBody.

        快照时间间隔, 单位为秒，默认值为10。

        :return: The checkpoint_interval of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._checkpoint_interval

    @checkpoint_interval.setter
    def checkpoint_interval(self, checkpoint_interval):
        r"""Sets the checkpoint_interval of this UpdateFlinkSqlJobRequestBody.

        快照时间间隔, 单位为秒，默认值为10。

        :param checkpoint_interval: The checkpoint_interval of this UpdateFlinkSqlJobRequestBody.
        :type checkpoint_interval: int
        """
        self._checkpoint_interval = checkpoint_interval

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this UpdateFlinkSqlJobRequestBody.

        当checkpoint_enabled为true时，该参数是用户授权保存快照的OBS路径。当log_enabled 为true时，该参数是用户授权保存作业日志的OBS路径。

        :return: The obs_bucket of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this UpdateFlinkSqlJobRequestBody.

        当checkpoint_enabled为true时，该参数是用户授权保存快照的OBS路径。当log_enabled 为true时，该参数是用户授权保存作业日志的OBS路径。

        :param obs_bucket: The obs_bucket of this UpdateFlinkSqlJobRequestBody.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def log_enabled(self):
        r"""Gets the log_enabled of this UpdateFlinkSqlJobRequestBody.

        是否开启作业的日志上传到用户的OBS功能，默认为false。

        :return: The log_enabled of this UpdateFlinkSqlJobRequestBody.
        :rtype: bool
        """
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, log_enabled):
        r"""Sets the log_enabled of this UpdateFlinkSqlJobRequestBody.

        是否开启作业的日志上传到用户的OBS功能，默认为false。

        :param log_enabled: The log_enabled of this UpdateFlinkSqlJobRequestBody.
        :type log_enabled: bool
        """
        self._log_enabled = log_enabled

    @property
    def smn_topic(self):
        r"""Gets the smn_topic of this UpdateFlinkSqlJobRequestBody.

        当作业异常时，向该SMN主题推送告警信息。

        :return: The smn_topic of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        r"""Sets the smn_topic of this UpdateFlinkSqlJobRequestBody.

        当作业异常时，向该SMN主题推送告警信息。

        :param smn_topic: The smn_topic of this UpdateFlinkSqlJobRequestBody.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

    @property
    def restart_when_exception(self):
        r"""Gets the restart_when_exception of this UpdateFlinkSqlJobRequestBody.

        是否开启作业异常自动重启，默认为false。

        :return: The restart_when_exception of this UpdateFlinkSqlJobRequestBody.
        :rtype: bool
        """
        return self._restart_when_exception

    @restart_when_exception.setter
    def restart_when_exception(self, restart_when_exception):
        r"""Sets the restart_when_exception of this UpdateFlinkSqlJobRequestBody.

        是否开启作业异常自动重启，默认为false。

        :param restart_when_exception: The restart_when_exception of this UpdateFlinkSqlJobRequestBody.
        :type restart_when_exception: bool
        """
        self._restart_when_exception = restart_when_exception

    @property
    def idle_state_retention(self):
        r"""Gets the idle_state_retention of this UpdateFlinkSqlJobRequestBody.

        空闲状态过期周期，单位为秒，默认值为3600。

        :return: The idle_state_retention of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._idle_state_retention

    @idle_state_retention.setter
    def idle_state_retention(self, idle_state_retention):
        r"""Sets the idle_state_retention of this UpdateFlinkSqlJobRequestBody.

        空闲状态过期周期，单位为秒，默认值为3600。

        :param idle_state_retention: The idle_state_retention of this UpdateFlinkSqlJobRequestBody.
        :type idle_state_retention: int
        """
        self._idle_state_retention = idle_state_retention

    @property
    def edge_group_ids(self):
        r"""Gets the edge_group_ids of this UpdateFlinkSqlJobRequestBody.

        边缘计算组ID列表。

        :return: The edge_group_ids of this UpdateFlinkSqlJobRequestBody.
        :rtype: list[str]
        """
        return self._edge_group_ids

    @edge_group_ids.setter
    def edge_group_ids(self, edge_group_ids):
        r"""Sets the edge_group_ids of this UpdateFlinkSqlJobRequestBody.

        边缘计算组ID列表。

        :param edge_group_ids: The edge_group_ids of this UpdateFlinkSqlJobRequestBody.
        :type edge_group_ids: list[str]
        """
        self._edge_group_ids = edge_group_ids

    @property
    def dirty_data_strategy(self):
        r"""Gets the dirty_data_strategy of this UpdateFlinkSqlJobRequestBody.

        作业脏数据策略。 “2”：保存； “1”：抛出异常； “0”：忽略； 默认值为“0”。

        :return: The dirty_data_strategy of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._dirty_data_strategy

    @dirty_data_strategy.setter
    def dirty_data_strategy(self, dirty_data_strategy):
        r"""Sets the dirty_data_strategy of this UpdateFlinkSqlJobRequestBody.

        作业脏数据策略。 “2”：保存； “1”：抛出异常； “0”：忽略； 默认值为“0”。

        :param dirty_data_strategy: The dirty_data_strategy of this UpdateFlinkSqlJobRequestBody.
        :type dirty_data_strategy: str
        """
        self._dirty_data_strategy = dirty_data_strategy

    @property
    def udf_jar_url(self):
        r"""Gets the udf_jar_url of this UpdateFlinkSqlJobRequestBody.

        用户自定义UDF文件，在后续作业中可以调用插入Jar包中的自定义函数。 UDF Jar包的管理方式： 上传OBS管理UDF Jar包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理UDF Jar包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理>程序包管理”中创建程序包。 Flink1.15版本不再支持DLI管理UDF Jar包。

        :return: The udf_jar_url of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._udf_jar_url

    @udf_jar_url.setter
    def udf_jar_url(self, udf_jar_url):
        r"""Sets the udf_jar_url of this UpdateFlinkSqlJobRequestBody.

        用户自定义UDF文件，在后续作业中可以调用插入Jar包中的自定义函数。 UDF Jar包的管理方式： 上传OBS管理UDF Jar包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理UDF Jar包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理>程序包管理”中创建程序包。 Flink1.15版本不再支持DLI管理UDF Jar包。

        :param udf_jar_url: The udf_jar_url of this UpdateFlinkSqlJobRequestBody.
        :type udf_jar_url: str
        """
        self._udf_jar_url = udf_jar_url

    @property
    def manager_cu_number(self):
        r"""Gets the manager_cu_number of this UpdateFlinkSqlJobRequestBody.

        用户为作业选择的管理单元（jobmanager）CU数量，默认值为“1”。

        :return: The manager_cu_number of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._manager_cu_number

    @manager_cu_number.setter
    def manager_cu_number(self, manager_cu_number):
        r"""Sets the manager_cu_number of this UpdateFlinkSqlJobRequestBody.

        用户为作业选择的管理单元（jobmanager）CU数量，默认值为“1”。

        :param manager_cu_number: The manager_cu_number of this UpdateFlinkSqlJobRequestBody.
        :type manager_cu_number: int
        """
        self._manager_cu_number = manager_cu_number

    @property
    def tm_cus(self):
        r"""Gets the tm_cus of this UpdateFlinkSqlJobRequestBody.

        每个taskmanager的CU数，默认值为“1”。

        :return: The tm_cus of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._tm_cus

    @tm_cus.setter
    def tm_cus(self, tm_cus):
        r"""Sets the tm_cus of this UpdateFlinkSqlJobRequestBody.

        每个taskmanager的CU数，默认值为“1”。

        :param tm_cus: The tm_cus of this UpdateFlinkSqlJobRequestBody.
        :type tm_cus: int
        """
        self._tm_cus = tm_cus

    @property
    def tm_slot_num(self):
        r"""Gets the tm_slot_num of this UpdateFlinkSqlJobRequestBody.

        每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。

        :return: The tm_slot_num of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._tm_slot_num

    @tm_slot_num.setter
    def tm_slot_num(self, tm_slot_num):
        r"""Sets the tm_slot_num of this UpdateFlinkSqlJobRequestBody.

        每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。

        :param tm_slot_num: The tm_slot_num of this UpdateFlinkSqlJobRequestBody.
        :type tm_slot_num: int
        """
        self._tm_slot_num = tm_slot_num

    @property
    def resume_checkpoint(self):
        r"""Gets the resume_checkpoint of this UpdateFlinkSqlJobRequestBody.

        异常重启是否从checkpoint恢复。

        :return: The resume_checkpoint of this UpdateFlinkSqlJobRequestBody.
        :rtype: bool
        """
        return self._resume_checkpoint

    @resume_checkpoint.setter
    def resume_checkpoint(self, resume_checkpoint):
        r"""Sets the resume_checkpoint of this UpdateFlinkSqlJobRequestBody.

        异常重启是否从checkpoint恢复。

        :param resume_checkpoint: The resume_checkpoint of this UpdateFlinkSqlJobRequestBody.
        :type resume_checkpoint: bool
        """
        self._resume_checkpoint = resume_checkpoint

    @property
    def resume_max_num(self):
        r"""Gets the resume_max_num of this UpdateFlinkSqlJobRequestBody.

        异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。

        :return: The resume_max_num of this UpdateFlinkSqlJobRequestBody.
        :rtype: int
        """
        return self._resume_max_num

    @resume_max_num.setter
    def resume_max_num(self, resume_max_num):
        r"""Sets the resume_max_num of this UpdateFlinkSqlJobRequestBody.

        异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。

        :param resume_max_num: The resume_max_num of this UpdateFlinkSqlJobRequestBody.
        :type resume_max_num: int
        """
        self._resume_max_num = resume_max_num

    @property
    def runtime_config(self):
        r"""Gets the runtime_config of this UpdateFlinkSqlJobRequestBody.

        Flink作业运行时自定义优化参数。

        :return: The runtime_config of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        r"""Sets the runtime_config of this UpdateFlinkSqlJobRequestBody.

        Flink作业运行时自定义优化参数。

        :param runtime_config: The runtime_config of this UpdateFlinkSqlJobRequestBody.
        :type runtime_config: str
        """
        self._runtime_config = runtime_config

    @property
    def operator_config(self):
        r"""Gets the operator_config of this UpdateFlinkSqlJobRequestBody.

        算子的并行度配置。

        :return: The operator_config of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._operator_config

    @operator_config.setter
    def operator_config(self, operator_config):
        r"""Sets the operator_config of this UpdateFlinkSqlJobRequestBody.

        算子的并行度配置。

        :param operator_config: The operator_config of this UpdateFlinkSqlJobRequestBody.
        :type operator_config: str
        """
        self._operator_config = operator_config

    @property
    def static_estimator_config(self):
        r"""Gets the static_estimator_config of this UpdateFlinkSqlJobRequestBody.

        每个算子的流量/命中率配置，json格式的字符串。例如： {\"operator_list\":[   {\"id\":\"0a448493b4782967b150582570326227\",\"rate_factor\":0.55},   {\"id\":\"6d2677a0ecc3fd8df0b72ec675edf8f4\",\"rate_factor\":1},   {\"id\":\"ea632d67b7d595e5b851708ae9ad79d6\",\"rate_factor\":0.55},   {\"id\":\"bc764cd8ddf7a0cff126f51c16239658\",\"output_rate\":2000} ]}

        :return: The static_estimator_config of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._static_estimator_config

    @static_estimator_config.setter
    def static_estimator_config(self, static_estimator_config):
        r"""Sets the static_estimator_config of this UpdateFlinkSqlJobRequestBody.

        每个算子的流量/命中率配置，json格式的字符串。例如： {\"operator_list\":[   {\"id\":\"0a448493b4782967b150582570326227\",\"rate_factor\":0.55},   {\"id\":\"6d2677a0ecc3fd8df0b72ec675edf8f4\",\"rate_factor\":1},   {\"id\":\"ea632d67b7d595e5b851708ae9ad79d6\",\"rate_factor\":0.55},   {\"id\":\"bc764cd8ddf7a0cff126f51c16239658\",\"output_rate\":2000} ]}

        :param static_estimator_config: The static_estimator_config of this UpdateFlinkSqlJobRequestBody.
        :type static_estimator_config: str
        """
        self._static_estimator_config = static_estimator_config

    @property
    def flink_version(self):
        r"""Gets the flink_version of this UpdateFlinkSqlJobRequestBody.

        Flink版本。当前只支持1.10和1.12。

        :return: The flink_version of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._flink_version

    @flink_version.setter
    def flink_version(self, flink_version):
        r"""Sets the flink_version of this UpdateFlinkSqlJobRequestBody.

        Flink版本。当前只支持1.10和1.12。

        :param flink_version: The flink_version of this UpdateFlinkSqlJobRequestBody.
        :type flink_version: str
        """
        self._flink_version = flink_version

    @property
    def execution_agency_urn(self):
        r"""Gets the execution_agency_urn of this UpdateFlinkSqlJobRequestBody.

        授权给DLI的委托名。Flink1.15版本时支持配置该参数。

        :return: The execution_agency_urn of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._execution_agency_urn

    @execution_agency_urn.setter
    def execution_agency_urn(self, execution_agency_urn):
        r"""Sets the execution_agency_urn of this UpdateFlinkSqlJobRequestBody.

        授权给DLI的委托名。Flink1.15版本时支持配置该参数。

        :param execution_agency_urn: The execution_agency_urn of this UpdateFlinkSqlJobRequestBody.
        :type execution_agency_urn: str
        """
        self._execution_agency_urn = execution_agency_urn

    @property
    def resource_config_version(self):
        r"""Gets the resource_config_version of this UpdateFlinkSqlJobRequestBody.

        资源配置版本。可选值 \"v1\" ,\"v2\".默认为“v1”。v2版本对比于v1模版不支持设置CU数量，支持直接设置Job Manager Memory和Task Manager Memory。v1：适用于Flink 1.12、Flink 1.13、Flink 1.15。v2：适用于Flink 1.13、Flink 1.15、Flink 1.17。优先推荐使用V2版本的参数设置。

        :return: The resource_config_version of this UpdateFlinkSqlJobRequestBody.
        :rtype: str
        """
        return self._resource_config_version

    @resource_config_version.setter
    def resource_config_version(self, resource_config_version):
        r"""Sets the resource_config_version of this UpdateFlinkSqlJobRequestBody.

        资源配置版本。可选值 \"v1\" ,\"v2\".默认为“v1”。v2版本对比于v1模版不支持设置CU数量，支持直接设置Job Manager Memory和Task Manager Memory。v1：适用于Flink 1.12、Flink 1.13、Flink 1.15。v2：适用于Flink 1.13、Flink 1.15、Flink 1.17。优先推荐使用V2版本的参数设置。

        :param resource_config_version: The resource_config_version of this UpdateFlinkSqlJobRequestBody.
        :type resource_config_version: str
        """
        self._resource_config_version = resource_config_version

    @property
    def resource_config(self):
        r"""Gets the resource_config of this UpdateFlinkSqlJobRequestBody.

        :return: The resource_config of this UpdateFlinkSqlJobRequestBody.
        :rtype: :class:`huaweicloudsdkdli.v1.ResourceConfig`
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        r"""Sets the resource_config of this UpdateFlinkSqlJobRequestBody.

        :param resource_config: The resource_config of this UpdateFlinkSqlJobRequestBody.
        :type resource_config: :class:`huaweicloudsdkdli.v1.ResourceConfig`
        """
        self._resource_config = resource_config

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
        if not isinstance(other, UpdateFlinkSqlJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
