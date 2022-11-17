# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Clusters:

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
        """Clusters

        The model defined in huaweicloud sdk

        :param name: 集群名字。 - 若不存在publicIp（虚拟机弹性IP），则集群列表的集群数量为1，该字段值为“internalCluster”。 - 若存在publicIp，则集群列表的集群数量大于1，所有扩展的cluster的name的值为“externalCluster”。 
        :type name: str
        :param cluster: 
        :type cluster: :class:`huaweicloudsdkcce.v3.ClusterCert`
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
        """Gets the name of this Clusters.

        集群名字。 - 若不存在publicIp（虚拟机弹性IP），则集群列表的集群数量为1，该字段值为“internalCluster”。 - 若存在publicIp，则集群列表的集群数量大于1，所有扩展的cluster的name的值为“externalCluster”。 

        :return: The name of this Clusters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Clusters.

        集群名字。 - 若不存在publicIp（虚拟机弹性IP），则集群列表的集群数量为1，该字段值为“internalCluster”。 - 若存在publicIp，则集群列表的集群数量大于1，所有扩展的cluster的name的值为“externalCluster”。 

        :param name: The name of this Clusters.
        :type name: str
        """
        self._name = name

    @property
    def cluster(self):
        """Gets the cluster of this Clusters.

        :return: The cluster of this Clusters.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterCert`
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Clusters.

        :param cluster: The cluster of this Clusters.
        :type cluster: :class:`huaweicloudsdkcce.v3.ClusterCert`
        """
        self._cluster = cluster

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
        if not isinstance(other, Clusters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
