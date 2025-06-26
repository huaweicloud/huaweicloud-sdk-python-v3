# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlinkJarJobRequestBody:

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
        'cu_number': 'int',
        'manager_cu_number': 'int',
        'parallel_number': 'int',
        'log_enabled': 'bool',
        'obs_bucket': 'str',
        'smn_topic': 'str',
        'main_class': 'str',
        'entrypoint_args': 'str',
        'restart_when_exception': 'bool',
        'entrypoint': 'str',
        'dependency_jars': 'list[str]',
        'dependency_files': 'list[str]',
        'tm_cus': 'int',
        'tm_slot_num': 'int',
        'feature': 'str',
        'flink_version': 'str',
        'execution_agency_urn': 'str',
        'image': 'str',
        'resume_checkpoint': 'bool',
        'resume_max_num': 'int',
        'checkpoint_path': 'str',
        'runtime_config': 'str',
        'job_type': 'str',
        'resource_config': 'ResourceConfig',
        'resource_config_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'queue_name': 'queue_name',
        'cu_number': 'cu_number',
        'manager_cu_number': 'manager_cu_number',
        'parallel_number': 'parallel_number',
        'log_enabled': 'log_enabled',
        'obs_bucket': 'obs_bucket',
        'smn_topic': 'smn_topic',
        'main_class': 'main_class',
        'entrypoint_args': 'entrypoint_args',
        'restart_when_exception': 'restart_when_exception',
        'entrypoint': 'entrypoint',
        'dependency_jars': 'dependency_jars',
        'dependency_files': 'dependency_files',
        'tm_cus': 'tm_cus',
        'tm_slot_num': 'tm_slot_num',
        'feature': 'feature',
        'flink_version': 'flink_version',
        'execution_agency_urn': 'execution_agency_urn',
        'image': 'image',
        'resume_checkpoint': 'resume_checkpoint',
        'resume_max_num': 'resume_max_num',
        'checkpoint_path': 'checkpoint_path',
        'runtime_config': 'runtime_config',
        'job_type': 'job_type',
        'resource_config': 'resource_config',
        'resource_config_version': 'resource_config_version'
    }

    def __init__(self, name=None, desc=None, queue_name=None, cu_number=None, manager_cu_number=None, parallel_number=None, log_enabled=None, obs_bucket=None, smn_topic=None, main_class=None, entrypoint_args=None, restart_when_exception=None, entrypoint=None, dependency_jars=None, dependency_files=None, tm_cus=None, tm_slot_num=None, feature=None, flink_version=None, execution_agency_urn=None, image=None, resume_checkpoint=None, resume_max_num=None, checkpoint_path=None, runtime_config=None, job_type=None, resource_config=None, resource_config_version=None):
        r"""UpdateFlinkJarJobRequestBody

        The model defined in huaweicloud sdk

        :param name: 作业名称。长度限制：0-57个字符。
        :type name: str
        :param desc: 作业描述。长度限制：0-2048个字符。
        :type desc: str
        :param queue_name: 队列名称。长度限制：1-128个字符。
        :type queue_name: str
        :param cu_number: 用户为作业选择的CU数量。默认值为2。
        :type cu_number: int
        :param manager_cu_number: 用户为作业选择的管理节点CU数量，对应为flink jobmanager数量。默认为1。
        :type manager_cu_number: int
        :param parallel_number: 用户为作业选择的并发量。默认为1。
        :type parallel_number: int
        :param log_enabled: 是否开启作业日志。 开启：true； 关闭：false； 默认：false。
        :type log_enabled: bool
        :param obs_bucket: 当log_enabled&#x3D;&#x3D;true时，用户授权保存日志的OBS路。
        :type obs_bucket: str
        :param smn_topic: 当作业异常时，向该SMN主题推送告警信息。
        :type smn_topic: str
        :param main_class: 作业入口类。
        :type main_class: str
        :param entrypoint_args: 作业入口类参数，多个参数之间空格分隔。
        :type entrypoint_args: str
        :param restart_when_exception: 是否开启异常重启功能，默认值为“false”。
        :type restart_when_exception: bool
        :param entrypoint: 选择Jar作业程序包。 Jar包的管理方式： 上传OBS管理程序包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理程序包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理&gt;程序包管理”中创建程序包。 Flink1.15版本不推荐DLI管理程序包，Flink1.15版本以上不再支持DLI管理程序包。
        :type entrypoint: str
        :param dependency_jars: 用户自定义的依赖程序包。依赖的相关程序包将会被放置到集群classpath下。 依赖程序包的管理方式： 上传OBS管理依赖程序包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理依赖程序包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理&gt;程序包管理”中创建程序包。 Flink1.15版本不推荐DLI管理依赖程序包，Flink1.15版本以上不再支持DLI管理依赖程序包。
        :type dependency_jars: list[str]
        :param dependency_files: 用户自定义的依赖文件。 依赖文件的管理方式： 上传OBS管理依赖文件：提前将对应的依赖文件上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理依赖文件：提前将对应的依赖文件上传至OBS桶中，并在DLI管理控制台的“数据管理&gt;程序包管理”中创建程序包 Flink1.15版本不推荐DLI管理依赖依赖文件，Flink1.15版本以上不再支持DLI管理依赖依赖文件。
        :type dependency_files: list[str]
        :param tm_cus: 每个taskmanager的CU数，默认值为“1”。
        :type tm_cus: int
        :param tm_slot_num: 每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。
        :type tm_slot_num: int
        :param feature: 作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像。
        :type feature: str
        :param flink_version: Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本。
        :type flink_version: str
        :param execution_agency_urn: 授权给DLI的委托名。Flink1.15版本时支持配置该参数。
        :type execution_agency_urn: str
        :param image: 自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。
        :type image: str
        :param resume_checkpoint: 异常重启是否从checkpoint恢复。
        :type resume_checkpoint: bool
        :param resume_max_num: 异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。
        :type resume_max_num: int
        :param checkpoint_path: 用户Jar中checkpoint的储存地址，不同作业路径需要保持不同。
        :type checkpoint_path: str
        :param runtime_config: Flink作业运行时自定义优化参数。
        :type runtime_config: str
        :param job_type: 作业类型。
        :type job_type: str
        :param resource_config: 
        :type resource_config: :class:`huaweicloudsdkdli.v1.ResourceConfig`
        :param resource_config_version: 资源配置版本。可选值 \&quot;v1\&quot; ,\&quot;v2\&quot;.默认为“v1”。
        :type resource_config_version: str
        """
        
        

        self._name = None
        self._desc = None
        self._queue_name = None
        self._cu_number = None
        self._manager_cu_number = None
        self._parallel_number = None
        self._log_enabled = None
        self._obs_bucket = None
        self._smn_topic = None
        self._main_class = None
        self._entrypoint_args = None
        self._restart_when_exception = None
        self._entrypoint = None
        self._dependency_jars = None
        self._dependency_files = None
        self._tm_cus = None
        self._tm_slot_num = None
        self._feature = None
        self._flink_version = None
        self._execution_agency_urn = None
        self._image = None
        self._resume_checkpoint = None
        self._resume_max_num = None
        self._checkpoint_path = None
        self._runtime_config = None
        self._job_type = None
        self._resource_config = None
        self._resource_config_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if queue_name is not None:
            self.queue_name = queue_name
        if cu_number is not None:
            self.cu_number = cu_number
        if manager_cu_number is not None:
            self.manager_cu_number = manager_cu_number
        if parallel_number is not None:
            self.parallel_number = parallel_number
        if log_enabled is not None:
            self.log_enabled = log_enabled
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if smn_topic is not None:
            self.smn_topic = smn_topic
        if main_class is not None:
            self.main_class = main_class
        if entrypoint_args is not None:
            self.entrypoint_args = entrypoint_args
        if restart_when_exception is not None:
            self.restart_when_exception = restart_when_exception
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars
        if dependency_files is not None:
            self.dependency_files = dependency_files
        if tm_cus is not None:
            self.tm_cus = tm_cus
        if tm_slot_num is not None:
            self.tm_slot_num = tm_slot_num
        if feature is not None:
            self.feature = feature
        if flink_version is not None:
            self.flink_version = flink_version
        if execution_agency_urn is not None:
            self.execution_agency_urn = execution_agency_urn
        if image is not None:
            self.image = image
        if resume_checkpoint is not None:
            self.resume_checkpoint = resume_checkpoint
        if resume_max_num is not None:
            self.resume_max_num = resume_max_num
        if checkpoint_path is not None:
            self.checkpoint_path = checkpoint_path
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if job_type is not None:
            self.job_type = job_type
        if resource_config is not None:
            self.resource_config = resource_config
        if resource_config_version is not None:
            self.resource_config_version = resource_config_version

    @property
    def name(self):
        r"""Gets the name of this UpdateFlinkJarJobRequestBody.

        作业名称。长度限制：0-57个字符。

        :return: The name of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateFlinkJarJobRequestBody.

        作业名称。长度限制：0-57个字符。

        :param name: The name of this UpdateFlinkJarJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this UpdateFlinkJarJobRequestBody.

        作业描述。长度限制：0-2048个字符。

        :return: The desc of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this UpdateFlinkJarJobRequestBody.

        作业描述。长度限制：0-2048个字符。

        :param desc: The desc of this UpdateFlinkJarJobRequestBody.
        :type desc: str
        """
        self._desc = desc

    @property
    def queue_name(self):
        r"""Gets the queue_name of this UpdateFlinkJarJobRequestBody.

        队列名称。长度限制：1-128个字符。

        :return: The queue_name of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this UpdateFlinkJarJobRequestBody.

        队列名称。长度限制：1-128个字符。

        :param queue_name: The queue_name of this UpdateFlinkJarJobRequestBody.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def cu_number(self):
        r"""Gets the cu_number of this UpdateFlinkJarJobRequestBody.

        用户为作业选择的CU数量。默认值为2。

        :return: The cu_number of this UpdateFlinkJarJobRequestBody.
        :rtype: int
        """
        return self._cu_number

    @cu_number.setter
    def cu_number(self, cu_number):
        r"""Sets the cu_number of this UpdateFlinkJarJobRequestBody.

        用户为作业选择的CU数量。默认值为2。

        :param cu_number: The cu_number of this UpdateFlinkJarJobRequestBody.
        :type cu_number: int
        """
        self._cu_number = cu_number

    @property
    def manager_cu_number(self):
        r"""Gets the manager_cu_number of this UpdateFlinkJarJobRequestBody.

        用户为作业选择的管理节点CU数量，对应为flink jobmanager数量。默认为1。

        :return: The manager_cu_number of this UpdateFlinkJarJobRequestBody.
        :rtype: int
        """
        return self._manager_cu_number

    @manager_cu_number.setter
    def manager_cu_number(self, manager_cu_number):
        r"""Sets the manager_cu_number of this UpdateFlinkJarJobRequestBody.

        用户为作业选择的管理节点CU数量，对应为flink jobmanager数量。默认为1。

        :param manager_cu_number: The manager_cu_number of this UpdateFlinkJarJobRequestBody.
        :type manager_cu_number: int
        """
        self._manager_cu_number = manager_cu_number

    @property
    def parallel_number(self):
        r"""Gets the parallel_number of this UpdateFlinkJarJobRequestBody.

        用户为作业选择的并发量。默认为1。

        :return: The parallel_number of this UpdateFlinkJarJobRequestBody.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        r"""Sets the parallel_number of this UpdateFlinkJarJobRequestBody.

        用户为作业选择的并发量。默认为1。

        :param parallel_number: The parallel_number of this UpdateFlinkJarJobRequestBody.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def log_enabled(self):
        r"""Gets the log_enabled of this UpdateFlinkJarJobRequestBody.

        是否开启作业日志。 开启：true； 关闭：false； 默认：false。

        :return: The log_enabled of this UpdateFlinkJarJobRequestBody.
        :rtype: bool
        """
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, log_enabled):
        r"""Sets the log_enabled of this UpdateFlinkJarJobRequestBody.

        是否开启作业日志。 开启：true； 关闭：false； 默认：false。

        :param log_enabled: The log_enabled of this UpdateFlinkJarJobRequestBody.
        :type log_enabled: bool
        """
        self._log_enabled = log_enabled

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this UpdateFlinkJarJobRequestBody.

        当log_enabled==true时，用户授权保存日志的OBS路。

        :return: The obs_bucket of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this UpdateFlinkJarJobRequestBody.

        当log_enabled==true时，用户授权保存日志的OBS路。

        :param obs_bucket: The obs_bucket of this UpdateFlinkJarJobRequestBody.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def smn_topic(self):
        r"""Gets the smn_topic of this UpdateFlinkJarJobRequestBody.

        当作业异常时，向该SMN主题推送告警信息。

        :return: The smn_topic of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        r"""Sets the smn_topic of this UpdateFlinkJarJobRequestBody.

        当作业异常时，向该SMN主题推送告警信息。

        :param smn_topic: The smn_topic of this UpdateFlinkJarJobRequestBody.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

    @property
    def main_class(self):
        r"""Gets the main_class of this UpdateFlinkJarJobRequestBody.

        作业入口类。

        :return: The main_class of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this UpdateFlinkJarJobRequestBody.

        作业入口类。

        :param main_class: The main_class of this UpdateFlinkJarJobRequestBody.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def entrypoint_args(self):
        r"""Gets the entrypoint_args of this UpdateFlinkJarJobRequestBody.

        作业入口类参数，多个参数之间空格分隔。

        :return: The entrypoint_args of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._entrypoint_args

    @entrypoint_args.setter
    def entrypoint_args(self, entrypoint_args):
        r"""Sets the entrypoint_args of this UpdateFlinkJarJobRequestBody.

        作业入口类参数，多个参数之间空格分隔。

        :param entrypoint_args: The entrypoint_args of this UpdateFlinkJarJobRequestBody.
        :type entrypoint_args: str
        """
        self._entrypoint_args = entrypoint_args

    @property
    def restart_when_exception(self):
        r"""Gets the restart_when_exception of this UpdateFlinkJarJobRequestBody.

        是否开启异常重启功能，默认值为“false”。

        :return: The restart_when_exception of this UpdateFlinkJarJobRequestBody.
        :rtype: bool
        """
        return self._restart_when_exception

    @restart_when_exception.setter
    def restart_when_exception(self, restart_when_exception):
        r"""Sets the restart_when_exception of this UpdateFlinkJarJobRequestBody.

        是否开启异常重启功能，默认值为“false”。

        :param restart_when_exception: The restart_when_exception of this UpdateFlinkJarJobRequestBody.
        :type restart_when_exception: bool
        """
        self._restart_when_exception = restart_when_exception

    @property
    def entrypoint(self):
        r"""Gets the entrypoint of this UpdateFlinkJarJobRequestBody.

        选择Jar作业程序包。 Jar包的管理方式： 上传OBS管理程序包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理程序包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理>程序包管理”中创建程序包。 Flink1.15版本不推荐DLI管理程序包，Flink1.15版本以上不再支持DLI管理程序包。

        :return: The entrypoint of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        r"""Sets the entrypoint of this UpdateFlinkJarJobRequestBody.

        选择Jar作业程序包。 Jar包的管理方式： 上传OBS管理程序包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理程序包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理>程序包管理”中创建程序包。 Flink1.15版本不推荐DLI管理程序包，Flink1.15版本以上不再支持DLI管理程序包。

        :param entrypoint: The entrypoint of this UpdateFlinkJarJobRequestBody.
        :type entrypoint: str
        """
        self._entrypoint = entrypoint

    @property
    def dependency_jars(self):
        r"""Gets the dependency_jars of this UpdateFlinkJarJobRequestBody.

        用户自定义的依赖程序包。依赖的相关程序包将会被放置到集群classpath下。 依赖程序包的管理方式： 上传OBS管理依赖程序包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理依赖程序包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理>程序包管理”中创建程序包。 Flink1.15版本不推荐DLI管理依赖程序包，Flink1.15版本以上不再支持DLI管理依赖程序包。

        :return: The dependency_jars of this UpdateFlinkJarJobRequestBody.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        r"""Sets the dependency_jars of this UpdateFlinkJarJobRequestBody.

        用户自定义的依赖程序包。依赖的相关程序包将会被放置到集群classpath下。 依赖程序包的管理方式： 上传OBS管理依赖程序包：提前将对应的Jar包上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理依赖程序包：提前将对应的Jar包上传至OBS桶中，并在DLI管理控制台的“数据管理>程序包管理”中创建程序包。 Flink1.15版本不推荐DLI管理依赖程序包，Flink1.15版本以上不再支持DLI管理依赖程序包。

        :param dependency_jars: The dependency_jars of this UpdateFlinkJarJobRequestBody.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        r"""Gets the dependency_files of this UpdateFlinkJarJobRequestBody.

        用户自定义的依赖文件。 依赖文件的管理方式： 上传OBS管理依赖文件：提前将对应的依赖文件上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理依赖文件：提前将对应的依赖文件上传至OBS桶中，并在DLI管理控制台的“数据管理>程序包管理”中创建程序包 Flink1.15版本不推荐DLI管理依赖依赖文件，Flink1.15版本以上不再支持DLI管理依赖依赖文件。

        :return: The dependency_files of this UpdateFlinkJarJobRequestBody.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        r"""Sets the dependency_files of this UpdateFlinkJarJobRequestBody.

        用户自定义的依赖文件。 依赖文件的管理方式： 上传OBS管理依赖文件：提前将对应的依赖文件上传至OBS桶中。并在此处选择对应的OBS路径。 上传DLI管理依赖文件：提前将对应的依赖文件上传至OBS桶中，并在DLI管理控制台的“数据管理>程序包管理”中创建程序包 Flink1.15版本不推荐DLI管理依赖依赖文件，Flink1.15版本以上不再支持DLI管理依赖依赖文件。

        :param dependency_files: The dependency_files of this UpdateFlinkJarJobRequestBody.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def tm_cus(self):
        r"""Gets the tm_cus of this UpdateFlinkJarJobRequestBody.

        每个taskmanager的CU数，默认值为“1”。

        :return: The tm_cus of this UpdateFlinkJarJobRequestBody.
        :rtype: int
        """
        return self._tm_cus

    @tm_cus.setter
    def tm_cus(self, tm_cus):
        r"""Sets the tm_cus of this UpdateFlinkJarJobRequestBody.

        每个taskmanager的CU数，默认值为“1”。

        :param tm_cus: The tm_cus of this UpdateFlinkJarJobRequestBody.
        :type tm_cus: int
        """
        self._tm_cus = tm_cus

    @property
    def tm_slot_num(self):
        r"""Gets the tm_slot_num of this UpdateFlinkJarJobRequestBody.

        每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。

        :return: The tm_slot_num of this UpdateFlinkJarJobRequestBody.
        :rtype: int
        """
        return self._tm_slot_num

    @tm_slot_num.setter
    def tm_slot_num(self, tm_slot_num):
        r"""Sets the tm_slot_num of this UpdateFlinkJarJobRequestBody.

        每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。

        :param tm_slot_num: The tm_slot_num of this UpdateFlinkJarJobRequestBody.
        :type tm_slot_num: int
        """
        self._tm_slot_num = tm_slot_num

    @property
    def feature(self):
        r"""Gets the feature of this UpdateFlinkJarJobRequestBody.

        作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像。

        :return: The feature of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this UpdateFlinkJarJobRequestBody.

        作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像。

        :param feature: The feature of this UpdateFlinkJarJobRequestBody.
        :type feature: str
        """
        self._feature = feature

    @property
    def flink_version(self):
        r"""Gets the flink_version of this UpdateFlinkJarJobRequestBody.

        Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本。

        :return: The flink_version of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._flink_version

    @flink_version.setter
    def flink_version(self, flink_version):
        r"""Sets the flink_version of this UpdateFlinkJarJobRequestBody.

        Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本。

        :param flink_version: The flink_version of this UpdateFlinkJarJobRequestBody.
        :type flink_version: str
        """
        self._flink_version = flink_version

    @property
    def execution_agency_urn(self):
        r"""Gets the execution_agency_urn of this UpdateFlinkJarJobRequestBody.

        授权给DLI的委托名。Flink1.15版本时支持配置该参数。

        :return: The execution_agency_urn of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._execution_agency_urn

    @execution_agency_urn.setter
    def execution_agency_urn(self, execution_agency_urn):
        r"""Sets the execution_agency_urn of this UpdateFlinkJarJobRequestBody.

        授权给DLI的委托名。Flink1.15版本时支持配置该参数。

        :param execution_agency_urn: The execution_agency_urn of this UpdateFlinkJarJobRequestBody.
        :type execution_agency_urn: str
        """
        self._execution_agency_urn = execution_agency_urn

    @property
    def image(self):
        r"""Gets the image of this UpdateFlinkJarJobRequestBody.

        自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。

        :return: The image of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this UpdateFlinkJarJobRequestBody.

        自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。

        :param image: The image of this UpdateFlinkJarJobRequestBody.
        :type image: str
        """
        self._image = image

    @property
    def resume_checkpoint(self):
        r"""Gets the resume_checkpoint of this UpdateFlinkJarJobRequestBody.

        异常重启是否从checkpoint恢复。

        :return: The resume_checkpoint of this UpdateFlinkJarJobRequestBody.
        :rtype: bool
        """
        return self._resume_checkpoint

    @resume_checkpoint.setter
    def resume_checkpoint(self, resume_checkpoint):
        r"""Sets the resume_checkpoint of this UpdateFlinkJarJobRequestBody.

        异常重启是否从checkpoint恢复。

        :param resume_checkpoint: The resume_checkpoint of this UpdateFlinkJarJobRequestBody.
        :type resume_checkpoint: bool
        """
        self._resume_checkpoint = resume_checkpoint

    @property
    def resume_max_num(self):
        r"""Gets the resume_max_num of this UpdateFlinkJarJobRequestBody.

        异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。

        :return: The resume_max_num of this UpdateFlinkJarJobRequestBody.
        :rtype: int
        """
        return self._resume_max_num

    @resume_max_num.setter
    def resume_max_num(self, resume_max_num):
        r"""Sets the resume_max_num of this UpdateFlinkJarJobRequestBody.

        异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。

        :param resume_max_num: The resume_max_num of this UpdateFlinkJarJobRequestBody.
        :type resume_max_num: int
        """
        self._resume_max_num = resume_max_num

    @property
    def checkpoint_path(self):
        r"""Gets the checkpoint_path of this UpdateFlinkJarJobRequestBody.

        用户Jar中checkpoint的储存地址，不同作业路径需要保持不同。

        :return: The checkpoint_path of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._checkpoint_path

    @checkpoint_path.setter
    def checkpoint_path(self, checkpoint_path):
        r"""Sets the checkpoint_path of this UpdateFlinkJarJobRequestBody.

        用户Jar中checkpoint的储存地址，不同作业路径需要保持不同。

        :param checkpoint_path: The checkpoint_path of this UpdateFlinkJarJobRequestBody.
        :type checkpoint_path: str
        """
        self._checkpoint_path = checkpoint_path

    @property
    def runtime_config(self):
        r"""Gets the runtime_config of this UpdateFlinkJarJobRequestBody.

        Flink作业运行时自定义优化参数。

        :return: The runtime_config of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        r"""Sets the runtime_config of this UpdateFlinkJarJobRequestBody.

        Flink作业运行时自定义优化参数。

        :param runtime_config: The runtime_config of this UpdateFlinkJarJobRequestBody.
        :type runtime_config: str
        """
        self._runtime_config = runtime_config

    @property
    def job_type(self):
        r"""Gets the job_type of this UpdateFlinkJarJobRequestBody.

        作业类型。

        :return: The job_type of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this UpdateFlinkJarJobRequestBody.

        作业类型。

        :param job_type: The job_type of this UpdateFlinkJarJobRequestBody.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def resource_config(self):
        r"""Gets the resource_config of this UpdateFlinkJarJobRequestBody.

        :return: The resource_config of this UpdateFlinkJarJobRequestBody.
        :rtype: :class:`huaweicloudsdkdli.v1.ResourceConfig`
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        r"""Sets the resource_config of this UpdateFlinkJarJobRequestBody.

        :param resource_config: The resource_config of this UpdateFlinkJarJobRequestBody.
        :type resource_config: :class:`huaweicloudsdkdli.v1.ResourceConfig`
        """
        self._resource_config = resource_config

    @property
    def resource_config_version(self):
        r"""Gets the resource_config_version of this UpdateFlinkJarJobRequestBody.

        资源配置版本。可选值 \"v1\" ,\"v2\".默认为“v1”。

        :return: The resource_config_version of this UpdateFlinkJarJobRequestBody.
        :rtype: str
        """
        return self._resource_config_version

    @resource_config_version.setter
    def resource_config_version(self, resource_config_version):
        r"""Sets the resource_config_version of this UpdateFlinkJarJobRequestBody.

        资源配置版本。可选值 \"v1\" ,\"v2\".默认为“v1”。

        :param resource_config_version: The resource_config_version of this UpdateFlinkJarJobRequestBody.
        :type resource_config_version: str
        """
        self._resource_config_version = resource_config_version

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
        if not isinstance(other, UpdateFlinkJarJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
