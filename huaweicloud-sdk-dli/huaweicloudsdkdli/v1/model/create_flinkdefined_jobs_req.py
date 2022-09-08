# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlinkdefinedJobsReq:

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
        'flink_version': 'str',
        'image': 'str',
        'tm_slot_num': 'int',
        'tm_cus': 'int',
        'feature': 'str',
        'resume_checkpoint': 'bool',
        'resume_max_num': 'int',
        'checkpoint_path': 'str',
        'runtime_config': 'str',
        'tags': 'list[TmsTagEntity]'
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
        'flink_version': 'flink_version',
        'image': 'image',
        'tm_slot_num': 'tm_slot_num',
        'tm_cus': 'tm_cus',
        'feature': 'feature',
        'resume_checkpoint': 'resume_checkpoint',
        'resume_max_num': 'resume_max_num',
        'checkpoint_path': 'checkpoint_path',
        'runtime_config': 'runtime_config',
        'tags': 'tags'
    }

    def __init__(self, name=None, desc=None, queue_name=None, cu_number=None, manager_cu_number=None, parallel_number=None, log_enabled=None, obs_bucket=None, smn_topic=None, main_class=None, entrypoint_args=None, restart_when_exception=None, entrypoint=None, dependency_jars=None, dependency_files=None, flink_version=None, image=None, tm_slot_num=None, tm_cus=None, feature=None, resume_checkpoint=None, resume_max_num=None, checkpoint_path=None, runtime_config=None, tags=None):
        """CreateFlinkdefinedJobsReq

        The model defined in huaweicloud sdk

        :param name: 作业名称。长度限制：0-57个字符。
        :type name: str
        :param desc: 作业描述。长度限制：0-512个字符。
        :type desc: str
        :param queue_name: 队列名称。长度限制：1-128个字符。
        :type queue_name: str
        :param cu_number: 用户为作业选择的CU数量，默认值为2。
        :type cu_number: int
        :param manager_cu_number: 用户为作业选择的管理节点CU数量，对应为flink jobmanager数量，默认值为1。
        :type manager_cu_number: int
        :param parallel_number: 用户为作业选择的并发量，默认值为1.
        :type parallel_number: int
        :param log_enabled: 是否开启作业日志。 开启：true 关闭：false 默认：false
        :type log_enabled: bool
        :param obs_bucket: 当“log_enabled”为“true”时, 用户授权保存作业日志的OBS桶名。
        :type obs_bucket: str
        :param smn_topic: 当作业异常时，向该SMN主题推送告警信息。
        :type smn_topic: str
        :param main_class: 作业入口类。
        :type main_class: str
        :param entrypoint_args: 作业入口类参数，多个参数之间空格分隔。
        :type entrypoint_args: str
        :param restart_when_exception: 是否开启异常重启功能，默认值为“false”。
        :type restart_when_exception: bool
        :param entrypoint: 用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包。
        :type entrypoint: str
        :param dependency_jars: 用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包。示例：[Group/test.jar,myGroup/test1.jar]
        :type dependency_jars: list[str]
        :param dependency_files: 用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件，示例：[myGroup/test.cvs,myGroup/test1.csv] 
        :type dependency_files: list[str]
        :param flink_version: Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本。
        :type flink_version: str
        :param image: 自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》
        :type image: str
        :param tm_slot_num: 每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。
        :type tm_slot_num: int
        :param tm_cus: 每个taskmanager的CU数，默认值为“1”。
        :type tm_cus: int
        :param feature: 作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像。
        :type feature: str
        :param resume_checkpoint: 异常重启是否从checkpoint恢复。
        :type resume_checkpoint: bool
        :param resume_max_num: 异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。
        :type resume_max_num: int
        :param checkpoint_path: 用户Jar中checkpoint的储存地址，不同作业路径需要保持不同。
        :type checkpoint_path: str
        :param runtime_config: Flink作业运行时自定义优化参数。
        :type runtime_config: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
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
        self._flink_version = None
        self._image = None
        self._tm_slot_num = None
        self._tm_cus = None
        self._feature = None
        self._resume_checkpoint = None
        self._resume_max_num = None
        self._checkpoint_path = None
        self._runtime_config = None
        self._tags = None
        self.discriminator = None

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
        if flink_version is not None:
            self.flink_version = flink_version
        if image is not None:
            self.image = image
        if tm_slot_num is not None:
            self.tm_slot_num = tm_slot_num
        if tm_cus is not None:
            self.tm_cus = tm_cus
        if feature is not None:
            self.feature = feature
        if resume_checkpoint is not None:
            self.resume_checkpoint = resume_checkpoint
        if resume_max_num is not None:
            self.resume_max_num = resume_max_num
        if checkpoint_path is not None:
            self.checkpoint_path = checkpoint_path
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateFlinkdefinedJobsReq.

        作业名称。长度限制：0-57个字符。

        :return: The name of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFlinkdefinedJobsReq.

        作业名称。长度限制：0-57个字符。

        :param name: The name of this CreateFlinkdefinedJobsReq.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        """Gets the desc of this CreateFlinkdefinedJobsReq.

        作业描述。长度限制：0-512个字符。

        :return: The desc of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CreateFlinkdefinedJobsReq.

        作业描述。长度限制：0-512个字符。

        :param desc: The desc of this CreateFlinkdefinedJobsReq.
        :type desc: str
        """
        self._desc = desc

    @property
    def queue_name(self):
        """Gets the queue_name of this CreateFlinkdefinedJobsReq.

        队列名称。长度限制：1-128个字符。

        :return: The queue_name of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this CreateFlinkdefinedJobsReq.

        队列名称。长度限制：1-128个字符。

        :param queue_name: The queue_name of this CreateFlinkdefinedJobsReq.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def cu_number(self):
        """Gets the cu_number of this CreateFlinkdefinedJobsReq.

        用户为作业选择的CU数量，默认值为2。

        :return: The cu_number of this CreateFlinkdefinedJobsReq.
        :rtype: int
        """
        return self._cu_number

    @cu_number.setter
    def cu_number(self, cu_number):
        """Sets the cu_number of this CreateFlinkdefinedJobsReq.

        用户为作业选择的CU数量，默认值为2。

        :param cu_number: The cu_number of this CreateFlinkdefinedJobsReq.
        :type cu_number: int
        """
        self._cu_number = cu_number

    @property
    def manager_cu_number(self):
        """Gets the manager_cu_number of this CreateFlinkdefinedJobsReq.

        用户为作业选择的管理节点CU数量，对应为flink jobmanager数量，默认值为1。

        :return: The manager_cu_number of this CreateFlinkdefinedJobsReq.
        :rtype: int
        """
        return self._manager_cu_number

    @manager_cu_number.setter
    def manager_cu_number(self, manager_cu_number):
        """Sets the manager_cu_number of this CreateFlinkdefinedJobsReq.

        用户为作业选择的管理节点CU数量，对应为flink jobmanager数量，默认值为1。

        :param manager_cu_number: The manager_cu_number of this CreateFlinkdefinedJobsReq.
        :type manager_cu_number: int
        """
        self._manager_cu_number = manager_cu_number

    @property
    def parallel_number(self):
        """Gets the parallel_number of this CreateFlinkdefinedJobsReq.

        用户为作业选择的并发量，默认值为1.

        :return: The parallel_number of this CreateFlinkdefinedJobsReq.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        """Sets the parallel_number of this CreateFlinkdefinedJobsReq.

        用户为作业选择的并发量，默认值为1.

        :param parallel_number: The parallel_number of this CreateFlinkdefinedJobsReq.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def log_enabled(self):
        """Gets the log_enabled of this CreateFlinkdefinedJobsReq.

        是否开启作业日志。 开启：true 关闭：false 默认：false

        :return: The log_enabled of this CreateFlinkdefinedJobsReq.
        :rtype: bool
        """
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, log_enabled):
        """Sets the log_enabled of this CreateFlinkdefinedJobsReq.

        是否开启作业日志。 开启：true 关闭：false 默认：false

        :param log_enabled: The log_enabled of this CreateFlinkdefinedJobsReq.
        :type log_enabled: bool
        """
        self._log_enabled = log_enabled

    @property
    def obs_bucket(self):
        """Gets the obs_bucket of this CreateFlinkdefinedJobsReq.

        当“log_enabled”为“true”时, 用户授权保存作业日志的OBS桶名。

        :return: The obs_bucket of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        """Sets the obs_bucket of this CreateFlinkdefinedJobsReq.

        当“log_enabled”为“true”时, 用户授权保存作业日志的OBS桶名。

        :param obs_bucket: The obs_bucket of this CreateFlinkdefinedJobsReq.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def smn_topic(self):
        """Gets the smn_topic of this CreateFlinkdefinedJobsReq.

        当作业异常时，向该SMN主题推送告警信息。

        :return: The smn_topic of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._smn_topic

    @smn_topic.setter
    def smn_topic(self, smn_topic):
        """Sets the smn_topic of this CreateFlinkdefinedJobsReq.

        当作业异常时，向该SMN主题推送告警信息。

        :param smn_topic: The smn_topic of this CreateFlinkdefinedJobsReq.
        :type smn_topic: str
        """
        self._smn_topic = smn_topic

    @property
    def main_class(self):
        """Gets the main_class of this CreateFlinkdefinedJobsReq.

        作业入口类。

        :return: The main_class of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        """Sets the main_class of this CreateFlinkdefinedJobsReq.

        作业入口类。

        :param main_class: The main_class of this CreateFlinkdefinedJobsReq.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def entrypoint_args(self):
        """Gets the entrypoint_args of this CreateFlinkdefinedJobsReq.

        作业入口类参数，多个参数之间空格分隔。

        :return: The entrypoint_args of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._entrypoint_args

    @entrypoint_args.setter
    def entrypoint_args(self, entrypoint_args):
        """Sets the entrypoint_args of this CreateFlinkdefinedJobsReq.

        作业入口类参数，多个参数之间空格分隔。

        :param entrypoint_args: The entrypoint_args of this CreateFlinkdefinedJobsReq.
        :type entrypoint_args: str
        """
        self._entrypoint_args = entrypoint_args

    @property
    def restart_when_exception(self):
        """Gets the restart_when_exception of this CreateFlinkdefinedJobsReq.

        是否开启异常重启功能，默认值为“false”。

        :return: The restart_when_exception of this CreateFlinkdefinedJobsReq.
        :rtype: bool
        """
        return self._restart_when_exception

    @restart_when_exception.setter
    def restart_when_exception(self, restart_when_exception):
        """Sets the restart_when_exception of this CreateFlinkdefinedJobsReq.

        是否开启异常重启功能，默认值为“false”。

        :param restart_when_exception: The restart_when_exception of this CreateFlinkdefinedJobsReq.
        :type restart_when_exception: bool
        """
        self._restart_when_exception = restart_when_exception

    @property
    def entrypoint(self):
        """Gets the entrypoint of this CreateFlinkdefinedJobsReq.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包。

        :return: The entrypoint of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this CreateFlinkdefinedJobsReq.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业主类所在的jar包。

        :param entrypoint: The entrypoint of this CreateFlinkdefinedJobsReq.
        :type entrypoint: str
        """
        self._entrypoint = entrypoint

    @property
    def dependency_jars(self):
        """Gets the dependency_jars of this CreateFlinkdefinedJobsReq.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包。示例：[Group/test.jar,myGroup/test1.jar]

        :return: The dependency_jars of this CreateFlinkdefinedJobsReq.
        :rtype: list[str]
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        """Sets the dependency_jars of this CreateFlinkdefinedJobsReq.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业的其他依赖包。示例：[Group/test.jar,myGroup/test1.jar]

        :param dependency_jars: The dependency_jars of this CreateFlinkdefinedJobsReq.
        :type dependency_jars: list[str]
        """
        self._dependency_jars = dependency_jars

    @property
    def dependency_files(self):
        """Gets the dependency_files of this CreateFlinkdefinedJobsReq.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件，示例：[myGroup/test.cvs,myGroup/test1.csv] 

        :return: The dependency_files of this CreateFlinkdefinedJobsReq.
        :rtype: list[str]
        """
        return self._dependency_files

    @dependency_files.setter
    def dependency_files(self, dependency_files):
        """Sets the dependency_files of this CreateFlinkdefinedJobsReq.

        用户已上传到DLI资源管理系统的资源包名，用户自定义作业的依赖文件，示例：[myGroup/test.cvs,myGroup/test1.csv] 

        :param dependency_files: The dependency_files of this CreateFlinkdefinedJobsReq.
        :type dependency_files: list[str]
        """
        self._dependency_files = dependency_files

    @property
    def flink_version(self):
        """Gets the flink_version of this CreateFlinkdefinedJobsReq.

        Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本。

        :return: The flink_version of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._flink_version

    @flink_version.setter
    def flink_version(self, flink_version):
        """Sets the flink_version of this CreateFlinkdefinedJobsReq.

        Flink版本。当用户设置“feature”为“basic”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用的DLI基础Flink镜像的版本。

        :param flink_version: The flink_version of this CreateFlinkdefinedJobsReq.
        :type flink_version: str
        """
        self._flink_version = flink_version

    @property
    def image(self):
        """Gets the image of this CreateFlinkdefinedJobsReq.

        自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》

        :return: The image of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CreateFlinkdefinedJobsReq.

        自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Flink镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》

        :param image: The image of this CreateFlinkdefinedJobsReq.
        :type image: str
        """
        self._image = image

    @property
    def tm_slot_num(self):
        """Gets the tm_slot_num of this CreateFlinkdefinedJobsReq.

        每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。

        :return: The tm_slot_num of this CreateFlinkdefinedJobsReq.
        :rtype: int
        """
        return self._tm_slot_num

    @tm_slot_num.setter
    def tm_slot_num(self, tm_slot_num):
        """Sets the tm_slot_num of this CreateFlinkdefinedJobsReq.

        每个taskmanager的slot数，默认值为“(parallel_number*tm_cus)/(cu_number-manager_cu_number)”。

        :param tm_slot_num: The tm_slot_num of this CreateFlinkdefinedJobsReq.
        :type tm_slot_num: int
        """
        self._tm_slot_num = tm_slot_num

    @property
    def tm_cus(self):
        """Gets the tm_cus of this CreateFlinkdefinedJobsReq.

        每个taskmanager的CU数，默认值为“1”。

        :return: The tm_cus of this CreateFlinkdefinedJobsReq.
        :rtype: int
        """
        return self._tm_cus

    @tm_cus.setter
    def tm_cus(self, tm_cus):
        """Sets the tm_cus of this CreateFlinkdefinedJobsReq.

        每个taskmanager的CU数，默认值为“1”。

        :param tm_cus: The tm_cus of this CreateFlinkdefinedJobsReq.
        :type tm_cus: int
        """
        self._tm_cus = tm_cus

    @property
    def feature(self):
        """Gets the feature of this CreateFlinkdefinedJobsReq.

        作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像。

        :return: The feature of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this CreateFlinkdefinedJobsReq.

        作业特性。表示用户作业使用的Flink镜像类型。basic：表示使用DLI提供的基础Flink镜像。custom：表示使用用户自定义的Flink镜像。

        :param feature: The feature of this CreateFlinkdefinedJobsReq.
        :type feature: str
        """
        self._feature = feature

    @property
    def resume_checkpoint(self):
        """Gets the resume_checkpoint of this CreateFlinkdefinedJobsReq.

        异常重启是否从checkpoint恢复。

        :return: The resume_checkpoint of this CreateFlinkdefinedJobsReq.
        :rtype: bool
        """
        return self._resume_checkpoint

    @resume_checkpoint.setter
    def resume_checkpoint(self, resume_checkpoint):
        """Sets the resume_checkpoint of this CreateFlinkdefinedJobsReq.

        异常重启是否从checkpoint恢复。

        :param resume_checkpoint: The resume_checkpoint of this CreateFlinkdefinedJobsReq.
        :type resume_checkpoint: bool
        """
        self._resume_checkpoint = resume_checkpoint

    @property
    def resume_max_num(self):
        """Gets the resume_max_num of this CreateFlinkdefinedJobsReq.

        异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。

        :return: The resume_max_num of this CreateFlinkdefinedJobsReq.
        :rtype: int
        """
        return self._resume_max_num

    @resume_max_num.setter
    def resume_max_num(self, resume_max_num):
        """Sets the resume_max_num of this CreateFlinkdefinedJobsReq.

        异常重试最大次数，单位：次/小时。取值范围：-1或大于0。默认值为“-1”，表示无限次数。

        :param resume_max_num: The resume_max_num of this CreateFlinkdefinedJobsReq.
        :type resume_max_num: int
        """
        self._resume_max_num = resume_max_num

    @property
    def checkpoint_path(self):
        """Gets the checkpoint_path of this CreateFlinkdefinedJobsReq.

        用户Jar中checkpoint的储存地址，不同作业路径需要保持不同。

        :return: The checkpoint_path of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._checkpoint_path

    @checkpoint_path.setter
    def checkpoint_path(self, checkpoint_path):
        """Sets the checkpoint_path of this CreateFlinkdefinedJobsReq.

        用户Jar中checkpoint的储存地址，不同作业路径需要保持不同。

        :param checkpoint_path: The checkpoint_path of this CreateFlinkdefinedJobsReq.
        :type checkpoint_path: str
        """
        self._checkpoint_path = checkpoint_path

    @property
    def runtime_config(self):
        """Gets the runtime_config of this CreateFlinkdefinedJobsReq.

        Flink作业运行时自定义优化参数。

        :return: The runtime_config of this CreateFlinkdefinedJobsReq.
        :rtype: str
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        """Sets the runtime_config of this CreateFlinkdefinedJobsReq.

        Flink作业运行时自定义优化参数。

        :param runtime_config: The runtime_config of this CreateFlinkdefinedJobsReq.
        :type runtime_config: str
        """
        self._runtime_config = runtime_config

    @property
    def tags(self):
        """Gets the tags of this CreateFlinkdefinedJobsReq.

        标签

        :return: The tags of this CreateFlinkdefinedJobsReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateFlinkdefinedJobsReq.

        标签

        :param tags: The tags of this CreateFlinkdefinedJobsReq.
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
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
        if not isinstance(other, CreateFlinkdefinedJobsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
