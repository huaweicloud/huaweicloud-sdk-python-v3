# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigDeatilUpdate:

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
        'format': 'AccessConfigFormatUpdate',
        'windows_log_info': 'AccessConfigWindowsLogInfoUpdate',
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
        'log_k8s': 'dict(str, str)'
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
        'log_k8s': 'logK8s'
    }

    def __init__(self, paths=None, black_paths=None, format=None, windows_log_info=None, stdout=None, stderr=None, path_type=None, namespace_regex=None, pod_name_regex=None, container_name_regex=None, include_labels=None, exclude_labels=None, include_envs=None, exclude_envs=None, log_labels=None, log_envs=None, include_k8s_labels=None, exclude_k8s_labels=None, log_k8s=None):
        """AccessConfigDeatilUpdate

        The model defined in huaweicloud sdk

        :param paths: 1.路径必须以/或者字母:\\开头 2.不能包含特殊字符&lt;&gt; &#39; | \&quot; 且不能只输入/ 3.第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 5.最大数量为10
        :type paths: list[str]
        :param black_paths: 1.路径必须以/或者字母:\\开头 2.不能包含特殊字符&lt;&gt; &#39; | \&quot; 且不能只输入/ 3.第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 5.最大数量为10
        :type black_paths: list[str]
        :param format: 
        :type format: :class:`huaweicloudsdklts.v2.AccessConfigFormatUpdate`
        :param windows_log_info: 
        :type windows_log_info: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoUpdate`
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
        self.discriminator = None

        if paths is not None:
            self.paths = paths
        if black_paths is not None:
            self.black_paths = black_paths
        if format is not None:
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

    @property
    def paths(self):
        """Gets the paths of this AccessConfigDeatilUpdate.

        1.路径必须以/或者字母:\\开头 2.不能包含特殊字符<> ' | \" 且不能只输入/ 3.第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 5.最大数量为10

        :return: The paths of this AccessConfigDeatilUpdate.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this AccessConfigDeatilUpdate.

        1.路径必须以/或者字母:\\开头 2.不能包含特殊字符<> ' | \" 且不能只输入/ 3.第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 5.最大数量为10

        :param paths: The paths of this AccessConfigDeatilUpdate.
        :type paths: list[str]
        """
        self._paths = paths

    @property
    def black_paths(self):
        """Gets the black_paths of this AccessConfigDeatilUpdate.

        1.路径必须以/或者字母:\\开头 2.不能包含特殊字符<> ' | \" 且不能只输入/ 3.第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 5.最大数量为10

        :return: The black_paths of this AccessConfigDeatilUpdate.
        :rtype: list[str]
        """
        return self._black_paths

    @black_paths.setter
    def black_paths(self, black_paths):
        """Sets the black_paths of this AccessConfigDeatilUpdate.

        1.路径必须以/或者字母:\\开头 2.不能包含特殊字符<> ' | \" 且不能只输入/ 3.第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次 5.最大数量为10

        :param black_paths: The black_paths of this AccessConfigDeatilUpdate.
        :type black_paths: list[str]
        """
        self._black_paths = black_paths

    @property
    def format(self):
        """Gets the format of this AccessConfigDeatilUpdate.

        :return: The format of this AccessConfigDeatilUpdate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigFormatUpdate`
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AccessConfigDeatilUpdate.

        :param format: The format of this AccessConfigDeatilUpdate.
        :type format: :class:`huaweicloudsdklts.v2.AccessConfigFormatUpdate`
        """
        self._format = format

    @property
    def windows_log_info(self):
        """Gets the windows_log_info of this AccessConfigDeatilUpdate.

        :return: The windows_log_info of this AccessConfigDeatilUpdate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoUpdate`
        """
        return self._windows_log_info

    @windows_log_info.setter
    def windows_log_info(self, windows_log_info):
        """Sets the windows_log_info of this AccessConfigDeatilUpdate.

        :param windows_log_info: The windows_log_info of this AccessConfigDeatilUpdate.
        :type windows_log_info: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoUpdate`
        """
        self._windows_log_info = windows_log_info

    @property
    def stdout(self):
        """Gets the stdout of this AccessConfigDeatilUpdate.

        标准输出开关，仅CCE接入类型时使用

        :return: The stdout of this AccessConfigDeatilUpdate.
        :rtype: bool
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        """Sets the stdout of this AccessConfigDeatilUpdate.

        标准输出开关，仅CCE接入类型时使用

        :param stdout: The stdout of this AccessConfigDeatilUpdate.
        :type stdout: bool
        """
        self._stdout = stdout

    @property
    def stderr(self):
        """Gets the stderr of this AccessConfigDeatilUpdate.

        标准输出开关标准错误开关，仅CCE接入类型时使用

        :return: The stderr of this AccessConfigDeatilUpdate.
        :rtype: bool
        """
        return self._stderr

    @stderr.setter
    def stderr(self, stderr):
        """Sets the stderr of this AccessConfigDeatilUpdate.

        标准输出开关标准错误开关，仅CCE接入类型时使用

        :param stderr: The stderr of this AccessConfigDeatilUpdate.
        :type stderr: bool
        """
        self._stderr = stderr

    @property
    def path_type(self):
        """Gets the path_type of this AccessConfigDeatilUpdate.

        CCE接入类型，仅CCE接入类型时使用

        :return: The path_type of this AccessConfigDeatilUpdate.
        :rtype: str
        """
        return self._path_type

    @path_type.setter
    def path_type(self, path_type):
        """Sets the path_type of this AccessConfigDeatilUpdate.

        CCE接入类型，仅CCE接入类型时使用

        :param path_type: The path_type of this AccessConfigDeatilUpdate.
        :type path_type: str
        """
        self._path_type = path_type

    @property
    def namespace_regex(self):
        """Gets the namespace_regex of this AccessConfigDeatilUpdate.

        K8s Namespace正则匹配，仅CCE接入类型时使用

        :return: The namespace_regex of this AccessConfigDeatilUpdate.
        :rtype: str
        """
        return self._namespace_regex

    @namespace_regex.setter
    def namespace_regex(self, namespace_regex):
        """Sets the namespace_regex of this AccessConfigDeatilUpdate.

        K8s Namespace正则匹配，仅CCE接入类型时使用

        :param namespace_regex: The namespace_regex of this AccessConfigDeatilUpdate.
        :type namespace_regex: str
        """
        self._namespace_regex = namespace_regex

    @property
    def pod_name_regex(self):
        """Gets the pod_name_regex of this AccessConfigDeatilUpdate.

        K8s Pod正则匹配，仅CCE接入类型时使用

        :return: The pod_name_regex of this AccessConfigDeatilUpdate.
        :rtype: str
        """
        return self._pod_name_regex

    @pod_name_regex.setter
    def pod_name_regex(self, pod_name_regex):
        """Sets the pod_name_regex of this AccessConfigDeatilUpdate.

        K8s Pod正则匹配，仅CCE接入类型时使用

        :param pod_name_regex: The pod_name_regex of this AccessConfigDeatilUpdate.
        :type pod_name_regex: str
        """
        self._pod_name_regex = pod_name_regex

    @property
    def container_name_regex(self):
        """Gets the container_name_regex of this AccessConfigDeatilUpdate.

        K8s 容器名称正则匹配，仅CCE接入类型时使用

        :return: The container_name_regex of this AccessConfigDeatilUpdate.
        :rtype: str
        """
        return self._container_name_regex

    @container_name_regex.setter
    def container_name_regex(self, container_name_regex):
        """Sets the container_name_regex of this AccessConfigDeatilUpdate.

        K8s 容器名称正则匹配，仅CCE接入类型时使用

        :param container_name_regex: The container_name_regex of this AccessConfigDeatilUpdate.
        :type container_name_regex: str
        """
        self._container_name_regex = container_name_regex

    @property
    def include_labels(self):
        """Gets the include_labels of this AccessConfigDeatilUpdate.

        容器 Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The include_labels of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._include_labels

    @include_labels.setter
    def include_labels(self, include_labels):
        """Sets the include_labels of this AccessConfigDeatilUpdate.

        容器 Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param include_labels: The include_labels of this AccessConfigDeatilUpdate.
        :type include_labels: dict(str, str)
        """
        self._include_labels = include_labels

    @property
    def exclude_labels(self):
        """Gets the exclude_labels of this AccessConfigDeatilUpdate.

        容器 Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The exclude_labels of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._exclude_labels

    @exclude_labels.setter
    def exclude_labels(self, exclude_labels):
        """Sets the exclude_labels of this AccessConfigDeatilUpdate.

        容器 Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param exclude_labels: The exclude_labels of this AccessConfigDeatilUpdate.
        :type exclude_labels: dict(str, str)
        """
        self._exclude_labels = exclude_labels

    @property
    def include_envs(self):
        """Gets the include_envs of this AccessConfigDeatilUpdate.

        环境变量白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The include_envs of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._include_envs

    @include_envs.setter
    def include_envs(self, include_envs):
        """Sets the include_envs of this AccessConfigDeatilUpdate.

        环境变量白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param include_envs: The include_envs of this AccessConfigDeatilUpdate.
        :type include_envs: dict(str, str)
        """
        self._include_envs = include_envs

    @property
    def exclude_envs(self):
        """Gets the exclude_envs of this AccessConfigDeatilUpdate.

        环境变量黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The exclude_envs of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._exclude_envs

    @exclude_envs.setter
    def exclude_envs(self, exclude_envs):
        """Sets the exclude_envs of this AccessConfigDeatilUpdate.

        环境变量黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param exclude_envs: The exclude_envs of this AccessConfigDeatilUpdate.
        :type exclude_envs: dict(str, str)
        """
        self._exclude_envs = exclude_envs

    @property
    def log_labels(self):
        """Gets the log_labels of this AccessConfigDeatilUpdate.

        容器 Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The log_labels of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._log_labels

    @log_labels.setter
    def log_labels(self, log_labels):
        """Sets the log_labels of this AccessConfigDeatilUpdate.

        容器 Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param log_labels: The log_labels of this AccessConfigDeatilUpdate.
        :type log_labels: dict(str, str)
        """
        self._log_labels = log_labels

    @property
    def log_envs(self):
        """Gets the log_envs of this AccessConfigDeatilUpdate.

        环境变量日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The log_envs of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._log_envs

    @log_envs.setter
    def log_envs(self, log_envs):
        """Sets the log_envs of this AccessConfigDeatilUpdate.

        环境变量日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param log_envs: The log_envs of this AccessConfigDeatilUpdate.
        :type log_envs: dict(str, str)
        """
        self._log_envs = log_envs

    @property
    def include_k8s_labels(self):
        """Gets the include_k8s_labels of this AccessConfigDeatilUpdate.

        K8s Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The include_k8s_labels of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._include_k8s_labels

    @include_k8s_labels.setter
    def include_k8s_labels(self, include_k8s_labels):
        """Sets the include_k8s_labels of this AccessConfigDeatilUpdate.

        K8s Label白名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param include_k8s_labels: The include_k8s_labels of this AccessConfigDeatilUpdate.
        :type include_k8s_labels: dict(str, str)
        """
        self._include_k8s_labels = include_k8s_labels

    @property
    def exclude_k8s_labels(self):
        """Gets the exclude_k8s_labels of this AccessConfigDeatilUpdate.

        K8s Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The exclude_k8s_labels of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._exclude_k8s_labels

    @exclude_k8s_labels.setter
    def exclude_k8s_labels(self, exclude_k8s_labels):
        """Sets the exclude_k8s_labels of this AccessConfigDeatilUpdate.

        K8s Label黑名单，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param exclude_k8s_labels: The exclude_k8s_labels of this AccessConfigDeatilUpdate.
        :type exclude_k8s_labels: dict(str, str)
        """
        self._exclude_k8s_labels = exclude_k8s_labels

    @property
    def log_k8s(self):
        """Gets the log_k8s of this AccessConfigDeatilUpdate.

        K8s Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :return: The log_k8s of this AccessConfigDeatilUpdate.
        :rtype: dict(str, str)
        """
        return self._log_k8s

    @log_k8s.setter
    def log_k8s(self, log_k8s):
        """Sets the log_k8s of this AccessConfigDeatilUpdate.

        K8s Label日志标签，最多支持创建30个，keyname不支持重名，仅CCE接入类型时使用

        :param log_k8s: The log_k8s of this AccessConfigDeatilUpdate.
        :type log_k8s: dict(str, str)
        """
        self._log_k8s = log_k8s

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
        if not isinstance(other, AccessConfigDeatilUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
