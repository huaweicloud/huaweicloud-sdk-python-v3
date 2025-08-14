# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerlessPodInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pod_name': 'str',
        'namespace_name': 'str',
        'cluster_name': 'str',
        'cpu': 'str',
        'memory': 'str',
        'cpu_limit': 'str',
        'memory_limit': 'str',
        'pod_ip': 'str',
        'protect_status': 'str',
        'detect_result': 'str',
        'status': 'object',
        'create_time': 'int'
    }

    attribute_map = {
        'pod_name': 'pod_name',
        'namespace_name': 'namespace_name',
        'cluster_name': 'cluster_name',
        'cpu': 'cpu',
        'memory': 'memory',
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit',
        'pod_ip': 'pod_ip',
        'protect_status': 'protect_status',
        'detect_result': 'detect_result',
        'status': 'status',
        'create_time': 'create_time'
    }

    def __init__(self, pod_name=None, namespace_name=None, cluster_name=None, cpu=None, memory=None, cpu_limit=None, memory_limit=None, pod_ip=None, protect_status=None, detect_result=None, status=None, create_time=None):
        r"""ServerlessPodInfo

        The model defined in huaweicloud sdk

        :param pod_name: 实例名称
        :type pod_name: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param cluster_name: 所属集群
        :type cluster_name: str
        :param cpu: CPU使用量
        :type cpu: str
        :param memory: 内存使用量
        :type memory: str
        :param cpu_limit: cpu限制
        :type cpu_limit: str
        :param memory_limit: 内存限制
        :type memory_limit: str
        :param pod_ip: 实例 IP
        :type pod_ip: str
        :param protect_status: 防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。 - protection_exception ：防护异常。
        :type protect_status: str
        :param detect_result: Serverless安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。
        :type detect_result: str
        :param status: Pod状态，包含以下几种 -Pending：pod已被Kubernetes系统接受，但尚未创建一个或多个容器镜像 -Running：pod已经绑定到一个节点，并且所有的容器都已经创建完毕 -Succeeded：pod中的所有容器都已成功终止，不会重新启动 -Failed：pod中的所有容器都已终止，并且至少有一个容器因故障而终止 -Unknown：由于某种原因无法获取pod的状态，通常是由于与pod的主机通信时出错
        :type status: object
        :param create_time: 创建时间
        :type create_time: int
        """
        
        

        self._pod_name = None
        self._namespace_name = None
        self._cluster_name = None
        self._cpu = None
        self._memory = None
        self._cpu_limit = None
        self._memory_limit = None
        self._pod_ip = None
        self._protect_status = None
        self._detect_result = None
        self._status = None
        self._create_time = None
        self.discriminator = None

        if pod_name is not None:
            self.pod_name = pod_name
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if protect_status is not None:
            self.protect_status = protect_status
        if detect_result is not None:
            self.detect_result = detect_result
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ServerlessPodInfo.

        实例名称

        :return: The pod_name of this ServerlessPodInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ServerlessPodInfo.

        实例名称

        :param pod_name: The pod_name of this ServerlessPodInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ServerlessPodInfo.

        命名空间名称

        :return: The namespace_name of this ServerlessPodInfo.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ServerlessPodInfo.

        命名空间名称

        :param namespace_name: The namespace_name of this ServerlessPodInfo.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ServerlessPodInfo.

        所属集群

        :return: The cluster_name of this ServerlessPodInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ServerlessPodInfo.

        所属集群

        :param cluster_name: The cluster_name of this ServerlessPodInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cpu(self):
        r"""Gets the cpu of this ServerlessPodInfo.

        CPU使用量

        :return: The cpu of this ServerlessPodInfo.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ServerlessPodInfo.

        CPU使用量

        :param cpu: The cpu of this ServerlessPodInfo.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this ServerlessPodInfo.

        内存使用量

        :return: The memory of this ServerlessPodInfo.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ServerlessPodInfo.

        内存使用量

        :param memory: The memory of this ServerlessPodInfo.
        :type memory: str
        """
        self._memory = memory

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this ServerlessPodInfo.

        cpu限制

        :return: The cpu_limit of this ServerlessPodInfo.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this ServerlessPodInfo.

        cpu限制

        :param cpu_limit: The cpu_limit of this ServerlessPodInfo.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        r"""Gets the memory_limit of this ServerlessPodInfo.

        内存限制

        :return: The memory_limit of this ServerlessPodInfo.
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        r"""Sets the memory_limit of this ServerlessPodInfo.

        内存限制

        :param memory_limit: The memory_limit of this ServerlessPodInfo.
        :type memory_limit: str
        """
        self._memory_limit = memory_limit

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this ServerlessPodInfo.

        实例 IP

        :return: The pod_ip of this ServerlessPodInfo.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this ServerlessPodInfo.

        实例 IP

        :param pod_ip: The pod_ip of this ServerlessPodInfo.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ServerlessPodInfo.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。 - protection_exception ：防护异常。

        :return: The protect_status of this ServerlessPodInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ServerlessPodInfo.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。 - protection_exception ：防护异常。

        :param protect_status: The protect_status of this ServerlessPodInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def detect_result(self):
        r"""Gets the detect_result of this ServerlessPodInfo.

        Serverless安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :return: The detect_result of this ServerlessPodInfo.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        r"""Sets the detect_result of this ServerlessPodInfo.

        Serverless安全检测结果，包含如下4种。 - undetected ：未检测。 - clean ：无风险。 - risk ：有风险。 - scanning ：检测中。

        :param detect_result: The detect_result of this ServerlessPodInfo.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def status(self):
        r"""Gets the status of this ServerlessPodInfo.

        Pod状态，包含以下几种 -Pending：pod已被Kubernetes系统接受，但尚未创建一个或多个容器镜像 -Running：pod已经绑定到一个节点，并且所有的容器都已经创建完毕 -Succeeded：pod中的所有容器都已成功终止，不会重新启动 -Failed：pod中的所有容器都已终止，并且至少有一个容器因故障而终止 -Unknown：由于某种原因无法获取pod的状态，通常是由于与pod的主机通信时出错

        :return: The status of this ServerlessPodInfo.
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerlessPodInfo.

        Pod状态，包含以下几种 -Pending：pod已被Kubernetes系统接受，但尚未创建一个或多个容器镜像 -Running：pod已经绑定到一个节点，并且所有的容器都已经创建完毕 -Succeeded：pod中的所有容器都已成功终止，不会重新启动 -Failed：pod中的所有容器都已终止，并且至少有一个容器因故障而终止 -Unknown：由于某种原因无法获取pod的状态，通常是由于与pod的主机通信时出错

        :param status: The status of this ServerlessPodInfo.
        :type status: object
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ServerlessPodInfo.

        创建时间

        :return: The create_time of this ServerlessPodInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ServerlessPodInfo.

        创建时间

        :param create_time: The create_time of this ServerlessPodInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ServerlessPodInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
