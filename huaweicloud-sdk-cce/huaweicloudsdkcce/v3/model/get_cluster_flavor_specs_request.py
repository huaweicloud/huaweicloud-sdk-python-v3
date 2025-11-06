# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetClusterFlavorSpecsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_type': 'str'
    }

    attribute_map = {
        'cluster_type': 'clusterType'
    }

    def __init__(self, cluster_type=None):
        r"""GetClusterFlavorSpecsRequest

        The model defined in huaweicloud sdk

        :param cluster_type: **参数解释**： 该参数用于按集群架构查询可售卖规格 **取值范围**： - VirtualMachine: CCE集群 - ARM64: 鲲鹏集群
        :type cluster_type: str
        """
        
        

        self._cluster_type = None
        self.discriminator = None

        self.cluster_type = cluster_type

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this GetClusterFlavorSpecsRequest.

        **参数解释**： 该参数用于按集群架构查询可售卖规格 **取值范围**： - VirtualMachine: CCE集群 - ARM64: 鲲鹏集群

        :return: The cluster_type of this GetClusterFlavorSpecsRequest.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this GetClusterFlavorSpecsRequest.

        **参数解释**： 该参数用于按集群架构查询可售卖规格 **取值范围**： - VirtualMachine: CCE集群 - ARM64: 鲲鹏集群

        :param cluster_type: The cluster_type of this GetClusterFlavorSpecsRequest.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

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
        if not isinstance(other, GetClusterFlavorSpecsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
