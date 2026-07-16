# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserVpcResponse:

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
        'connect_cidrs': 'str',
        'port_id': 'list[str]',
        'port_ip': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_ids': 'security_group_ids',
        'connect_cidrs': 'connect_cidrs',
        'port_id': 'port_id',
        'port_ip': 'port_ip'
    }

    def __init__(self, vpc_id=None, subnet_id=None, security_group_ids=None, connect_cidrs=None, port_id=None, port_ip=None):
        r"""UserVpcResponse

        The model defined in huaweicloud sdk

        :param vpc_id: **参数解释**：虚拟私有网络（VPC）ID。 **取值范围**：不涉及。
        :type vpc_id: str
        :param subnet_id: **参数解释**：子网ID。 **取值范围**：不涉及。
        :type subnet_id: str
        :param security_group_ids: **参数解释**：安全组ID列表。 **取值范围**：不涉及。
        :type security_group_ids: list[str]
        :param connect_cidrs: **参数解释**：连接的CIDR地址列表。 **取值范围**：不涉及。
        :type connect_cidrs: str
        :param port_id: **参数解释**：网卡ID。 **取值范围**：不涉及。
        :type port_id: list[str]
        :param port_ip: **参数解释**：网卡ip。 **取值范围**：不涉及。
        :type port_ip: str
        """
        
        

        self._vpc_id = None
        self._subnet_id = None
        self._security_group_ids = None
        self._connect_cidrs = None
        self._port_id = None
        self._port_ip = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if connect_cidrs is not None:
            self.connect_cidrs = connect_cidrs
        if port_id is not None:
            self.port_id = port_id
        if port_ip is not None:
            self.port_ip = port_ip

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UserVpcResponse.

        **参数解释**：虚拟私有网络（VPC）ID。 **取值范围**：不涉及。

        :return: The vpc_id of this UserVpcResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UserVpcResponse.

        **参数解释**：虚拟私有网络（VPC）ID。 **取值范围**：不涉及。

        :param vpc_id: The vpc_id of this UserVpcResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this UserVpcResponse.

        **参数解释**：子网ID。 **取值范围**：不涉及。

        :return: The subnet_id of this UserVpcResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this UserVpcResponse.

        **参数解释**：子网ID。 **取值范围**：不涉及。

        :param subnet_id: The subnet_id of this UserVpcResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_ids(self):
        r"""Gets the security_group_ids of this UserVpcResponse.

        **参数解释**：安全组ID列表。 **取值范围**：不涉及。

        :return: The security_group_ids of this UserVpcResponse.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        r"""Sets the security_group_ids of this UserVpcResponse.

        **参数解释**：安全组ID列表。 **取值范围**：不涉及。

        :param security_group_ids: The security_group_ids of this UserVpcResponse.
        :type security_group_ids: list[str]
        """
        self._security_group_ids = security_group_ids

    @property
    def connect_cidrs(self):
        r"""Gets the connect_cidrs of this UserVpcResponse.

        **参数解释**：连接的CIDR地址列表。 **取值范围**：不涉及。

        :return: The connect_cidrs of this UserVpcResponse.
        :rtype: str
        """
        return self._connect_cidrs

    @connect_cidrs.setter
    def connect_cidrs(self, connect_cidrs):
        r"""Sets the connect_cidrs of this UserVpcResponse.

        **参数解释**：连接的CIDR地址列表。 **取值范围**：不涉及。

        :param connect_cidrs: The connect_cidrs of this UserVpcResponse.
        :type connect_cidrs: str
        """
        self._connect_cidrs = connect_cidrs

    @property
    def port_id(self):
        r"""Gets the port_id of this UserVpcResponse.

        **参数解释**：网卡ID。 **取值范围**：不涉及。

        :return: The port_id of this UserVpcResponse.
        :rtype: list[str]
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this UserVpcResponse.

        **参数解释**：网卡ID。 **取值范围**：不涉及。

        :param port_id: The port_id of this UserVpcResponse.
        :type port_id: list[str]
        """
        self._port_id = port_id

    @property
    def port_ip(self):
        r"""Gets the port_ip of this UserVpcResponse.

        **参数解释**：网卡ip。 **取值范围**：不涉及。

        :return: The port_ip of this UserVpcResponse.
        :rtype: str
        """
        return self._port_ip

    @port_ip.setter
    def port_ip(self, port_ip):
        r"""Sets the port_ip of this UserVpcResponse.

        **参数解释**：网卡ip。 **取值范围**：不涉及。

        :param port_ip: The port_ip of this UserVpcResponse.
        :type port_ip: str
        """
        self._port_ip = port_ip

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
        if not isinstance(other, UserVpcResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
