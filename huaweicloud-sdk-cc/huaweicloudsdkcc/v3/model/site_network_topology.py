# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteNetworkTopology:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topology': 'str'
    }

    attribute_map = {
        'topology': 'topology'
    }

    def __init__(self, topology=None):
        r"""SiteNetworkTopology

        The model defined in huaweicloud sdk

        :param topology: 拓扑结构。 - p2p（点对点拓扑） - mesh （网状拓扑） - star （星形拓扑） - hybrid （混合拓扑）
        :type topology: str
        """
        
        

        self._topology = None
        self.discriminator = None

        self.topology = topology

    @property
    def topology(self):
        r"""Gets the topology of this SiteNetworkTopology.

        拓扑结构。 - p2p（点对点拓扑） - mesh （网状拓扑） - star （星形拓扑） - hybrid （混合拓扑）

        :return: The topology of this SiteNetworkTopology.
        :rtype: str
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        r"""Sets the topology of this SiteNetworkTopology.

        拓扑结构。 - p2p（点对点拓扑） - mesh （网状拓扑） - star （星形拓扑） - hybrid （混合拓扑）

        :param topology: The topology of this SiteNetworkTopology.
        :type topology: str
        """
        self._topology = topology

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
        if not isinstance(other, SiteNetworkTopology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
