# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsWhiteListVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_address': 'str',
        'dest_address': 'str',
        'name': 'str',
        'list_id': 'str',
        'effective_scopes': 'list[str]',
        'ips_id': 'str',
        'ip_version': 'int',
        'description': 'str'
    }

    attribute_map = {
        'source_address': 'source_address',
        'dest_address': 'dest_address',
        'name': 'name',
        'list_id': 'list_id',
        'effective_scopes': 'effective_scopes',
        'ips_id': 'ips_id',
        'ip_version': 'ip_version',
        'description': 'description'
    }

    def __init__(self, source_address=None, dest_address=None, name=None, list_id=None, effective_scopes=None, ips_id=None, ip_version=None, description=None):
        r"""IpsWhiteListVO

        The model defined in huaweicloud sdk

        :param source_address: **参数解释**： 白名单源地址 **取值范围**： 不涉及
        :type source_address: str
        :param dest_address: **参数解释**：  目的地址  **取值范围**：  不涉及
        :type dest_address: str
        :param name: **参数解释**：  白名单名称  **取值范围**： 不涉及
        :type name: str
        :param list_id: **参数解释**：  IPS白名单ID  **取值范围**： 不涉及
        :type list_id: str
        :param effective_scopes: **参数解释**：  生效范围：NAT EIP VPC HCS场景中还有VGW信息  **取值范围**： 不涉及
        :type effective_scopes: list[str]
        :param ips_id: **参数解释**：  生效范围：IPS规则ID，all代表所有IPS **取值范围**： 不涉及
        :type ips_id: str
        :param ip_version: **参数解释**：  IP类型 **取值范围**：  4：表示IP类型为IPv4 6：表示IP类型为IPv6
        :type ip_version: int
        :param description: **参数解释**：  白名单描述 **取值范围**： 不涉及
        :type description: str
        """
        
        

        self._source_address = None
        self._dest_address = None
        self._name = None
        self._list_id = None
        self._effective_scopes = None
        self._ips_id = None
        self._ip_version = None
        self._description = None
        self.discriminator = None

        if source_address is not None:
            self.source_address = source_address
        if dest_address is not None:
            self.dest_address = dest_address
        if name is not None:
            self.name = name
        if list_id is not None:
            self.list_id = list_id
        if effective_scopes is not None:
            self.effective_scopes = effective_scopes
        if ips_id is not None:
            self.ips_id = ips_id
        if ip_version is not None:
            self.ip_version = ip_version
        if description is not None:
            self.description = description

    @property
    def source_address(self):
        r"""Gets the source_address of this IpsWhiteListVO.

        **参数解释**： 白名单源地址 **取值范围**： 不涉及

        :return: The source_address of this IpsWhiteListVO.
        :rtype: str
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        r"""Sets the source_address of this IpsWhiteListVO.

        **参数解释**： 白名单源地址 **取值范围**： 不涉及

        :param source_address: The source_address of this IpsWhiteListVO.
        :type source_address: str
        """
        self._source_address = source_address

    @property
    def dest_address(self):
        r"""Gets the dest_address of this IpsWhiteListVO.

        **参数解释**：  目的地址  **取值范围**：  不涉及

        :return: The dest_address of this IpsWhiteListVO.
        :rtype: str
        """
        return self._dest_address

    @dest_address.setter
    def dest_address(self, dest_address):
        r"""Sets the dest_address of this IpsWhiteListVO.

        **参数解释**：  目的地址  **取值范围**：  不涉及

        :param dest_address: The dest_address of this IpsWhiteListVO.
        :type dest_address: str
        """
        self._dest_address = dest_address

    @property
    def name(self):
        r"""Gets the name of this IpsWhiteListVO.

        **参数解释**：  白名单名称  **取值范围**： 不涉及

        :return: The name of this IpsWhiteListVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IpsWhiteListVO.

        **参数解释**：  白名单名称  **取值范围**： 不涉及

        :param name: The name of this IpsWhiteListVO.
        :type name: str
        """
        self._name = name

    @property
    def list_id(self):
        r"""Gets the list_id of this IpsWhiteListVO.

        **参数解释**：  IPS白名单ID  **取值范围**： 不涉及

        :return: The list_id of this IpsWhiteListVO.
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        r"""Sets the list_id of this IpsWhiteListVO.

        **参数解释**：  IPS白名单ID  **取值范围**： 不涉及

        :param list_id: The list_id of this IpsWhiteListVO.
        :type list_id: str
        """
        self._list_id = list_id

    @property
    def effective_scopes(self):
        r"""Gets the effective_scopes of this IpsWhiteListVO.

        **参数解释**：  生效范围：NAT EIP VPC HCS场景中还有VGW信息  **取值范围**： 不涉及

        :return: The effective_scopes of this IpsWhiteListVO.
        :rtype: list[str]
        """
        return self._effective_scopes

    @effective_scopes.setter
    def effective_scopes(self, effective_scopes):
        r"""Sets the effective_scopes of this IpsWhiteListVO.

        **参数解释**：  生效范围：NAT EIP VPC HCS场景中还有VGW信息  **取值范围**： 不涉及

        :param effective_scopes: The effective_scopes of this IpsWhiteListVO.
        :type effective_scopes: list[str]
        """
        self._effective_scopes = effective_scopes

    @property
    def ips_id(self):
        r"""Gets the ips_id of this IpsWhiteListVO.

        **参数解释**：  生效范围：IPS规则ID，all代表所有IPS **取值范围**： 不涉及

        :return: The ips_id of this IpsWhiteListVO.
        :rtype: str
        """
        return self._ips_id

    @ips_id.setter
    def ips_id(self, ips_id):
        r"""Sets the ips_id of this IpsWhiteListVO.

        **参数解释**：  生效范围：IPS规则ID，all代表所有IPS **取值范围**： 不涉及

        :param ips_id: The ips_id of this IpsWhiteListVO.
        :type ips_id: str
        """
        self._ips_id = ips_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this IpsWhiteListVO.

        **参数解释**：  IP类型 **取值范围**：  4：表示IP类型为IPv4 6：表示IP类型为IPv6

        :return: The ip_version of this IpsWhiteListVO.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this IpsWhiteListVO.

        **参数解释**：  IP类型 **取值范围**：  4：表示IP类型为IPv4 6：表示IP类型为IPv6

        :param ip_version: The ip_version of this IpsWhiteListVO.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def description(self):
        r"""Gets the description of this IpsWhiteListVO.

        **参数解释**：  白名单描述 **取值范围**： 不涉及

        :return: The description of this IpsWhiteListVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IpsWhiteListVO.

        **参数解释**：  白名单描述 **取值范围**： 不涉及

        :param description: The description of this IpsWhiteListVO.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, IpsWhiteListVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
