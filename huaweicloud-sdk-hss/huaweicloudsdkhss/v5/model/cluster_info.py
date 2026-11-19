# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_name': 'str',
        'cluster_version': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'cluster_status': 'str',
        'installed_pod_num': 'int',
        'pod_num': 'int',
        'protect_pod_num': 'int',
        'create_time': 'int',
        'protect_status': 'str'
    }

    attribute_map = {
        'enterprise_project_name': 'enterprise_project_name',
        'cluster_version': 'cluster_version',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_status': 'cluster_status',
        'installed_pod_num': 'installed_pod_num',
        'pod_num': 'pod_num',
        'protect_pod_num': 'protect_pod_num',
        'create_time': 'create_time',
        'protect_status': 'protect_status'
    }

    def __init__(self, enterprise_project_name=None, cluster_version=None, cluster_id=None, cluster_name=None, cluster_status=None, installed_pod_num=None, pod_num=None, protect_pod_num=None, create_time=None, protect_status=None):
        r"""ClusterInfo

        The model defined in huaweicloud sdk

        :param enterprise_project_name: **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 
        :type enterprise_project_name: str
        :param cluster_version: **参数解释**: 集群版本 **取值范围**: 字符长度0-256位 
        :type cluster_version: str
        :param cluster_id: **参数解释**: 集群id **取值范围**: 字符长度0-64位 
        :type cluster_id: str
        :param cluster_name: **参数解释**: 所属集群 **取值范围**: 字符长度0-256位 
        :type cluster_name: str
        :param cluster_status: **参数解释**： 集群状态，从CCE同步状态 **取值范围**： - workload：工作负载。 - cluster：集群。 
        :type cluster_status: str
        :param installed_pod_num: **参数解释**: 已安装实例个数 **取值范围**: 最小值0，最大值2147483647 
        :type installed_pod_num: int
        :param pod_num: **参数解释**: 全部实例个数 **取值范围**: 最小值0，最大值2147483647 
        :type pod_num: int
        :param protect_pod_num: **参数解释**: 已防护实例数 **取值范围**: 最小值0，最大值2147483647 
        :type protect_pod_num: int
        :param create_time: **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type create_time: int
        :param protect_status: **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 
        :type protect_status: str
        """
        
        

        self._enterprise_project_name = None
        self._cluster_version = None
        self._cluster_id = None
        self._cluster_name = None
        self._cluster_status = None
        self._installed_pod_num = None
        self._pod_num = None
        self._protect_pod_num = None
        self._create_time = None
        self._protect_status = None
        self.discriminator = None

        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if cluster_version is not None:
            self.cluster_version = cluster_version
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_status is not None:
            self.cluster_status = cluster_status
        if installed_pod_num is not None:
            self.installed_pod_num = installed_pod_num
        if pod_num is not None:
            self.pod_num = pod_num
        if protect_pod_num is not None:
            self.protect_pod_num = protect_pod_num
        if create_time is not None:
            self.create_time = create_time
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this ClusterInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 

        :return: The enterprise_project_name of this ClusterInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this ClusterInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 

        :param enterprise_project_name: The enterprise_project_name of this ClusterInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this ClusterInfo.

        **参数解释**: 集群版本 **取值范围**: 字符长度0-256位 

        :return: The cluster_version of this ClusterInfo.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this ClusterInfo.

        **参数解释**: 集群版本 **取值范围**: 字符长度0-256位 

        :param cluster_version: The cluster_version of this ClusterInfo.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterInfo.

        **参数解释**: 集群id **取值范围**: 字符长度0-64位 

        :return: The cluster_id of this ClusterInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterInfo.

        **参数解释**: 集群id **取值范围**: 字符长度0-64位 

        :param cluster_id: The cluster_id of this ClusterInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterInfo.

        **参数解释**: 所属集群 **取值范围**: 字符长度0-256位 

        :return: The cluster_name of this ClusterInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterInfo.

        **参数解释**: 所属集群 **取值范围**: 字符长度0-256位 

        :param cluster_name: The cluster_name of this ClusterInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_status(self):
        r"""Gets the cluster_status of this ClusterInfo.

        **参数解释**： 集群状态，从CCE同步状态 **取值范围**： - workload：工作负载。 - cluster：集群。 

        :return: The cluster_status of this ClusterInfo.
        :rtype: str
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        r"""Sets the cluster_status of this ClusterInfo.

        **参数解释**： 集群状态，从CCE同步状态 **取值范围**： - workload：工作负载。 - cluster：集群。 

        :param cluster_status: The cluster_status of this ClusterInfo.
        :type cluster_status: str
        """
        self._cluster_status = cluster_status

    @property
    def installed_pod_num(self):
        r"""Gets the installed_pod_num of this ClusterInfo.

        **参数解释**: 已安装实例个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The installed_pod_num of this ClusterInfo.
        :rtype: int
        """
        return self._installed_pod_num

    @installed_pod_num.setter
    def installed_pod_num(self, installed_pod_num):
        r"""Sets the installed_pod_num of this ClusterInfo.

        **参数解释**: 已安装实例个数 **取值范围**: 最小值0，最大值2147483647 

        :param installed_pod_num: The installed_pod_num of this ClusterInfo.
        :type installed_pod_num: int
        """
        self._installed_pod_num = installed_pod_num

    @property
    def pod_num(self):
        r"""Gets the pod_num of this ClusterInfo.

        **参数解释**: 全部实例个数 **取值范围**: 最小值0，最大值2147483647 

        :return: The pod_num of this ClusterInfo.
        :rtype: int
        """
        return self._pod_num

    @pod_num.setter
    def pod_num(self, pod_num):
        r"""Sets the pod_num of this ClusterInfo.

        **参数解释**: 全部实例个数 **取值范围**: 最小值0，最大值2147483647 

        :param pod_num: The pod_num of this ClusterInfo.
        :type pod_num: int
        """
        self._pod_num = pod_num

    @property
    def protect_pod_num(self):
        r"""Gets the protect_pod_num of this ClusterInfo.

        **参数解释**: 已防护实例数 **取值范围**: 最小值0，最大值2147483647 

        :return: The protect_pod_num of this ClusterInfo.
        :rtype: int
        """
        return self._protect_pod_num

    @protect_pod_num.setter
    def protect_pod_num(self, protect_pod_num):
        r"""Sets the protect_pod_num of this ClusterInfo.

        **参数解释**: 已防护实例数 **取值范围**: 最小值0，最大值2147483647 

        :param protect_pod_num: The protect_pod_num of this ClusterInfo.
        :type protect_pod_num: int
        """
        self._protect_pod_num = protect_pod_num

    @property
    def create_time(self):
        r"""Gets the create_time of this ClusterInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The create_time of this ClusterInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ClusterInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this ClusterInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ClusterInfo.

        **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 

        :return: The protect_status of this ClusterInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ClusterInfo.

        **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 

        :param protect_status: The protect_status of this ClusterInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

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
        if not isinstance(other, ClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
