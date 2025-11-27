# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterReconcileStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'config_set_total_num': 'int',
        'health_status_num': 'int',
        'failed_status_num': 'int',
        'unknown_status_num': 'int',
        'progressing_status_num': 'int',
        'k8s_resource_num': 'int',
        'source_repo_num': 'int'
    }

    attribute_map = {
        'cluster_id': 'clusterID',
        'config_set_total_num': 'configSetTotalNum',
        'health_status_num': 'healthStatusNum',
        'failed_status_num': 'failedStatusNum',
        'unknown_status_num': 'unknownStatusNum',
        'progressing_status_num': 'progressingStatusNum',
        'k8s_resource_num': 'k8sResourceNum',
        'source_repo_num': 'sourceRepoNum'
    }

    def __init__(self, cluster_id=None, config_set_total_num=None, health_status_num=None, failed_status_num=None, unknown_status_num=None, progressing_status_num=None, k8s_resource_num=None, source_repo_num=None):
        r"""ClusterReconcileStatus

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param config_set_total_num: 集群中配置集合的总数
        :type config_set_total_num: int
        :param health_status_num: 健康状态的配置集合数量
        :type health_status_num: int
        :param failed_status_num: 失败状态的配置集合数量
        :type failed_status_num: int
        :param unknown_status_num: 未知状态的配置集合数量
        :type unknown_status_num: int
        :param progressing_status_num: 正在处理中的配置集合数量
        :type progressing_status_num: int
        :param k8s_resource_num: 与集群关联的Kubernetes资源数量
        :type k8s_resource_num: int
        :param source_repo_num: 与集群关联的源代码仓库数量
        :type source_repo_num: int
        """
        
        

        self._cluster_id = None
        self._config_set_total_num = None
        self._health_status_num = None
        self._failed_status_num = None
        self._unknown_status_num = None
        self._progressing_status_num = None
        self._k8s_resource_num = None
        self._source_repo_num = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if config_set_total_num is not None:
            self.config_set_total_num = config_set_total_num
        if health_status_num is not None:
            self.health_status_num = health_status_num
        if failed_status_num is not None:
            self.failed_status_num = failed_status_num
        if unknown_status_num is not None:
            self.unknown_status_num = unknown_status_num
        if progressing_status_num is not None:
            self.progressing_status_num = progressing_status_num
        if k8s_resource_num is not None:
            self.k8s_resource_num = k8s_resource_num
        if source_repo_num is not None:
            self.source_repo_num = source_repo_num

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterReconcileStatus.

        集群id

        :return: The cluster_id of this ClusterReconcileStatus.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterReconcileStatus.

        集群id

        :param cluster_id: The cluster_id of this ClusterReconcileStatus.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def config_set_total_num(self):
        r"""Gets the config_set_total_num of this ClusterReconcileStatus.

        集群中配置集合的总数

        :return: The config_set_total_num of this ClusterReconcileStatus.
        :rtype: int
        """
        return self._config_set_total_num

    @config_set_total_num.setter
    def config_set_total_num(self, config_set_total_num):
        r"""Sets the config_set_total_num of this ClusterReconcileStatus.

        集群中配置集合的总数

        :param config_set_total_num: The config_set_total_num of this ClusterReconcileStatus.
        :type config_set_total_num: int
        """
        self._config_set_total_num = config_set_total_num

    @property
    def health_status_num(self):
        r"""Gets the health_status_num of this ClusterReconcileStatus.

        健康状态的配置集合数量

        :return: The health_status_num of this ClusterReconcileStatus.
        :rtype: int
        """
        return self._health_status_num

    @health_status_num.setter
    def health_status_num(self, health_status_num):
        r"""Sets the health_status_num of this ClusterReconcileStatus.

        健康状态的配置集合数量

        :param health_status_num: The health_status_num of this ClusterReconcileStatus.
        :type health_status_num: int
        """
        self._health_status_num = health_status_num

    @property
    def failed_status_num(self):
        r"""Gets the failed_status_num of this ClusterReconcileStatus.

        失败状态的配置集合数量

        :return: The failed_status_num of this ClusterReconcileStatus.
        :rtype: int
        """
        return self._failed_status_num

    @failed_status_num.setter
    def failed_status_num(self, failed_status_num):
        r"""Sets the failed_status_num of this ClusterReconcileStatus.

        失败状态的配置集合数量

        :param failed_status_num: The failed_status_num of this ClusterReconcileStatus.
        :type failed_status_num: int
        """
        self._failed_status_num = failed_status_num

    @property
    def unknown_status_num(self):
        r"""Gets the unknown_status_num of this ClusterReconcileStatus.

        未知状态的配置集合数量

        :return: The unknown_status_num of this ClusterReconcileStatus.
        :rtype: int
        """
        return self._unknown_status_num

    @unknown_status_num.setter
    def unknown_status_num(self, unknown_status_num):
        r"""Sets the unknown_status_num of this ClusterReconcileStatus.

        未知状态的配置集合数量

        :param unknown_status_num: The unknown_status_num of this ClusterReconcileStatus.
        :type unknown_status_num: int
        """
        self._unknown_status_num = unknown_status_num

    @property
    def progressing_status_num(self):
        r"""Gets the progressing_status_num of this ClusterReconcileStatus.

        正在处理中的配置集合数量

        :return: The progressing_status_num of this ClusterReconcileStatus.
        :rtype: int
        """
        return self._progressing_status_num

    @progressing_status_num.setter
    def progressing_status_num(self, progressing_status_num):
        r"""Sets the progressing_status_num of this ClusterReconcileStatus.

        正在处理中的配置集合数量

        :param progressing_status_num: The progressing_status_num of this ClusterReconcileStatus.
        :type progressing_status_num: int
        """
        self._progressing_status_num = progressing_status_num

    @property
    def k8s_resource_num(self):
        r"""Gets the k8s_resource_num of this ClusterReconcileStatus.

        与集群关联的Kubernetes资源数量

        :return: The k8s_resource_num of this ClusterReconcileStatus.
        :rtype: int
        """
        return self._k8s_resource_num

    @k8s_resource_num.setter
    def k8s_resource_num(self, k8s_resource_num):
        r"""Sets the k8s_resource_num of this ClusterReconcileStatus.

        与集群关联的Kubernetes资源数量

        :param k8s_resource_num: The k8s_resource_num of this ClusterReconcileStatus.
        :type k8s_resource_num: int
        """
        self._k8s_resource_num = k8s_resource_num

    @property
    def source_repo_num(self):
        r"""Gets the source_repo_num of this ClusterReconcileStatus.

        与集群关联的源代码仓库数量

        :return: The source_repo_num of this ClusterReconcileStatus.
        :rtype: int
        """
        return self._source_repo_num

    @source_repo_num.setter
    def source_repo_num(self, source_repo_num):
        r"""Sets the source_repo_num of this ClusterReconcileStatus.

        与集群关联的源代码仓库数量

        :param source_repo_num: The source_repo_num of this ClusterReconcileStatus.
        :type source_repo_num: int
        """
        self._source_repo_num = source_repo_num

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
        if not isinstance(other, ClusterReconcileStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
