# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerBaseInfo:

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
        'image_name': 'str',
        'status': 'str',
        'create_time': 'int',
        'cpu_limit': 'str',
        'memory_limit': 'str',
        'restart_count': 'int',
        'pod_name': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'risky': 'bool',
        'low_risk': 'int',
        'medium_risk': 'int',
        'high_risk': 'int',
        'fatal_risk': 'int'
    }

    attribute_map = {
        'container_id': 'container_id',
        'container_name': 'container_name',
        'image_name': 'image_name',
        'status': 'status',
        'create_time': 'create_time',
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit',
        'restart_count': 'restart_count',
        'pod_name': 'pod_name',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'risky': 'risky',
        'low_risk': 'low_risk',
        'medium_risk': 'medium_risk',
        'high_risk': 'high_risk',
        'fatal_risk': 'fatal_risk'
    }

    def __init__(self, container_id=None, container_name=None, image_name=None, status=None, create_time=None, cpu_limit=None, memory_limit=None, restart_count=None, pod_name=None, cluster_name=None, cluster_id=None, cluster_type=None, risky=None, low_risk=None, medium_risk=None, high_risk=None, fatal_risk=None):
        """ContainerBaseInfo

        The model defined in huaweicloud sdk

        :param container_id: 容器ID
        :type container_id: str
        :param container_name: 容器名称
        :type container_name: str
        :param image_name: 镜像名称
        :type image_name: str
        :param status: 容器状态，包含以下几种： -Running 运行中 -Terminated 终止 -Waiting 等待
        :type status: str
        :param create_time: 创建时间
        :type create_time: int
        :param cpu_limit: cpu限制
        :type cpu_limit: str
        :param memory_limit: 内存限制
        :type memory_limit: str
        :param restart_count: 重启次数
        :type restart_count: int
        :param pod_name: 所属pod名称
        :type pod_name: str
        :param cluster_name: 所属集群
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_type: 集群类型，包含以下几种： -k8s 原生集群 -cce CCE集群 -ali 阿里云集群 -tencent 腾讯云集群 -azure 微软云集群 -aws 亚马逊集群 -self_built_hw 华为云自建集群 -self_built_idc IDC自建集群
        :type cluster_type: str
        :param risky: 是否有风险
        :type risky: bool
        :param low_risk: 低危风险数量
        :type low_risk: int
        :param medium_risk: 中危风险数量
        :type medium_risk: int
        :param high_risk: 高危风险数量
        :type high_risk: int
        :param fatal_risk: 致命风险数量
        :type fatal_risk: int
        """
        
        

        self._container_id = None
        self._container_name = None
        self._image_name = None
        self._status = None
        self._create_time = None
        self._cpu_limit = None
        self._memory_limit = None
        self._restart_count = None
        self._pod_name = None
        self._cluster_name = None
        self._cluster_id = None
        self._cluster_type = None
        self._risky = None
        self._low_risk = None
        self._medium_risk = None
        self._high_risk = None
        self._fatal_risk = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if image_name is not None:
            self.image_name = image_name
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if restart_count is not None:
            self.restart_count = restart_count
        if pod_name is not None:
            self.pod_name = pod_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if risky is not None:
            self.risky = risky
        if low_risk is not None:
            self.low_risk = low_risk
        if medium_risk is not None:
            self.medium_risk = medium_risk
        if high_risk is not None:
            self.high_risk = high_risk
        if fatal_risk is not None:
            self.fatal_risk = fatal_risk

    @property
    def container_id(self):
        """Gets the container_id of this ContainerBaseInfo.

        容器ID

        :return: The container_id of this ContainerBaseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this ContainerBaseInfo.

        容器ID

        :param container_id: The container_id of this ContainerBaseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        """Gets the container_name of this ContainerBaseInfo.

        容器名称

        :return: The container_name of this ContainerBaseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this ContainerBaseInfo.

        容器名称

        :param container_name: The container_name of this ContainerBaseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def image_name(self):
        """Gets the image_name of this ContainerBaseInfo.

        镜像名称

        :return: The image_name of this ContainerBaseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ContainerBaseInfo.

        镜像名称

        :param image_name: The image_name of this ContainerBaseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def status(self):
        """Gets the status of this ContainerBaseInfo.

        容器状态，包含以下几种： -Running 运行中 -Terminated 终止 -Waiting 等待

        :return: The status of this ContainerBaseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ContainerBaseInfo.

        容器状态，包含以下几种： -Running 运行中 -Terminated 终止 -Waiting 等待

        :param status: The status of this ContainerBaseInfo.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ContainerBaseInfo.

        创建时间

        :return: The create_time of this ContainerBaseInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ContainerBaseInfo.

        创建时间

        :param create_time: The create_time of this ContainerBaseInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def cpu_limit(self):
        """Gets the cpu_limit of this ContainerBaseInfo.

        cpu限制

        :return: The cpu_limit of this ContainerBaseInfo.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        """Sets the cpu_limit of this ContainerBaseInfo.

        cpu限制

        :param cpu_limit: The cpu_limit of this ContainerBaseInfo.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        """Gets the memory_limit of this ContainerBaseInfo.

        内存限制

        :return: The memory_limit of this ContainerBaseInfo.
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        """Sets the memory_limit of this ContainerBaseInfo.

        内存限制

        :param memory_limit: The memory_limit of this ContainerBaseInfo.
        :type memory_limit: str
        """
        self._memory_limit = memory_limit

    @property
    def restart_count(self):
        """Gets the restart_count of this ContainerBaseInfo.

        重启次数

        :return: The restart_count of this ContainerBaseInfo.
        :rtype: int
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        """Sets the restart_count of this ContainerBaseInfo.

        重启次数

        :param restart_count: The restart_count of this ContainerBaseInfo.
        :type restart_count: int
        """
        self._restart_count = restart_count

    @property
    def pod_name(self):
        """Gets the pod_name of this ContainerBaseInfo.

        所属pod名称

        :return: The pod_name of this ContainerBaseInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this ContainerBaseInfo.

        所属pod名称

        :param pod_name: The pod_name of this ContainerBaseInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ContainerBaseInfo.

        所属集群

        :return: The cluster_name of this ContainerBaseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ContainerBaseInfo.

        所属集群

        :param cluster_name: The cluster_name of this ContainerBaseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ContainerBaseInfo.

        集群id

        :return: The cluster_id of this ContainerBaseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ContainerBaseInfo.

        集群id

        :param cluster_id: The cluster_id of this ContainerBaseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        """Gets the cluster_type of this ContainerBaseInfo.

        集群类型，包含以下几种： -k8s 原生集群 -cce CCE集群 -ali 阿里云集群 -tencent 腾讯云集群 -azure 微软云集群 -aws 亚马逊集群 -self_built_hw 华为云自建集群 -self_built_idc IDC自建集群

        :return: The cluster_type of this ContainerBaseInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this ContainerBaseInfo.

        集群类型，包含以下几种： -k8s 原生集群 -cce CCE集群 -ali 阿里云集群 -tencent 腾讯云集群 -azure 微软云集群 -aws 亚马逊集群 -self_built_hw 华为云自建集群 -self_built_idc IDC自建集群

        :param cluster_type: The cluster_type of this ContainerBaseInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def risky(self):
        """Gets the risky of this ContainerBaseInfo.

        是否有风险

        :return: The risky of this ContainerBaseInfo.
        :rtype: bool
        """
        return self._risky

    @risky.setter
    def risky(self, risky):
        """Sets the risky of this ContainerBaseInfo.

        是否有风险

        :param risky: The risky of this ContainerBaseInfo.
        :type risky: bool
        """
        self._risky = risky

    @property
    def low_risk(self):
        """Gets the low_risk of this ContainerBaseInfo.

        低危风险数量

        :return: The low_risk of this ContainerBaseInfo.
        :rtype: int
        """
        return self._low_risk

    @low_risk.setter
    def low_risk(self, low_risk):
        """Sets the low_risk of this ContainerBaseInfo.

        低危风险数量

        :param low_risk: The low_risk of this ContainerBaseInfo.
        :type low_risk: int
        """
        self._low_risk = low_risk

    @property
    def medium_risk(self):
        """Gets the medium_risk of this ContainerBaseInfo.

        中危风险数量

        :return: The medium_risk of this ContainerBaseInfo.
        :rtype: int
        """
        return self._medium_risk

    @medium_risk.setter
    def medium_risk(self, medium_risk):
        """Sets the medium_risk of this ContainerBaseInfo.

        中危风险数量

        :param medium_risk: The medium_risk of this ContainerBaseInfo.
        :type medium_risk: int
        """
        self._medium_risk = medium_risk

    @property
    def high_risk(self):
        """Gets the high_risk of this ContainerBaseInfo.

        高危风险数量

        :return: The high_risk of this ContainerBaseInfo.
        :rtype: int
        """
        return self._high_risk

    @high_risk.setter
    def high_risk(self, high_risk):
        """Sets the high_risk of this ContainerBaseInfo.

        高危风险数量

        :param high_risk: The high_risk of this ContainerBaseInfo.
        :type high_risk: int
        """
        self._high_risk = high_risk

    @property
    def fatal_risk(self):
        """Gets the fatal_risk of this ContainerBaseInfo.

        致命风险数量

        :return: The fatal_risk of this ContainerBaseInfo.
        :rtype: int
        """
        return self._fatal_risk

    @fatal_risk.setter
    def fatal_risk(self, fatal_risk):
        """Sets the fatal_risk of this ContainerBaseInfo.

        致命风险数量

        :param fatal_risk: The fatal_risk of this ContainerBaseInfo.
        :type fatal_risk: int
        """
        self._fatal_risk = fatal_risk

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
        if not isinstance(other, ContainerBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
