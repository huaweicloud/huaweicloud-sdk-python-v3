# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryNodeResp:

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
        'internal_ip': 'str',
        'hostname': 'str',
        'allocatable': 'NodeResourceDTO',
        'capacity': 'NodeResourceDTO',
        'allocated_resources': 'NodeAllocatedResourceDTO',
        'status': 'str',
        'architecture': 'str',
        'labels': 'dict(str, str)',
        'node_type': 'str',
        'kernel_version': 'str',
        'os_image': 'str',
        'container_runtime_version': 'str',
        'kubernetes_version': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'internal_ip': 'internal_ip',
        'hostname': 'hostname',
        'allocatable': 'allocatable',
        'capacity': 'capacity',
        'allocated_resources': 'allocated_resources',
        'status': 'status',
        'architecture': 'architecture',
        'labels': 'labels',
        'node_type': 'node_type',
        'kernel_version': 'kernel_version',
        'os_image': 'os_image',
        'container_runtime_version': 'container_runtime_version',
        'kubernetes_version': 'kubernetes_version',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, internal_ip=None, hostname=None, allocatable=None, capacity=None, allocated_resources=None, status=None, architecture=None, labels=None, node_type=None, kernel_version=None, os_image=None, container_runtime_version=None, kubernetes_version=None, create_time=None):
        r"""QueryNodeResp

        The model defined in huaweicloud sdk

        :param name: 节点名称
        :type name: str
        :param internal_ip: 节点ip
        :type internal_ip: str
        :param hostname: 主机名
        :type hostname: str
        :param allocatable: 
        :type allocatable: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        :param capacity: 
        :type capacity: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        :param allocated_resources: 
        :type allocated_resources: :class:`huaweicloudsdkiotedge.v3.NodeAllocatedResourceDTO`
        :param status: 状态，Ready or NotReady
        :type status: str
        :param architecture: 架构，amd64 or arm64
        :type architecture: str
        :param labels: map类型，key为string,value为string
        :type labels: dict(str, str)
        :param node_type: 节点类型
        :type node_type: str
        :param kernel_version: 内核版本
        :type kernel_version: str
        :param os_image: 操作系统版本
        :type os_image: str
        :param container_runtime_version: 容器运行时版本
        :type container_runtime_version: str
        :param kubernetes_version: k8s版本
        :type kubernetes_version: str
        :param create_time: 创建时间
        :type create_time: str
        """
        
        

        self._name = None
        self._internal_ip = None
        self._hostname = None
        self._allocatable = None
        self._capacity = None
        self._allocated_resources = None
        self._status = None
        self._architecture = None
        self._labels = None
        self._node_type = None
        self._kernel_version = None
        self._os_image = None
        self._container_runtime_version = None
        self._kubernetes_version = None
        self._create_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if internal_ip is not None:
            self.internal_ip = internal_ip
        if hostname is not None:
            self.hostname = hostname
        if allocatable is not None:
            self.allocatable = allocatable
        if capacity is not None:
            self.capacity = capacity
        if allocated_resources is not None:
            self.allocated_resources = allocated_resources
        if status is not None:
            self.status = status
        if architecture is not None:
            self.architecture = architecture
        if labels is not None:
            self.labels = labels
        if node_type is not None:
            self.node_type = node_type
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if os_image is not None:
            self.os_image = os_image
        if container_runtime_version is not None:
            self.container_runtime_version = container_runtime_version
        if kubernetes_version is not None:
            self.kubernetes_version = kubernetes_version
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this QueryNodeResp.

        节点名称

        :return: The name of this QueryNodeResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryNodeResp.

        节点名称

        :param name: The name of this QueryNodeResp.
        :type name: str
        """
        self._name = name

    @property
    def internal_ip(self):
        r"""Gets the internal_ip of this QueryNodeResp.

        节点ip

        :return: The internal_ip of this QueryNodeResp.
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        r"""Sets the internal_ip of this QueryNodeResp.

        节点ip

        :param internal_ip: The internal_ip of this QueryNodeResp.
        :type internal_ip: str
        """
        self._internal_ip = internal_ip

    @property
    def hostname(self):
        r"""Gets the hostname of this QueryNodeResp.

        主机名

        :return: The hostname of this QueryNodeResp.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this QueryNodeResp.

        主机名

        :param hostname: The hostname of this QueryNodeResp.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def allocatable(self):
        r"""Gets the allocatable of this QueryNodeResp.

        :return: The allocatable of this QueryNodeResp.
        :rtype: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        return self._allocatable

    @allocatable.setter
    def allocatable(self, allocatable):
        r"""Sets the allocatable of this QueryNodeResp.

        :param allocatable: The allocatable of this QueryNodeResp.
        :type allocatable: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        self._allocatable = allocatable

    @property
    def capacity(self):
        r"""Gets the capacity of this QueryNodeResp.

        :return: The capacity of this QueryNodeResp.
        :rtype: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this QueryNodeResp.

        :param capacity: The capacity of this QueryNodeResp.
        :type capacity: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        self._capacity = capacity

    @property
    def allocated_resources(self):
        r"""Gets the allocated_resources of this QueryNodeResp.

        :return: The allocated_resources of this QueryNodeResp.
        :rtype: :class:`huaweicloudsdkiotedge.v3.NodeAllocatedResourceDTO`
        """
        return self._allocated_resources

    @allocated_resources.setter
    def allocated_resources(self, allocated_resources):
        r"""Sets the allocated_resources of this QueryNodeResp.

        :param allocated_resources: The allocated_resources of this QueryNodeResp.
        :type allocated_resources: :class:`huaweicloudsdkiotedge.v3.NodeAllocatedResourceDTO`
        """
        self._allocated_resources = allocated_resources

    @property
    def status(self):
        r"""Gets the status of this QueryNodeResp.

        状态，Ready or NotReady

        :return: The status of this QueryNodeResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryNodeResp.

        状态，Ready or NotReady

        :param status: The status of this QueryNodeResp.
        :type status: str
        """
        self._status = status

    @property
    def architecture(self):
        r"""Gets the architecture of this QueryNodeResp.

        架构，amd64 or arm64

        :return: The architecture of this QueryNodeResp.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this QueryNodeResp.

        架构，amd64 or arm64

        :param architecture: The architecture of this QueryNodeResp.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def labels(self):
        r"""Gets the labels of this QueryNodeResp.

        map类型，key为string,value为string

        :return: The labels of this QueryNodeResp.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this QueryNodeResp.

        map类型，key为string,value为string

        :param labels: The labels of this QueryNodeResp.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def node_type(self):
        r"""Gets the node_type of this QueryNodeResp.

        节点类型

        :return: The node_type of this QueryNodeResp.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this QueryNodeResp.

        节点类型

        :param node_type: The node_type of this QueryNodeResp.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this QueryNodeResp.

        内核版本

        :return: The kernel_version of this QueryNodeResp.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this QueryNodeResp.

        内核版本

        :param kernel_version: The kernel_version of this QueryNodeResp.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    @property
    def os_image(self):
        r"""Gets the os_image of this QueryNodeResp.

        操作系统版本

        :return: The os_image of this QueryNodeResp.
        :rtype: str
        """
        return self._os_image

    @os_image.setter
    def os_image(self, os_image):
        r"""Sets the os_image of this QueryNodeResp.

        操作系统版本

        :param os_image: The os_image of this QueryNodeResp.
        :type os_image: str
        """
        self._os_image = os_image

    @property
    def container_runtime_version(self):
        r"""Gets the container_runtime_version of this QueryNodeResp.

        容器运行时版本

        :return: The container_runtime_version of this QueryNodeResp.
        :rtype: str
        """
        return self._container_runtime_version

    @container_runtime_version.setter
    def container_runtime_version(self, container_runtime_version):
        r"""Sets the container_runtime_version of this QueryNodeResp.

        容器运行时版本

        :param container_runtime_version: The container_runtime_version of this QueryNodeResp.
        :type container_runtime_version: str
        """
        self._container_runtime_version = container_runtime_version

    @property
    def kubernetes_version(self):
        r"""Gets the kubernetes_version of this QueryNodeResp.

        k8s版本

        :return: The kubernetes_version of this QueryNodeResp.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        r"""Sets the kubernetes_version of this QueryNodeResp.

        k8s版本

        :param kubernetes_version: The kubernetes_version of this QueryNodeResp.
        :type kubernetes_version: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def create_time(self):
        r"""Gets the create_time of this QueryNodeResp.

        创建时间

        :return: The create_time of this QueryNodeResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QueryNodeResp.

        创建时间

        :param create_time: The create_time of this QueryNodeResp.
        :type create_time: str
        """
        self._create_time = create_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryNodeResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
