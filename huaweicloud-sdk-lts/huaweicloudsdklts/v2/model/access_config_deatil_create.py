# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigDeatilCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'paths': 'list[str]',
        'black_paths': 'list[str]',
        'format': 'AccessConfigFormatCreate',
        'windows_log_info': 'AccessConfigWindowsLogInfoCreate',
        'stdout': 'bool',
        'stderr': 'bool',
        'path_type': 'str',
        'namespace_regex': 'str',
        'pod_name_regex': 'str',
        'container_name_regex': 'str',
        'include_labels': 'dict(str, str)',
        'exclude_labels': 'dict(str, str)',
        'include_envs': 'dict(str, str)',
        'exclude_envs': 'dict(str, str)',
        'log_labels': 'dict(str, str)',
        'log_envs': 'dict(str, str)',
        'include_k8s_labels': 'dict(str, str)',
        'exclude_k8s_labels': 'dict(str, str)',
        'log_k8s': 'dict(str, str)',
        'repeat_collect': 'bool',
        'system_fields': 'list[str]',
        'custom_key_value': 'dict(str, str)',
        'include_labels_logical': 'str',
        'exclude_labels_logical': 'str',
        'include_k8s_labels_logical': 'str',
        'exclude_k8s_labels_logical': 'str',
        'include_envs_logical': 'str',
        'exclude_envs_logical': 'str'
    }

    attribute_map = {
        'paths': 'paths',
        'black_paths': 'black_paths',
        'format': 'format',
        'windows_log_info': 'windows_log_info',
        'stdout': 'stdout',
        'stderr': 'stderr',
        'path_type': 'pathType',
        'namespace_regex': 'namespaceRegex',
        'pod_name_regex': 'podNameRegex',
        'container_name_regex': 'containerNameRegex',
        'include_labels': 'includeLabels',
        'exclude_labels': 'excludeLabels',
        'include_envs': 'includeEnvs',
        'exclude_envs': 'excludeEnvs',
        'log_labels': 'logLabels',
        'log_envs': 'logEnvs',
        'include_k8s_labels': 'includeK8sLabels',
        'exclude_k8s_labels': 'excludeK8sLabels',
        'log_k8s': 'logK8s',
        'repeat_collect': 'repeat_collect',
        'system_fields': 'system_fields',
        'custom_key_value': 'custom_key_value',
        'include_labels_logical': 'includeLabelsLogical',
        'exclude_labels_logical': 'excludeLabelsLogical',
        'include_k8s_labels_logical': 'includeK8sLabelsLogical',
        'exclude_k8s_labels_logical': 'excludeK8sLabelsLogical',
        'include_envs_logical': 'includeEnvsLogical',
        'exclude_envs_logical': 'excludeEnvsLogical'
    }

    def __init__(self, paths=None, black_paths=None, format=None, windows_log_info=None, stdout=None, stderr=None, path_type=None, namespace_regex=None, pod_name_regex=None, container_name_regex=None, include_labels=None, exclude_labels=None, include_envs=None, exclude_envs=None, log_labels=None, log_envs=None, include_k8s_labels=None, exclude_k8s_labels=None, log_k8s=None, repeat_collect=None, system_fields=None, custom_key_value=None, include_labels_logical=None, exclude_labels_logical=None, include_k8s_labels_logical=None, exclude_k8s_labels_logical=None, include_envs_logical=None, exclude_envs_logical=None):
        r"""AccessConfigDeatilCreate

        The model defined in huaweicloud sdk

        :param paths: 采集路径。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符&lt;&gt; &#39; | \&quot; 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次&#x60;&#x60; CCE类型中 容器路径和主机路径必填，标准输出不用 最小长度：1 最大长度：128
        :type paths: list[str]
        :param black_paths: 采集路径黑名单。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符&lt;&gt; &#39; | \&quot; 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 最小长度：1 最大长度：128
        :type black_paths: list[str]
        :param format: 
        :type format: :class:`huaweicloudsdklts.v2.AccessConfigFormatCreate`
        :param windows_log_info: 
        :type windows_log_info: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoCreate`
        :param stdout: 标准输出开关，仅CCE接入类型时使用
        :type stdout: bool
        :param stderr: 标准输出开关标准错误开关，仅CCE接入类型时使用
        :type stderr: bool
        :param path_type: CCE接入类型，仅CCE接入类型时使用
        :type path_type: str
        :param namespace_regex: K8s Namespace正则匹配，仅CCE接入类型时使用
        :type namespace_regex: str
        :param pod_name_regex: K8s Pod正则匹配，仅CCE接入类型时使用
        :type pod_name_regex: str
        :param container_name_regex: K8s 容器名称正则匹配，仅CCE接入类型时使用
        :type container_name_regex: str
        :param include_labels: 容器 Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type include_labels: dict(str, str)
        :param exclude_labels: 容器 Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type exclude_labels: dict(str, str)
        :param include_envs: 环境变量白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type include_envs: dict(str, str)
        :param exclude_envs: 环境变量黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type exclude_envs: dict(str, str)
        :param log_labels: 容器 Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type log_labels: dict(str, str)
        :param log_envs: 环境变量日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type log_envs: dict(str, str)
        :param include_k8s_labels: K8s Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type include_k8s_labels: dict(str, str)
        :param exclude_k8s_labels: K8s Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type exclude_k8s_labels: dict(str, str)
        :param log_k8s: K8s Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用
        :type log_k8s: dict(str, str)
        :param repeat_collect: 是否允许此文件重复采集
        :type repeat_collect: bool
        :param system_fields: 系统内置字段：配置日志接入规则时，可以配置系统内置字段，上报日志后，每条日志数据的标签数据中将会有系统字段 采集场景为主机文件的内置字段为：hostName、hostId、hostIP、pathFile、hostIPv6、category、collectTime、__host_group__ 采集场景为K8S集群容器文件的内置字段为：hostName、hostId、hostIP、pathFile、hostIPv6、clusterId、podName、appName、containerName、nameSpace、category、collectTime、__host_group__、serviceID、podIp、clusterName、workloadType 若修改时传入此字段，将覆盖原有配置
        :type system_fields: list[str]
        :param custom_key_value: 自定义键值对：配置日志接入规则时，可以配置自定义键值对规则，上报日志后，每条日志数据的标签数据中将会有用户自定义的键值对字段，键值对数量不超过20 键的长度限制为128，允许的字符有a-zA-Z0-9_- 值的长度限制为1024
        :type custom_key_value: dict(str, str)
        :param include_labels_logical: 容器 Label白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效
        :type include_labels_logical: str
        :param exclude_labels_logical: 容器 Label黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效
        :type exclude_labels_logical: str
        :param include_k8s_labels_logical: K8S Label白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效
        :type include_k8s_labels_logical: str
        :param exclude_k8s_labels_logical: K8S Label黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效
        :type exclude_k8s_labels_logical: str
        :param include_envs_logical: 环境变量白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效
        :type include_envs_logical: str
        :param exclude_envs_logical: 环境变量黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效
        :type exclude_envs_logical: str
        """
        
        

        self._paths = None
        self._black_paths = None
        self._format = None
        self._windows_log_info = None
        self._stdout = None
        self._stderr = None
        self._path_type = None
        self._namespace_regex = None
        self._pod_name_regex = None
        self._container_name_regex = None
        self._include_labels = None
        self._exclude_labels = None
        self._include_envs = None
        self._exclude_envs = None
        self._log_labels = None
        self._log_envs = None
        self._include_k8s_labels = None
        self._exclude_k8s_labels = None
        self._log_k8s = None
        self._repeat_collect = None
        self._system_fields = None
        self._custom_key_value = None
        self._include_labels_logical = None
        self._exclude_labels_logical = None
        self._include_k8s_labels_logical = None
        self._exclude_k8s_labels_logical = None
        self._include_envs_logical = None
        self._exclude_envs_logical = None
        self.discriminator = None

        if paths is not None:
            self.paths = paths
        if black_paths is not None:
            self.black_paths = black_paths
        self.format = format
        if windows_log_info is not None:
            self.windows_log_info = windows_log_info
        if stdout is not None:
            self.stdout = stdout
        if stderr is not None:
            self.stderr = stderr
        if path_type is not None:
            self.path_type = path_type
        if namespace_regex is not None:
            self.namespace_regex = namespace_regex
        if pod_name_regex is not None:
            self.pod_name_regex = pod_name_regex
        if container_name_regex is not None:
            self.container_name_regex = container_name_regex
        if include_labels is not None:
            self.include_labels = include_labels
        if exclude_labels is not None:
            self.exclude_labels = exclude_labels
        if include_envs is not None:
            self.include_envs = include_envs
        if exclude_envs is not None:
            self.exclude_envs = exclude_envs
        if log_labels is not None:
            self.log_labels = log_labels
        if log_envs is not None:
            self.log_envs = log_envs
        if include_k8s_labels is not None:
            self.include_k8s_labels = include_k8s_labels
        if exclude_k8s_labels is not None:
            self.exclude_k8s_labels = exclude_k8s_labels
        if log_k8s is not None:
            self.log_k8s = log_k8s
        if repeat_collect is not None:
            self.repeat_collect = repeat_collect
        if system_fields is not None:
            self.system_fields = system_fields
        if custom_key_value is not None:
            self.custom_key_value = custom_key_value
        if include_labels_logical is not None:
            self.include_labels_logical = include_labels_logical
        if exclude_labels_logical is not None:
            self.exclude_labels_logical = exclude_labels_logical
        if include_k8s_labels_logical is not None:
            self.include_k8s_labels_logical = include_k8s_labels_logical
        if exclude_k8s_labels_logical is not None:
            self.exclude_k8s_labels_logical = exclude_k8s_labels_logical
        if include_envs_logical is not None:
            self.include_envs_logical = include_envs_logical
        if exclude_envs_logical is not None:
            self.exclude_envs_logical = exclude_envs_logical

    @property
    def paths(self):
        r"""Gets the paths of this AccessConfigDeatilCreate.

        采集路径。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符<> ' | \" 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次`` CCE类型中 容器路径和主机路径必填，标准输出不用 最小长度：1 最大长度：128

        :return: The paths of this AccessConfigDeatilCreate.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        r"""Sets the paths of this AccessConfigDeatilCreate.

        采集路径。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符<> ' | \" 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次`` CCE类型中 容器路径和主机路径必填，标准输出不用 最小长度：1 最大长度：128

        :param paths: The paths of this AccessConfigDeatilCreate.
        :type paths: list[str]
        """
        self._paths = paths

    @property
    def black_paths(self):
        r"""Gets the black_paths of this AccessConfigDeatilCreate.

        采集路径黑名单。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符<> ' | \" 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 最小长度：1 最大长度：128

        :return: The black_paths of this AccessConfigDeatilCreate.
        :rtype: list[str]
        """
        return self._black_paths

    @black_paths.setter
    def black_paths(self, black_paths):
        r"""Sets the black_paths of this AccessConfigDeatilCreate.

        采集路径黑名单。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符<> ' | \" 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 最小长度：1 最大长度：128

        :param black_paths: The black_paths of this AccessConfigDeatilCreate.
        :type black_paths: list[str]
        """
        self._black_paths = black_paths

    @property
    def format(self):
        r"""Gets the format of this AccessConfigDeatilCreate.

        :return: The format of this AccessConfigDeatilCreate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigFormatCreate`
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this AccessConfigDeatilCreate.

        :param format: The format of this AccessConfigDeatilCreate.
        :type format: :class:`huaweicloudsdklts.v2.AccessConfigFormatCreate`
        """
        self._format = format

    @property
    def windows_log_info(self):
        r"""Gets the windows_log_info of this AccessConfigDeatilCreate.

        :return: The windows_log_info of this AccessConfigDeatilCreate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoCreate`
        """
        return self._windows_log_info

    @windows_log_info.setter
    def windows_log_info(self, windows_log_info):
        r"""Sets the windows_log_info of this AccessConfigDeatilCreate.

        :param windows_log_info: The windows_log_info of this AccessConfigDeatilCreate.
        :type windows_log_info: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoCreate`
        """
        self._windows_log_info = windows_log_info

    @property
    def stdout(self):
        r"""Gets the stdout of this AccessConfigDeatilCreate.

        标准输出开关，仅CCE接入类型时使用

        :return: The stdout of this AccessConfigDeatilCreate.
        :rtype: bool
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        r"""Sets the stdout of this AccessConfigDeatilCreate.

        标准输出开关，仅CCE接入类型时使用

        :param stdout: The stdout of this AccessConfigDeatilCreate.
        :type stdout: bool
        """
        self._stdout = stdout

    @property
    def stderr(self):
        r"""Gets the stderr of this AccessConfigDeatilCreate.

        标准输出开关标准错误开关，仅CCE接入类型时使用

        :return: The stderr of this AccessConfigDeatilCreate.
        :rtype: bool
        """
        return self._stderr

    @stderr.setter
    def stderr(self, stderr):
        r"""Sets the stderr of this AccessConfigDeatilCreate.

        标准输出开关标准错误开关，仅CCE接入类型时使用

        :param stderr: The stderr of this AccessConfigDeatilCreate.
        :type stderr: bool
        """
        self._stderr = stderr

    @property
    def path_type(self):
        r"""Gets the path_type of this AccessConfigDeatilCreate.

        CCE接入类型，仅CCE接入类型时使用

        :return: The path_type of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._path_type

    @path_type.setter
    def path_type(self, path_type):
        r"""Sets the path_type of this AccessConfigDeatilCreate.

        CCE接入类型，仅CCE接入类型时使用

        :param path_type: The path_type of this AccessConfigDeatilCreate.
        :type path_type: str
        """
        self._path_type = path_type

    @property
    def namespace_regex(self):
        r"""Gets the namespace_regex of this AccessConfigDeatilCreate.

        K8s Namespace正则匹配，仅CCE接入类型时使用

        :return: The namespace_regex of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._namespace_regex

    @namespace_regex.setter
    def namespace_regex(self, namespace_regex):
        r"""Sets the namespace_regex of this AccessConfigDeatilCreate.

        K8s Namespace正则匹配，仅CCE接入类型时使用

        :param namespace_regex: The namespace_regex of this AccessConfigDeatilCreate.
        :type namespace_regex: str
        """
        self._namespace_regex = namespace_regex

    @property
    def pod_name_regex(self):
        r"""Gets the pod_name_regex of this AccessConfigDeatilCreate.

        K8s Pod正则匹配，仅CCE接入类型时使用

        :return: The pod_name_regex of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._pod_name_regex

    @pod_name_regex.setter
    def pod_name_regex(self, pod_name_regex):
        r"""Sets the pod_name_regex of this AccessConfigDeatilCreate.

        K8s Pod正则匹配，仅CCE接入类型时使用

        :param pod_name_regex: The pod_name_regex of this AccessConfigDeatilCreate.
        :type pod_name_regex: str
        """
        self._pod_name_regex = pod_name_regex

    @property
    def container_name_regex(self):
        r"""Gets the container_name_regex of this AccessConfigDeatilCreate.

        K8s 容器名称正则匹配，仅CCE接入类型时使用

        :return: The container_name_regex of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._container_name_regex

    @container_name_regex.setter
    def container_name_regex(self, container_name_regex):
        r"""Sets the container_name_regex of this AccessConfigDeatilCreate.

        K8s 容器名称正则匹配，仅CCE接入类型时使用

        :param container_name_regex: The container_name_regex of this AccessConfigDeatilCreate.
        :type container_name_regex: str
        """
        self._container_name_regex = container_name_regex

    @property
    def include_labels(self):
        r"""Gets the include_labels of this AccessConfigDeatilCreate.

        容器 Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The include_labels of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._include_labels

    @include_labels.setter
    def include_labels(self, include_labels):
        r"""Sets the include_labels of this AccessConfigDeatilCreate.

        容器 Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param include_labels: The include_labels of this AccessConfigDeatilCreate.
        :type include_labels: dict(str, str)
        """
        self._include_labels = include_labels

    @property
    def exclude_labels(self):
        r"""Gets the exclude_labels of this AccessConfigDeatilCreate.

        容器 Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The exclude_labels of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._exclude_labels

    @exclude_labels.setter
    def exclude_labels(self, exclude_labels):
        r"""Sets the exclude_labels of this AccessConfigDeatilCreate.

        容器 Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param exclude_labels: The exclude_labels of this AccessConfigDeatilCreate.
        :type exclude_labels: dict(str, str)
        """
        self._exclude_labels = exclude_labels

    @property
    def include_envs(self):
        r"""Gets the include_envs of this AccessConfigDeatilCreate.

        环境变量白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The include_envs of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._include_envs

    @include_envs.setter
    def include_envs(self, include_envs):
        r"""Sets the include_envs of this AccessConfigDeatilCreate.

        环境变量白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param include_envs: The include_envs of this AccessConfigDeatilCreate.
        :type include_envs: dict(str, str)
        """
        self._include_envs = include_envs

    @property
    def exclude_envs(self):
        r"""Gets the exclude_envs of this AccessConfigDeatilCreate.

        环境变量黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The exclude_envs of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._exclude_envs

    @exclude_envs.setter
    def exclude_envs(self, exclude_envs):
        r"""Sets the exclude_envs of this AccessConfigDeatilCreate.

        环境变量黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param exclude_envs: The exclude_envs of this AccessConfigDeatilCreate.
        :type exclude_envs: dict(str, str)
        """
        self._exclude_envs = exclude_envs

    @property
    def log_labels(self):
        r"""Gets the log_labels of this AccessConfigDeatilCreate.

        容器 Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The log_labels of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._log_labels

    @log_labels.setter
    def log_labels(self, log_labels):
        r"""Sets the log_labels of this AccessConfigDeatilCreate.

        容器 Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param log_labels: The log_labels of this AccessConfigDeatilCreate.
        :type log_labels: dict(str, str)
        """
        self._log_labels = log_labels

    @property
    def log_envs(self):
        r"""Gets the log_envs of this AccessConfigDeatilCreate.

        环境变量日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The log_envs of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._log_envs

    @log_envs.setter
    def log_envs(self, log_envs):
        r"""Sets the log_envs of this AccessConfigDeatilCreate.

        环境变量日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param log_envs: The log_envs of this AccessConfigDeatilCreate.
        :type log_envs: dict(str, str)
        """
        self._log_envs = log_envs

    @property
    def include_k8s_labels(self):
        r"""Gets the include_k8s_labels of this AccessConfigDeatilCreate.

        K8s Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The include_k8s_labels of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._include_k8s_labels

    @include_k8s_labels.setter
    def include_k8s_labels(self, include_k8s_labels):
        r"""Sets the include_k8s_labels of this AccessConfigDeatilCreate.

        K8s Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param include_k8s_labels: The include_k8s_labels of this AccessConfigDeatilCreate.
        :type include_k8s_labels: dict(str, str)
        """
        self._include_k8s_labels = include_k8s_labels

    @property
    def exclude_k8s_labels(self):
        r"""Gets the exclude_k8s_labels of this AccessConfigDeatilCreate.

        K8s Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The exclude_k8s_labels of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._exclude_k8s_labels

    @exclude_k8s_labels.setter
    def exclude_k8s_labels(self, exclude_k8s_labels):
        r"""Sets the exclude_k8s_labels of this AccessConfigDeatilCreate.

        K8s Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param exclude_k8s_labels: The exclude_k8s_labels of this AccessConfigDeatilCreate.
        :type exclude_k8s_labels: dict(str, str)
        """
        self._exclude_k8s_labels = exclude_k8s_labels

    @property
    def log_k8s(self):
        r"""Gets the log_k8s of this AccessConfigDeatilCreate.

        K8s Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The log_k8s of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._log_k8s

    @log_k8s.setter
    def log_k8s(self, log_k8s):
        r"""Sets the log_k8s of this AccessConfigDeatilCreate.

        K8s Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param log_k8s: The log_k8s of this AccessConfigDeatilCreate.
        :type log_k8s: dict(str, str)
        """
        self._log_k8s = log_k8s

    @property
    def repeat_collect(self):
        r"""Gets the repeat_collect of this AccessConfigDeatilCreate.

        是否允许此文件重复采集

        :return: The repeat_collect of this AccessConfigDeatilCreate.
        :rtype: bool
        """
        return self._repeat_collect

    @repeat_collect.setter
    def repeat_collect(self, repeat_collect):
        r"""Sets the repeat_collect of this AccessConfigDeatilCreate.

        是否允许此文件重复采集

        :param repeat_collect: The repeat_collect of this AccessConfigDeatilCreate.
        :type repeat_collect: bool
        """
        self._repeat_collect = repeat_collect

    @property
    def system_fields(self):
        r"""Gets the system_fields of this AccessConfigDeatilCreate.

        系统内置字段：配置日志接入规则时，可以配置系统内置字段，上报日志后，每条日志数据的标签数据中将会有系统字段 采集场景为主机文件的内置字段为：hostName、hostId、hostIP、pathFile、hostIPv6、category、collectTime、__host_group__ 采集场景为K8S集群容器文件的内置字段为：hostName、hostId、hostIP、pathFile、hostIPv6、clusterId、podName、appName、containerName、nameSpace、category、collectTime、__host_group__、serviceID、podIp、clusterName、workloadType 若修改时传入此字段，将覆盖原有配置

        :return: The system_fields of this AccessConfigDeatilCreate.
        :rtype: list[str]
        """
        return self._system_fields

    @system_fields.setter
    def system_fields(self, system_fields):
        r"""Sets the system_fields of this AccessConfigDeatilCreate.

        系统内置字段：配置日志接入规则时，可以配置系统内置字段，上报日志后，每条日志数据的标签数据中将会有系统字段 采集场景为主机文件的内置字段为：hostName、hostId、hostIP、pathFile、hostIPv6、category、collectTime、__host_group__ 采集场景为K8S集群容器文件的内置字段为：hostName、hostId、hostIP、pathFile、hostIPv6、clusterId、podName、appName、containerName、nameSpace、category、collectTime、__host_group__、serviceID、podIp、clusterName、workloadType 若修改时传入此字段，将覆盖原有配置

        :param system_fields: The system_fields of this AccessConfigDeatilCreate.
        :type system_fields: list[str]
        """
        self._system_fields = system_fields

    @property
    def custom_key_value(self):
        r"""Gets the custom_key_value of this AccessConfigDeatilCreate.

        自定义键值对：配置日志接入规则时，可以配置自定义键值对规则，上报日志后，每条日志数据的标签数据中将会有用户自定义的键值对字段，键值对数量不超过20 键的长度限制为128，允许的字符有a-zA-Z0-9_- 值的长度限制为1024

        :return: The custom_key_value of this AccessConfigDeatilCreate.
        :rtype: dict(str, str)
        """
        return self._custom_key_value

    @custom_key_value.setter
    def custom_key_value(self, custom_key_value):
        r"""Sets the custom_key_value of this AccessConfigDeatilCreate.

        自定义键值对：配置日志接入规则时，可以配置自定义键值对规则，上报日志后，每条日志数据的标签数据中将会有用户自定义的键值对字段，键值对数量不超过20 键的长度限制为128，允许的字符有a-zA-Z0-9_- 值的长度限制为1024

        :param custom_key_value: The custom_key_value of this AccessConfigDeatilCreate.
        :type custom_key_value: dict(str, str)
        """
        self._custom_key_value = custom_key_value

    @property
    def include_labels_logical(self):
        r"""Gets the include_labels_logical of this AccessConfigDeatilCreate.

        容器 Label白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :return: The include_labels_logical of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._include_labels_logical

    @include_labels_logical.setter
    def include_labels_logical(self, include_labels_logical):
        r"""Sets the include_labels_logical of this AccessConfigDeatilCreate.

        容器 Label白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :param include_labels_logical: The include_labels_logical of this AccessConfigDeatilCreate.
        :type include_labels_logical: str
        """
        self._include_labels_logical = include_labels_logical

    @property
    def exclude_labels_logical(self):
        r"""Gets the exclude_labels_logical of this AccessConfigDeatilCreate.

        容器 Label黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :return: The exclude_labels_logical of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._exclude_labels_logical

    @exclude_labels_logical.setter
    def exclude_labels_logical(self, exclude_labels_logical):
        r"""Sets the exclude_labels_logical of this AccessConfigDeatilCreate.

        容器 Label黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :param exclude_labels_logical: The exclude_labels_logical of this AccessConfigDeatilCreate.
        :type exclude_labels_logical: str
        """
        self._exclude_labels_logical = exclude_labels_logical

    @property
    def include_k8s_labels_logical(self):
        r"""Gets the include_k8s_labels_logical of this AccessConfigDeatilCreate.

        K8S Label白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :return: The include_k8s_labels_logical of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._include_k8s_labels_logical

    @include_k8s_labels_logical.setter
    def include_k8s_labels_logical(self, include_k8s_labels_logical):
        r"""Sets the include_k8s_labels_logical of this AccessConfigDeatilCreate.

        K8S Label白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :param include_k8s_labels_logical: The include_k8s_labels_logical of this AccessConfigDeatilCreate.
        :type include_k8s_labels_logical: str
        """
        self._include_k8s_labels_logical = include_k8s_labels_logical

    @property
    def exclude_k8s_labels_logical(self):
        r"""Gets the exclude_k8s_labels_logical of this AccessConfigDeatilCreate.

        K8S Label黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :return: The exclude_k8s_labels_logical of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._exclude_k8s_labels_logical

    @exclude_k8s_labels_logical.setter
    def exclude_k8s_labels_logical(self, exclude_k8s_labels_logical):
        r"""Sets the exclude_k8s_labels_logical of this AccessConfigDeatilCreate.

        K8S Label黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :param exclude_k8s_labels_logical: The exclude_k8s_labels_logical of this AccessConfigDeatilCreate.
        :type exclude_k8s_labels_logical: str
        """
        self._exclude_k8s_labels_logical = exclude_k8s_labels_logical

    @property
    def include_envs_logical(self):
        r"""Gets the include_envs_logical of this AccessConfigDeatilCreate.

        环境变量白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :return: The include_envs_logical of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._include_envs_logical

    @include_envs_logical.setter
    def include_envs_logical(self, include_envs_logical):
        r"""Sets the include_envs_logical of this AccessConfigDeatilCreate.

        环境变量白名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :param include_envs_logical: The include_envs_logical of this AccessConfigDeatilCreate.
        :type include_envs_logical: str
        """
        self._include_envs_logical = include_envs_logical

    @property
    def exclude_envs_logical(self):
        r"""Gets the exclude_envs_logical of this AccessConfigDeatilCreate.

        环境变量黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :return: The exclude_envs_logical of this AccessConfigDeatilCreate.
        :rtype: str
        """
        return self._exclude_envs_logical

    @exclude_envs_logical.setter
    def exclude_envs_logical(self, exclude_envs_logical):
        r"""Sets the exclude_envs_logical of this AccessConfigDeatilCreate.

        环境变量黑名单，可选为AND，OR，不配置时默认为OR；当存在多个值时的处理逻辑，AND表示同时满足才会生效，OR表示有一项满足就会生效

        :param exclude_envs_logical: The exclude_envs_logical of this AccessConfigDeatilCreate.
        :type exclude_envs_logical: str
        """
        self._exclude_envs_logical = exclude_envs_logical

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
        if not isinstance(other, AccessConfigDeatilCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
