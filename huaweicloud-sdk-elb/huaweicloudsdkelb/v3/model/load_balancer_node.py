# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancerNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'guaranteed': 'bool',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'vip_address': 'str',
        'ipv6_vip_address': 'str',
        'availability_zone_list': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'guaranteed': 'guaranteed',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'vip_address': 'vip_address',
        'ipv6_vip_address': 'ipv6_vip_address',
        'availability_zone_list': 'availability_zone_list'
    }

    def __init__(self, id=None, name=None, guaranteed=None, l4_flavor_id=None, l7_flavor_id=None, vip_address=None, ipv6_vip_address=None, availability_zone_list=None):
        r"""LoadBalancerNode

        The model defined in huaweicloud sdk

        :param id: **参数解释**：负载均衡器id。  **取值范围**：不涉及
        :type id: str
        :param name: **参数解释**：负载均衡器名称。  **取值范围**：不涉及
        :type name: str
        :param guaranteed: **参数解释**：是否独享型LB。  **取值范围**： - false：共享型。 - true：独享型。
        :type guaranteed: bool
        :param l4_flavor_id: **参数解释**：网络型规格ID。  **取值范围**：不涉及
        :type l4_flavor_id: str
        :param l7_flavor_id: **参数解释**：应用型规格ID。  **取值范围**：不涉及
        :type l7_flavor_id: str
        :param vip_address: **参数解释**：ipv4地址。  **取值范围**：不涉及
        :type vip_address: str
        :param ipv6_vip_address: **参数解释**：ipv6地址。  **取值范围**：不涉及
        :type ipv6_vip_address: str
        :param availability_zone_list: **参数解释**：负载均衡器所在的可用区列表。  **取值范围**：不涉及
        :type availability_zone_list: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._guaranteed = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._vip_address = None
        self._ipv6_vip_address = None
        self._availability_zone_list = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.guaranteed = guaranteed
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if vip_address is not None:
            self.vip_address = vip_address
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        if availability_zone_list is not None:
            self.availability_zone_list = availability_zone_list

    @property
    def id(self):
        r"""Gets the id of this LoadBalancerNode.

        **参数解释**：负载均衡器id。  **取值范围**：不涉及

        :return: The id of this LoadBalancerNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LoadBalancerNode.

        **参数解释**：负载均衡器id。  **取值范围**：不涉及

        :param id: The id of this LoadBalancerNode.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this LoadBalancerNode.

        **参数解释**：负载均衡器名称。  **取值范围**：不涉及

        :return: The name of this LoadBalancerNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LoadBalancerNode.

        **参数解释**：负载均衡器名称。  **取值范围**：不涉及

        :param name: The name of this LoadBalancerNode.
        :type name: str
        """
        self._name = name

    @property
    def guaranteed(self):
        r"""Gets the guaranteed of this LoadBalancerNode.

        **参数解释**：是否独享型LB。  **取值范围**： - false：共享型。 - true：独享型。

        :return: The guaranteed of this LoadBalancerNode.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        r"""Sets the guaranteed of this LoadBalancerNode.

        **参数解释**：是否独享型LB。  **取值范围**： - false：共享型。 - true：独享型。

        :param guaranteed: The guaranteed of this LoadBalancerNode.
        :type guaranteed: bool
        """
        self._guaranteed = guaranteed

    @property
    def l4_flavor_id(self):
        r"""Gets the l4_flavor_id of this LoadBalancerNode.

        **参数解释**：网络型规格ID。  **取值范围**：不涉及

        :return: The l4_flavor_id of this LoadBalancerNode.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        r"""Sets the l4_flavor_id of this LoadBalancerNode.

        **参数解释**：网络型规格ID。  **取值范围**：不涉及

        :param l4_flavor_id: The l4_flavor_id of this LoadBalancerNode.
        :type l4_flavor_id: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        r"""Gets the l7_flavor_id of this LoadBalancerNode.

        **参数解释**：应用型规格ID。  **取值范围**：不涉及

        :return: The l7_flavor_id of this LoadBalancerNode.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        r"""Sets the l7_flavor_id of this LoadBalancerNode.

        **参数解释**：应用型规格ID。  **取值范围**：不涉及

        :param l7_flavor_id: The l7_flavor_id of this LoadBalancerNode.
        :type l7_flavor_id: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def vip_address(self):
        r"""Gets the vip_address of this LoadBalancerNode.

        **参数解释**：ipv4地址。  **取值范围**：不涉及

        :return: The vip_address of this LoadBalancerNode.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this LoadBalancerNode.

        **参数解释**：ipv4地址。  **取值范围**：不涉及

        :param vip_address: The vip_address of this LoadBalancerNode.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this LoadBalancerNode.

        **参数解释**：ipv6地址。  **取值范围**：不涉及

        :return: The ipv6_vip_address of this LoadBalancerNode.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this LoadBalancerNode.

        **参数解释**：ipv6地址。  **取值范围**：不涉及

        :param ipv6_vip_address: The ipv6_vip_address of this LoadBalancerNode.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def availability_zone_list(self):
        r"""Gets the availability_zone_list of this LoadBalancerNode.

        **参数解释**：负载均衡器所在的可用区列表。  **取值范围**：不涉及

        :return: The availability_zone_list of this LoadBalancerNode.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        r"""Sets the availability_zone_list of this LoadBalancerNode.

        **参数解释**：负载均衡器所在的可用区列表。  **取值范围**：不涉及

        :param availability_zone_list: The availability_zone_list of this LoadBalancerNode.
        :type availability_zone_list: list[str]
        """
        self._availability_zone_list = availability_zone_list

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
        if not isinstance(other, LoadBalancerNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
