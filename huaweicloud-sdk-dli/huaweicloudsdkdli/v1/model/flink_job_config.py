# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkJobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checkpoint_enabled': 'bool',
        'checkpoint_mode': 'str',
        'checkpoint_interval': 'int',
        'log_enabled': 'bool',
        'obs_bucket': 'str',
        'smn_topic': 'str',
        'edge_group_ids': 'list[str]',
        'root_id': 'int',
        'manager_cu_number': 'int',
        'cu_number': 'int',
        'parallel_number': 'int',
        'restart_when_exception': 'bool',
        'idle_state_retention': 'int',
        'udf_jar_url': 'str',
        'dirty_data_strategy': 'str',
        'entrypoint': 'str',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]',
        'executor_number': 'int',
        'executor_cu_number': 'int',
        'execution_agency_urn': 'str',
        'resume_checkpoint': 'bool',
        'runtime_config': 'str',
        'graph_editor_enabled': 'bool',
        'graph_editor_data': 'str',
        'resume_max_num': 'int',
        'checkpoint_path': 'str',
        'config_url': 'str',
        'tm_cus': 'int',
        'tm_slot_num': 'int',
        'image': 'str',
        'feature': 'str',
        'flink_version': 'str',
        'operator_config': 'str',
        'static_estimator_config': 'str',
        'real_cu_number': 'int'
    }

    attribute_map = {
        'checkpoint_enabled': 'checkpoint_enabled',
        'checkpoint_mode': 'checkpoint_mode',
        'checkpoint_interval': 'checkpoint_interval',
        'log_enabled': 'log_enabled',
        'obs_bucket': 'obs_bucket',
        'smn_topic': 'smn_topic',
        'edge_group_ids': 'edge_group_ids',
        'root_id': 'root_id',
        'manager_cu_number': 'manager_cu_number',
        'cu_number': 'cu_number',
        'parallel_number': 'parallel_number',
        'restart_when_exception': 'restart_when_exception',
        'idle_state_retention': 'idle_state_retention',
        'udf_jar_url': 'udf_jar_url',
        'dirty_data_strategy': 'dirty_data_strategy',
        'entrypoint': 'entrypoint',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files',
        'executor_number': 'executor_number',
        'executor_cu_number': 'executor_cu_number',
        'execution_agency_urn': 'execution_agency_urn',
        'resume_checkpoint': 'resume_checkpoint',
        'runtime_config': 'runtime_config',
        'graph_editor_enabled': 'graph_editor_enabled',
        'graph_editor_data': 'graph_editor_data',
        'resume_max_num': 'resume_max_num',
        'checkpoint_path': 'checkpoint_path',
        'config_url': 'config_url',
        'tm_cus': 'tm_cus',
        'tm_slot_num': 'tm_slot_num',
        'image': 'image',
        'feature': 'feature',
        'flink_version': 'flink_version',
        'operator_config': 'operator_config',
        'static_estimator_config': 'static_estimator_config',
        'real_cu_number': 'real_cu_number'
    }

    def __init__(self, checkpoint_enabled=None, checkpoint_mode=None, checkpoint_interval=None, log_enabled=None, obs_bucket=None, smn_topic=None, edge_group_ids=None, root_id=None, manager_cu_number=None, cu_number=None, parallel_number=None, restart_when_exception=None, idle_state_retention=None, udf_jar_url=None, dirty_data_strategy=None, entrypoint=None, dependency_jars=None, dependency_files=None, executor_number=None, executor_cu_number=None, execution_agency_urn=None, resume_checkpoint=None, runtime_config=None, graph_editor_enabled=None, graph_editor_data=None, resume_max_num=None, checkpoint_path=None, config_url=None, tm_cus=None, tm_slot_num=None, image=None, feature=None, flink_version=None, operator_config=None, static_estimator_config=None, real_cu_number=None):
        r"""FlinkJobConfig

        The model defined in huaweicloud sdk

        :param checkpoint_enabled: 参数解释:  是否开启作业自动快照功能 示例: false 约束限制:  无 取值范围: true,false 默认取值: false
        :type checkpoint_enabled: bool
        :param checkpoint_mode: 参数解释:  快照模式 示例: exactly_once 约束限制:  无 取值范围: exactly_once（数据只被消费一次） at_least_once（数据至少被消费一次） 默认取值: 无
        :type checkpoint_mode: str
        :param checkpoint_interval: 参数解释:  快照时间间隔, 单位为秒 示例: 10 约束限制:  无 取值范围: 无 默认取值: 10
        :type checkpoint_interval: int
        :param log_enabled: 参数解释:  是否启用日志存储 示例: false 约束限制:  无 取值范围: true,false 默认取值: false
        :type log_enabled: bool
        :param obs_bucket: 参数解释:  OBS桶名 示例: obs-demo 约束限制:  无 取值范围: 无 默认取值: 无
        :type obs_bucket: str
        :param smn_topic: 参数解释:  当作业异常时，向该SMN主题推送告警信息 示例: cs_job_exception 约束限制:  无 取值范围: 无 默认取值: 无
        :type smn_topic: str
        :param edge_group_ids: 参数解释:  边缘计算组ID列表 示例: 62de1e1c-066e-48a8-a79d-f461a31b2ee1,2eb00f85-99f2-4144-bcb7-d39ff47f9002 约束限制:  无 取值范围: 无 默认取值: 无
        :type edge_group_ids: list[str]
        :param root_id: 参数解释:  父作业ID 示例: 11 约束限制:  无 取值范围: 无 默认取值: 无
        :type root_id: int
        :param manager_cu_number: 参数解释:  管理单元CU数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type manager_cu_number: int
        :param cu_number: 参数解释:  用户为作业选择的CU数量 示例: 2 约束限制:  无 取值范围: [2,400] 默认取值: 2
        :type cu_number: int
        :param parallel_number: 参数解释:  用户设置的作业并行数， “show_detail”为“true”时独有 示例: 1 约束限制:  无 取值范围: [1,2000] 默认取值: 1
        :type parallel_number: int
        :param restart_when_exception: 参数解释:  是否开启异常重启功能 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无
        :type restart_when_exception: bool
        :param idle_state_retention: 参数解释:  空闲状态过期周期 示例: 3600 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type idle_state_retention: int
        :param udf_jar_url: 参数解释:  用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入 示例: obs://cs-append/jar/udf/flink-1.13-demo-1.0-udf.jar obs://onlyci-7/flink/udx.jar 约束限制:  无 取值范围: 无 默认取值: 无
        :type udf_jar_url: str
        :param dirty_data_strategy: 参数解释:  作业脏数据策略 示例: 0 约束限制:  无 取值范围: 0（忽略） 1（抛出异常） 2:obsDir（保存，obsDir表示脏数据存储路径） 默认取值: 无
        :type dirty_data_strategy: str
        :param entrypoint: 参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包 示例: obs://test/demo/WindowJoin.jar 约束限制:  无 取值范围: 无 默认取值: 无
        :type entrypoint: str
        :param dependency_jars: 参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包 示例: [\&quot;zsdas/wordcount.jar\&quot;,\&quot;ygj/flink-dis-to-kafka-v5.jar\&quot;] 约束限制:  无 取值范围: 无 默认取值: 无
        :type dependency_jars: list[str]
        :param dependency_files: 参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件 示例: [\&quot;zsdas/wordcount.jar\&quot;,\&quot;ygj/flink-dis-to-kafka-v5.jar\&quot;] 约束限制:  无 取值范围: 无 默认取值: 无
        :type dependency_files: list[str]
        :param executor_number: 参数解释:  作业使用计算节点个数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type executor_number: int
        :param executor_cu_number: 参数解释:  计算节点cu数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type executor_cu_number: int
        :param execution_agency_urn: 参数解释:  授权给DLI的委托名。Flink1.15版本时支持配置该参数。 示例: agency 约束限制:  无 取值范围: 无 默认取值: 无
        :type execution_agency_urn: str
        :param resume_checkpoint: 参数解释:  异常自动重启时，是否从最新checkpoint恢复，默认false 示例: 0 约束限制:  无 取值范围: true,false 默认取值: false
        :type resume_checkpoint: bool
        :param runtime_config: 参数解释: Flink作业运行时自定义优化参数 示例: [{\\\&quot;key\\\&quot;:\\\&quot;high-availability\\\&quot;,\\\&quot;value\\\&quot;:\\\&quot;org.apache.flink.kubernetes.highavailability.KubernetesHaServicesFactory\\\&quot; },{ \\\&quot;key\\\&quot;:\\\&quot;kubernetes.jobmanager.replicas\\\&quot;,\\\&quot;value\\\&quot;:\\\&quot;2\\\&quot; },{ \\\&quot;key\\\&quot;:\\\&quot;high-availability.storageDir\\\&quot;,\\\&quot;value\\\&quot;:\\\&quot;obs://fz-test/test\\\&quot;}] 约束限制:  无 取值范围: 无 默认取值: 无
        :type runtime_config: str
        :param graph_editor_enabled: 参数解释: 流图编辑开关 示例: false 约束限制:  无 取值范围: 无 默认取值: false
        :type graph_editor_enabled: bool
        :param graph_editor_data: 参数解释: 流图编辑数据 约束限制:  无 取值范围: 无 默认取值: 无
        :type graph_editor_data: str
        :param resume_max_num: 参数解释: 异常重试最大次数。-1代表无限 示例: -1 约束限制:  无 取值范围: 无 默认取值: 无
        :type resume_max_num: int
        :param checkpoint_path: 参数解释: 检查点保存路径 示例: obs://cwk/checkpoint/ 约束限制:  无 取值范围: 无 默认取值: 无
        :type checkpoint_path: str
        :param config_url: 参数解释: 用户上传的config包OBS路径。 示例: obs://bucket-62099355b894428e8916573ae635f1f9/di-flink/lib/client.jks,obs://bucket-62099355b894428e8916573ae635f1f9/di-flink/lib/client.jks 约束限制:  无 取值范围: 无 默认取值: 无
        :type config_url: str
        :param tm_cus: 参数解释: 单TM所占CU数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type tm_cus: int
        :param tm_slot_num: 参数解释: 单TM Slot数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type tm_slot_num: int
        :param image: 参数解释: 自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像 示例: dli/spark:2.4.8 约束限制:  无 取值范围: 无 默认取值: 无
        :type image: str
        :param feature: 参数解释: 自定义作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像 示例: basic 约束限制:  无 取值范围: basic：表示使用DLI提供的基础Flink镜像 custom：表示使用用户自定义的Flink镜像 默认取值: 无
        :type feature: str
        :param flink_version: 参数解释: Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本 示例: 1.17 约束限制:  无 取值范围: 无 默认取值: 无
        :type flink_version: str
        :param operator_config: 参数解释: 各算子并行度参数，以json的形式展示各算子id和并行度 示例: &#39;{\&quot;operator_list\&quot;:[{\&quot;id\&quot;:\&quot;0a448493b4782967b150582570326227\&quot;,\&quot;parallelism\&quot;:1},{\&quot;id\&quot;:\&quot;6d2677a0ecc3fd8df0b72ec675edf8f4\&quot;,\&quot;parallelism\&quot;:1},{\&quot;id\&quot;:\&quot;ea632d67b7d595e5b851708ae9ad79d6\&quot;,\&quot;parallelism\&quot;:1},{\&quot;id\&quot;:\&quot;ddb598ad156ed281023ba4eebbe487e3\&quot;,\&quot;parallelism\&quot;:1},{\&quot;id\&quot;:\&quot;bc764cd8ddf7a0cff126f51c16239658\&quot;,\&quot;parallelism\&quot;:1}]}&#39; 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无
        :type operator_config: str
        :param static_estimator_config: 参数解释: 静态流图资源预估参数，以json的形式展示 示例: &#39;{\&quot;operator_list\&quot;:[{\&quot;id\&quot;:\&quot;0a448493b4782967b150582570326227\&quot;,\&quot;parallelism\&quot;:1},{\&quot;id\&quot;:\&quot;6d2677a0ecc3fd8df0b72ec675edf8f4\&quot;,\&quot;parallelism\&quot;:1},{\&quot;id\&quot;:\&quot;ea632d67b7d595e5b851708ae9ad79d6\&quot;,\&quot;parallelism\&quot;:1},{\&quot;id\&quot;:\&quot;ddb598ad156ed281023ba4eebbe487e3\&quot;,\&quot;parallelism\&quot;:1},{\&quot;id\&quot;:\&quot;bc764cd8ddf7a0cff126f51c16239658\&quot;,\&quot;parallelism\&quot;:1}]}&#39; 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无
        :type static_estimator_config: str
        :param real_cu_number: 参数解释: 实际使用的CU数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 0
        :type real_cu_number: int
        """
        
        

        self._checkpoint_enabled = None
        self._checkpoint_mode = None
        self._checkpoint_interval = None
        self._log_enabled = None
        self._obs_bucket = None
        self._smn_topic = None
        self._edge_group_ids = None
        self._root_id = None
        self._manager_cu_number = None
        self._cu_number = None
        self._parallel_number = None
        self._restart_when_exception = None
        self._idle_state_retention = None
        self._udf_jar_url = None
        self._dirty_data_strategy = None
        self._entrypoint = None
        self._dependency_jars = None
        self._dependency_files = None
        self._executor_number = None
        self._executor_cu_number = None
        self._execution_agency_urn = None
        self._resume_checkpoint = None
        self._runtime_config = None
        self._graph_editor_enabled = None
        self._graph_editor_data = None
        self._resume_max_num = None
        self._checkpoint_path = None
        self._config_url = None
        self._tm_cus = None
        self._tm_slot_num = None
        self._image = None
        self._feature = None
        self._flink_version = None
        self._operator_config = None
        self._static_estimator_config = None
        self._real_cu_number = None
        self.discriminator = None

        if checkpoint_enabled is not None:
            self.checkpoint_enabled = checkpoint_enabled
        if checkpoint_mode is not None:
            self.checkpoint_mode = checkpoint_mode
        if checkpoint_interval is not None:
            self.checkpoint_interval = checkpoint_interval
        if log_enabled is not None:
            self.log_enabled = log_enabled
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if smn_topic is not None:
            self.smn_topic = smn_topic
        if edge_group_ids is not None:
            self.edge_group_ids = edge_group_ids
        if root_id is not None:
            self.root_id = root_id
        if manager_cu_number is not None:
            self.manager_cu_number = manager_cu_number
        if cu_number is not None:
            self.cu_number = cu_number
        if parallel_number is not None:
            self.parallel_number = parallel_number
        if restart_when_exception is not None:
            self.restart_when_exception = restart_when_exception
        if idle_state_retention is not None:
            self.idle_state_retention = idle_state_retention
        if udf_jar_url is not None:
            self.udf_jar_url = udf_jar_url
        if dirty_data_strategy is not None:
            self.dirty_data_strategy = dirty_data_strategy
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if executor_number is not None:
            self.executor_number = executor_number
        if executor_cu_number is not None:
            self.executor_cu_number = executor_cu_number
        if execution_agency_urn is not None:
            self.execution_agency_urn = execution_agency_urn
        if resume_checkpoint is not None:
            self.resume_checkpoint = resume_checkpoint
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if graph_editor_enabled is not None:
            self.graph_editor_enabled = graph_editor_enabled
        if graph_editor_data is not None:
            self.graph_editor_data = graph_editor_data
        if resume_max_num is not None:
            self.resume_max_num = resume_max_num
        if checkpoint_path is not None:
            self.checkpoint_path = checkpoint_path
        if config_url is not None:
            self.config_url = config_url
        if tm_cus is not None:
            self.tm_cus = tm_cus
        if tm_slot_num is not None:
            self.tm_slot_num = tm_slot_num
        if image is not None:
            self.image = image
        if feature is not None:
            self.feature = feature
        if flink_version is not None:
            self.flink_version = flink_version
        if operator_config is not None:
            self.operator_config = operator_config
        if static_estimator_config is not None:
            self.static_estimator_config = static_estimator_config
        if real_cu_number is not None:
            self.real_cu_number = real_cu_number

    @property
    def checkpoint_enabled(self):
        r"""Gets the checkpoint_enabled of this FlinkJobConfig.

        参数解释:  是否开启作业自动快照功能 示例: false 约束限制:  无 取值范围: true,false 默认取值: false

        :return: The checkpoint_enabled of this FlinkJobConfig.
        :rtype: bool
        """
        return self._checkpoint_enabled

    @checkpoint_enabled.setter
    def checkpoint_enabled(self, checkpoint_enabled):
        r"""Sets the checkpoint_enabled of this FlinkJobConfig.

        参数解释:  是否开启作业自动快照功能 示例: false 约束限制:  无 取值范围: true,false 默认取值: false

        :param checkpoint_enabled: The checkpoint_enabled of this FlinkJobConfig.
        :type checkpoint_enabled: bool
        """
        self._checkpoint_enabled = checkpoint_enabled

    @property
    def checkpoint_mode(self):
        r"""Gets the checkpoint_mode of this FlinkJobConfig.

        参数解释:  快照模式 示例: exactly_once 约束限制:  无 取值范围: exactly_once（数据只被消费一次） at_least_once（数据至少被消费一次） 默认取值: 无

        :return: The checkpoint_mode of this FlinkJobConfig.
        :rtype: str
        """
        return self._checkpoint_mode

    @checkpoint_mode.setter
    def checkpoint_mode(self, checkpoint_mode):
        r"""Sets the checkpoint_mode of this FlinkJobConfig.

        参数解释:  快照模式 示例: exactly_once 约束限制:  无 取值范围: exactly_once（数据只被消费一次） at_least_once（数据至少被消费一次） 默认取值: 无

        :param checkpoint_mode: The checkpoint_mode of this FlinkJobConfig.
        :type checkpoint_mode: str
        """
        self._checkpoint_mode = checkpoint_mode

    @property
    def checkpoint_interval(self):
        r"""Gets the checkpoint_interval of this FlinkJobConfig.

        参数解释:  快照时间间隔, 单位为秒 示例: 10 约束限制:  无 取值范围: 无 默认取值: 10

        :return: The checkpoint_interval of this FlinkJobConfig.
        :rtype: int
        """
        return self._checkpoint_interval

    @checkpoint_interval.setter
    def checkpoint_interval(self, checkpoint_interval):
        r"""Sets the checkpoint_interval of this FlinkJobConfig.

        参数解释:  快照时间间隔, 单位为秒 示例: 10 约束限制:  无 取值范围: 无 默认取值: 10

        :param checkpoint_interval: The checkpoint_interval of this FlinkJobConfig.
        :type checkpoint_interval: int
        """
        self._checkpoint_interval = checkpoint_interval

    @property
    def log_enabled(self):
        r"""Gets the log_enabled of this FlinkJobConfig.

        参数解释:  是否启用日志存储 示例: false 约束限制:  无 取值范围: true,false 默认取值: false

        :return: The log_enabled of this FlinkJobConfig.
        :rtype: bool
        """
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, log_enabled):
        r"""Sets the log_enabled of this FlinkJobConfig.

        参数解释:  是否启用日志存储 示例: false 约束限制:  无 取值范围: true,false 默认取值: false

        :param log_enabled: The log_enabled of this FlinkJobConfig.
        :type log_enabled: bool
        """
        self._log_enabled = log_enabled

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this FlinkJobConfig.

        参数解释:  OBS桶名 示例: obs-demo 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The obs_bucket of this FlinkJobConfig.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this FlinkJobConfig.

        参数解释:  OBS桶名 示例: obs-demo 约束限制:  无 取值范围: 无 默认取值: 无

        :param obs_bucket: The obs_bucket of this FlinkJobConfig.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def smn_topic(self):
        r"""Gets the smn_topic of this FlinkJobConfig.

        参数解释:  当作业异常时，向该SMN主题推送告警信息 示例: cs_job_exception 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The smn_topic of this FlinkJobConfig.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        r"""Sets the smn_topic of this FlinkJobConfig.

        参数解释:  当作业异常时，向该SMN主题推送告警信息 示例: cs_job_exception 约束限制:  无 取值范围: 无 默认取值: 无

        :param smn_topic: The smn_topic of this FlinkJobConfig.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

    @property
    def edge_group_ids(self):
        r"""Gets the edge_group_ids of this FlinkJobConfig.

        参数解释:  边缘计算组ID列表 示例: 62de1e1c-066e-48a8-a79d-f461a31b2ee1,2eb00f85-99f2-4144-bcb7-d39ff47f9002 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The edge_group_ids of this FlinkJobConfig.
        :rtype: list[str]
        """
        return self._edge_group_ids

    @edge_group_ids.setter
    def edge_group_ids(self, edge_group_ids):
        r"""Sets the edge_group_ids of this FlinkJobConfig.

        参数解释:  边缘计算组ID列表 示例: 62de1e1c-066e-48a8-a79d-f461a31b2ee1,2eb00f85-99f2-4144-bcb7-d39ff47f9002 约束限制:  无 取值范围: 无 默认取值: 无

        :param edge_group_ids: The edge_group_ids of this FlinkJobConfig.
        :type edge_group_ids: list[str]
        """
        self._edge_group_ids = edge_group_ids

    @property
    def root_id(self):
        r"""Gets the root_id of this FlinkJobConfig.

        参数解释:  父作业ID 示例: 11 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The root_id of this FlinkJobConfig.
        :rtype: int
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this FlinkJobConfig.

        参数解释:  父作业ID 示例: 11 约束限制:  无 取值范围: 无 默认取值: 无

        :param root_id: The root_id of this FlinkJobConfig.
        :type root_id: int
        """
        self._root_id = root_id

    @property
    def manager_cu_number(self):
        r"""Gets the manager_cu_number of this FlinkJobConfig.

        参数解释:  管理单元CU数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The manager_cu_number of this FlinkJobConfig.
        :rtype: int
        """
        return self._manager_cu_number

    @manager_cu_number.setter
    def manager_cu_number(self, manager_cu_number):
        r"""Sets the manager_cu_number of this FlinkJobConfig.

        参数解释:  管理单元CU数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param manager_cu_number: The manager_cu_number of this FlinkJobConfig.
        :type manager_cu_number: int
        """
        self._manager_cu_number = manager_cu_number

    @property
    def cu_number(self):
        r"""Gets the cu_number of this FlinkJobConfig.

        参数解释:  用户为作业选择的CU数量 示例: 2 约束限制:  无 取值范围: [2,400] 默认取值: 2

        :return: The cu_number of this FlinkJobConfig.
        :rtype: int
        """
        return self._cu_number

    @cu_number.setter
    def cu_number(self, cu_number):
        r"""Sets the cu_number of this FlinkJobConfig.

        参数解释:  用户为作业选择的CU数量 示例: 2 约束限制:  无 取值范围: [2,400] 默认取值: 2

        :param cu_number: The cu_number of this FlinkJobConfig.
        :type cu_number: int
        """
        self._cu_number = cu_number

    @property
    def parallel_number(self):
        r"""Gets the parallel_number of this FlinkJobConfig.

        参数解释:  用户设置的作业并行数， “show_detail”为“true”时独有 示例: 1 约束限制:  无 取值范围: [1,2000] 默认取值: 1

        :return: The parallel_number of this FlinkJobConfig.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        r"""Sets the parallel_number of this FlinkJobConfig.

        参数解释:  用户设置的作业并行数， “show_detail”为“true”时独有 示例: 1 约束限制:  无 取值范围: [1,2000] 默认取值: 1

        :param parallel_number: The parallel_number of this FlinkJobConfig.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def restart_when_exception(self):
        r"""Gets the restart_when_exception of this FlinkJobConfig.

        参数解释:  是否开启异常重启功能 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无

        :return: The restart_when_exception of this FlinkJobConfig.
        :rtype: bool
        """
        return self._restart_when_exception

    @restart_when_exception.setter
    def restart_when_exception(self, restart_when_exception):
        r"""Sets the restart_when_exception of this FlinkJobConfig.

        参数解释:  是否开启异常重启功能 示例: false 约束限制:  无 取值范围: true,false 默认取值: 无

        :param restart_when_exception: The restart_when_exception of this FlinkJobConfig.
        :type restart_when_exception: bool
        """
        self._restart_when_exception = restart_when_exception

    @property
    def idle_state_retention(self):
        r"""Gets the idle_state_retention of this FlinkJobConfig.

        参数解释:  空闲状态过期周期 示例: 3600 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The idle_state_retention of this FlinkJobConfig.
        :rtype: int
        """
        return self._idle_state_retention

    @idle_state_retention.setter
    def idle_state_retention(self, idle_state_retention):
        r"""Sets the idle_state_retention of this FlinkJobConfig.

        参数解释:  空闲状态过期周期 示例: 3600 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param idle_state_retention: The idle_state_retention of this FlinkJobConfig.
        :type idle_state_retention: int
        """
        self._idle_state_retention = idle_state_retention

    @property
    def udf_jar_url(self):
        r"""Gets the udf_jar_url of this FlinkJobConfig.

        参数解释:  用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入 示例: obs://cs-append/jar/udf/flink-1.13-demo-1.0-udf.jar obs://onlyci-7/flink/udx.jar 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The udf_jar_url of this FlinkJobConfig.
        :rtype: str
        """
        return self._udf_jar_url

    @udf_jar_url.setter
    def udf_jar_url(self, udf_jar_url):
        r"""Sets the udf_jar_url of this FlinkJobConfig.

        参数解释:  用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入 示例: obs://cs-append/jar/udf/flink-1.13-demo-1.0-udf.jar obs://onlyci-7/flink/udx.jar 约束限制:  无 取值范围: 无 默认取值: 无

        :param udf_jar_url: The udf_jar_url of this FlinkJobConfig.
        :type udf_jar_url: str
        """
        self._udf_jar_url = udf_jar_url

    @property
    def dirty_data_strategy(self):
        r"""Gets the dirty_data_strategy of this FlinkJobConfig.

        参数解释:  作业脏数据策略 示例: 0 约束限制:  无 取值范围: 0（忽略） 1（抛出异常） 2:obsDir（保存，obsDir表示脏数据存储路径） 默认取值: 无

        :return: The dirty_data_strategy of this FlinkJobConfig.
        :rtype: str
        """
        return self._dirty_data_strategy

    @dirty_data_strategy.setter
    def dirty_data_strategy(self, dirty_data_strategy):
        r"""Sets the dirty_data_strategy of this FlinkJobConfig.

        参数解释:  作业脏数据策略 示例: 0 约束限制:  无 取值范围: 0（忽略） 1（抛出异常） 2:obsDir（保存，obsDir表示脏数据存储路径） 默认取值: 无

        :param dirty_data_strategy: The dirty_data_strategy of this FlinkJobConfig.
        :type dirty_data_strategy: str
        """
        self._dirty_data_strategy = dirty_data_strategy

    @property
    def entrypoint(self):
        r"""Gets the entrypoint of this FlinkJobConfig.

        参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包 示例: obs://test/demo/WindowJoin.jar 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The entrypoint of this FlinkJobConfig.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        r"""Sets the entrypoint of this FlinkJobConfig.

        参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包 示例: obs://test/demo/WindowJoin.jar 约束限制:  无 取值范围: 无 默认取值: 无

        :param entrypoint: The entrypoint of this FlinkJobConfig.
        :type entrypoint: str
        """
        self._entrypoint = entrypoint

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this FlinkJobConfig.

        参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包 示例: [\"zsdas/wordcount.jar\",\"ygj/flink-dis-to-kafka-v5.jar\"] 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The dependency_jars of this FlinkJobConfig.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this FlinkJobConfig.

        参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包 示例: [\"zsdas/wordcount.jar\",\"ygj/flink-dis-to-kafka-v5.jar\"] 约束限制:  无 取值范围: 无 默认取值: 无

        :param dependency_jars: The dependency_jars of this FlinkJobConfig.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this FlinkJobConfig.

        参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件 示例: [\"zsdas/wordcount.jar\",\"ygj/flink-dis-to-kafka-v5.jar\"] 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The dependency_files of this FlinkJobConfig.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this FlinkJobConfig.

        参数解释:  用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件 示例: [\"zsdas/wordcount.jar\",\"ygj/flink-dis-to-kafka-v5.jar\"] 约束限制:  无 取值范围: 无 默认取值: 无

        :param dependency_files: The dependency_files of this FlinkJobConfig.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def executor_number(self):
        r"""Gets the executor_number of this FlinkJobConfig.

        参数解释:  作业使用计算节点个数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The executor_number of this FlinkJobConfig.
        :rtype: int
        """
        return self._executor_number

    @executor_number.setter
    def executor_number(self, executor_number):
        r"""Sets the executor_number of this FlinkJobConfig.

        参数解释:  作业使用计算节点个数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param executor_number: The executor_number of this FlinkJobConfig.
        :type executor_number: int
        """
        self._executor_number = executor_number

    @property
    def executor_cu_number(self):
        r"""Gets the executor_cu_number of this FlinkJobConfig.

        参数解释:  计算节点cu数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The executor_cu_number of this FlinkJobConfig.
        :rtype: int
        """
        return self._executor_cu_number

    @executor_cu_number.setter
    def executor_cu_number(self, executor_cu_number):
        r"""Sets the executor_cu_number of this FlinkJobConfig.

        参数解释:  计算节点cu数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param executor_cu_number: The executor_cu_number of this FlinkJobConfig.
        :type executor_cu_number: int
        """
        self._executor_cu_number = executor_cu_number

    @property
    def execution_agency_urn(self):
        r"""Gets the execution_agency_urn of this FlinkJobConfig.

        参数解释:  授权给DLI的委托名。Flink1.15版本时支持配置该参数。 示例: agency 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The execution_agency_urn of this FlinkJobConfig.
        :rtype: str
        """
        return self._execution_agency_urn

    @execution_agency_urn.setter
    def execution_agency_urn(self, execution_agency_urn):
        r"""Sets the execution_agency_urn of this FlinkJobConfig.

        参数解释:  授权给DLI的委托名。Flink1.15版本时支持配置该参数。 示例: agency 约束限制:  无 取值范围: 无 默认取值: 无

        :param execution_agency_urn: The execution_agency_urn of this FlinkJobConfig.
        :type execution_agency_urn: str
        """
        self._execution_agency_urn = execution_agency_urn

    @property
    def resume_checkpoint(self):
        r"""Gets the resume_checkpoint of this FlinkJobConfig.

        参数解释:  异常自动重启时，是否从最新checkpoint恢复，默认false 示例: 0 约束限制:  无 取值范围: true,false 默认取值: false

        :return: The resume_checkpoint of this FlinkJobConfig.
        :rtype: bool
        """
        return self._resume_checkpoint

    @resume_checkpoint.setter
    def resume_checkpoint(self, resume_checkpoint):
        r"""Sets the resume_checkpoint of this FlinkJobConfig.

        参数解释:  异常自动重启时，是否从最新checkpoint恢复，默认false 示例: 0 约束限制:  无 取值范围: true,false 默认取值: false

        :param resume_checkpoint: The resume_checkpoint of this FlinkJobConfig.
        :type resume_checkpoint: bool
        """
        self._resume_checkpoint = resume_checkpoint

    @property
    def runtime_config(self):
        r"""Gets the runtime_config of this FlinkJobConfig.

        参数解释: Flink作业运行时自定义优化参数 示例: [{\\\"key\\\":\\\"high-availability\\\",\\\"value\\\":\\\"org.apache.flink.kubernetes.highavailability.KubernetesHaServicesFactory\\\" },{ \\\"key\\\":\\\"kubernetes.jobmanager.replicas\\\",\\\"value\\\":\\\"2\\\" },{ \\\"key\\\":\\\"high-availability.storageDir\\\",\\\"value\\\":\\\"obs://fz-test/test\\\"}] 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The runtime_config of this FlinkJobConfig.
        :rtype: str
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        r"""Sets the runtime_config of this FlinkJobConfig.

        参数解释: Flink作业运行时自定义优化参数 示例: [{\\\"key\\\":\\\"high-availability\\\",\\\"value\\\":\\\"org.apache.flink.kubernetes.highavailability.KubernetesHaServicesFactory\\\" },{ \\\"key\\\":\\\"kubernetes.jobmanager.replicas\\\",\\\"value\\\":\\\"2\\\" },{ \\\"key\\\":\\\"high-availability.storageDir\\\",\\\"value\\\":\\\"obs://fz-test/test\\\"}] 约束限制:  无 取值范围: 无 默认取值: 无

        :param runtime_config: The runtime_config of this FlinkJobConfig.
        :type runtime_config: str
        """
        self._runtime_config = runtime_config

    @property
    def graph_editor_enabled(self):
        r"""Gets the graph_editor_enabled of this FlinkJobConfig.

        参数解释: 流图编辑开关 示例: false 约束限制:  无 取值范围: 无 默认取值: false

        :return: The graph_editor_enabled of this FlinkJobConfig.
        :rtype: bool
        """
        return self._graph_editor_enabled

    @graph_editor_enabled.setter
    def graph_editor_enabled(self, graph_editor_enabled):
        r"""Sets the graph_editor_enabled of this FlinkJobConfig.

        参数解释: 流图编辑开关 示例: false 约束限制:  无 取值范围: 无 默认取值: false

        :param graph_editor_enabled: The graph_editor_enabled of this FlinkJobConfig.
        :type graph_editor_enabled: bool
        """
        self._graph_editor_enabled = graph_editor_enabled

    @property
    def graph_editor_data(self):
        r"""Gets the graph_editor_data of this FlinkJobConfig.

        参数解释: 流图编辑数据 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The graph_editor_data of this FlinkJobConfig.
        :rtype: str
        """
        return self._graph_editor_data

    @graph_editor_data.setter
    def graph_editor_data(self, graph_editor_data):
        r"""Sets the graph_editor_data of this FlinkJobConfig.

        参数解释: 流图编辑数据 约束限制:  无 取值范围: 无 默认取值: 无

        :param graph_editor_data: The graph_editor_data of this FlinkJobConfig.
        :type graph_editor_data: str
        """
        self._graph_editor_data = graph_editor_data

    @property
    def resume_max_num(self):
        r"""Gets the resume_max_num of this FlinkJobConfig.

        参数解释: 异常重试最大次数。-1代表无限 示例: -1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The resume_max_num of this FlinkJobConfig.
        :rtype: int
        """
        return self._resume_max_num

    @resume_max_num.setter
    def resume_max_num(self, resume_max_num):
        r"""Sets the resume_max_num of this FlinkJobConfig.

        参数解释: 异常重试最大次数。-1代表无限 示例: -1 约束限制:  无 取值范围: 无 默认取值: 无

        :param resume_max_num: The resume_max_num of this FlinkJobConfig.
        :type resume_max_num: int
        """
        self._resume_max_num = resume_max_num

    @property
    def checkpoint_path(self):
        r"""Gets the checkpoint_path of this FlinkJobConfig.

        参数解释: 检查点保存路径 示例: obs://cwk/checkpoint/ 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The checkpoint_path of this FlinkJobConfig.
        :rtype: str
        """
        return self._checkpoint_path

    @checkpoint_path.setter
    def checkpoint_path(self, checkpoint_path):
        r"""Sets the checkpoint_path of this FlinkJobConfig.

        参数解释: 检查点保存路径 示例: obs://cwk/checkpoint/ 约束限制:  无 取值范围: 无 默认取值: 无

        :param checkpoint_path: The checkpoint_path of this FlinkJobConfig.
        :type checkpoint_path: str
        """
        self._checkpoint_path = checkpoint_path

    @property
    def config_url(self):
        r"""Gets the config_url of this FlinkJobConfig.

        参数解释: 用户上传的config包OBS路径。 示例: obs://bucket-62099355b894428e8916573ae635f1f9/di-flink/lib/client.jks,obs://bucket-62099355b894428e8916573ae635f1f9/di-flink/lib/client.jks 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The config_url of this FlinkJobConfig.
        :rtype: str
        """
        return self._config_url

    @config_url.setter
    def config_url(self, config_url):
        r"""Sets the config_url of this FlinkJobConfig.

        参数解释: 用户上传的config包OBS路径。 示例: obs://bucket-62099355b894428e8916573ae635f1f9/di-flink/lib/client.jks,obs://bucket-62099355b894428e8916573ae635f1f9/di-flink/lib/client.jks 约束限制:  无 取值范围: 无 默认取值: 无

        :param config_url: The config_url of this FlinkJobConfig.
        :type config_url: str
        """
        self._config_url = config_url

    @property
    def tm_cus(self):
        r"""Gets the tm_cus of this FlinkJobConfig.

        参数解释: 单TM所占CU数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The tm_cus of this FlinkJobConfig.
        :rtype: int
        """
        return self._tm_cus

    @tm_cus.setter
    def tm_cus(self, tm_cus):
        r"""Sets the tm_cus of this FlinkJobConfig.

        参数解释: 单TM所占CU数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param tm_cus: The tm_cus of this FlinkJobConfig.
        :type tm_cus: int
        """
        self._tm_cus = tm_cus

    @property
    def tm_slot_num(self):
        r"""Gets the tm_slot_num of this FlinkJobConfig.

        参数解释: 单TM Slot数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The tm_slot_num of this FlinkJobConfig.
        :rtype: int
        """
        return self._tm_slot_num

    @tm_slot_num.setter
    def tm_slot_num(self, tm_slot_num):
        r"""Sets the tm_slot_num of this FlinkJobConfig.

        参数解释: 单TM Slot数 示例: 1 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param tm_slot_num: The tm_slot_num of this FlinkJobConfig.
        :type tm_slot_num: int
        """
        self._tm_slot_num = tm_slot_num

    @property
    def image(self):
        r"""Gets the image of this FlinkJobConfig.

        参数解释: 自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像 示例: dli/spark:2.4.8 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The image of this FlinkJobConfig.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this FlinkJobConfig.

        参数解释: 自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像 示例: dli/spark:2.4.8 约束限制:  无 取值范围: 无 默认取值: 无

        :param image: The image of this FlinkJobConfig.
        :type image: str
        """
        self._image = image

    @property
    def feature(self):
        r"""Gets the feature of this FlinkJobConfig.

        参数解释: 自定义作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像 示例: basic 约束限制:  无 取值范围: basic：表示使用DLI提供的基础Flink镜像 custom：表示使用用户自定义的Flink镜像 默认取值: 无

        :return: The feature of this FlinkJobConfig.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this FlinkJobConfig.

        参数解释: 自定义作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像 示例: basic 约束限制:  无 取值范围: basic：表示使用DLI提供的基础Flink镜像 custom：表示使用用户自定义的Flink镜像 默认取值: 无

        :param feature: The feature of this FlinkJobConfig.
        :type feature: str
        """
        self._feature = feature

    @property
    def flink_version(self):
        r"""Gets the flink_version of this FlinkJobConfig.

        参数解释: Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本 示例: 1.17 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The flink_version of this FlinkJobConfig.
        :rtype: str
        """
        return self._flink_version

    @flink_version.setter
    def flink_version(self, flink_version):
        r"""Sets the flink_version of this FlinkJobConfig.

        参数解释: Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本 示例: 1.17 约束限制:  无 取值范围: 无 默认取值: 无

        :param flink_version: The flink_version of this FlinkJobConfig.
        :type flink_version: str
        """
        self._flink_version = flink_version

    @property
    def operator_config(self):
        r"""Gets the operator_config of this FlinkJobConfig.

        参数解释: 各算子并行度参数，以json的形式展示各算子id和并行度 示例: '{\"operator_list\":[{\"id\":\"0a448493b4782967b150582570326227\",\"parallelism\":1},{\"id\":\"6d2677a0ecc3fd8df0b72ec675edf8f4\",\"parallelism\":1},{\"id\":\"ea632d67b7d595e5b851708ae9ad79d6\",\"parallelism\":1},{\"id\":\"ddb598ad156ed281023ba4eebbe487e3\",\"parallelism\":1},{\"id\":\"bc764cd8ddf7a0cff126f51c16239658\",\"parallelism\":1}]}' 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :return: The operator_config of this FlinkJobConfig.
        :rtype: str
        """
        return self._operator_config

    @operator_config.setter
    def operator_config(self, operator_config):
        r"""Sets the operator_config of this FlinkJobConfig.

        参数解释: 各算子并行度参数，以json的形式展示各算子id和并行度 示例: '{\"operator_list\":[{\"id\":\"0a448493b4782967b150582570326227\",\"parallelism\":1},{\"id\":\"6d2677a0ecc3fd8df0b72ec675edf8f4\",\"parallelism\":1},{\"id\":\"ea632d67b7d595e5b851708ae9ad79d6\",\"parallelism\":1},{\"id\":\"ddb598ad156ed281023ba4eebbe487e3\",\"parallelism\":1},{\"id\":\"bc764cd8ddf7a0cff126f51c16239658\",\"parallelism\":1}]}' 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :param operator_config: The operator_config of this FlinkJobConfig.
        :type operator_config: str
        """
        self._operator_config = operator_config

    @property
    def static_estimator_config(self):
        r"""Gets the static_estimator_config of this FlinkJobConfig.

        参数解释: 静态流图资源预估参数，以json的形式展示 示例: '{\"operator_list\":[{\"id\":\"0a448493b4782967b150582570326227\",\"parallelism\":1},{\"id\":\"6d2677a0ecc3fd8df0b72ec675edf8f4\",\"parallelism\":1},{\"id\":\"ea632d67b7d595e5b851708ae9ad79d6\",\"parallelism\":1},{\"id\":\"ddb598ad156ed281023ba4eebbe487e3\",\"parallelism\":1},{\"id\":\"bc764cd8ddf7a0cff126f51c16239658\",\"parallelism\":1}]}' 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :return: The static_estimator_config of this FlinkJobConfig.
        :rtype: str
        """
        return self._static_estimator_config

    @static_estimator_config.setter
    def static_estimator_config(self, static_estimator_config):
        r"""Sets the static_estimator_config of this FlinkJobConfig.

        参数解释: 静态流图资源预估参数，以json的形式展示 示例: '{\"operator_list\":[{\"id\":\"0a448493b4782967b150582570326227\",\"parallelism\":1},{\"id\":\"6d2677a0ecc3fd8df0b72ec675edf8f4\",\"parallelism\":1},{\"id\":\"ea632d67b7d595e5b851708ae9ad79d6\",\"parallelism\":1},{\"id\":\"ddb598ad156ed281023ba4eebbe487e3\",\"parallelism\":1},{\"id\":\"bc764cd8ddf7a0cff126f51c16239658\",\"parallelism\":1}]}' 约束限制:  符合Json格式的字符串 取值范围: 无 默认取值: 无

        :param static_estimator_config: The static_estimator_config of this FlinkJobConfig.
        :type static_estimator_config: str
        """
        self._static_estimator_config = static_estimator_config

    @property
    def real_cu_number(self):
        r"""Gets the real_cu_number of this FlinkJobConfig.

        参数解释: 实际使用的CU数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 0

        :return: The real_cu_number of this FlinkJobConfig.
        :rtype: int
        """
        return self._real_cu_number

    @real_cu_number.setter
    def real_cu_number(self, real_cu_number):
        r"""Sets the real_cu_number of this FlinkJobConfig.

        参数解释: 实际使用的CU数 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 0

        :param real_cu_number: The real_cu_number of this FlinkJobConfig.
        :type real_cu_number: int
        """
        self._real_cu_number = real_cu_number

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
        if not isinstance(other, FlinkJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
