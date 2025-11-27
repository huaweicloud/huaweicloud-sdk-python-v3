# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Placement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_affinity': 'ClusterAffinity',
        'cluster_tolerations': 'list[Toleration]',
        'replica_scheduling': 'object'
    }

    attribute_map = {
        'cluster_affinity': 'clusterAffinity',
        'cluster_tolerations': 'clusterTolerations',
        'replica_scheduling': 'replicaScheduling'
    }

    def __init__(self, cluster_affinity=None, cluster_tolerations=None, replica_scheduling=None):
        r"""Placement

        The model defined in huaweicloud sdk

        :param cluster_affinity: 
        :type cluster_affinity: :class:`huaweicloudsdkucs.v1.ClusterAffinity`
        :param cluster_tolerations: 集群容忍规则
        :type cluster_tolerations: list[:class:`huaweicloudsdkucs.v1.Toleration`]
        :param replica_scheduling: 定义如何在成员集群间分配副本
        :type replica_scheduling: object
        """
        
        

        self._cluster_affinity = None
        self._cluster_tolerations = None
        self._replica_scheduling = None
        self.discriminator = None

        if cluster_affinity is not None:
            self.cluster_affinity = cluster_affinity
        if cluster_tolerations is not None:
            self.cluster_tolerations = cluster_tolerations
        if replica_scheduling is not None:
            self.replica_scheduling = replica_scheduling

    @property
    def cluster_affinity(self):
        r"""Gets the cluster_affinity of this Placement.

        :return: The cluster_affinity of this Placement.
        :rtype: :class:`huaweicloudsdkucs.v1.ClusterAffinity`
        """
        return self._cluster_affinity

    @cluster_affinity.setter
    def cluster_affinity(self, cluster_affinity):
        r"""Sets the cluster_affinity of this Placement.

        :param cluster_affinity: The cluster_affinity of this Placement.
        :type cluster_affinity: :class:`huaweicloudsdkucs.v1.ClusterAffinity`
        """
        self._cluster_affinity = cluster_affinity

    @property
    def cluster_tolerations(self):
        r"""Gets the cluster_tolerations of this Placement.

        集群容忍规则

        :return: The cluster_tolerations of this Placement.
        :rtype: list[:class:`huaweicloudsdkucs.v1.Toleration`]
        """
        return self._cluster_tolerations

    @cluster_tolerations.setter
    def cluster_tolerations(self, cluster_tolerations):
        r"""Sets the cluster_tolerations of this Placement.

        集群容忍规则

        :param cluster_tolerations: The cluster_tolerations of this Placement.
        :type cluster_tolerations: list[:class:`huaweicloudsdkucs.v1.Toleration`]
        """
        self._cluster_tolerations = cluster_tolerations

    @property
    def replica_scheduling(self):
        r"""Gets the replica_scheduling of this Placement.

        定义如何在成员集群间分配副本

        :return: The replica_scheduling of this Placement.
        :rtype: object
        """
        return self._replica_scheduling

    @replica_scheduling.setter
    def replica_scheduling(self, replica_scheduling):
        r"""Sets the replica_scheduling of this Placement.

        定义如何在成员集群间分配副本

        :param replica_scheduling: The replica_scheduling of this Placement.
        :type replica_scheduling: object
        """
        self._replica_scheduling = replica_scheduling

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
        if not isinstance(other, Placement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
