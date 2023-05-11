# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'description': 'str',
        'cluster_node_config': 'ClusterNodeConfig'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'description': 'description',
        'cluster_node_config': 'cluster_node_config'
    }

    def __init__(self, cluster_name=None, description=None, cluster_node_config=None):
        """CreateClusterRequestDTO

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param description: 集群描述
        :type description: str
        :param cluster_node_config: 
        :type cluster_node_config: :class:`huaweicloudsdkiotedge.v3.ClusterNodeConfig`
        """
        
        

        self._cluster_name = None
        self._description = None
        self._cluster_node_config = None
        self.discriminator = None

        self.cluster_name = cluster_name
        if description is not None:
            self.description = description
        if cluster_node_config is not None:
            self.cluster_node_config = cluster_node_config

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateClusterRequestDTO.

        集群名称

        :return: The cluster_name of this CreateClusterRequestDTO.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateClusterRequestDTO.

        集群名称

        :param cluster_name: The cluster_name of this CreateClusterRequestDTO.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def description(self):
        """Gets the description of this CreateClusterRequestDTO.

        集群描述

        :return: The description of this CreateClusterRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateClusterRequestDTO.

        集群描述

        :param description: The description of this CreateClusterRequestDTO.
        :type description: str
        """
        self._description = description

    @property
    def cluster_node_config(self):
        """Gets the cluster_node_config of this CreateClusterRequestDTO.

        :return: The cluster_node_config of this CreateClusterRequestDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v3.ClusterNodeConfig`
        """
        return self._cluster_node_config

    @cluster_node_config.setter
    def cluster_node_config(self, cluster_node_config):
        """Sets the cluster_node_config of this CreateClusterRequestDTO.

        :param cluster_node_config: The cluster_node_config of this CreateClusterRequestDTO.
        :type cluster_node_config: :class:`huaweicloudsdkiotedge.v3.ClusterNodeConfig`
        """
        self._cluster_node_config = cluster_node_config

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
        if not isinstance(other, CreateClusterRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
