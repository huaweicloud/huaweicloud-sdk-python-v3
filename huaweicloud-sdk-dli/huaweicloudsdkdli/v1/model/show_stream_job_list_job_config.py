# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStreamJobListJobConfig:

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
        'resume_checkpoint': 'bool'
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
        'resume_checkpoint': 'resume_checkpoint'
    }

    def __init__(self, checkpoint_enabled=None, checkpoint_mode=None, checkpoint_interval=None, log_enabled=None, obs_bucket=None, smn_topic=None, edge_group_ids=None, root_id=None, manager_cu_number=None, cu_number=None, parallel_number=None, restart_when_exception=None, idle_state_retention=None, udf_jar_url=None, dirty_data_strategy=None, entrypoint=None, dependency_jars=None, dependency_files=None, executor_number=None, executor_cu_number=None, resume_checkpoint=None):
        """ShowStreamJobListJobConfig

        The model defined in huaweicloud sdk

        :param checkpoint_enabled: 是否开启作业自动快照功能。 开启：true； 关闭：false； 默认：false。
        :type checkpoint_enabled: bool
        :param checkpoint_mode: 快照模式： exactly_once：数据只被消费一次。 at_least_once：数据至少被消费一次。 默认值为exactly_once。
        :type checkpoint_mode: str
        :param checkpoint_interval: 快照时间间隔, 单位为秒，默认值为10。
        :type checkpoint_interval: int
        :param log_enabled: 是否启用日志存储。默认为false。
        :type log_enabled: bool
        :param obs_bucket: OBS桶名。
        :type obs_bucket: str
        :param smn_topic: 当作业异常时，向该SMN主题推送告警信息。
        :type smn_topic: str
        :param edge_group_ids: 边缘计算组ID列表。
        :type edge_group_ids: list[str]
        :param root_id: 父作业ID。
        :type root_id: int
        :param manager_cu_number: 管理单元CU数。默认为1。
        :type manager_cu_number: int
        :param cu_number: 用户为作业选择的CU数量, “show_detail”。默认为2。
        :type cu_number: int
        :param parallel_number: 用户设置的作业并行数， “show_detail”为“true”时独有。默认值为1。 最小值：1，最大值：2000。 
        :type parallel_number: int
        :param restart_when_exception: 是否开启异常重启功能。
        :type restart_when_exception: bool
        :param idle_state_retention: 空闲状态过期周期。
        :type idle_state_retention: int
        :param udf_jar_url: 用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入。
        :type udf_jar_url: str
        :param dirty_data_strategy: 作业脏数据策略。 “2:obs-wan-wulan3/jobs”：保存 “1”：抛出异常 “0”：忽略
        :type dirty_data_strategy: str
        :param entrypoint: 用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包.
        :type entrypoint: str
        :param dependency_jars: 用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包
        :type dependency_jars: list[str]
        :param dependency_files: 用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件.
        :type dependency_files: list[str]
        :param executor_number: 作业使用计算节点个数
        :type executor_number: int
        :param executor_cu_number: 计算节点cu数
        :type executor_cu_number: int
        :param resume_checkpoint: 异常自动重启时，是否从最新checkpoint恢复，默认false
        :type resume_checkpoint: bool
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
        self._resume_checkpoint = None
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
        if resume_checkpoint is not None:
            self.resume_checkpoint = resume_checkpoint

    @property
    def checkpoint_enabled(self):
        """Gets the checkpoint_enabled of this ShowStreamJobListJobConfig.

        是否开启作业自动快照功能。 开启：true； 关闭：false； 默认：false。

        :return: The checkpoint_enabled of this ShowStreamJobListJobConfig.
        :rtype: bool
        """
        return self._checkpoint_enabled

    @checkpoint_enabled.setter
    def checkpoint_enabled(self, checkpoint_enabled):
        """Sets the checkpoint_enabled of this ShowStreamJobListJobConfig.

        是否开启作业自动快照功能。 开启：true； 关闭：false； 默认：false。

        :param checkpoint_enabled: The checkpoint_enabled of this ShowStreamJobListJobConfig.
        :type checkpoint_enabled: bool
        """
        self._checkpoint_enabled = checkpoint_enabled

    @property
    def checkpoint_mode(self):
        """Gets the checkpoint_mode of this ShowStreamJobListJobConfig.

        快照模式： exactly_once：数据只被消费一次。 at_least_once：数据至少被消费一次。 默认值为exactly_once。

        :return: The checkpoint_mode of this ShowStreamJobListJobConfig.
        :rtype: str
        """
        return self._checkpoint_mode

    @checkpoint_mode.setter
    def checkpoint_mode(self, checkpoint_mode):
        """Sets the checkpoint_mode of this ShowStreamJobListJobConfig.

        快照模式： exactly_once：数据只被消费一次。 at_least_once：数据至少被消费一次。 默认值为exactly_once。

        :param checkpoint_mode: The checkpoint_mode of this ShowStreamJobListJobConfig.
        :type checkpoint_mode: str
        """
        self._checkpoint_mode = checkpoint_mode

    @property
    def checkpoint_interval(self):
        """Gets the checkpoint_interval of this ShowStreamJobListJobConfig.

        快照时间间隔, 单位为秒，默认值为10。

        :return: The checkpoint_interval of this ShowStreamJobListJobConfig.
        :rtype: int
        """
        return self._checkpoint_interval

    @checkpoint_interval.setter
    def checkpoint_interval(self, checkpoint_interval):
        """Sets the checkpoint_interval of this ShowStreamJobListJobConfig.

        快照时间间隔, 单位为秒，默认值为10。

        :param checkpoint_interval: The checkpoint_interval of this ShowStreamJobListJobConfig.
        :type checkpoint_interval: int
        """
        self._checkpoint_interval = checkpoint_interval

    @property
    def log_enabled(self):
        """Gets the log_enabled of this ShowStreamJobListJobConfig.

        是否启用日志存储。默认为false。

        :return: The log_enabled of this ShowStreamJobListJobConfig.
        :rtype: bool
        """
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, log_enabled):
        """Sets the log_enabled of this ShowStreamJobListJobConfig.

        是否启用日志存储。默认为false。

        :param log_enabled: The log_enabled of this ShowStreamJobListJobConfig.
        :type log_enabled: bool
        """
        self._log_enabled = log_enabled

    @property
    def obs_bucket(self):
        """Gets the obs_bucket of this ShowStreamJobListJobConfig.

        OBS桶名。

        :return: The obs_bucket of this ShowStreamJobListJobConfig.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        """Sets the obs_bucket of this ShowStreamJobListJobConfig.

        OBS桶名。

        :param obs_bucket: The obs_bucket of this ShowStreamJobListJobConfig.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def smn_topic(self):
        """Gets the smn_topic of this ShowStreamJobListJobConfig.

        当作业异常时，向该SMN主题推送告警信息。

        :return: The smn_topic of this ShowStreamJobListJobConfig.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        """Sets the smn_topic of this ShowStreamJobListJobConfig.

        当作业异常时，向该SMN主题推送告警信息。

        :param smn_topic: The smn_topic of this ShowStreamJobListJobConfig.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

    @property
    def edge_group_ids(self):
        """Gets the edge_group_ids of this ShowStreamJobListJobConfig.

        边缘计算组ID列表。

        :return: The edge_group_ids of this ShowStreamJobListJobConfig.
        :rtype: list[str]
        """
        return self._edge_group_ids

    @edge_group_ids.setter
    def edge_group_ids(self, edge_group_ids):
        """Sets the edge_group_ids of this ShowStreamJobListJobConfig.

        边缘计算组ID列表。

        :param edge_group_ids: The edge_group_ids of this ShowStreamJobListJobConfig.
        :type edge_group_ids: list[str]
        """
        self._edge_group_ids = edge_group_ids

    @property
    def root_id(self):
        """Gets the root_id of this ShowStreamJobListJobConfig.

        父作业ID。

        :return: The root_id of this ShowStreamJobListJobConfig.
        :rtype: int
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this ShowStreamJobListJobConfig.

        父作业ID。

        :param root_id: The root_id of this ShowStreamJobListJobConfig.
        :type root_id: int
        """
        self._root_id = root_id

    @property
    def manager_cu_number(self):
        """Gets the manager_cu_number of this ShowStreamJobListJobConfig.

        管理单元CU数。默认为1。

        :return: The manager_cu_number of this ShowStreamJobListJobConfig.
        :rtype: int
        """
        return self._manager_cu_number

    @manager_cu_number.setter
    def manager_cu_number(self, manager_cu_number):
        """Sets the manager_cu_number of this ShowStreamJobListJobConfig.

        管理单元CU数。默认为1。

        :param manager_cu_number: The manager_cu_number of this ShowStreamJobListJobConfig.
        :type manager_cu_number: int
        """
        self._manager_cu_number = manager_cu_number

    @property
    def cu_number(self):
        """Gets the cu_number of this ShowStreamJobListJobConfig.

        用户为作业选择的CU数量, “show_detail”。默认为2。

        :return: The cu_number of this ShowStreamJobListJobConfig.
        :rtype: int
        """
        return self._cu_number

    @cu_number.setter
    def cu_number(self, cu_number):
        """Sets the cu_number of this ShowStreamJobListJobConfig.

        用户为作业选择的CU数量, “show_detail”。默认为2。

        :param cu_number: The cu_number of this ShowStreamJobListJobConfig.
        :type cu_number: int
        """
        self._cu_number = cu_number

    @property
    def parallel_number(self):
        """Gets the parallel_number of this ShowStreamJobListJobConfig.

        用户设置的作业并行数， “show_detail”为“true”时独有。默认值为1。 最小值：1，最大值：2000。 

        :return: The parallel_number of this ShowStreamJobListJobConfig.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        """Sets the parallel_number of this ShowStreamJobListJobConfig.

        用户设置的作业并行数， “show_detail”为“true”时独有。默认值为1。 最小值：1，最大值：2000。 

        :param parallel_number: The parallel_number of this ShowStreamJobListJobConfig.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def restart_when_exception(self):
        """Gets the restart_when_exception of this ShowStreamJobListJobConfig.

        是否开启异常重启功能。

        :return: The restart_when_exception of this ShowStreamJobListJobConfig.
        :rtype: bool
        """
        return self._restart_when_exception

    @restart_when_exception.setter
    def restart_when_exception(self, restart_when_exception):
        """Sets the restart_when_exception of this ShowStreamJobListJobConfig.

        是否开启异常重启功能。

        :param restart_when_exception: The restart_when_exception of this ShowStreamJobListJobConfig.
        :type restart_when_exception: bool
        """
        self._restart_when_exception = restart_when_exception

    @property
    def idle_state_retention(self):
        """Gets the idle_state_retention of this ShowStreamJobListJobConfig.

        空闲状态过期周期。

        :return: The idle_state_retention of this ShowStreamJobListJobConfig.
        :rtype: int
        """
        return self._idle_state_retention

    @idle_state_retention.setter
    def idle_state_retention(self, idle_state_retention):
        """Sets the idle_state_retention of this ShowStreamJobListJobConfig.

        空闲状态过期周期。

        :param idle_state_retention: The idle_state_retention of this ShowStreamJobListJobConfig.
        :type idle_state_retention: int
        """
        self._idle_state_retention = idle_state_retention

    @property
    def udf_jar_url(self):
        """Gets the udf_jar_url of this ShowStreamJobListJobConfig.

        用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入。

        :return: The udf_jar_url of this ShowStreamJobListJobConfig.
        :rtype: str
        """
        return self._udf_jar_url

    @udf_jar_url.setter
    def udf_jar_url(self, udf_jar_url):
        """Sets the udf_jar_url of this ShowStreamJobListJobConfig.

        用户已上传到DLI资源管理系统的资源包名，用户sql作业的udf jar通过该参数传入。

        :param udf_jar_url: The udf_jar_url of this ShowStreamJobListJobConfig.
        :type udf_jar_url: str
        """
        self._udf_jar_url = udf_jar_url

    @property
    def dirty_data_strategy(self):
        """Gets the dirty_data_strategy of this ShowStreamJobListJobConfig.

        作业脏数据策略。 “2:obs-wan-wulan3/jobs”：保存 “1”：抛出异常 “0”：忽略

        :return: The dirty_data_strategy of this ShowStreamJobListJobConfig.
        :rtype: str
        """
        return self._dirty_data_strategy

    @dirty_data_strategy.setter
    def dirty_data_strategy(self, dirty_data_strategy):
        """Sets the dirty_data_strategy of this ShowStreamJobListJobConfig.

        作业脏数据策略。 “2:obs-wan-wulan3/jobs”：保存 “1”：抛出异常 “0”：忽略

        :param dirty_data_strategy: The dirty_data_strategy of this ShowStreamJobListJobConfig.
        :type dirty_data_strategy: str
        """
        self._dirty_data_strategy = dirty_data_strategy

    @property
    def entrypoint(self):
        """Gets the entrypoint of this ShowStreamJobListJobConfig.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包.

        :return: The entrypoint of this ShowStreamJobListJobConfig.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this ShowStreamJobListJobConfig.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包.

        :param entrypoint: The entrypoint of this ShowStreamJobListJobConfig.
        :type entrypoint: str
        """
        self._entrypoint = entrypoint

    @property
    def dependency_jars(self):
        """Gets the dependency_jars of this ShowStreamJobListJobConfig.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包

        :return: The dependency_jars of this ShowStreamJobListJobConfig.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        """Sets the dependency_jars of this ShowStreamJobListJobConfig.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包

        :param dependency_jars: The dependency_jars of this ShowStreamJobListJobConfig.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        """Gets the dependency_files of this ShowStreamJobListJobConfig.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件.

        :return: The dependency_files of this ShowStreamJobListJobConfig.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        """Sets the dependency_files of this ShowStreamJobListJobConfig.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件.

        :param dependency_files: The dependency_files of this ShowStreamJobListJobConfig.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def executor_number(self):
        """Gets the executor_number of this ShowStreamJobListJobConfig.

        作业使用计算节点个数

        :return: The executor_number of this ShowStreamJobListJobConfig.
        :rtype: int
        """
        return self._executor_number

    @executor_number.setter
    def executor_number(self, executor_number):
        """Sets the executor_number of this ShowStreamJobListJobConfig.

        作业使用计算节点个数

        :param executor_number: The executor_number of this ShowStreamJobListJobConfig.
        :type executor_number: int
        """
        self._executor_number = executor_number

    @property
    def executor_cu_number(self):
        """Gets the executor_cu_number of this ShowStreamJobListJobConfig.

        计算节点cu数

        :return: The executor_cu_number of this ShowStreamJobListJobConfig.
        :rtype: int
        """
        return self._executor_cu_number

    @executor_cu_number.setter
    def executor_cu_number(self, executor_cu_number):
        """Sets the executor_cu_number of this ShowStreamJobListJobConfig.

        计算节点cu数

        :param executor_cu_number: The executor_cu_number of this ShowStreamJobListJobConfig.
        :type executor_cu_number: int
        """
        self._executor_cu_number = executor_cu_number

    @property
    def resume_checkpoint(self):
        """Gets the resume_checkpoint of this ShowStreamJobListJobConfig.

        异常自动重启时，是否从最新checkpoint恢复，默认false

        :return: The resume_checkpoint of this ShowStreamJobListJobConfig.
        :rtype: bool
        """
        return self._resume_checkpoint

    @resume_checkpoint.setter
    def resume_checkpoint(self, resume_checkpoint):
        """Sets the resume_checkpoint of this ShowStreamJobListJobConfig.

        异常自动重启时，是否从最新checkpoint恢复，默认false

        :param resume_checkpoint: The resume_checkpoint of this ShowStreamJobListJobConfig.
        :type resume_checkpoint: bool
        """
        self._resume_checkpoint = resume_checkpoint

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
        if not isinstance(other, ShowStreamJobListJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
