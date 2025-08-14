# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowK8sPodDetailResponse(SdkResponse):

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
        'node_name': 'str',
        'label': 'str',
        'cpu': 'str',
        'memory': 'str',
        'cpu_limit': 'str',
        'memory_limit': 'str',
        'node_ip': 'str',
        'pod_ip': 'str',
        'status': 'str',
        'create_time': 'int',
        'containers': 'list[ContainerBaseInfo]'
    }

    attribute_map = {
        'pod_name': 'pod_name',
        'namespace_name': 'namespace_name',
        'cluster_name': 'cluster_name',
        'node_name': 'node_name',
        'label': 'label',
        'cpu': 'cpu',
        'memory': 'memory',
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit',
        'node_ip': 'node_ip',
        'pod_ip': 'pod_ip',
        'status': 'status',
        'create_time': 'create_time',
        'containers': 'containers'
    }

    def __init__(self, pod_name=None, namespace_name=None, cluster_name=None, node_name=None, label=None, cpu=None, memory=None, cpu_limit=None, memory_limit=None, node_ip=None, pod_ip=None, status=None, create_time=None, containers=None):
        r"""ShowK8sPodDetailResponse

        The model defined in huaweicloud sdk

        :param pod_name: pod名称
        :type pod_name: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param cluster_name: 所属集群
        :type cluster_name: str
        :param node_name: 所属节点名称
        :type node_name: str
        :param label: 标签
        :type label: str
        :param cpu: CPU使用量
        :type cpu: str
        :param memory: 内存使用量
        :type memory: str
        :param cpu_limit: cpu限制
        :type cpu_limit: str
        :param memory_limit: 内存限制
        :type memory_limit: str
        :param node_ip: 所属节点IP
        :type node_ip: str
        :param pod_ip: Pod IP
        :type pod_ip: str
        :param status: Pod状态，包含以下几种 -Pending：pod已被Kubernetes系统接受，但尚未创建一个或多个容器镜像 -Running：pod已经绑定到一个节点，并且所有的容器都已经创建完毕 -Succeeded：pod中的所有容器都已成功终止，不会重新启动 -Failed：pod中的所有容器都已终止，并且至少有一个容器因故障而终止 -Unknown：由于某种原因无法获取pod的状态，通常是由于与pod的主机通信时出错
        :type status: str
        :param create_time: 创建时间
        :type create_time: int
        :param containers: pod容器列表
        :type containers: list[:class:`huaweicloudsdkhss.v5.ContainerBaseInfo`]
        """
        
        super(ShowK8sPodDetailResponse, self).__init__()

        self._pod_name = None
        self._namespace_name = None
        self._cluster_name = None
        self._node_name = None
        self._label = None
        self._cpu = None
        self._memory = None
        self._cpu_limit = None
        self._memory_limit = None
        self._node_ip = None
        self._pod_ip = None
        self._status = None
        self._create_time = None
        self._containers = None
        self.discriminator = None

        if pod_name is not None:
            self.pod_name = pod_name
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if node_name is not None:
            self.node_name = node_name
        if label is not None:
            self.label = label
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if node_ip is not None:
            self.node_ip = node_ip
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if containers is not None:
            self.containers = containers

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ShowK8sPodDetailResponse.

        pod名称

        :return: The pod_name of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ShowK8sPodDetailResponse.

        pod名称

        :param pod_name: The pod_name of this ShowK8sPodDetailResponse.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ShowK8sPodDetailResponse.

        命名空间名称

        :return: The namespace_name of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ShowK8sPodDetailResponse.

        命名空间名称

        :param namespace_name: The namespace_name of this ShowK8sPodDetailResponse.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ShowK8sPodDetailResponse.

        所属集群

        :return: The cluster_name of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ShowK8sPodDetailResponse.

        所属集群

        :param cluster_name: The cluster_name of this ShowK8sPodDetailResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def node_name(self):
        r"""Gets the node_name of this ShowK8sPodDetailResponse.

        所属节点名称

        :return: The node_name of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ShowK8sPodDetailResponse.

        所属节点名称

        :param node_name: The node_name of this ShowK8sPodDetailResponse.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def label(self):
        r"""Gets the label of this ShowK8sPodDetailResponse.

        标签

        :return: The label of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ShowK8sPodDetailResponse.

        标签

        :param label: The label of this ShowK8sPodDetailResponse.
        :type label: str
        """
        self._label = label

    @property
    def cpu(self):
        r"""Gets the cpu of this ShowK8sPodDetailResponse.

        CPU使用量

        :return: The cpu of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ShowK8sPodDetailResponse.

        CPU使用量

        :param cpu: The cpu of this ShowK8sPodDetailResponse.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this ShowK8sPodDetailResponse.

        内存使用量

        :return: The memory of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ShowK8sPodDetailResponse.

        内存使用量

        :param memory: The memory of this ShowK8sPodDetailResponse.
        :type memory: str
        """
        self._memory = memory

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this ShowK8sPodDetailResponse.

        cpu限制

        :return: The cpu_limit of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this ShowK8sPodDetailResponse.

        cpu限制

        :param cpu_limit: The cpu_limit of this ShowK8sPodDetailResponse.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        r"""Gets the memory_limit of this ShowK8sPodDetailResponse.

        内存限制

        :return: The memory_limit of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        r"""Sets the memory_limit of this ShowK8sPodDetailResponse.

        内存限制

        :param memory_limit: The memory_limit of this ShowK8sPodDetailResponse.
        :type memory_limit: str
        """
        self._memory_limit = memory_limit

    @property
    def node_ip(self):
        r"""Gets the node_ip of this ShowK8sPodDetailResponse.

        所属节点IP

        :return: The node_ip of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        r"""Sets the node_ip of this ShowK8sPodDetailResponse.

        所属节点IP

        :param node_ip: The node_ip of this ShowK8sPodDetailResponse.
        :type node_ip: str
        """
        self._node_ip = node_ip

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this ShowK8sPodDetailResponse.

        Pod IP

        :return: The pod_ip of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this ShowK8sPodDetailResponse.

        Pod IP

        :param pod_ip: The pod_ip of this ShowK8sPodDetailResponse.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def status(self):
        r"""Gets the status of this ShowK8sPodDetailResponse.

        Pod状态，包含以下几种 -Pending：pod已被Kubernetes系统接受，但尚未创建一个或多个容器镜像 -Running：pod已经绑定到一个节点，并且所有的容器都已经创建完毕 -Succeeded：pod中的所有容器都已成功终止，不会重新启动 -Failed：pod中的所有容器都已终止，并且至少有一个容器因故障而终止 -Unknown：由于某种原因无法获取pod的状态，通常是由于与pod的主机通信时出错

        :return: The status of this ShowK8sPodDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowK8sPodDetailResponse.

        Pod状态，包含以下几种 -Pending：pod已被Kubernetes系统接受，但尚未创建一个或多个容器镜像 -Running：pod已经绑定到一个节点，并且所有的容器都已经创建完毕 -Succeeded：pod中的所有容器都已成功终止，不会重新启动 -Failed：pod中的所有容器都已终止，并且至少有一个容器因故障而终止 -Unknown：由于某种原因无法获取pod的状态，通常是由于与pod的主机通信时出错

        :param status: The status of this ShowK8sPodDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowK8sPodDetailResponse.

        创建时间

        :return: The create_time of this ShowK8sPodDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowK8sPodDetailResponse.

        创建时间

        :param create_time: The create_time of this ShowK8sPodDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def containers(self):
        r"""Gets the containers of this ShowK8sPodDetailResponse.

        pod容器列表

        :return: The containers of this ShowK8sPodDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ContainerBaseInfo`]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        r"""Sets the containers of this ShowK8sPodDetailResponse.

        pod容器列表

        :param containers: The containers of this ShowK8sPodDetailResponse.
        :type containers: list[:class:`huaweicloudsdkhss.v5.ContainerBaseInfo`]
        """
        self._containers = containers

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
        if not isinstance(other, ShowK8sPodDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
