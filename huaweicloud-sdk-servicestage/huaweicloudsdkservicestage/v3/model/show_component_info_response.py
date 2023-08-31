# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComponentInfoResponse(SdkResponse):

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
        'description': 'str',
        'labels': 'list[Label]',
        'runtime_stack': 'RuntimeStack',
        'source': 'SourceObject',
        'build': 'Build',
        'environment_id': 'str',
        'application_id': 'str',
        'limit_cpu': 'float',
        'limit_memory': 'float',
        'request_cpu': 'float',
        'request_memory': 'float',
        'replica': 'int',
        'version': 'str',
        'envs': 'list[ComponentEnvironment]',
        'storages': 'list[ComponentStorage]',
        'command': 'ComponentCommand',
        'post_start': 'ComponentLifecycle',
        'pre_stop': 'ComponentLifecycle',
        'timezone': 'str',
        'mesher': 'Mesher',
        'deploy_strategy': 'DeployStrategy',
        'jvm_opts': 'str',
        'tomcat_opts': 'ComponentInfoTomcatOpts',
        'logs': 'list[ComponentLogs]',
        'custom_metric': 'ComponentInfoCustomMetric',
        'affinity': 'ComponentAffinity',
        'anti_affinity': 'ComponentAffinity',
        'liveness_probe': 'ComponentProbe',
        'readiness_probe': 'ComponentProbe',
        'refer_resources': 'list[ReferResourceCreate]',
        'status': 'ComponentStatusView'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'runtime_stack': 'runtime_stack',
        'source': 'source',
        'build': 'build',
        'environment_id': 'environment_id',
        'application_id': 'application_id',
        'limit_cpu': 'limit_cpu',
        'limit_memory': 'limit_memory',
        'request_cpu': 'request_cpu',
        'request_memory': 'request_memory',
        'replica': 'replica',
        'version': 'version',
        'envs': 'envs',
        'storages': 'storages',
        'command': 'command',
        'post_start': 'post_start',
        'pre_stop': 'pre_stop',
        'timezone': 'timezone',
        'mesher': 'mesher',
        'deploy_strategy': 'deploy_strategy',
        'jvm_opts': 'jvm_opts',
        'tomcat_opts': 'tomcat_opts',
        'logs': 'logs',
        'custom_metric': 'custom_metric',
        'affinity': 'affinity',
        'anti_affinity': 'anti_affinity',
        'liveness_probe': 'liveness_probe',
        'readiness_probe': 'readiness_probe',
        'refer_resources': 'refer_resources',
        'status': 'status'
    }

    def __init__(self, name=None, description=None, labels=None, runtime_stack=None, source=None, build=None, environment_id=None, application_id=None, limit_cpu=None, limit_memory=None, request_cpu=None, request_memory=None, replica=None, version=None, envs=None, storages=None, command=None, post_start=None, pre_stop=None, timezone=None, mesher=None, deploy_strategy=None, jvm_opts=None, tomcat_opts=None, logs=None, custom_metric=None, affinity=None, anti_affinity=None, liveness_probe=None, readiness_probe=None, refer_resources=None, status=None):
        """ShowComponentInfoResponse

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param description: 
        :type description: str
        :param labels: 
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.Label`]
        :param runtime_stack: 
        :type runtime_stack: :class:`huaweicloudsdkservicestage.v3.RuntimeStack`
        :param source: 
        :type source: :class:`huaweicloudsdkservicestage.v3.SourceObject`
        :param build: 
        :type build: :class:`huaweicloudsdkservicestage.v3.Build`
        :param environment_id: 
        :type environment_id: str
        :param application_id: 
        :type application_id: str
        :param limit_cpu: 单位为Core
        :type limit_cpu: float
        :param limit_memory: 单位为GiB
        :type limit_memory: float
        :param request_cpu: 单位为Core
        :type request_cpu: float
        :param request_memory: 单位为GiB
        :type request_memory: float
        :param replica: 
        :type replica: int
        :param version: 
        :type version: str
        :param envs: 
        :type envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentEnvironment`]
        :param storages: 
        :type storages: list[:class:`huaweicloudsdkservicestage.v3.ComponentStorage`]
        :param command: 
        :type command: :class:`huaweicloudsdkservicestage.v3.ComponentCommand`
        :param post_start: 
        :type post_start: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        :param pre_stop: 
        :type pre_stop: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        :param timezone: 指定组件运行的时区，比如Asia/Shanghai
        :type timezone: str
        :param mesher: 
        :type mesher: :class:`huaweicloudsdkservicestage.v3.Mesher`
        :param deploy_strategy: 
        :type deploy_strategy: :class:`huaweicloudsdkservicestage.v3.DeployStrategy`
        :param jvm_opts: jvm参数
        :type jvm_opts: str
        :param tomcat_opts: 
        :type tomcat_opts: :class:`huaweicloudsdkservicestage.v3.ComponentInfoTomcatOpts`
        :param logs: 
        :type logs: list[:class:`huaweicloudsdkservicestage.v3.ComponentLogs`]
        :param custom_metric: 
        :type custom_metric: :class:`huaweicloudsdkservicestage.v3.ComponentInfoCustomMetric`
        :param affinity: 
        :type affinity: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        :param anti_affinity: 
        :type anti_affinity: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        :param refer_resources: 
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v3.ReferResourceCreate`]
        :param status: 
        :type status: :class:`huaweicloudsdkservicestage.v3.ComponentStatusView`
        """
        
        super(ShowComponentInfoResponse, self).__init__()

        self._name = None
        self._description = None
        self._labels = None
        self._runtime_stack = None
        self._source = None
        self._build = None
        self._environment_id = None
        self._application_id = None
        self._limit_cpu = None
        self._limit_memory = None
        self._request_cpu = None
        self._request_memory = None
        self._replica = None
        self._version = None
        self._envs = None
        self._storages = None
        self._command = None
        self._post_start = None
        self._pre_stop = None
        self._timezone = None
        self._mesher = None
        self._deploy_strategy = None
        self._jvm_opts = None
        self._tomcat_opts = None
        self._logs = None
        self._custom_metric = None
        self._affinity = None
        self._anti_affinity = None
        self._liveness_probe = None
        self._readiness_probe = None
        self._refer_resources = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if runtime_stack is not None:
            self.runtime_stack = runtime_stack
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build
        if environment_id is not None:
            self.environment_id = environment_id
        if application_id is not None:
            self.application_id = application_id
        if limit_cpu is not None:
            self.limit_cpu = limit_cpu
        if limit_memory is not None:
            self.limit_memory = limit_memory
        if request_cpu is not None:
            self.request_cpu = request_cpu
        if request_memory is not None:
            self.request_memory = request_memory
        if replica is not None:
            self.replica = replica
        if version is not None:
            self.version = version
        if envs is not None:
            self.envs = envs
        if storages is not None:
            self.storages = storages
        if command is not None:
            self.command = command
        if post_start is not None:
            self.post_start = post_start
        if pre_stop is not None:
            self.pre_stop = pre_stop
        if timezone is not None:
            self.timezone = timezone
        if mesher is not None:
            self.mesher = mesher
        if deploy_strategy is not None:
            self.deploy_strategy = deploy_strategy
        if jvm_opts is not None:
            self.jvm_opts = jvm_opts
        if tomcat_opts is not None:
            self.tomcat_opts = tomcat_opts
        if logs is not None:
            self.logs = logs
        if custom_metric is not None:
            self.custom_metric = custom_metric
        if affinity is not None:
            self.affinity = affinity
        if anti_affinity is not None:
            self.anti_affinity = anti_affinity
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if refer_resources is not None:
            self.refer_resources = refer_resources
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Gets the name of this ShowComponentInfoResponse.

        :return: The name of this ShowComponentInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowComponentInfoResponse.

        :param name: The name of this ShowComponentInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowComponentInfoResponse.

        :return: The description of this ShowComponentInfoResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowComponentInfoResponse.

        :param description: The description of this ShowComponentInfoResponse.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this ShowComponentInfoResponse.

        :return: The labels of this ShowComponentInfoResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.Label`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ShowComponentInfoResponse.

        :param labels: The labels of this ShowComponentInfoResponse.
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.Label`]
        """
        self._labels = labels

    @property
    def runtime_stack(self):
        """Gets the runtime_stack of this ShowComponentInfoResponse.

        :return: The runtime_stack of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.RuntimeStack`
        """
        return self._runtime_stack

    @runtime_stack.setter
    def runtime_stack(self, runtime_stack):
        """Sets the runtime_stack of this ShowComponentInfoResponse.

        :param runtime_stack: The runtime_stack of this ShowComponentInfoResponse.
        :type runtime_stack: :class:`huaweicloudsdkservicestage.v3.RuntimeStack`
        """
        self._runtime_stack = runtime_stack

    @property
    def source(self):
        """Gets the source of this ShowComponentInfoResponse.

        :return: The source of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.SourceObject`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ShowComponentInfoResponse.

        :param source: The source of this ShowComponentInfoResponse.
        :type source: :class:`huaweicloudsdkservicestage.v3.SourceObject`
        """
        self._source = source

    @property
    def build(self):
        """Gets the build of this ShowComponentInfoResponse.

        :return: The build of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.Build`
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ShowComponentInfoResponse.

        :param build: The build of this ShowComponentInfoResponse.
        :type build: :class:`huaweicloudsdkservicestage.v3.Build`
        """
        self._build = build

    @property
    def environment_id(self):
        """Gets the environment_id of this ShowComponentInfoResponse.

        :return: The environment_id of this ShowComponentInfoResponse.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this ShowComponentInfoResponse.

        :param environment_id: The environment_id of this ShowComponentInfoResponse.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def application_id(self):
        """Gets the application_id of this ShowComponentInfoResponse.

        :return: The application_id of this ShowComponentInfoResponse.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ShowComponentInfoResponse.

        :param application_id: The application_id of this ShowComponentInfoResponse.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def limit_cpu(self):
        """Gets the limit_cpu of this ShowComponentInfoResponse.

        单位为Core

        :return: The limit_cpu of this ShowComponentInfoResponse.
        :rtype: float
        """
        return self._limit_cpu

    @limit_cpu.setter
    def limit_cpu(self, limit_cpu):
        """Sets the limit_cpu of this ShowComponentInfoResponse.

        单位为Core

        :param limit_cpu: The limit_cpu of this ShowComponentInfoResponse.
        :type limit_cpu: float
        """
        self._limit_cpu = limit_cpu

    @property
    def limit_memory(self):
        """Gets the limit_memory of this ShowComponentInfoResponse.

        单位为GiB

        :return: The limit_memory of this ShowComponentInfoResponse.
        :rtype: float
        """
        return self._limit_memory

    @limit_memory.setter
    def limit_memory(self, limit_memory):
        """Sets the limit_memory of this ShowComponentInfoResponse.

        单位为GiB

        :param limit_memory: The limit_memory of this ShowComponentInfoResponse.
        :type limit_memory: float
        """
        self._limit_memory = limit_memory

    @property
    def request_cpu(self):
        """Gets the request_cpu of this ShowComponentInfoResponse.

        单位为Core

        :return: The request_cpu of this ShowComponentInfoResponse.
        :rtype: float
        """
        return self._request_cpu

    @request_cpu.setter
    def request_cpu(self, request_cpu):
        """Sets the request_cpu of this ShowComponentInfoResponse.

        单位为Core

        :param request_cpu: The request_cpu of this ShowComponentInfoResponse.
        :type request_cpu: float
        """
        self._request_cpu = request_cpu

    @property
    def request_memory(self):
        """Gets the request_memory of this ShowComponentInfoResponse.

        单位为GiB

        :return: The request_memory of this ShowComponentInfoResponse.
        :rtype: float
        """
        return self._request_memory

    @request_memory.setter
    def request_memory(self, request_memory):
        """Sets the request_memory of this ShowComponentInfoResponse.

        单位为GiB

        :param request_memory: The request_memory of this ShowComponentInfoResponse.
        :type request_memory: float
        """
        self._request_memory = request_memory

    @property
    def replica(self):
        """Gets the replica of this ShowComponentInfoResponse.

        :return: The replica of this ShowComponentInfoResponse.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        """Sets the replica of this ShowComponentInfoResponse.

        :param replica: The replica of this ShowComponentInfoResponse.
        :type replica: int
        """
        self._replica = replica

    @property
    def version(self):
        """Gets the version of this ShowComponentInfoResponse.

        :return: The version of this ShowComponentInfoResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowComponentInfoResponse.

        :param version: The version of this ShowComponentInfoResponse.
        :type version: str
        """
        self._version = version

    @property
    def envs(self):
        """Gets the envs of this ShowComponentInfoResponse.

        :return: The envs of this ShowComponentInfoResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentEnvironment`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this ShowComponentInfoResponse.

        :param envs: The envs of this ShowComponentInfoResponse.
        :type envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentEnvironment`]
        """
        self._envs = envs

    @property
    def storages(self):
        """Gets the storages of this ShowComponentInfoResponse.

        :return: The storages of this ShowComponentInfoResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentStorage`]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        """Sets the storages of this ShowComponentInfoResponse.

        :param storages: The storages of this ShowComponentInfoResponse.
        :type storages: list[:class:`huaweicloudsdkservicestage.v3.ComponentStorage`]
        """
        self._storages = storages

    @property
    def command(self):
        """Gets the command of this ShowComponentInfoResponse.

        :return: The command of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentCommand`
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ShowComponentInfoResponse.

        :param command: The command of this ShowComponentInfoResponse.
        :type command: :class:`huaweicloudsdkservicestage.v3.ComponentCommand`
        """
        self._command = command

    @property
    def post_start(self):
        """Gets the post_start of this ShowComponentInfoResponse.

        :return: The post_start of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        """Sets the post_start of this ShowComponentInfoResponse.

        :param post_start: The post_start of this ShowComponentInfoResponse.
        :type post_start: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        """
        self._post_start = post_start

    @property
    def pre_stop(self):
        """Gets the pre_stop of this ShowComponentInfoResponse.

        :return: The pre_stop of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        """Sets the pre_stop of this ShowComponentInfoResponse.

        :param pre_stop: The pre_stop of this ShowComponentInfoResponse.
        :type pre_stop: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        """
        self._pre_stop = pre_stop

    @property
    def timezone(self):
        """Gets the timezone of this ShowComponentInfoResponse.

        指定组件运行的时区，比如Asia/Shanghai

        :return: The timezone of this ShowComponentInfoResponse.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ShowComponentInfoResponse.

        指定组件运行的时区，比如Asia/Shanghai

        :param timezone: The timezone of this ShowComponentInfoResponse.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def mesher(self):
        """Gets the mesher of this ShowComponentInfoResponse.

        :return: The mesher of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.Mesher`
        """
        return self._mesher

    @mesher.setter
    def mesher(self, mesher):
        """Sets the mesher of this ShowComponentInfoResponse.

        :param mesher: The mesher of this ShowComponentInfoResponse.
        :type mesher: :class:`huaweicloudsdkservicestage.v3.Mesher`
        """
        self._mesher = mesher

    @property
    def deploy_strategy(self):
        """Gets the deploy_strategy of this ShowComponentInfoResponse.

        :return: The deploy_strategy of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.DeployStrategy`
        """
        return self._deploy_strategy

    @deploy_strategy.setter
    def deploy_strategy(self, deploy_strategy):
        """Sets the deploy_strategy of this ShowComponentInfoResponse.

        :param deploy_strategy: The deploy_strategy of this ShowComponentInfoResponse.
        :type deploy_strategy: :class:`huaweicloudsdkservicestage.v3.DeployStrategy`
        """
        self._deploy_strategy = deploy_strategy

    @property
    def jvm_opts(self):
        """Gets the jvm_opts of this ShowComponentInfoResponse.

        jvm参数

        :return: The jvm_opts of this ShowComponentInfoResponse.
        :rtype: str
        """
        return self._jvm_opts

    @jvm_opts.setter
    def jvm_opts(self, jvm_opts):
        """Sets the jvm_opts of this ShowComponentInfoResponse.

        jvm参数

        :param jvm_opts: The jvm_opts of this ShowComponentInfoResponse.
        :type jvm_opts: str
        """
        self._jvm_opts = jvm_opts

    @property
    def tomcat_opts(self):
        """Gets the tomcat_opts of this ShowComponentInfoResponse.

        :return: The tomcat_opts of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentInfoTomcatOpts`
        """
        return self._tomcat_opts

    @tomcat_opts.setter
    def tomcat_opts(self, tomcat_opts):
        """Sets the tomcat_opts of this ShowComponentInfoResponse.

        :param tomcat_opts: The tomcat_opts of this ShowComponentInfoResponse.
        :type tomcat_opts: :class:`huaweicloudsdkservicestage.v3.ComponentInfoTomcatOpts`
        """
        self._tomcat_opts = tomcat_opts

    @property
    def logs(self):
        """Gets the logs of this ShowComponentInfoResponse.

        :return: The logs of this ShowComponentInfoResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentLogs`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ShowComponentInfoResponse.

        :param logs: The logs of this ShowComponentInfoResponse.
        :type logs: list[:class:`huaweicloudsdkservicestage.v3.ComponentLogs`]
        """
        self._logs = logs

    @property
    def custom_metric(self):
        """Gets the custom_metric of this ShowComponentInfoResponse.

        :return: The custom_metric of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentInfoCustomMetric`
        """
        return self._custom_metric

    @custom_metric.setter
    def custom_metric(self, custom_metric):
        """Sets the custom_metric of this ShowComponentInfoResponse.

        :param custom_metric: The custom_metric of this ShowComponentInfoResponse.
        :type custom_metric: :class:`huaweicloudsdkservicestage.v3.ComponentInfoCustomMetric`
        """
        self._custom_metric = custom_metric

    @property
    def affinity(self):
        """Gets the affinity of this ShowComponentInfoResponse.

        :return: The affinity of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this ShowComponentInfoResponse.

        :param affinity: The affinity of this ShowComponentInfoResponse.
        :type affinity: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        """
        self._affinity = affinity

    @property
    def anti_affinity(self):
        """Gets the anti_affinity of this ShowComponentInfoResponse.

        :return: The anti_affinity of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        """
        return self._anti_affinity

    @anti_affinity.setter
    def anti_affinity(self, anti_affinity):
        """Sets the anti_affinity of this ShowComponentInfoResponse.

        :param anti_affinity: The anti_affinity of this ShowComponentInfoResponse.
        :type anti_affinity: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        """
        self._anti_affinity = anti_affinity

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this ShowComponentInfoResponse.

        :return: The liveness_probe of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this ShowComponentInfoResponse.

        :param liveness_probe: The liveness_probe of this ShowComponentInfoResponse.
        :type liveness_probe: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        """
        self._liveness_probe = liveness_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this ShowComponentInfoResponse.

        :return: The readiness_probe of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this ShowComponentInfoResponse.

        :param readiness_probe: The readiness_probe of this ShowComponentInfoResponse.
        :type readiness_probe: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        """
        self._readiness_probe = readiness_probe

    @property
    def refer_resources(self):
        """Gets the refer_resources of this ShowComponentInfoResponse.

        :return: The refer_resources of this ShowComponentInfoResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ReferResourceCreate`]
        """
        return self._refer_resources

    @refer_resources.setter
    def refer_resources(self, refer_resources):
        """Sets the refer_resources of this ShowComponentInfoResponse.

        :param refer_resources: The refer_resources of this ShowComponentInfoResponse.
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v3.ReferResourceCreate`]
        """
        self._refer_resources = refer_resources

    @property
    def status(self):
        """Gets the status of this ShowComponentInfoResponse.

        :return: The status of this ShowComponentInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentStatusView`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowComponentInfoResponse.

        :param status: The status of this ShowComponentInfoResponse.
        :type status: :class:`huaweicloudsdkservicestage.v3.ComponentStatusView`
        """
        self._status = status

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
        if not isinstance(other, ShowComponentInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
