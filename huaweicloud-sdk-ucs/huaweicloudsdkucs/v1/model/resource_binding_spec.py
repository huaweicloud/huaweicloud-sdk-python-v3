# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceBindingSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'object',
        'propagate_deps': 'bool',
        'replica_requirements': 'object',
        'replicas': 'int',
        'placement': 'Placement',
        'clusters': 'list[TargetCluster]'
    }

    attribute_map = {
        'resource': 'resource',
        'propagate_deps': 'propagateDeps',
        'replica_requirements': 'replicaRequirements',
        'replicas': 'replicas',
        'placement': 'placement',
        'clusters': 'clusters'
    }

    def __init__(self, resource=None, propagate_deps=None, replica_requirements=None, replicas=None, placement=None, clusters=None):
        r"""ResourceBindingSpec

        The model defined in huaweicloud sdk

        :param resource: 要传播的Kubernetes资源引用
        :type resource: object
        :param propagate_deps: 是否自动传播相关资源
        :type propagate_deps: bool
        :param replica_requirements: 定义每个副本的需求
        :type replica_requirements: object
        :param replicas: 要创建的副本数量
        :type replicas: int
        :param placement: 
        :type placement: :class:`huaweicloudsdkucs.v1.Placement`
        :param clusters: 目标成员集群列表
        :type clusters: list[:class:`huaweicloudsdkucs.v1.TargetCluster`]
        """
        
        

        self._resource = None
        self._propagate_deps = None
        self._replica_requirements = None
        self._replicas = None
        self._placement = None
        self._clusters = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if propagate_deps is not None:
            self.propagate_deps = propagate_deps
        if replica_requirements is not None:
            self.replica_requirements = replica_requirements
        if replicas is not None:
            self.replicas = replicas
        if placement is not None:
            self.placement = placement
        if clusters is not None:
            self.clusters = clusters

    @property
    def resource(self):
        r"""Gets the resource of this ResourceBindingSpec.

        要传播的Kubernetes资源引用

        :return: The resource of this ResourceBindingSpec.
        :rtype: object
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ResourceBindingSpec.

        要传播的Kubernetes资源引用

        :param resource: The resource of this ResourceBindingSpec.
        :type resource: object
        """
        self._resource = resource

    @property
    def propagate_deps(self):
        r"""Gets the propagate_deps of this ResourceBindingSpec.

        是否自动传播相关资源

        :return: The propagate_deps of this ResourceBindingSpec.
        :rtype: bool
        """
        return self._propagate_deps

    @propagate_deps.setter
    def propagate_deps(self, propagate_deps):
        r"""Sets the propagate_deps of this ResourceBindingSpec.

        是否自动传播相关资源

        :param propagate_deps: The propagate_deps of this ResourceBindingSpec.
        :type propagate_deps: bool
        """
        self._propagate_deps = propagate_deps

    @property
    def replica_requirements(self):
        r"""Gets the replica_requirements of this ResourceBindingSpec.

        定义每个副本的需求

        :return: The replica_requirements of this ResourceBindingSpec.
        :rtype: object
        """
        return self._replica_requirements

    @replica_requirements.setter
    def replica_requirements(self, replica_requirements):
        r"""Sets the replica_requirements of this ResourceBindingSpec.

        定义每个副本的需求

        :param replica_requirements: The replica_requirements of this ResourceBindingSpec.
        :type replica_requirements: object
        """
        self._replica_requirements = replica_requirements

    @property
    def replicas(self):
        r"""Gets the replicas of this ResourceBindingSpec.

        要创建的副本数量

        :return: The replicas of this ResourceBindingSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        r"""Sets the replicas of this ResourceBindingSpec.

        要创建的副本数量

        :param replicas: The replicas of this ResourceBindingSpec.
        :type replicas: int
        """
        self._replicas = replicas

    @property
    def placement(self):
        r"""Gets the placement of this ResourceBindingSpec.

        :return: The placement of this ResourceBindingSpec.
        :rtype: :class:`huaweicloudsdkucs.v1.Placement`
        """
        return self._placement

    @placement.setter
    def placement(self, placement):
        r"""Sets the placement of this ResourceBindingSpec.

        :param placement: The placement of this ResourceBindingSpec.
        :type placement: :class:`huaweicloudsdkucs.v1.Placement`
        """
        self._placement = placement

    @property
    def clusters(self):
        r"""Gets the clusters of this ResourceBindingSpec.

        目标成员集群列表

        :return: The clusters of this ResourceBindingSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.TargetCluster`]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this ResourceBindingSpec.

        目标成员集群列表

        :param clusters: The clusters of this ResourceBindingSpec.
        :type clusters: list[:class:`huaweicloudsdkucs.v1.TargetCluster`]
        """
        self._clusters = clusters

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
        if not isinstance(other, ResourceBindingSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
