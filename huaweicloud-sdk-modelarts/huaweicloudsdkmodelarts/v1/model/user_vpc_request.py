# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserVpcRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_ids': 'list[str]',
        'connect_cidrs': 'list[str]',
        'nat_id': 'str',
        'eip_id': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_ids': 'security_group_ids',
        'connect_cidrs': 'connect_cidrs',
        'nat_id': 'nat_id',
        'eip_id': 'eip_id'
    }

    def __init__(self, vpc_id=None, subnet_id=None, security_group_ids=None, connect_cidrs=None, nat_id=None, eip_id=None):
        r"""UserVpcRequest

        The model defined in huaweicloud sdk

        :param vpc_id: **参数解释**：虚拟私有网络（VPC） ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type vpc_id: str
        :param subnet_id: **参数解释**：子网ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type subnet_id: str
        :param security_group_ids: **参数解释**：安全组ID列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type security_group_ids: list[str]
        :param connect_cidrs: **参数解释**：连接的CIDR地址列表。 **约束限制**：选填参数，适用场景：用户希望通过挂载的网卡，访问其他网段的地址。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type connect_cidrs: list[str]
        :param nat_id: **参数解释**：NAT ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type nat_id: str
        :param eip_id: **参数解释**：EIP ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type eip_id: str
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._security_group_ids = None
        self._connect_cidrs = None
        self._nat_id = None
        self._eip_id = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_ids = security_group_ids
        if connect_cidrs is not None:
            self.connect_cidrs = connect_cidrs
        if nat_id is not None:
            self.nat_id = nat_id
        if eip_id is not None:
            self.eip_id = eip_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UserVpcRequest.

        **参数解释**：虚拟私有网络（VPC） ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The vpc_id of this UserVpcRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UserVpcRequest.

        **参数解释**：虚拟私有网络（VPC） ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param vpc_id: The vpc_id of this UserVpcRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this UserVpcRequest.

        **参数解释**：子网ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The subnet_id of this UserVpcRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this UserVpcRequest.

        **参数解释**：子网ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param subnet_id: The subnet_id of this UserVpcRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_ids(self):
        r"""Gets the security_group_ids of this UserVpcRequest.

        **参数解释**：安全组ID列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The security_group_ids of this UserVpcRequest.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        r"""Sets the security_group_ids of this UserVpcRequest.

        **参数解释**：安全组ID列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param security_group_ids: The security_group_ids of this UserVpcRequest.
        :type security_group_ids: list[str]
        """
        self._security_group_ids = security_group_ids

    @property
    def connect_cidrs(self):
        r"""Gets the connect_cidrs of this UserVpcRequest.

        **参数解释**：连接的CIDR地址列表。 **约束限制**：选填参数，适用场景：用户希望通过挂载的网卡，访问其他网段的地址。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The connect_cidrs of this UserVpcRequest.
        :rtype: list[str]
        """
        return self._connect_cidrs

    @connect_cidrs.setter
    def connect_cidrs(self, connect_cidrs):
        r"""Sets the connect_cidrs of this UserVpcRequest.

        **参数解释**：连接的CIDR地址列表。 **约束限制**：选填参数，适用场景：用户希望通过挂载的网卡，访问其他网段的地址。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param connect_cidrs: The connect_cidrs of this UserVpcRequest.
        :type connect_cidrs: list[str]
        """
        self._connect_cidrs = connect_cidrs

    @property
    def nat_id(self):
        r"""Gets the nat_id of this UserVpcRequest.

        **参数解释**：NAT ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The nat_id of this UserVpcRequest.
        :rtype: str
        """
        return self._nat_id

    @nat_id.setter
    def nat_id(self, nat_id):
        r"""Sets the nat_id of this UserVpcRequest.

        **参数解释**：NAT ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param nat_id: The nat_id of this UserVpcRequest.
        :type nat_id: str
        """
        self._nat_id = nat_id

    @property
    def eip_id(self):
        r"""Gets the eip_id of this UserVpcRequest.

        **参数解释**：EIP ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The eip_id of this UserVpcRequest.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        r"""Sets the eip_id of this UserVpcRequest.

        **参数解释**：EIP ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param eip_id: The eip_id of this UserVpcRequest.
        :type eip_id: str
        """
        self._eip_id = eip_id

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
        if not isinstance(other, UserVpcRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
