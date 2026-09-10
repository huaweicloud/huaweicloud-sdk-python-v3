# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachDevServerPortsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'name': 'str',
        'network_id': 'str',
        'ip_address': 'str',
        'security_groups': 'list[str]',
        'enable_efi': 'bool',
        'efi_protocol': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'name': 'name',
        'network_id': 'network_id',
        'ip_address': 'ip_address',
        'security_groups': 'security_groups',
        'enable_efi': 'enable_efi',
        'efi_protocol': 'efi_protocol'
    }

    def __init__(self, port_id=None, name=None, network_id=None, ip_address=None, security_groups=None, enable_efi=None, efi_protocol=None):
        r"""AttachDevServerPortsRequestBody

        The model defined in huaweicloud sdk

        :param port_id: **参数解释**：网卡ID，填该参数时，表明挂载已有网卡，其他参数不用填。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type port_id: str
        :param name: **参数解释**：网卡名称。 **约束限制**：不涉及。 **取值范围**：默认为空，最大长度不超过255。 **默认取值**：不涉及。
        :type name: str
        :param network_id: **参数解释**：端口子网ID。 **约束限制**：参数port_id未填时，需要新建网卡进行挂载，此时network_id为必填项。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。
        :type network_id: str
        :param ip_address: **参数解释**：端口IP地址。 **约束限制**：不支持更新。 **取值范围**：所属网络网段。 **默认取值**：不涉及。
        :type ip_address: str
        :param security_groups: **参数解释**：关联安全组ID列表。 **约束限制**：一个端口默认最多吃吃100个安全组。 **默认取值**：不涉及。
        :type security_groups: list[str]
        :param enable_efi: **参数解释**：是否使能efi。 **约束限制**：不涉及。 **取值范围**： - true：启用efi - false：不启用efi  **默认取值**：不涉及。
        :type enable_efi: bool
        :param efi_protocol: **参数解释**：efi 协议。 **约束限制**：不涉及。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。
        :type efi_protocol: str
        """
        
        

        self._port_id = None
        self._name = None
        self._network_id = None
        self._ip_address = None
        self._security_groups = None
        self._enable_efi = None
        self._efi_protocol = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if name is not None:
            self.name = name
        if network_id is not None:
            self.network_id = network_id
        if ip_address is not None:
            self.ip_address = ip_address
        if security_groups is not None:
            self.security_groups = security_groups
        if enable_efi is not None:
            self.enable_efi = enable_efi
        if efi_protocol is not None:
            self.efi_protocol = efi_protocol

    @property
    def port_id(self):
        r"""Gets the port_id of this AttachDevServerPortsRequestBody.

        **参数解释**：网卡ID，填该参数时，表明挂载已有网卡，其他参数不用填。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The port_id of this AttachDevServerPortsRequestBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this AttachDevServerPortsRequestBody.

        **参数解释**：网卡ID，填该参数时，表明挂载已有网卡，其他参数不用填。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param port_id: The port_id of this AttachDevServerPortsRequestBody.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def name(self):
        r"""Gets the name of this AttachDevServerPortsRequestBody.

        **参数解释**：网卡名称。 **约束限制**：不涉及。 **取值范围**：默认为空，最大长度不超过255。 **默认取值**：不涉及。

        :return: The name of this AttachDevServerPortsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AttachDevServerPortsRequestBody.

        **参数解释**：网卡名称。 **约束限制**：不涉及。 **取值范围**：默认为空，最大长度不超过255。 **默认取值**：不涉及。

        :param name: The name of this AttachDevServerPortsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def network_id(self):
        r"""Gets the network_id of this AttachDevServerPortsRequestBody.

        **参数解释**：端口子网ID。 **约束限制**：参数port_id未填时，需要新建网卡进行挂载，此时network_id为必填项。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :return: The network_id of this AttachDevServerPortsRequestBody.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        r"""Sets the network_id of this AttachDevServerPortsRequestBody.

        **参数解释**：端口子网ID。 **约束限制**：参数port_id未填时，需要新建网卡进行挂载，此时network_id为必填项。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :param network_id: The network_id of this AttachDevServerPortsRequestBody.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this AttachDevServerPortsRequestBody.

        **参数解释**：端口IP地址。 **约束限制**：不支持更新。 **取值范围**：所属网络网段。 **默认取值**：不涉及。

        :return: The ip_address of this AttachDevServerPortsRequestBody.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this AttachDevServerPortsRequestBody.

        **参数解释**：端口IP地址。 **约束限制**：不支持更新。 **取值范围**：所属网络网段。 **默认取值**：不涉及。

        :param ip_address: The ip_address of this AttachDevServerPortsRequestBody.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def security_groups(self):
        r"""Gets the security_groups of this AttachDevServerPortsRequestBody.

        **参数解释**：关联安全组ID列表。 **约束限制**：一个端口默认最多吃吃100个安全组。 **默认取值**：不涉及。

        :return: The security_groups of this AttachDevServerPortsRequestBody.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this AttachDevServerPortsRequestBody.

        **参数解释**：关联安全组ID列表。 **约束限制**：一个端口默认最多吃吃100个安全组。 **默认取值**：不涉及。

        :param security_groups: The security_groups of this AttachDevServerPortsRequestBody.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def enable_efi(self):
        r"""Gets the enable_efi of this AttachDevServerPortsRequestBody.

        **参数解释**：是否使能efi。 **约束限制**：不涉及。 **取值范围**： - true：启用efi - false：不启用efi  **默认取值**：不涉及。

        :return: The enable_efi of this AttachDevServerPortsRequestBody.
        :rtype: bool
        """
        return self._enable_efi

    @enable_efi.setter
    def enable_efi(self, enable_efi):
        r"""Sets the enable_efi of this AttachDevServerPortsRequestBody.

        **参数解释**：是否使能efi。 **约束限制**：不涉及。 **取值范围**： - true：启用efi - false：不启用efi  **默认取值**：不涉及。

        :param enable_efi: The enable_efi of this AttachDevServerPortsRequestBody.
        :type enable_efi: bool
        """
        self._enable_efi = enable_efi

    @property
    def efi_protocol(self):
        r"""Gets the efi_protocol of this AttachDevServerPortsRequestBody.

        **参数解释**：efi 协议。 **约束限制**：不涉及。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。

        :return: The efi_protocol of this AttachDevServerPortsRequestBody.
        :rtype: str
        """
        return self._efi_protocol

    @efi_protocol.setter
    def efi_protocol(self, efi_protocol):
        r"""Sets the efi_protocol of this AttachDevServerPortsRequestBody.

        **参数解释**：efi 协议。 **约束限制**：不涉及。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。

        :param efi_protocol: The efi_protocol of this AttachDevServerPortsRequestBody.
        :type efi_protocol: str
        """
        self._efi_protocol = efi_protocol

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
        if not isinstance(other, AttachDevServerPortsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
