# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NamedCluster:

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
        'cluster': 'ClusterCert'
    }

    attribute_map = {
        'name': 'name',
        'cluster': 'cluster'
    }

    def __init__(self, name=None, cluster=None):
        r"""NamedCluster

        The model defined in huaweicloud sdk

        :param name: 集群名称
        :type name: str
        :param cluster: 
        :type cluster: :class:`huaweicloudsdkucs.v1.ClusterCert`
        """
        
        

        self._name = None
        self._cluster = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cluster is not None:
            self.cluster = cluster

    @property
    def name(self):
        r"""Gets the name of this NamedCluster.

        集群名称

        :return: The name of this NamedCluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NamedCluster.

        集群名称

        :param name: The name of this NamedCluster.
        :type name: str
        """
        self._name = name

    @property
    def cluster(self):
        r"""Gets the cluster of this NamedCluster.

        :return: The cluster of this NamedCluster.
        :rtype: :class:`huaweicloudsdkucs.v1.ClusterCert`
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        r"""Sets the cluster of this NamedCluster.

        :param cluster: The cluster of this NamedCluster.
        :type cluster: :class:`huaweicloudsdkucs.v1.ClusterCert`
        """
        self._cluster = cluster

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
        if not isinstance(other, NamedCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
