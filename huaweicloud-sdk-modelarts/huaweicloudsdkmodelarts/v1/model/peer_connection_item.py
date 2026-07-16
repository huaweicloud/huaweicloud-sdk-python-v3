# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeerConnectionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peer_vpc_id': 'str',
        'peer_subnet_id': 'str',
        'default_gate_way': 'bool'
    }

    attribute_map = {
        'peer_vpc_id': 'peerVpcId',
        'peer_subnet_id': 'peerSubnetId',
        'default_gate_way': 'defaultGateWay'
    }

    def __init__(self, peer_vpc_id=None, peer_subnet_id=None, default_gate_way=None):
        r"""PeerConnectionItem

        The model defined in huaweicloud sdk

        :param peer_vpc_id: **参数解释**：对端的VPC ID。 **取值范围**：不涉及。
        :type peer_vpc_id: str
        :param peer_subnet_id: **参数解释**：对端的子网ID。 **取值范围**：不涉及。
        :type peer_subnet_id: str
        :param default_gate_way: **参数解释**：创建默认路由的开关，默认为false不创建。 **取值范围**：不涉及。
        :type default_gate_way: bool
        """
        
        

        self._peer_vpc_id = None
        self._peer_subnet_id = None
        self._default_gate_way = None
        self.discriminator = None

        self.peer_vpc_id = peer_vpc_id
        self.peer_subnet_id = peer_subnet_id
        if default_gate_way is not None:
            self.default_gate_way = default_gate_way

    @property
    def peer_vpc_id(self):
        r"""Gets the peer_vpc_id of this PeerConnectionItem.

        **参数解释**：对端的VPC ID。 **取值范围**：不涉及。

        :return: The peer_vpc_id of this PeerConnectionItem.
        :rtype: str
        """
        return self._peer_vpc_id

    @peer_vpc_id.setter
    def peer_vpc_id(self, peer_vpc_id):
        r"""Sets the peer_vpc_id of this PeerConnectionItem.

        **参数解释**：对端的VPC ID。 **取值范围**：不涉及。

        :param peer_vpc_id: The peer_vpc_id of this PeerConnectionItem.
        :type peer_vpc_id: str
        """
        self._peer_vpc_id = peer_vpc_id

    @property
    def peer_subnet_id(self):
        r"""Gets the peer_subnet_id of this PeerConnectionItem.

        **参数解释**：对端的子网ID。 **取值范围**：不涉及。

        :return: The peer_subnet_id of this PeerConnectionItem.
        :rtype: str
        """
        return self._peer_subnet_id

    @peer_subnet_id.setter
    def peer_subnet_id(self, peer_subnet_id):
        r"""Sets the peer_subnet_id of this PeerConnectionItem.

        **参数解释**：对端的子网ID。 **取值范围**：不涉及。

        :param peer_subnet_id: The peer_subnet_id of this PeerConnectionItem.
        :type peer_subnet_id: str
        """
        self._peer_subnet_id = peer_subnet_id

    @property
    def default_gate_way(self):
        r"""Gets the default_gate_way of this PeerConnectionItem.

        **参数解释**：创建默认路由的开关，默认为false不创建。 **取值范围**：不涉及。

        :return: The default_gate_way of this PeerConnectionItem.
        :rtype: bool
        """
        return self._default_gate_way

    @default_gate_way.setter
    def default_gate_way(self, default_gate_way):
        r"""Sets the default_gate_way of this PeerConnectionItem.

        **参数解释**：创建默认路由的开关，默认为false不创建。 **取值范围**：不涉及。

        :param default_gate_way: The default_gate_way of this PeerConnectionItem.
        :type default_gate_way: bool
        """
        self._default_gate_way = default_gate_way

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
        if not isinstance(other, PeerConnectionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
