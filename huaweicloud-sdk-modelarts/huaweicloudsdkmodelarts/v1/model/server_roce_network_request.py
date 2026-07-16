# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerRoceNetworkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_type': 'str',
        'physical_network': 'str'
    }

    attribute_map = {
        'network_type': 'network_type',
        'physical_network': 'physical_network'
    }

    def __init__(self, network_type=None, physical_network=None):
        r"""ServerRoceNetworkRequest

        The model defined in huaweicloud sdk

        :param network_type: **参数解释**：RoCE网络类型。 **约束限制**：不涉及。 **取值范围**：  - vxlan_roce  - roce_v2  **默认取值**：不涉及。
        :type network_type: str
        :param physical_network: **参数解释**：物理网络名称。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type physical_network: str
        """
        
        

        self._network_type = None
        self._physical_network = None
        self.discriminator = None

        if network_type is not None:
            self.network_type = network_type
        if physical_network is not None:
            self.physical_network = physical_network

    @property
    def network_type(self):
        r"""Gets the network_type of this ServerRoceNetworkRequest.

        **参数解释**：RoCE网络类型。 **约束限制**：不涉及。 **取值范围**：  - vxlan_roce  - roce_v2  **默认取值**：不涉及。

        :return: The network_type of this ServerRoceNetworkRequest.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this ServerRoceNetworkRequest.

        **参数解释**：RoCE网络类型。 **约束限制**：不涉及。 **取值范围**：  - vxlan_roce  - roce_v2  **默认取值**：不涉及。

        :param network_type: The network_type of this ServerRoceNetworkRequest.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def physical_network(self):
        r"""Gets the physical_network of this ServerRoceNetworkRequest.

        **参数解释**：物理网络名称。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The physical_network of this ServerRoceNetworkRequest.
        :rtype: str
        """
        return self._physical_network

    @physical_network.setter
    def physical_network(self, physical_network):
        r"""Sets the physical_network of this ServerRoceNetworkRequest.

        **参数解释**：物理网络名称。 **约束限制**：^[-_.a-zA-Z0-9]{1,64}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param physical_network: The physical_network of this ServerRoceNetworkRequest.
        :type physical_network: str
        """
        self._physical_network = physical_network

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
        if not isinstance(other, ServerRoceNetworkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
