# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentCreate:

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
        'limit_cpu': 'float',
        'limit_memory': 'float',
        'request_cpu': 'float',
        'request_memory': 'float',
        'replica': 'int',
        'version': 'str',
        'envs': 'list[ComponentEnvironment]',
        'storages': 'list[ComponentStorage]',
        'deploy_strategy': 'DeployStrategy',
        'command': 'ComponentCommand',
        'post_start': 'ComponentLifecycle',
        'pre_stop': 'ComponentLifecycle',
        'mesher': 'Mesher',
        'timezone': 'str',
        'jvm_opts': 'str',
        'tomcat_opts': 'ComponentModifyTomcatOpts',
        'logs': 'list[ComponentLogs]',
        'custom_metric': 'ComponentModifyCustomMetric',
        'affinity': 'ComponentAffinity',
        'anti_affinity': 'ComponentAffinity',
        'liveness_probe': 'ComponentProbe',
        'readiness_probe': 'ComponentProbe',
        'refer_resources': 'list[ReferResourceCreate]',
        'external_accesses': 'list[ExternalAccesses]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'runtime_stack': 'runtime_stack',
        'source': 'source',
        'build': 'build',
        'environment_id': 'environment_id',
        'limit_cpu': 'limit_cpu',
        'limit_memory': 'limit_memory',
        'request_cpu': 'request_cpu',
        'request_memory': 'request_memory',
        'replica': 'replica',
        'version': 'version',
        'envs': 'envs',
        'storages': 'storages',
        'deploy_strategy': 'deploy_strategy',
        'command': 'command',
        'post_start': 'post_start',
        'pre_stop': 'pre_stop',
        'mesher': 'mesher',
        'timezone': 'timezone',
        'jvm_opts': 'jvm_opts',
        'tomcat_opts': 'tomcat_opts',
        'logs': 'logs',
        'custom_metric': 'custom_metric',
        'affinity': 'affinity',
        'anti_affinity': 'anti_affinity',
        'liveness_probe': 'liveness_probe',
        'readiness_probe': 'readiness_probe',
        'refer_resources': 'refer_resources',
        'external_accesses': 'external_accesses'
    }

    def __init__(self, name=None, description=None, labels=None, runtime_stack=None, source=None, build=None, environment_id=None, limit_cpu=None, limit_memory=None, request_cpu=None, request_memory=None, replica=None, version=None, envs=None, storages=None, deploy_strategy=None, command=None, post_start=None, pre_stop=None, mesher=None, timezone=None, jvm_opts=None, tomcat_opts=None, logs=None, custom_metric=None, affinity=None, anti_affinity=None, liveness_probe=None, readiness_probe=None, refer_resources=None, external_accesses=None):
        """ComponentCreate

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
        :param deploy_strategy: 
        :type deploy_strategy: :class:`huaweicloudsdkservicestage.v3.DeployStrategy`
        :param command: 
        :type command: :class:`huaweicloudsdkservicestage.v3.ComponentCommand`
        :param post_start: 
        :type post_start: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        :param pre_stop: 
        :type pre_stop: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        :param mesher: 
        :type mesher: :class:`huaweicloudsdkservicestage.v3.Mesher`
        :param timezone: 指定组件运行的时区，比如Asia/Shanghai
        :type timezone: str
        :param jvm_opts: jvm参数
        :type jvm_opts: str
        :param tomcat_opts: 
        :type tomcat_opts: :class:`huaweicloudsdkservicestage.v3.ComponentModifyTomcatOpts`
        :param logs: 
        :type logs: list[:class:`huaweicloudsdkservicestage.v3.ComponentLogs`]
        :param custom_metric: 
        :type custom_metric: :class:`huaweicloudsdkservicestage.v3.ComponentModifyCustomMetric`
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
        :param external_accesses: 
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v3.ExternalAccesses`]
        """
        
        

        self._name = None
        self._description = None
        self._labels = None
        self._runtime_stack = None
        self._source = None
        self._build = None
        self._environment_id = None
        self._limit_cpu = None
        self._limit_memory = None
        self._request_cpu = None
        self._request_memory = None
        self._replica = None
        self._version = None
        self._envs = None
        self._storages = None
        self._deploy_strategy = None
        self._command = None
        self._post_start = None
        self._pre_stop = None
        self._mesher = None
        self._timezone = None
        self._jvm_opts = None
        self._tomcat_opts = None
        self._logs = None
        self._custom_metric = None
        self._affinity = None
        self._anti_affinity = None
        self._liveness_probe = None
        self._readiness_probe = None
        self._refer_resources = None
        self._external_accesses = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        self.runtime_stack = runtime_stack
        self.source = source
        if build is not None:
            self.build = build
        if environment_id is not None:
            self.environment_id = environment_id
        if limit_cpu is not None:
            self.limit_cpu = limit_cpu
        if limit_memory is not None:
            self.limit_memory = limit_memory
        if request_cpu is not None:
            self.request_cpu = request_cpu
        if request_memory is not None:
            self.request_memory = request_memory
        self.replica = replica
        self.version = version
        if envs is not None:
            self.envs = envs
        if storages is not None:
            self.storages = storages
        if deploy_strategy is not None:
            self.deploy_strategy = deploy_strategy
        if command is not None:
            self.command = command
        if post_start is not None:
            self.post_start = post_start
        if pre_stop is not None:
            self.pre_stop = pre_stop
        if mesher is not None:
            self.mesher = mesher
        if timezone is not None:
            self.timezone = timezone
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
        self.refer_resources = refer_resources
        if external_accesses is not None:
            self.external_accesses = external_accesses

    @property
    def name(self):
        """Gets the name of this ComponentCreate.

        :return: The name of this ComponentCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentCreate.

        :param name: The name of this ComponentCreate.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ComponentCreate.

        :return: The description of this ComponentCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComponentCreate.

        :param description: The description of this ComponentCreate.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this ComponentCreate.

        :return: The labels of this ComponentCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.Label`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ComponentCreate.

        :param labels: The labels of this ComponentCreate.
        :type labels: list[:class:`huaweicloudsdkservicestage.v3.Label`]
        """
        self._labels = labels

    @property
    def runtime_stack(self):
        """Gets the runtime_stack of this ComponentCreate.

        :return: The runtime_stack of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.RuntimeStack`
        """
        return self._runtime_stack

    @runtime_stack.setter
    def runtime_stack(self, runtime_stack):
        """Sets the runtime_stack of this ComponentCreate.

        :param runtime_stack: The runtime_stack of this ComponentCreate.
        :type runtime_stack: :class:`huaweicloudsdkservicestage.v3.RuntimeStack`
        """
        self._runtime_stack = runtime_stack

    @property
    def source(self):
        """Gets the source of this ComponentCreate.

        :return: The source of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.SourceObject`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ComponentCreate.

        :param source: The source of this ComponentCreate.
        :type source: :class:`huaweicloudsdkservicestage.v3.SourceObject`
        """
        self._source = source

    @property
    def build(self):
        """Gets the build of this ComponentCreate.

        :return: The build of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.Build`
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ComponentCreate.

        :param build: The build of this ComponentCreate.
        :type build: :class:`huaweicloudsdkservicestage.v3.Build`
        """
        self._build = build

    @property
    def environment_id(self):
        """Gets the environment_id of this ComponentCreate.

        :return: The environment_id of this ComponentCreate.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this ComponentCreate.

        :param environment_id: The environment_id of this ComponentCreate.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def limit_cpu(self):
        """Gets the limit_cpu of this ComponentCreate.

        单位为Core

        :return: The limit_cpu of this ComponentCreate.
        :rtype: float
        """
        return self._limit_cpu

    @limit_cpu.setter
    def limit_cpu(self, limit_cpu):
        """Sets the limit_cpu of this ComponentCreate.

        单位为Core

        :param limit_cpu: The limit_cpu of this ComponentCreate.
        :type limit_cpu: float
        """
        self._limit_cpu = limit_cpu

    @property
    def limit_memory(self):
        """Gets the limit_memory of this ComponentCreate.

        单位为GiB

        :return: The limit_memory of this ComponentCreate.
        :rtype: float
        """
        return self._limit_memory

    @limit_memory.setter
    def limit_memory(self, limit_memory):
        """Sets the limit_memory of this ComponentCreate.

        单位为GiB

        :param limit_memory: The limit_memory of this ComponentCreate.
        :type limit_memory: float
        """
        self._limit_memory = limit_memory

    @property
    def request_cpu(self):
        """Gets the request_cpu of this ComponentCreate.

        单位为Core

        :return: The request_cpu of this ComponentCreate.
        :rtype: float
        """
        return self._request_cpu

    @request_cpu.setter
    def request_cpu(self, request_cpu):
        """Sets the request_cpu of this ComponentCreate.

        单位为Core

        :param request_cpu: The request_cpu of this ComponentCreate.
        :type request_cpu: float
        """
        self._request_cpu = request_cpu

    @property
    def request_memory(self):
        """Gets the request_memory of this ComponentCreate.

        单位为GiB

        :return: The request_memory of this ComponentCreate.
        :rtype: float
        """
        return self._request_memory

    @request_memory.setter
    def request_memory(self, request_memory):
        """Sets the request_memory of this ComponentCreate.

        单位为GiB

        :param request_memory: The request_memory of this ComponentCreate.
        :type request_memory: float
        """
        self._request_memory = request_memory

    @property
    def replica(self):
        """Gets the replica of this ComponentCreate.

        :return: The replica of this ComponentCreate.
        :rtype: int
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        """Sets the replica of this ComponentCreate.

        :param replica: The replica of this ComponentCreate.
        :type replica: int
        """
        self._replica = replica

    @property
    def version(self):
        """Gets the version of this ComponentCreate.

        :return: The version of this ComponentCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ComponentCreate.

        :param version: The version of this ComponentCreate.
        :type version: str
        """
        self._version = version

    @property
    def envs(self):
        """Gets the envs of this ComponentCreate.

        :return: The envs of this ComponentCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentEnvironment`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this ComponentCreate.

        :param envs: The envs of this ComponentCreate.
        :type envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentEnvironment`]
        """
        self._envs = envs

    @property
    def storages(self):
        """Gets the storages of this ComponentCreate.

        :return: The storages of this ComponentCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentStorage`]
        """
        return self._storages

    @storages.setter
    def storages(self, storages):
        """Sets the storages of this ComponentCreate.

        :param storages: The storages of this ComponentCreate.
        :type storages: list[:class:`huaweicloudsdkservicestage.v3.ComponentStorage`]
        """
        self._storages = storages

    @property
    def deploy_strategy(self):
        """Gets the deploy_strategy of this ComponentCreate.

        :return: The deploy_strategy of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.DeployStrategy`
        """
        return self._deploy_strategy

    @deploy_strategy.setter
    def deploy_strategy(self, deploy_strategy):
        """Sets the deploy_strategy of this ComponentCreate.

        :param deploy_strategy: The deploy_strategy of this ComponentCreate.
        :type deploy_strategy: :class:`huaweicloudsdkservicestage.v3.DeployStrategy`
        """
        self._deploy_strategy = deploy_strategy

    @property
    def command(self):
        """Gets the command of this ComponentCreate.

        :return: The command of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentCommand`
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ComponentCreate.

        :param command: The command of this ComponentCreate.
        :type command: :class:`huaweicloudsdkservicestage.v3.ComponentCommand`
        """
        self._command = command

    @property
    def post_start(self):
        """Gets the post_start of this ComponentCreate.

        :return: The post_start of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        """Sets the post_start of this ComponentCreate.

        :param post_start: The post_start of this ComponentCreate.
        :type post_start: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        """
        self._post_start = post_start

    @property
    def pre_stop(self):
        """Gets the pre_stop of this ComponentCreate.

        :return: The pre_stop of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        """Sets the pre_stop of this ComponentCreate.

        :param pre_stop: The pre_stop of this ComponentCreate.
        :type pre_stop: :class:`huaweicloudsdkservicestage.v3.ComponentLifecycle`
        """
        self._pre_stop = pre_stop

    @property
    def mesher(self):
        """Gets the mesher of this ComponentCreate.

        :return: The mesher of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.Mesher`
        """
        return self._mesher

    @mesher.setter
    def mesher(self, mesher):
        """Sets the mesher of this ComponentCreate.

        :param mesher: The mesher of this ComponentCreate.
        :type mesher: :class:`huaweicloudsdkservicestage.v3.Mesher`
        """
        self._mesher = mesher

    @property
    def timezone(self):
        """Gets the timezone of this ComponentCreate.

        指定组件运行的时区，比如Asia/Shanghai

        :return: The timezone of this ComponentCreate.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ComponentCreate.

        指定组件运行的时区，比如Asia/Shanghai

        :param timezone: The timezone of this ComponentCreate.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def jvm_opts(self):
        """Gets the jvm_opts of this ComponentCreate.

        jvm参数

        :return: The jvm_opts of this ComponentCreate.
        :rtype: str
        """
        return self._jvm_opts

    @jvm_opts.setter
    def jvm_opts(self, jvm_opts):
        """Sets the jvm_opts of this ComponentCreate.

        jvm参数

        :param jvm_opts: The jvm_opts of this ComponentCreate.
        :type jvm_opts: str
        """
        self._jvm_opts = jvm_opts

    @property
    def tomcat_opts(self):
        """Gets the tomcat_opts of this ComponentCreate.

        :return: The tomcat_opts of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentModifyTomcatOpts`
        """
        return self._tomcat_opts

    @tomcat_opts.setter
    def tomcat_opts(self, tomcat_opts):
        """Sets the tomcat_opts of this ComponentCreate.

        :param tomcat_opts: The tomcat_opts of this ComponentCreate.
        :type tomcat_opts: :class:`huaweicloudsdkservicestage.v3.ComponentModifyTomcatOpts`
        """
        self._tomcat_opts = tomcat_opts

    @property
    def logs(self):
        """Gets the logs of this ComponentCreate.

        :return: The logs of this ComponentCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentLogs`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ComponentCreate.

        :param logs: The logs of this ComponentCreate.
        :type logs: list[:class:`huaweicloudsdkservicestage.v3.ComponentLogs`]
        """
        self._logs = logs

    @property
    def custom_metric(self):
        """Gets the custom_metric of this ComponentCreate.

        :return: The custom_metric of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentModifyCustomMetric`
        """
        return self._custom_metric

    @custom_metric.setter
    def custom_metric(self, custom_metric):
        """Sets the custom_metric of this ComponentCreate.

        :param custom_metric: The custom_metric of this ComponentCreate.
        :type custom_metric: :class:`huaweicloudsdkservicestage.v3.ComponentModifyCustomMetric`
        """
        self._custom_metric = custom_metric

    @property
    def affinity(self):
        """Gets the affinity of this ComponentCreate.

        :return: The affinity of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this ComponentCreate.

        :param affinity: The affinity of this ComponentCreate.
        :type affinity: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        """
        self._affinity = affinity

    @property
    def anti_affinity(self):
        """Gets the anti_affinity of this ComponentCreate.

        :return: The anti_affinity of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        """
        return self._anti_affinity

    @anti_affinity.setter
    def anti_affinity(self, anti_affinity):
        """Sets the anti_affinity of this ComponentCreate.

        :param anti_affinity: The anti_affinity of this ComponentCreate.
        :type anti_affinity: :class:`huaweicloudsdkservicestage.v3.ComponentAffinity`
        """
        self._anti_affinity = anti_affinity

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this ComponentCreate.

        :return: The liveness_probe of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this ComponentCreate.

        :param liveness_probe: The liveness_probe of this ComponentCreate.
        :type liveness_probe: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        """
        self._liveness_probe = liveness_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this ComponentCreate.

        :return: The readiness_probe of this ComponentCreate.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this ComponentCreate.

        :param readiness_probe: The readiness_probe of this ComponentCreate.
        :type readiness_probe: :class:`huaweicloudsdkservicestage.v3.ComponentProbe`
        """
        self._readiness_probe = readiness_probe

    @property
    def refer_resources(self):
        """Gets the refer_resources of this ComponentCreate.

        :return: The refer_resources of this ComponentCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ReferResourceCreate`]
        """
        return self._refer_resources

    @refer_resources.setter
    def refer_resources(self, refer_resources):
        """Sets the refer_resources of this ComponentCreate.

        :param refer_resources: The refer_resources of this ComponentCreate.
        :type refer_resources: list[:class:`huaweicloudsdkservicestage.v3.ReferResourceCreate`]
        """
        self._refer_resources = refer_resources

    @property
    def external_accesses(self):
        """Gets the external_accesses of this ComponentCreate.

        :return: The external_accesses of this ComponentCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ExternalAccesses`]
        """
        return self._external_accesses

    @external_accesses.setter
    def external_accesses(self, external_accesses):
        """Sets the external_accesses of this ComponentCreate.

        :param external_accesses: The external_accesses of this ComponentCreate.
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v3.ExternalAccesses`]
        """
        self._external_accesses = external_accesses

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
        if not isinstance(other, ComponentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
