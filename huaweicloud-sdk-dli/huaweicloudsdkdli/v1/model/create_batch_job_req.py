# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBatchJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file': 'str',
        'class_name': 'str',
        'cluster_name': 'str',
        'args': 'list[str]',
        'sc_type': 'str',
        'jars': 'list[str]',
        'python_files': 'list[str]',
        'files': 'list[str]',
        'modules': 'list[str]',
        'resources': 'list[CreateSessionReqResource]',
        'groups': 'list[CreateSessionReqGroup]',
        'conf': 'list[object]',
        'name': 'str',
        'driver_memory': 'str',
        'driver_cores': 'int',
        'executor_memory': 'str',
        'executor_cores': 'int',
        'num_executors': 'int',
        'feature': 'str',
        'spark_version': 'str',
        'queue': 'str',
        'auto_recovery': 'bool',
        'max_retry_times': 'int',
        'image': 'str',
        'catalog_name': 'str',
        'obs_bucket': 'str'
    }

    attribute_map = {
        'file': 'file',
        'class_name': 'class_name',
        'cluster_name': 'cluster_name',
        'args': 'args',
        'sc_type': 'sc_type',
        'jars': 'jars',
        'python_files': 'python_files',
        'files': 'files',
        'modules': 'modules',
        'resources': 'resources',
        'groups': 'groups',
        'conf': 'conf',
        'name': 'name',
        'driver_memory': 'driver_memory',
        'driver_cores': 'driver_cores',
        'executor_memory': 'executor_memory',
        'executor_cores': 'executor_cores',
        'num_executors': 'num_executors',
        'feature': 'feature',
        'spark_version': 'spark_version',
        'queue': 'queue',
        'auto_recovery': 'auto_recovery',
        'max_retry_times': 'max_retry_times',
        'image': 'image',
        'catalog_name': 'catalog_name',
        'obs_bucket': 'obs_bucket'
    }

    def __init__(self, file=None, class_name=None, cluster_name=None, args=None, sc_type=None, jars=None, python_files=None, files=None, modules=None, resources=None, groups=None, conf=None, name=None, driver_memory=None, driver_cores=None, executor_memory=None, executor_cores=None, num_executors=None, feature=None, spark_version=None, queue=None, auto_recovery=None, max_retry_times=None, image=None, catalog_name=None, obs_bucket=None):
        """CreateBatchJobReq

        The model defined in huaweicloud sdk

        :param file: 用户已上传到DLI资源管理系统的类型为jar的资源包名。
        :type file: str
        :param class_name: 批处理作业的Java/Spark主类。
        :type class_name: str
        :param cluster_name: 用于指定队列，填写已创建DLI的队列名。
        :type cluster_name: str
        :param args: 传入主类的参数。
        :type args: list[str]
        :param sc_type: 计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 资源类型： A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6。 B：16核64G内存,2,2,7G,8G,7。 C：32核128G内存,4,2,15G,8G,14。
        :type sc_type: str
        :param jars: 用户已上传到DLI资源管理系统的类型为jar的资源包名。
        :type jars: list[str]
        :param python_files: 用户已上传到DLI资源管理系统的类型为pyFile的资源包名。
        :type python_files: list[str]
        :param files: 用户已上传到DLI资源管理系统的类型为file的资源包名。
        :type files: list[str]
        :param modules: 依赖的系统资源模块名，具体模块名可通过查询所有资源包接口查看。 DLI系统提供了用于执行跨源作业的依赖模块，各个不同的服务对应的模块列表如下： CloudTable/MRS HBase: sys.datasource.hbase CloudTable/MRS OpenTSDB: sys.datasource.opentsdb RDS MySQL: sys.datasource.rds RDS PostGre: 不需要选 DWS: 不需要选 CSS: sys.datasource.css
        :type modules: list[str]
        :param resources: JSON对象列表，填写用户已上传到队列的类型为JSON的资源包名和类型。
        :type resources: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqResource`]
        :param groups: JSON对象列表，填写用户组类型资源，格式详见请求示例。resources中的name未进行type校验，只要此分组中存在这个名字的包即可。
        :type groups: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqGroup`]
        :param conf: batch配置项。
        :type conf: list[object]
        :param name: 创建时用户指定的批处理名称，不能超过128个字符。
        :type name: str
        :param driver_memory: Spark应用的Driver内存, 参数配置例如2G, 2048M。该配置项会替换“sc_type”中对应的默认参数，使用时必需带单位，否则会启动失败。
        :type driver_memory: str
        :param driver_cores: Spark应用Driver的CPU核数。该配置项会替换sc_type中对应的默认参数。
        :type driver_cores: int
        :param executor_memory: Spark应用的Executor内存, 参数配置例如2G, 2048M。该配置项会替换“sc_type”中对应的默认参数，使用时必需带单位，否则会启动失败。
        :type executor_memory: str
        :param executor_cores: Spark应用每个Executor的CPU核数。该配置项会替换sc_type中对应的默认参数。
        :type executor_cores: int
        :param num_executors: Spark应用Executor的个数。该配置项会替换sc_type中对应的默认参数。
        :type num_executors: int
        :param feature: 作业特性，作业运行在vm队列上支持basic，在container队列上支持basic、ai、custom，其中填写custom时需要同时填写image参数。
        :type feature: str
        :param spark_version: 作业使用spark组件的版本号，在feature为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2。
        :type spark_version: str
        :param queue: 用于指定队列，填写已创建DLI的队列名
        :type queue: str
        :param auto_recovery: 是否开启重试功能，如果开启，可在Spark作业异常失败后自动重试。默认值为“false”。
        :type auto_recovery: bool
        :param max_retry_times: 最大重试次数。最大值为“100”，默认值为“20”。
        :type max_retry_times: int
        :param image: 自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Spark镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。
        :type image: str
        :param catalog_name: 访问元数据时，需要设置为dli
        :type catalog_name: str
        :param obs_bucket: 保存Spark作业的obs桶，需要保存作业时配置该参数
        :type obs_bucket: str
        """
        
        

        self._file = None
        self._class_name = None
        self._cluster_name = None
        self._args = None
        self._sc_type = None
        self._jars = None
        self._python_files = None
        self._files = None
        self._modules = None
        self._resources = None
        self._groups = None
        self._conf = None
        self._name = None
        self._driver_memory = None
        self._driver_cores = None
        self._executor_memory = None
        self._executor_cores = None
        self._num_executors = None
        self._feature = None
        self._spark_version = None
        self._queue = None
        self._auto_recovery = None
        self._max_retry_times = None
        self._image = None
        self._catalog_name = None
        self._obs_bucket = None
        self.discriminator = None

        self.file = file
        self.class_name = class_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if args is not None:
            self.args = args
        if sc_type is not None:
            self.sc_type = sc_type
        if jars is not None:
            self.jars = jars
        if python_files is not None:
            self.python_files = python_files
        if files is not None:
            self.files = files
        if modules is not None:
            self.modules = modules
        if resources is not None:
            self.resources = resources
        if groups is not None:
            self.groups = groups
        if conf is not None:
            self.conf = conf
        if name is not None:
            self.name = name
        if driver_memory is not None:
            self.driver_memory = driver_memory
        if driver_cores is not None:
            self.driver_cores = driver_cores
        if executor_memory is not None:
            self.executor_memory = executor_memory
        if executor_cores is not None:
            self.executor_cores = executor_cores
        if num_executors is not None:
            self.num_executors = num_executors
        if feature is not None:
            self.feature = feature
        if spark_version is not None:
            self.spark_version = spark_version
        if queue is not None:
            self.queue = queue
        if auto_recovery is not None:
            self.auto_recovery = auto_recovery
        if max_retry_times is not None:
            self.max_retry_times = max_retry_times
        if image is not None:
            self.image = image
        if catalog_name is not None:
            self.catalog_name = catalog_name
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket

    @property
    def file(self):
        """Gets the file of this CreateBatchJobReq.

        用户已上传到DLI资源管理系统的类型为jar的资源包名。

        :return: The file of this CreateBatchJobReq.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CreateBatchJobReq.

        用户已上传到DLI资源管理系统的类型为jar的资源包名。

        :param file: The file of this CreateBatchJobReq.
        :type file: str
        """
        self._file = file

    @property
    def class_name(self):
        """Gets the class_name of this CreateBatchJobReq.

        批处理作业的Java/Spark主类。

        :return: The class_name of this CreateBatchJobReq.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this CreateBatchJobReq.

        批处理作业的Java/Spark主类。

        :param class_name: The class_name of this CreateBatchJobReq.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateBatchJobReq.

        用于指定队列，填写已创建DLI的队列名。

        :return: The cluster_name of this CreateBatchJobReq.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateBatchJobReq.

        用于指定队列，填写已创建DLI的队列名。

        :param cluster_name: The cluster_name of this CreateBatchJobReq.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def args(self):
        """Gets the args of this CreateBatchJobReq.

        传入主类的参数。

        :return: The args of this CreateBatchJobReq.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this CreateBatchJobReq.

        传入主类的参数。

        :param args: The args of this CreateBatchJobReq.
        :type args: list[str]
        """
        self._args = args

    @property
    def sc_type(self):
        """Gets the sc_type of this CreateBatchJobReq.

        计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 资源类型： A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6。 B：16核64G内存,2,2,7G,8G,7。 C：32核128G内存,4,2,15G,8G,14。

        :return: The sc_type of this CreateBatchJobReq.
        :rtype: str
        """
        return self._sc_type

    @sc_type.setter
    def sc_type(self, sc_type):
        """Sets the sc_type of this CreateBatchJobReq.

        计算资源类型，目前可接受参数A, B, C。如果不指定，则按最小类型创建。 资源类型： A：物理资源：8核32G内存，driverCores：2；executorCores：1；driverMemory：7G；executorMemory：4G；numExecutor：6。 B：16核64G内存,2,2,7G,8G,7。 C：32核128G内存,4,2,15G,8G,14。

        :param sc_type: The sc_type of this CreateBatchJobReq.
        :type sc_type: str
        """
        self._sc_type = sc_type

    @property
    def jars(self):
        """Gets the jars of this CreateBatchJobReq.

        用户已上传到DLI资源管理系统的类型为jar的资源包名。

        :return: The jars of this CreateBatchJobReq.
        :rtype: list[str]
        """
        return self._jars

    @jars.setter
    def jars(self, jars):
        """Sets the jars of this CreateBatchJobReq.

        用户已上传到DLI资源管理系统的类型为jar的资源包名。

        :param jars: The jars of this CreateBatchJobReq.
        :type jars: list[str]
        """
        self._jars = jars

    @property
    def python_files(self):
        """Gets the python_files of this CreateBatchJobReq.

        用户已上传到DLI资源管理系统的类型为pyFile的资源包名。

        :return: The python_files of this CreateBatchJobReq.
        :rtype: list[str]
        """
        return self._python_files

    @python_files.setter
    def python_files(self, python_files):
        """Sets the python_files of this CreateBatchJobReq.

        用户已上传到DLI资源管理系统的类型为pyFile的资源包名。

        :param python_files: The python_files of this CreateBatchJobReq.
        :type python_files: list[str]
        """
        self._python_files = python_files

    @property
    def files(self):
        """Gets the files of this CreateBatchJobReq.

        用户已上传到DLI资源管理系统的类型为file的资源包名。

        :return: The files of this CreateBatchJobReq.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this CreateBatchJobReq.

        用户已上传到DLI资源管理系统的类型为file的资源包名。

        :param files: The files of this CreateBatchJobReq.
        :type files: list[str]
        """
        self._files = files

    @property
    def modules(self):
        """Gets the modules of this CreateBatchJobReq.

        依赖的系统资源模块名，具体模块名可通过查询所有资源包接口查看。 DLI系统提供了用于执行跨源作业的依赖模块，各个不同的服务对应的模块列表如下： CloudTable/MRS HBase: sys.datasource.hbase CloudTable/MRS OpenTSDB: sys.datasource.opentsdb RDS MySQL: sys.datasource.rds RDS PostGre: 不需要选 DWS: 不需要选 CSS: sys.datasource.css

        :return: The modules of this CreateBatchJobReq.
        :rtype: list[str]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this CreateBatchJobReq.

        依赖的系统资源模块名，具体模块名可通过查询所有资源包接口查看。 DLI系统提供了用于执行跨源作业的依赖模块，各个不同的服务对应的模块列表如下： CloudTable/MRS HBase: sys.datasource.hbase CloudTable/MRS OpenTSDB: sys.datasource.opentsdb RDS MySQL: sys.datasource.rds RDS PostGre: 不需要选 DWS: 不需要选 CSS: sys.datasource.css

        :param modules: The modules of this CreateBatchJobReq.
        :type modules: list[str]
        """
        self._modules = modules

    @property
    def resources(self):
        """Gets the resources of this CreateBatchJobReq.

        JSON对象列表，填写用户已上传到队列的类型为JSON的资源包名和类型。

        :return: The resources of this CreateBatchJobReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CreateBatchJobReq.

        JSON对象列表，填写用户已上传到队列的类型为JSON的资源包名和类型。

        :param resources: The resources of this CreateBatchJobReq.
        :type resources: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqResource`]
        """
        self._resources = resources

    @property
    def groups(self):
        """Gets the groups of this CreateBatchJobReq.

        JSON对象列表，填写用户组类型资源，格式详见请求示例。resources中的name未进行type校验，只要此分组中存在这个名字的包即可。

        :return: The groups of this CreateBatchJobReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqGroup`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this CreateBatchJobReq.

        JSON对象列表，填写用户组类型资源，格式详见请求示例。resources中的name未进行type校验，只要此分组中存在这个名字的包即可。

        :param groups: The groups of this CreateBatchJobReq.
        :type groups: list[:class:`huaweicloudsdkdli.v1.CreateSessionReqGroup`]
        """
        self._groups = groups

    @property
    def conf(self):
        """Gets the conf of this CreateBatchJobReq.

        batch配置项。

        :return: The conf of this CreateBatchJobReq.
        :rtype: list[object]
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this CreateBatchJobReq.

        batch配置项。

        :param conf: The conf of this CreateBatchJobReq.
        :type conf: list[object]
        """
        self._conf = conf

    @property
    def name(self):
        """Gets the name of this CreateBatchJobReq.

        创建时用户指定的批处理名称，不能超过128个字符。

        :return: The name of this CreateBatchJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateBatchJobReq.

        创建时用户指定的批处理名称，不能超过128个字符。

        :param name: The name of this CreateBatchJobReq.
        :type name: str
        """
        self._name = name

    @property
    def driver_memory(self):
        """Gets the driver_memory of this CreateBatchJobReq.

        Spark应用的Driver内存, 参数配置例如2G, 2048M。该配置项会替换“sc_type”中对应的默认参数，使用时必需带单位，否则会启动失败。

        :return: The driver_memory of this CreateBatchJobReq.
        :rtype: str
        """
        return self._driver_memory

    @driver_memory.setter
    def driver_memory(self, driver_memory):
        """Sets the driver_memory of this CreateBatchJobReq.

        Spark应用的Driver内存, 参数配置例如2G, 2048M。该配置项会替换“sc_type”中对应的默认参数，使用时必需带单位，否则会启动失败。

        :param driver_memory: The driver_memory of this CreateBatchJobReq.
        :type driver_memory: str
        """
        self._driver_memory = driver_memory

    @property
    def driver_cores(self):
        """Gets the driver_cores of this CreateBatchJobReq.

        Spark应用Driver的CPU核数。该配置项会替换sc_type中对应的默认参数。

        :return: The driver_cores of this CreateBatchJobReq.
        :rtype: int
        """
        return self._driver_cores

    @driver_cores.setter
    def driver_cores(self, driver_cores):
        """Sets the driver_cores of this CreateBatchJobReq.

        Spark应用Driver的CPU核数。该配置项会替换sc_type中对应的默认参数。

        :param driver_cores: The driver_cores of this CreateBatchJobReq.
        :type driver_cores: int
        """
        self._driver_cores = driver_cores

    @property
    def executor_memory(self):
        """Gets the executor_memory of this CreateBatchJobReq.

        Spark应用的Executor内存, 参数配置例如2G, 2048M。该配置项会替换“sc_type”中对应的默认参数，使用时必需带单位，否则会启动失败。

        :return: The executor_memory of this CreateBatchJobReq.
        :rtype: str
        """
        return self._executor_memory

    @executor_memory.setter
    def executor_memory(self, executor_memory):
        """Sets the executor_memory of this CreateBatchJobReq.

        Spark应用的Executor内存, 参数配置例如2G, 2048M。该配置项会替换“sc_type”中对应的默认参数，使用时必需带单位，否则会启动失败。

        :param executor_memory: The executor_memory of this CreateBatchJobReq.
        :type executor_memory: str
        """
        self._executor_memory = executor_memory

    @property
    def executor_cores(self):
        """Gets the executor_cores of this CreateBatchJobReq.

        Spark应用每个Executor的CPU核数。该配置项会替换sc_type中对应的默认参数。

        :return: The executor_cores of this CreateBatchJobReq.
        :rtype: int
        """
        return self._executor_cores

    @executor_cores.setter
    def executor_cores(self, executor_cores):
        """Sets the executor_cores of this CreateBatchJobReq.

        Spark应用每个Executor的CPU核数。该配置项会替换sc_type中对应的默认参数。

        :param executor_cores: The executor_cores of this CreateBatchJobReq.
        :type executor_cores: int
        """
        self._executor_cores = executor_cores

    @property
    def num_executors(self):
        """Gets the num_executors of this CreateBatchJobReq.

        Spark应用Executor的个数。该配置项会替换sc_type中对应的默认参数。

        :return: The num_executors of this CreateBatchJobReq.
        :rtype: int
        """
        return self._num_executors

    @num_executors.setter
    def num_executors(self, num_executors):
        """Sets the num_executors of this CreateBatchJobReq.

        Spark应用Executor的个数。该配置项会替换sc_type中对应的默认参数。

        :param num_executors: The num_executors of this CreateBatchJobReq.
        :type num_executors: int
        """
        self._num_executors = num_executors

    @property
    def feature(self):
        """Gets the feature of this CreateBatchJobReq.

        作业特性，作业运行在vm队列上支持basic，在container队列上支持basic、ai、custom，其中填写custom时需要同时填写image参数。

        :return: The feature of this CreateBatchJobReq.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this CreateBatchJobReq.

        作业特性，作业运行在vm队列上支持basic，在container队列上支持basic、ai、custom，其中填写custom时需要同时填写image参数。

        :param feature: The feature of this CreateBatchJobReq.
        :type feature: str
        """
        self._feature = feature

    @property
    def spark_version(self):
        """Gets the spark_version of this CreateBatchJobReq.

        作业使用spark组件的版本号，在feature为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2。

        :return: The spark_version of this CreateBatchJobReq.
        :rtype: str
        """
        return self._spark_version

    @spark_version.setter
    def spark_version(self, spark_version):
        """Sets the spark_version of this CreateBatchJobReq.

        作业使用spark组件的版本号，在feature为“basic”或“ai”时填写，若不填写，则使用默认的spark组件版本号2.3.2。

        :param spark_version: The spark_version of this CreateBatchJobReq.
        :type spark_version: str
        """
        self._spark_version = spark_version

    @property
    def queue(self):
        """Gets the queue of this CreateBatchJobReq.

        用于指定队列，填写已创建DLI的队列名

        :return: The queue of this CreateBatchJobReq.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this CreateBatchJobReq.

        用于指定队列，填写已创建DLI的队列名

        :param queue: The queue of this CreateBatchJobReq.
        :type queue: str
        """
        self._queue = queue

    @property
    def auto_recovery(self):
        """Gets the auto_recovery of this CreateBatchJobReq.

        是否开启重试功能，如果开启，可在Spark作业异常失败后自动重试。默认值为“false”。

        :return: The auto_recovery of this CreateBatchJobReq.
        :rtype: bool
        """
        return self._auto_recovery

    @auto_recovery.setter
    def auto_recovery(self, auto_recovery):
        """Sets the auto_recovery of this CreateBatchJobReq.

        是否开启重试功能，如果开启，可在Spark作业异常失败后自动重试。默认值为“false”。

        :param auto_recovery: The auto_recovery of this CreateBatchJobReq.
        :type auto_recovery: bool
        """
        self._auto_recovery = auto_recovery

    @property
    def max_retry_times(self):
        """Gets the max_retry_times of this CreateBatchJobReq.

        最大重试次数。最大值为“100”，默认值为“20”。

        :return: The max_retry_times of this CreateBatchJobReq.
        :rtype: int
        """
        return self._max_retry_times

    @max_retry_times.setter
    def max_retry_times(self, max_retry_times):
        """Sets the max_retry_times of this CreateBatchJobReq.

        最大重试次数。最大值为“100”，默认值为“20”。

        :param max_retry_times: The max_retry_times of this CreateBatchJobReq.
        :type max_retry_times: int
        """
        self._max_retry_times = max_retry_times

    @property
    def image(self):
        """Gets the image of this CreateBatchJobReq.

        自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Spark镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。

        :return: The image of this CreateBatchJobReq.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CreateBatchJobReq.

        自定义镜像。格式为：组织名/镜像名:镜像版本。当用户设置“feature”为“custom”时，该参数生效。用户可通过与“feature”参数配合使用，指定作业运行使用自定义的Spark镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。

        :param image: The image of this CreateBatchJobReq.
        :type image: str
        """
        self._image = image

    @property
    def catalog_name(self):
        """Gets the catalog_name of this CreateBatchJobReq.

        访问元数据时，需要设置为dli

        :return: The catalog_name of this CreateBatchJobReq.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this CreateBatchJobReq.

        访问元数据时，需要设置为dli

        :param catalog_name: The catalog_name of this CreateBatchJobReq.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def obs_bucket(self):
        """Gets the obs_bucket of this CreateBatchJobReq.

        保存Spark作业的obs桶，需要保存作业时配置该参数

        :return: The obs_bucket of this CreateBatchJobReq.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        """Sets the obs_bucket of this CreateBatchJobReq.

        保存Spark作业的obs桶，需要保存作业时配置该参数

        :param obs_bucket: The obs_bucket of this CreateBatchJobReq.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

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
        if not isinstance(other, CreateBatchJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
