# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSQLJobReq:

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
        'template_id': 'int',
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
        'job_type': 'str',
        'edge_group_ids': 'list[str]',
        'dirty_data_strategy': 'str',
        'udf_jar_url': 'str',
        'manager_cu_number': 'int',
        'tm_cus': 'int',
        'tm_slot_num': 'int',
        'tags': 'list[TmsTagEntity]',
        'resume_checkpoint': 'bool',
        'resume_max_num': 'int',
        'runtime_config': 'str',
        'flink_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'template_id': 'template_id',
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
        'job_type': 'job_type',
        'edge_group_ids': 'edge_group_ids',
        'dirty_data_strategy': 'dirty_data_strategy',
        'udf_jar_url': 'udf_jar_url',
        'manager_cu_number': 'manager_cu_number',
        'tm_cus': 'tm_cus',
        'tm_slot_num': 'tm_slot_num',
        'tags': 'tags',
        'resume_checkpoint': 'resume_checkpoint',
        'resume_max_num': 'resume_max_num',
        'runtime_config': 'runtime_config',
        'flink_version': 'flink_version'
    }

    def __init__(self, name=None, desc=None, template_id=None, queue_name=None, sql_body=None, run_mode=None, cu_number=None, parallel_number=None, checkpoint_enabled=None, checkpoint_mode=None, checkpoint_interval=None, obs_bucket=None, log_enabled=None, smn_topic=None, restart_when_exception=None, idle_state_retention=None, job_type=None, edge_group_ids=None, dirty_data_strategy=None, udf_jar_url=None, manager_cu_number=None, tm_cus=None, tm_slot_num=None, tags=None, resume_checkpoint=None, resume_max_num=None, runtime_config=None, flink_version=None):
        """CreateSQLJobReq

        The model defined in huaweicloud sdk

        :param name: 作业名称。长度限制：0-57个字符。
        :type name: str
        :param desc: 作业描述。长度限制：0-2048个字符。
        :type desc: str
        :param template_id: 模板Id。  如果template_id和sql_body都不为空，优先sql_body；如果template_id不空，sql_body为空，以template_id内容填充sql_body。
        :type template_id: int
        :param queue_name: 队列名称。长度限制：1-128个字符。
        :type queue_name: str
        :param sql_body: Stream SQL语句。长度限制：1024*1024个字符。
        :type sql_body: str
        :param run_mode: 作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 默认值为：shared_cluster
        :type run_mode: str
        :param cu_number: 用户为作业选择的CU数量，默认值为2。
        :type cu_number: int
        :param parallel_number: 用户设置的作业并行数目。默认值为1。
        :type parallel_number: int
        :param checkpoint_enabled: 是否开启作业自动快照功能。 开启：true； 关闭：false； 默认：false。
        :type checkpoint_enabled: bool
        :param checkpoint_mode: 快照模式： 1表示ExactlyOnce：数据只被消费一次。 2表示AtLeastOnce：数据至少被消费一次。 默认值为1。
        :type checkpoint_mode: int
        :param checkpoint_interval: 快照时间间隔, 单位为秒。默认值为10。
        :type checkpoint_interval: int
        :param obs_bucket: 当checkpoint_enabled&#x3D;&#x3D;true时，该参数是用户授权保存快照的OBS路径。当log_enabled &#x3D;&#x3D;true时，该参数是用户授权保存作业日志的OBS路径。
        :type obs_bucket: str
        :param log_enabled: 是否开启作业的日志上传到用户的OBS功能。默认为false。
        :type log_enabled: bool
        :param smn_topic: 当作业异常时，向该SMN主题推送告警信息。
        :type smn_topic: str
        :param restart_when_exception: 是否开启作业异常自动重启。默认为false。
        :type restart_when_exception: bool
        :param idle_state_retention: 空闲状态过期周期，单位为秒，默认值为3600。
        :type idle_state_retention: int
        :param job_type: 作业类型：flink_sql_job和flink_sql_edge_job。 run_mode为edge_node时，作业类型须为flink_sql_edge_job。 run_mode为shared_cluster跟exclusive_cluster时，作业类型须为flink_sql_job。 默认值：flink_sql_job。 
        :type job_type: str
        :param edge_group_ids: 边缘计算组ID列表。
        :type edge_group_ids: list[str]
        :param dirty_data_strategy: 作业脏数据策略。 “2”：保存； “1”：抛出异常； “0”：忽略； 默认值为“0”。
        :type dirty_data_strategy: str
        :param udf_jar_url: 用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入。
        :type udf_jar_url: str
        :param manager_cu_number: 用户为作业选择的管理单元（jobmanager）CU数量，默认值为“1”。
        :type manager_cu_number: int
        :param tm_cus: 每个taskmanager的CU数，默认值为“1”。
        :type tm_cus: int
        :param tm_slot_num: 每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”
        :type tm_slot_num: int
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        :param resume_checkpoint: 异常重启是否从checkpoint恢复。
        :type resume_checkpoint: bool
        :param resume_max_num: 异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。
        :type resume_max_num: int
        :param runtime_config: Flink作业运行时自定义优化参数。
        :type runtime_config: str
        :param flink_version: Flink版本。当前只支持1.10和1.12。
        :type flink_version: str
        """
        
        

        self._name = None
        self._desc = None
        self._template_id = None
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
        self._job_type = None
        self._edge_group_ids = None
        self._dirty_data_strategy = None
        self._udf_jar_url = None
        self._manager_cu_number = None
        self._tm_cus = None
        self._tm_slot_num = None
        self._tags = None
        self._resume_checkpoint = None
        self._resume_max_num = None
        self._runtime_config = None
        self._flink_version = None
        self.discriminator = None

        self.name = name
        if desc is not None:
            self.desc = desc
        if template_id is not None:
            self.template_id = template_id
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
        if job_type is not None:
            self.job_type = job_type
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
        if tags is not None:
            self.tags = tags
        if resume_checkpoint is not None:
            self.resume_checkpoint = resume_checkpoint
        if resume_max_num is not None:
            self.resume_max_num = resume_max_num
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if flink_version is not None:
            self.flink_version = flink_version

    @property
    def name(self):
        """Gets the name of this CreateSQLJobReq.

        作业名称。长度限制：0-57个字符。

        :return: The name of this CreateSQLJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSQLJobReq.

        作业名称。长度限制：0-57个字符。

        :param name: The name of this CreateSQLJobReq.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        """Gets the desc of this CreateSQLJobReq.

        作业描述。长度限制：0-2048个字符。

        :return: The desc of this CreateSQLJobReq.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CreateSQLJobReq.

        作业描述。长度限制：0-2048个字符。

        :param desc: The desc of this CreateSQLJobReq.
        :type desc: str
        """
        self._desc = desc

    @property
    def template_id(self):
        """Gets the template_id of this CreateSQLJobReq.

        模板Id。  如果template_id和sql_body都不为空，优先sql_body；如果template_id不空，sql_body为空，以template_id内容填充sql_body。

        :return: The template_id of this CreateSQLJobReq.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateSQLJobReq.

        模板Id。  如果template_id和sql_body都不为空，优先sql_body；如果template_id不空，sql_body为空，以template_id内容填充sql_body。

        :param template_id: The template_id of this CreateSQLJobReq.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def queue_name(self):
        """Gets the queue_name of this CreateSQLJobReq.

        队列名称。长度限制：1-128个字符。

        :return: The queue_name of this CreateSQLJobReq.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this CreateSQLJobReq.

        队列名称。长度限制：1-128个字符。

        :param queue_name: The queue_name of this CreateSQLJobReq.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def sql_body(self):
        """Gets the sql_body of this CreateSQLJobReq.

        Stream SQL语句。长度限制：1024*1024个字符。

        :return: The sql_body of this CreateSQLJobReq.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        """Sets the sql_body of this CreateSQLJobReq.

        Stream SQL语句。长度限制：1024*1024个字符。

        :param sql_body: The sql_body of this CreateSQLJobReq.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def run_mode(self):
        """Gets the run_mode of this CreateSQLJobReq.

        作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 默认值为：shared_cluster

        :return: The run_mode of this CreateSQLJobReq.
        :rtype: str
        """
        return self._run_mode

    @run_mode.setter
    def run_mode(self, run_mode):
        """Sets the run_mode of this CreateSQLJobReq.

        作业运行模式： shared_cluster：共享。 exclusive_cluster：独享。 edge_node：边缘节点。 默认值为：shared_cluster

        :param run_mode: The run_mode of this CreateSQLJobReq.
        :type run_mode: str
        """
        self._run_mode = run_mode

    @property
    def cu_number(self):
        """Gets the cu_number of this CreateSQLJobReq.

        用户为作业选择的CU数量，默认值为2。

        :return: The cu_number of this CreateSQLJobReq.
        :rtype: int
        """
        return self._cu_number

    @cu_number.setter
    def cu_number(self, cu_number):
        """Sets the cu_number of this CreateSQLJobReq.

        用户为作业选择的CU数量，默认值为2。

        :param cu_number: The cu_number of this CreateSQLJobReq.
        :type cu_number: int
        """
        self._cu_number = cu_number

    @property
    def parallel_number(self):
        """Gets the parallel_number of this CreateSQLJobReq.

        用户设置的作业并行数目。默认值为1。

        :return: The parallel_number of this CreateSQLJobReq.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        """Sets the parallel_number of this CreateSQLJobReq.

        用户设置的作业并行数目。默认值为1。

        :param parallel_number: The parallel_number of this CreateSQLJobReq.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def checkpoint_enabled(self):
        """Gets the checkpoint_enabled of this CreateSQLJobReq.

        是否开启作业自动快照功能。 开启：true； 关闭：false； 默认：false。

        :return: The checkpoint_enabled of this CreateSQLJobReq.
        :rtype: bool
        """
        return self._checkpoint_enabled

    @checkpoint_enabled.setter
    def checkpoint_enabled(self, checkpoint_enabled):
        """Sets the checkpoint_enabled of this CreateSQLJobReq.

        是否开启作业自动快照功能。 开启：true； 关闭：false； 默认：false。

        :param checkpoint_enabled: The checkpoint_enabled of this CreateSQLJobReq.
        :type checkpoint_enabled: bool
        """
        self._checkpoint_enabled = checkpoint_enabled

    @property
    def checkpoint_mode(self):
        """Gets the checkpoint_mode of this CreateSQLJobReq.

        快照模式： 1表示ExactlyOnce：数据只被消费一次。 2表示AtLeastOnce：数据至少被消费一次。 默认值为1。

        :return: The checkpoint_mode of this CreateSQLJobReq.
        :rtype: int
        """
        return self._checkpoint_mode

    @checkpoint_mode.setter
    def checkpoint_mode(self, checkpoint_mode):
        """Sets the checkpoint_mode of this CreateSQLJobReq.

        快照模式： 1表示ExactlyOnce：数据只被消费一次。 2表示AtLeastOnce：数据至少被消费一次。 默认值为1。

        :param checkpoint_mode: The checkpoint_mode of this CreateSQLJobReq.
        :type checkpoint_mode: int
        """
        self._checkpoint_mode = checkpoint_mode

    @property
    def checkpoint_interval(self):
        """Gets the checkpoint_interval of this CreateSQLJobReq.

        快照时间间隔, 单位为秒。默认值为10。

        :return: The checkpoint_interval of this CreateSQLJobReq.
        :rtype: int
        """
        return self._checkpoint_interval

    @checkpoint_interval.setter
    def checkpoint_interval(self, checkpoint_interval):
        """Sets the checkpoint_interval of this CreateSQLJobReq.

        快照时间间隔, 单位为秒。默认值为10。

        :param checkpoint_interval: The checkpoint_interval of this CreateSQLJobReq.
        :type checkpoint_interval: int
        """
        self._checkpoint_interval = checkpoint_interval

    @property
    def obs_bucket(self):
        """Gets the obs_bucket of this CreateSQLJobReq.

        当checkpoint_enabled==true时，该参数是用户授权保存快照的OBS路径。当log_enabled ==true时，该参数是用户授权保存作业日志的OBS路径。

        :return: The obs_bucket of this CreateSQLJobReq.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        """Sets the obs_bucket of this CreateSQLJobReq.

        当checkpoint_enabled==true时，该参数是用户授权保存快照的OBS路径。当log_enabled ==true时，该参数是用户授权保存作业日志的OBS路径。

        :param obs_bucket: The obs_bucket of this CreateSQLJobReq.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def log_enabled(self):
        """Gets the log_enabled of this CreateSQLJobReq.

        是否开启作业的日志上传到用户的OBS功能。默认为false。

        :return: The log_enabled of this CreateSQLJobReq.
        :rtype: bool
        """
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, log_enabled):
        """Sets the log_enabled of this CreateSQLJobReq.

        是否开启作业的日志上传到用户的OBS功能。默认为false。

        :param log_enabled: The log_enabled of this CreateSQLJobReq.
        :type log_enabled: bool
        """
        self._log_enabled = log_enabled

    @property
    def smn_topic(self):
        """Gets the smn_topic of this CreateSQLJobReq.

        当作业异常时，向该SMN主题推送告警信息。

        :return: The smn_topic of this CreateSQLJobReq.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        """Sets the smn_topic of this CreateSQLJobReq.

        当作业异常时，向该SMN主题推送告警信息。

        :param smn_topic: The smn_topic of this CreateSQLJobReq.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

    @property
    def restart_when_exception(self):
        """Gets the restart_when_exception of this CreateSQLJobReq.

        是否开启作业异常自动重启。默认为false。

        :return: The restart_when_exception of this CreateSQLJobReq.
        :rtype: bool
        """
        return self._restart_when_exception

    @restart_when_exception.setter
    def restart_when_exception(self, restart_when_exception):
        """Sets the restart_when_exception of this CreateSQLJobReq.

        是否开启作业异常自动重启。默认为false。

        :param restart_when_exception: The restart_when_exception of this CreateSQLJobReq.
        :type restart_when_exception: bool
        """
        self._restart_when_exception = restart_when_exception

    @property
    def idle_state_retention(self):
        """Gets the idle_state_retention of this CreateSQLJobReq.

        空闲状态过期周期，单位为秒，默认值为3600。

        :return: The idle_state_retention of this CreateSQLJobReq.
        :rtype: int
        """
        return self._idle_state_retention

    @idle_state_retention.setter
    def idle_state_retention(self, idle_state_retention):
        """Sets the idle_state_retention of this CreateSQLJobReq.

        空闲状态过期周期，单位为秒，默认值为3600。

        :param idle_state_retention: The idle_state_retention of this CreateSQLJobReq.
        :type idle_state_retention: int
        """
        self._idle_state_retention = idle_state_retention

    @property
    def job_type(self):
        """Gets the job_type of this CreateSQLJobReq.

        作业类型：flink_sql_job和flink_sql_edge_job。 run_mode为edge_node时，作业类型须为flink_sql_edge_job。 run_mode为shared_cluster跟exclusive_cluster时，作业类型须为flink_sql_job。 默认值：flink_sql_job。 

        :return: The job_type of this CreateSQLJobReq.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this CreateSQLJobReq.

        作业类型：flink_sql_job和flink_sql_edge_job。 run_mode为edge_node时，作业类型须为flink_sql_edge_job。 run_mode为shared_cluster跟exclusive_cluster时，作业类型须为flink_sql_job。 默认值：flink_sql_job。 

        :param job_type: The job_type of this CreateSQLJobReq.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def edge_group_ids(self):
        """Gets the edge_group_ids of this CreateSQLJobReq.

        边缘计算组ID列表。

        :return: The edge_group_ids of this CreateSQLJobReq.
        :rtype: list[str]
        """
        return self._edge_group_ids

    @edge_group_ids.setter
    def edge_group_ids(self, edge_group_ids):
        """Sets the edge_group_ids of this CreateSQLJobReq.

        边缘计算组ID列表。

        :param edge_group_ids: The edge_group_ids of this CreateSQLJobReq.
        :type edge_group_ids: list[str]
        """
        self._edge_group_ids = edge_group_ids

    @property
    def dirty_data_strategy(self):
        """Gets the dirty_data_strategy of this CreateSQLJobReq.

        作业脏数据策略。 “2”：保存； “1”：抛出异常； “0”：忽略； 默认值为“0”。

        :return: The dirty_data_strategy of this CreateSQLJobReq.
        :rtype: str
        """
        return self._dirty_data_strategy

    @dirty_data_strategy.setter
    def dirty_data_strategy(self, dirty_data_strategy):
        """Sets the dirty_data_strategy of this CreateSQLJobReq.

        作业脏数据策略。 “2”：保存； “1”：抛出异常； “0”：忽略； 默认值为“0”。

        :param dirty_data_strategy: The dirty_data_strategy of this CreateSQLJobReq.
        :type dirty_data_strategy: str
        """
        self._dirty_data_strategy = dirty_data_strategy

    @property
    def udf_jar_url(self):
        """Gets the udf_jar_url of this CreateSQLJobReq.

        用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入。

        :return: The udf_jar_url of this CreateSQLJobReq.
        :rtype: str
        """
        return self._udf_jar_url

    @udf_jar_url.setter
    def udf_jar_url(self, udf_jar_url):
        """Sets the udf_jar_url of this CreateSQLJobReq.

        用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入。

        :param udf_jar_url: The udf_jar_url of this CreateSQLJobReq.
        :type udf_jar_url: str
        """
        self._udf_jar_url = udf_jar_url

    @property
    def manager_cu_number(self):
        """Gets the manager_cu_number of this CreateSQLJobReq.

        用户为作业选择的管理单元（jobmanager）CU数量，默认值为“1”。

        :return: The manager_cu_number of this CreateSQLJobReq.
        :rtype: int
        """
        return self._manager_cu_number

    @manager_cu_number.setter
    def manager_cu_number(self, manager_cu_number):
        """Sets the manager_cu_number of this CreateSQLJobReq.

        用户为作业选择的管理单元（jobmanager）CU数量，默认值为“1”。

        :param manager_cu_number: The manager_cu_number of this CreateSQLJobReq.
        :type manager_cu_number: int
        """
        self._manager_cu_number = manager_cu_number

    @property
    def tm_cus(self):
        """Gets the tm_cus of this CreateSQLJobReq.

        每个taskmanager的CU数，默认值为“1”。

        :return: The tm_cus of this CreateSQLJobReq.
        :rtype: int
        """
        return self._tm_cus

    @tm_cus.setter
    def tm_cus(self, tm_cus):
        """Sets the tm_cus of this CreateSQLJobReq.

        每个taskmanager的CU数，默认值为“1”。

        :param tm_cus: The tm_cus of this CreateSQLJobReq.
        :type tm_cus: int
        """
        self._tm_cus = tm_cus

    @property
    def tm_slot_num(self):
        """Gets the tm_slot_num of this CreateSQLJobReq.

        每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”

        :return: The tm_slot_num of this CreateSQLJobReq.
        :rtype: int
        """
        return self._tm_slot_num

    @tm_slot_num.setter
    def tm_slot_num(self, tm_slot_num):
        """Sets the tm_slot_num of this CreateSQLJobReq.

        每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”

        :param tm_slot_num: The tm_slot_num of this CreateSQLJobReq.
        :type tm_slot_num: int
        """
        self._tm_slot_num = tm_slot_num

    @property
    def tags(self):
        """Gets the tags of this CreateSQLJobReq.

        标签

        :return: The tags of this CreateSQLJobReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateSQLJobReq.

        标签

        :param tags: The tags of this CreateSQLJobReq.
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        self._tags = tags

    @property
    def resume_checkpoint(self):
        """Gets the resume_checkpoint of this CreateSQLJobReq.

        异常重启是否从checkpoint恢复。

        :return: The resume_checkpoint of this CreateSQLJobReq.
        :rtype: bool
        """
        return self._resume_checkpoint

    @resume_checkpoint.setter
    def resume_checkpoint(self, resume_checkpoint):
        """Sets the resume_checkpoint of this CreateSQLJobReq.

        异常重启是否从checkpoint恢复。

        :param resume_checkpoint: The resume_checkpoint of this CreateSQLJobReq.
        :type resume_checkpoint: bool
        """
        self._resume_checkpoint = resume_checkpoint

    @property
    def resume_max_num(self):
        """Gets the resume_max_num of this CreateSQLJobReq.

        异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。

        :return: The resume_max_num of this CreateSQLJobReq.
        :rtype: int
        """
        return self._resume_max_num

    @resume_max_num.setter
    def resume_max_num(self, resume_max_num):
        """Sets the resume_max_num of this CreateSQLJobReq.

        异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。

        :param resume_max_num: The resume_max_num of this CreateSQLJobReq.
        :type resume_max_num: int
        """
        self._resume_max_num = resume_max_num

    @property
    def runtime_config(self):
        """Gets the runtime_config of this CreateSQLJobReq.

        Flink作业运行时自定义优化参数。

        :return: The runtime_config of this CreateSQLJobReq.
        :rtype: str
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        """Sets the runtime_config of this CreateSQLJobReq.

        Flink作业运行时自定义优化参数。

        :param runtime_config: The runtime_config of this CreateSQLJobReq.
        :type runtime_config: str
        """
        self._runtime_config = runtime_config

    @property
    def flink_version(self):
        """Gets the flink_version of this CreateSQLJobReq.

        Flink版本。当前只支持1.10和1.12。

        :return: The flink_version of this CreateSQLJobReq.
        :rtype: str
        """
        return self._flink_version

    @flink_version.setter
    def flink_version(self, flink_version):
        """Sets the flink_version of this CreateSQLJobReq.

        Flink版本。当前只支持1.10和1.12。

        :param flink_version: The flink_version of this CreateSQLJobReq.
        :type flink_version: str
        """
        self._flink_version = flink_version

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
        if not isinstance(other, CreateSQLJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
