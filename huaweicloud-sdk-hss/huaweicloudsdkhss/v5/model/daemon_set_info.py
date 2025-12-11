# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DaemonSetInfo:

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
        'namespace_name': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'cluster_name': 'str',
        'status': 'str',
        'pods_num': 'int',
        'image_name': 'str',
        'match_labels': 'list[LabelInfo]',
        'create_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'namespace_name': 'namespace_name',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'cluster_name': 'cluster_name',
        'status': 'status',
        'pods_num': 'pods_num',
        'image_name': 'image_name',
        'match_labels': 'match_labels',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, namespace_name=None, cluster_id=None, cluster_type=None, cluster_name=None, status=None, pods_num=None, image_name=None, match_labels=None, create_time=None):
        r"""DaemonSetInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**: daemonset名称。 **取值范围**: 字符长度0-256位 
        :type name: str
        :param namespace_name: **参数解释**: 命名空间名称。 **取值范围**: 字符长度0-256位 
        :type namespace_name: str
        :param cluster_id: **参数解释**: 集群的唯一标识ID，用于唯一确定DaemonSet所属的集群实例。 **取值范围**: 符合标准UUID格式，字符串长度36位 
        :type cluster_id: str
        :param cluster_type: **参数解释**: DaemonSet所属集群的部署类型，用于区分不同云厂商或部署模式的集群。 **取值范围**: k8s（原生集群）、cce（CCE集群）、ali（阿里云集群）、tencent（腾讯云集群）、azure（微软云集群）、aws（亚马逊集群）、self_built_hw（华为云自建集群）、self_built_idc（IDC自建集群） 
        :type cluster_type: str
        :param cluster_name: **参数解释**: 集群名称。 **取值范围**: 字符串长度0-256 
        :type cluster_name: str
        :param status: **参数解释**: DaemonSet的运行状态，用于标识当前实例的运行健康度； **取值范围**: Running（正常运行）、Failed（存在异常） 
        :type status: str
        :param pods_num: **参数解释**: 当前DaemonSet对应的Pod实例总数量； **取值范围**: 非负整数，单位为个，最小值0，无上限（取决于集群资源） 
        :type pods_num: int
        :param image_name: **参数解释**: DaemonSet实例所使用的容器镜像的完整名称，包含镜像仓库、镜像名及标签； **取值范围**: 符合容器镜像命名规范，字符长度1 - 256位 
        :type image_name: str
        :param match_labels: **参数解释**: 用于匹配Pod的标签集合，K8s通过该标签关联DaemonSet与对应Pod； **取值范围**: 数组元素数量≥0，每个元素的key为标签名称，val为标签值，key和val字符长度均为1 - 63位 
        :type match_labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        :param create_time: **参数解释**: DaemonSet资源的创建时间； **取值范围**: 以毫秒级时间戳格式返回，取值为非负长整数，对应UTC时间1970 - 01 - 01起的毫秒数 
        :type create_time: int
        """
        
        

        self._name = None
        self._namespace_name = None
        self._cluster_id = None
        self._cluster_type = None
        self._cluster_name = None
        self._status = None
        self._pods_num = None
        self._image_name = None
        self._match_labels = None
        self._create_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if status is not None:
            self.status = status
        if pods_num is not None:
            self.pods_num = pods_num
        if image_name is not None:
            self.image_name = image_name
        if match_labels is not None:
            self.match_labels = match_labels
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this DaemonSetInfo.

        **参数解释**: daemonset名称。 **取值范围**: 字符长度0-256位 

        :return: The name of this DaemonSetInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DaemonSetInfo.

        **参数解释**: daemonset名称。 **取值范围**: 字符长度0-256位 

        :param name: The name of this DaemonSetInfo.
        :type name: str
        """
        self._name = name

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this DaemonSetInfo.

        **参数解释**: 命名空间名称。 **取值范围**: 字符长度0-256位 

        :return: The namespace_name of this DaemonSetInfo.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this DaemonSetInfo.

        **参数解释**: 命名空间名称。 **取值范围**: 字符长度0-256位 

        :param namespace_name: The namespace_name of this DaemonSetInfo.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this DaemonSetInfo.

        **参数解释**: 集群的唯一标识ID，用于唯一确定DaemonSet所属的集群实例。 **取值范围**: 符合标准UUID格式，字符串长度36位 

        :return: The cluster_id of this DaemonSetInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this DaemonSetInfo.

        **参数解释**: 集群的唯一标识ID，用于唯一确定DaemonSet所属的集群实例。 **取值范围**: 符合标准UUID格式，字符串长度36位 

        :param cluster_id: The cluster_id of this DaemonSetInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this DaemonSetInfo.

        **参数解释**: DaemonSet所属集群的部署类型，用于区分不同云厂商或部署模式的集群。 **取值范围**: k8s（原生集群）、cce（CCE集群）、ali（阿里云集群）、tencent（腾讯云集群）、azure（微软云集群）、aws（亚马逊集群）、self_built_hw（华为云自建集群）、self_built_idc（IDC自建集群） 

        :return: The cluster_type of this DaemonSetInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this DaemonSetInfo.

        **参数解释**: DaemonSet所属集群的部署类型，用于区分不同云厂商或部署模式的集群。 **取值范围**: k8s（原生集群）、cce（CCE集群）、ali（阿里云集群）、tencent（腾讯云集群）、azure（微软云集群）、aws（亚马逊集群）、self_built_hw（华为云自建集群）、self_built_idc（IDC自建集群） 

        :param cluster_type: The cluster_type of this DaemonSetInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this DaemonSetInfo.

        **参数解释**: 集群名称。 **取值范围**: 字符串长度0-256 

        :return: The cluster_name of this DaemonSetInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this DaemonSetInfo.

        **参数解释**: 集群名称。 **取值范围**: 字符串长度0-256 

        :param cluster_name: The cluster_name of this DaemonSetInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def status(self):
        r"""Gets the status of this DaemonSetInfo.

        **参数解释**: DaemonSet的运行状态，用于标识当前实例的运行健康度； **取值范围**: Running（正常运行）、Failed（存在异常） 

        :return: The status of this DaemonSetInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DaemonSetInfo.

        **参数解释**: DaemonSet的运行状态，用于标识当前实例的运行健康度； **取值范围**: Running（正常运行）、Failed（存在异常） 

        :param status: The status of this DaemonSetInfo.
        :type status: str
        """
        self._status = status

    @property
    def pods_num(self):
        r"""Gets the pods_num of this DaemonSetInfo.

        **参数解释**: 当前DaemonSet对应的Pod实例总数量； **取值范围**: 非负整数，单位为个，最小值0，无上限（取决于集群资源） 

        :return: The pods_num of this DaemonSetInfo.
        :rtype: int
        """
        return self._pods_num

    @pods_num.setter
    def pods_num(self, pods_num):
        r"""Sets the pods_num of this DaemonSetInfo.

        **参数解释**: 当前DaemonSet对应的Pod实例总数量； **取值范围**: 非负整数，单位为个，最小值0，无上限（取决于集群资源） 

        :param pods_num: The pods_num of this DaemonSetInfo.
        :type pods_num: int
        """
        self._pods_num = pods_num

    @property
    def image_name(self):
        r"""Gets the image_name of this DaemonSetInfo.

        **参数解释**: DaemonSet实例所使用的容器镜像的完整名称，包含镜像仓库、镜像名及标签； **取值范围**: 符合容器镜像命名规范，字符长度1 - 256位 

        :return: The image_name of this DaemonSetInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this DaemonSetInfo.

        **参数解释**: DaemonSet实例所使用的容器镜像的完整名称，包含镜像仓库、镜像名及标签； **取值范围**: 符合容器镜像命名规范，字符长度1 - 256位 

        :param image_name: The image_name of this DaemonSetInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def match_labels(self):
        r"""Gets the match_labels of this DaemonSetInfo.

        **参数解释**: 用于匹配Pod的标签集合，K8s通过该标签关联DaemonSet与对应Pod； **取值范围**: 数组元素数量≥0，每个元素的key为标签名称，val为标签值，key和val字符长度均为1 - 63位 

        :return: The match_labels of this DaemonSetInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        return self._match_labels

    @match_labels.setter
    def match_labels(self, match_labels):
        r"""Sets the match_labels of this DaemonSetInfo.

        **参数解释**: 用于匹配Pod的标签集合，K8s通过该标签关联DaemonSet与对应Pod； **取值范围**: 数组元素数量≥0，每个元素的key为标签名称，val为标签值，key和val字符长度均为1 - 63位 

        :param match_labels: The match_labels of this DaemonSetInfo.
        :type match_labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        self._match_labels = match_labels

    @property
    def create_time(self):
        r"""Gets the create_time of this DaemonSetInfo.

        **参数解释**: DaemonSet资源的创建时间； **取值范围**: 以毫秒级时间戳格式返回，取值为非负长整数，对应UTC时间1970 - 01 - 01起的毫秒数 

        :return: The create_time of this DaemonSetInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DaemonSetInfo.

        **参数解释**: DaemonSet资源的创建时间； **取值范围**: 以毫秒级时间戳格式返回，取值为非负长整数，对应UTC时间1970 - 01 - 01起的毫秒数 

        :param create_time: The create_time of this DaemonSetInfo.
        :type create_time: int
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
        if not isinstance(other, DaemonSetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
