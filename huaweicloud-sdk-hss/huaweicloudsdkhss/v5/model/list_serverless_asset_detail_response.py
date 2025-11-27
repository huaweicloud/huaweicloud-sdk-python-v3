# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerlessAssetDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_id': 'str',
        'container_name': 'str',
        'container_status': 'str',
        'workload_id': 'str',
        'workload_name': 'str',
        'workload_type': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'namespace': 'str',
        'pod_id': 'str',
        'pod_name': 'str',
        'pod_ip': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'create_time': 'int',
        'labels': 'str',
        'cpu_limit': 'str',
        'memory_limit': 'str',
        'command': 'str',
        'args': 'str',
        'working_dir': 'str',
        'port_info': 'list[ContainerPortInfo]',
        'mount_list': 'list[ContainerMountInfo]'
    }

    attribute_map = {
        'container_id': 'container_id',
        'container_name': 'container_name',
        'container_status': 'container_status',
        'workload_id': 'workload_id',
        'workload_name': 'workload_name',
        'workload_type': 'workload_type',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'namespace': 'namespace',
        'pod_id': 'pod_id',
        'pod_name': 'pod_name',
        'pod_ip': 'pod_ip',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'create_time': 'create_time',
        'labels': 'labels',
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit',
        'command': 'command',
        'args': 'args',
        'working_dir': 'working_dir',
        'port_info': 'port_info',
        'mount_list': 'mount_list'
    }

    def __init__(self, container_id=None, container_name=None, container_status=None, workload_id=None, workload_name=None, workload_type=None, cluster_id=None, cluster_name=None, namespace=None, pod_id=None, pod_name=None, pod_ip=None, image_id=None, image_name=None, create_time=None, labels=None, cpu_limit=None, memory_limit=None, command=None, args=None, working_dir=None, port_info=None, mount_list=None):
        r"""ListServerlessAssetDetailResponse

        The model defined in huaweicloud sdk

        :param container_id: **参数解释**: 容器ID **取值范围**: 字符长度0-255位 
        :type container_id: str
        :param container_name: **参数解释**: 容器名称 **取值范围**: 字符长度0-255位 
        :type container_name: str
        :param container_status: **参数解释**: 容器状态 **取值范围**: - Running：运行中。 - Terminated：终止。 - Waiting：等待。 
        :type container_status: str
        :param workload_id: **参数解释**: 负载id **取值范围**: 字符长度0-255位 
        :type workload_id: str
        :param workload_name: **参数解释**: 负载名称 **取值范围**: 字符长度0-255位 
        :type workload_name: str
        :param workload_type: **参数解释**: 负载类型 **取值范围**: 字符长度0-255位 
        :type workload_type: str
        :param cluster_id: **参数解释**: 集群id **取值范围**: 字符长度0-64位 
        :type cluster_id: str
        :param cluster_name: **参数解释**: 所属集群 **取值范围**: 字符长度0-64位 
        :type cluster_name: str
        :param namespace: **参数解释**: 命名空间 **取值范围**: 字符长度0-64位 
        :type namespace: str
        :param pod_id: **参数解释**: pod id **取值范围**: 字符长度0-64位 
        :type pod_id: str
        :param pod_name: **参数解释**: 实例名称 **取值范围**: 字符长度0-255位 
        :type pod_name: str
        :param pod_ip: **参数解释**: 实例ip **取值范围**: 字符长度0-255位 
        :type pod_ip: str
        :param image_id: **参数解释**: 镜像id **取值范围**: 字符长度0-255位 
        :type image_id: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-255位 
        :type image_name: str
        :param create_time: **参数解释**: 创建时间 **取值范围**: 取值0-4071095999000 
        :type create_time: int
        :param labels: **参数解释**: 标签列表 **取值范围**: 字符长度0-255位 
        :type labels: str
        :param cpu_limit: **参数解释**: cpu限制 **取值范围**: 字符长度0-64位 
        :type cpu_limit: str
        :param memory_limit: **参数解释**: 内存限制 **取值范围**: 字符长度0-64位 
        :type memory_limit: str
        :param command: **参数解释**: 启动命令 **取值范围**: 字符长度0-65535位 
        :type command: str
        :param args: **参数解释**: 启动命令参数 **取值范围**: 字符长度0-65535位 
        :type args: str
        :param working_dir: **参数解释**: 工作目录 **取值范围**: 字符长度0-65535位 
        :type working_dir: str
        :param port_info: **参数解释**: 端口列表 **取值范围**: 取值0-65535个端口对象 
        :type port_info: list[:class:`huaweicloudsdkhss.v5.ContainerPortInfo`]
        :param mount_list: **参数解释**: 存储卷配置 **取值范围**: 取值0-65535个配置对象 
        :type mount_list: list[:class:`huaweicloudsdkhss.v5.ContainerMountInfo`]
        """
        
        super().__init__()

        self._container_id = None
        self._container_name = None
        self._container_status = None
        self._workload_id = None
        self._workload_name = None
        self._workload_type = None
        self._cluster_id = None
        self._cluster_name = None
        self._namespace = None
        self._pod_id = None
        self._pod_name = None
        self._pod_ip = None
        self._image_id = None
        self._image_name = None
        self._create_time = None
        self._labels = None
        self._cpu_limit = None
        self._memory_limit = None
        self._command = None
        self._args = None
        self._working_dir = None
        self._port_info = None
        self._mount_list = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if container_status is not None:
            self.container_status = container_status
        if workload_id is not None:
            self.workload_id = workload_id
        if workload_name is not None:
            self.workload_name = workload_name
        if workload_type is not None:
            self.workload_type = workload_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if namespace is not None:
            self.namespace = namespace
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_name is not None:
            self.pod_name = pod_name
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if create_time is not None:
            self.create_time = create_time
        if labels is not None:
            self.labels = labels
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args
        if working_dir is not None:
            self.working_dir = working_dir
        if port_info is not None:
            self.port_info = port_info
        if mount_list is not None:
            self.mount_list = mount_list

    @property
    def container_id(self):
        r"""Gets the container_id of this ListServerlessAssetDetailResponse.

        **参数解释**: 容器ID **取值范围**: 字符长度0-255位 

        :return: The container_id of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListServerlessAssetDetailResponse.

        **参数解释**: 容器ID **取值范围**: 字符长度0-255位 

        :param container_id: The container_id of this ListServerlessAssetDetailResponse.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 容器名称 **取值范围**: 字符长度0-255位 

        :return: The container_name of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 容器名称 **取值范围**: 字符长度0-255位 

        :param container_name: The container_name of this ListServerlessAssetDetailResponse.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_status(self):
        r"""Gets the container_status of this ListServerlessAssetDetailResponse.

        **参数解释**: 容器状态 **取值范围**: - Running：运行中。 - Terminated：终止。 - Waiting：等待。 

        :return: The container_status of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._container_status

    @container_status.setter
    def container_status(self, container_status):
        r"""Sets the container_status of this ListServerlessAssetDetailResponse.

        **参数解释**: 容器状态 **取值范围**: - Running：运行中。 - Terminated：终止。 - Waiting：等待。 

        :param container_status: The container_status of this ListServerlessAssetDetailResponse.
        :type container_status: str
        """
        self._container_status = container_status

    @property
    def workload_id(self):
        r"""Gets the workload_id of this ListServerlessAssetDetailResponse.

        **参数解释**: 负载id **取值范围**: 字符长度0-255位 

        :return: The workload_id of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._workload_id

    @workload_id.setter
    def workload_id(self, workload_id):
        r"""Sets the workload_id of this ListServerlessAssetDetailResponse.

        **参数解释**: 负载id **取值范围**: 字符长度0-255位 

        :param workload_id: The workload_id of this ListServerlessAssetDetailResponse.
        :type workload_id: str
        """
        self._workload_id = workload_id

    @property
    def workload_name(self):
        r"""Gets the workload_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 负载名称 **取值范围**: 字符长度0-255位 

        :return: The workload_name of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._workload_name

    @workload_name.setter
    def workload_name(self, workload_name):
        r"""Sets the workload_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 负载名称 **取值范围**: 字符长度0-255位 

        :param workload_name: The workload_name of this ListServerlessAssetDetailResponse.
        :type workload_name: str
        """
        self._workload_name = workload_name

    @property
    def workload_type(self):
        r"""Gets the workload_type of this ListServerlessAssetDetailResponse.

        **参数解释**: 负载类型 **取值范围**: 字符长度0-255位 

        :return: The workload_type of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        r"""Sets the workload_type of this ListServerlessAssetDetailResponse.

        **参数解释**: 负载类型 **取值范围**: 字符长度0-255位 

        :param workload_type: The workload_type of this ListServerlessAssetDetailResponse.
        :type workload_type: str
        """
        self._workload_type = workload_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListServerlessAssetDetailResponse.

        **参数解释**: 集群id **取值范围**: 字符长度0-64位 

        :return: The cluster_id of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListServerlessAssetDetailResponse.

        **参数解释**: 集群id **取值范围**: 字符长度0-64位 

        :param cluster_id: The cluster_id of this ListServerlessAssetDetailResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 所属集群 **取值范围**: 字符长度0-64位 

        :return: The cluster_name of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 所属集群 **取值范围**: 字符长度0-64位 

        :param cluster_name: The cluster_name of this ListServerlessAssetDetailResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def namespace(self):
        r"""Gets the namespace of this ListServerlessAssetDetailResponse.

        **参数解释**: 命名空间 **取值范围**: 字符长度0-64位 

        :return: The namespace of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListServerlessAssetDetailResponse.

        **参数解释**: 命名空间 **取值范围**: 字符长度0-64位 

        :param namespace: The namespace of this ListServerlessAssetDetailResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def pod_id(self):
        r"""Gets the pod_id of this ListServerlessAssetDetailResponse.

        **参数解释**: pod id **取值范围**: 字符长度0-64位 

        :return: The pod_id of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this ListServerlessAssetDetailResponse.

        **参数解释**: pod id **取值范围**: 字符长度0-64位 

        :param pod_id: The pod_id of this ListServerlessAssetDetailResponse.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 实例名称 **取值范围**: 字符长度0-255位 

        :return: The pod_name of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 实例名称 **取值范围**: 字符长度0-255位 

        :param pod_name: The pod_name of this ListServerlessAssetDetailResponse.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this ListServerlessAssetDetailResponse.

        **参数解释**: 实例ip **取值范围**: 字符长度0-255位 

        :return: The pod_ip of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this ListServerlessAssetDetailResponse.

        **参数解释**: 实例ip **取值范围**: 字符长度0-255位 

        :param pod_ip: The pod_ip of this ListServerlessAssetDetailResponse.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def image_id(self):
        r"""Gets the image_id of this ListServerlessAssetDetailResponse.

        **参数解释**: 镜像id **取值范围**: 字符长度0-255位 

        :return: The image_id of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListServerlessAssetDetailResponse.

        **参数解释**: 镜像id **取值范围**: 字符长度0-255位 

        :param image_id: The image_id of this ListServerlessAssetDetailResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-255位 

        :return: The image_name of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListServerlessAssetDetailResponse.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-255位 

        :param image_name: The image_name of this ListServerlessAssetDetailResponse.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ListServerlessAssetDetailResponse.

        **参数解释**: 创建时间 **取值范围**: 取值0-4071095999000 

        :return: The create_time of this ListServerlessAssetDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListServerlessAssetDetailResponse.

        **参数解释**: 创建时间 **取值范围**: 取值0-4071095999000 

        :param create_time: The create_time of this ListServerlessAssetDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def labels(self):
        r"""Gets the labels of this ListServerlessAssetDetailResponse.

        **参数解释**: 标签列表 **取值范围**: 字符长度0-255位 

        :return: The labels of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListServerlessAssetDetailResponse.

        **参数解释**: 标签列表 **取值范围**: 字符长度0-255位 

        :param labels: The labels of this ListServerlessAssetDetailResponse.
        :type labels: str
        """
        self._labels = labels

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this ListServerlessAssetDetailResponse.

        **参数解释**: cpu限制 **取值范围**: 字符长度0-64位 

        :return: The cpu_limit of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this ListServerlessAssetDetailResponse.

        **参数解释**: cpu限制 **取值范围**: 字符长度0-64位 

        :param cpu_limit: The cpu_limit of this ListServerlessAssetDetailResponse.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        r"""Gets the memory_limit of this ListServerlessAssetDetailResponse.

        **参数解释**: 内存限制 **取值范围**: 字符长度0-64位 

        :return: The memory_limit of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        r"""Sets the memory_limit of this ListServerlessAssetDetailResponse.

        **参数解释**: 内存限制 **取值范围**: 字符长度0-64位 

        :param memory_limit: The memory_limit of this ListServerlessAssetDetailResponse.
        :type memory_limit: str
        """
        self._memory_limit = memory_limit

    @property
    def command(self):
        r"""Gets the command of this ListServerlessAssetDetailResponse.

        **参数解释**: 启动命令 **取值范围**: 字符长度0-65535位 

        :return: The command of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ListServerlessAssetDetailResponse.

        **参数解释**: 启动命令 **取值范围**: 字符长度0-65535位 

        :param command: The command of this ListServerlessAssetDetailResponse.
        :type command: str
        """
        self._command = command

    @property
    def args(self):
        r"""Gets the args of this ListServerlessAssetDetailResponse.

        **参数解释**: 启动命令参数 **取值范围**: 字符长度0-65535位 

        :return: The args of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        r"""Sets the args of this ListServerlessAssetDetailResponse.

        **参数解释**: 启动命令参数 **取值范围**: 字符长度0-65535位 

        :param args: The args of this ListServerlessAssetDetailResponse.
        :type args: str
        """
        self._args = args

    @property
    def working_dir(self):
        r"""Gets the working_dir of this ListServerlessAssetDetailResponse.

        **参数解释**: 工作目录 **取值范围**: 字符长度0-65535位 

        :return: The working_dir of this ListServerlessAssetDetailResponse.
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        r"""Sets the working_dir of this ListServerlessAssetDetailResponse.

        **参数解释**: 工作目录 **取值范围**: 字符长度0-65535位 

        :param working_dir: The working_dir of this ListServerlessAssetDetailResponse.
        :type working_dir: str
        """
        self._working_dir = working_dir

    @property
    def port_info(self):
        r"""Gets the port_info of this ListServerlessAssetDetailResponse.

        **参数解释**: 端口列表 **取值范围**: 取值0-65535个端口对象 

        :return: The port_info of this ListServerlessAssetDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ContainerPortInfo`]
        """
        return self._port_info

    @port_info.setter
    def port_info(self, port_info):
        r"""Sets the port_info of this ListServerlessAssetDetailResponse.

        **参数解释**: 端口列表 **取值范围**: 取值0-65535个端口对象 

        :param port_info: The port_info of this ListServerlessAssetDetailResponse.
        :type port_info: list[:class:`huaweicloudsdkhss.v5.ContainerPortInfo`]
        """
        self._port_info = port_info

    @property
    def mount_list(self):
        r"""Gets the mount_list of this ListServerlessAssetDetailResponse.

        **参数解释**: 存储卷配置 **取值范围**: 取值0-65535个配置对象 

        :return: The mount_list of this ListServerlessAssetDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ContainerMountInfo`]
        """
        return self._mount_list

    @mount_list.setter
    def mount_list(self, mount_list):
        r"""Sets the mount_list of this ListServerlessAssetDetailResponse.

        **参数解释**: 存储卷配置 **取值范围**: 取值0-65535个配置对象 

        :param mount_list: The mount_list of this ListServerlessAssetDetailResponse.
        :type mount_list: list[:class:`huaweicloudsdkhss.v5.ContainerMountInfo`]
        """
        self._mount_list = mount_list

    def to_dict(self):
        import warnings
        warnings.warn("ListServerlessAssetDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListServerlessAssetDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
