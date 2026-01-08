# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnsIpResponse:

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
        'enable': 'bool',
        'ip_address': 'str',
        'type': 'str',
        'domain_name': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'enable': 'enable',
        'ip_address': 'ip_address',
        'type': 'type',
        'domain_name': 'domain_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, enable=None, ip_address=None, type=None, domain_name=None, created_at=None, updated_at=None):
        r"""DnsIpResponse

        The model defined in huaweicloud sdk

        :param id: dns ip信息的ID。
        :type id: str
        :param enable: **参数解释**：ip是否加入了域名解析。  **取值范围**： true：已加入域名解析。 false：未加入域名解析。
        :type enable: bool
        :param ip_address: **参数解释**：ip地址。可以是ipv4地址也可以是ipv6地址。  **约束限制**：必须是负载均衡器的私网地址或者公网地址。
        :type ip_address: str
        :param type: **参数解释**：地址类型。  **取值范围**： vip：私网ip。 eip：公网ip。
        :type type: str
        :param domain_name: **参数解释**：ip对应的域名。  **约束限制**： - 如果ip为私网类型，则这里为负载均衡实例的私网域名 - 如果ip为公网类型，则这里为负载均衡实例的公网域名
        :type domain_name: str
        :param created_at: 创建时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。
        :type created_at: str
        :param updated_at: 更新时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。
        :type updated_at: str
        """
        
        

        self._id = None
        self._enable = None
        self._ip_address = None
        self._type = None
        self._domain_name = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if enable is not None:
            self.enable = enable
        if ip_address is not None:
            self.ip_address = ip_address
        if type is not None:
            self.type = type
        if domain_name is not None:
            self.domain_name = domain_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this DnsIpResponse.

        dns ip信息的ID。

        :return: The id of this DnsIpResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DnsIpResponse.

        dns ip信息的ID。

        :param id: The id of this DnsIpResponse.
        :type id: str
        """
        self._id = id

    @property
    def enable(self):
        r"""Gets the enable of this DnsIpResponse.

        **参数解释**：ip是否加入了域名解析。  **取值范围**： true：已加入域名解析。 false：未加入域名解析。

        :return: The enable of this DnsIpResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this DnsIpResponse.

        **参数解释**：ip是否加入了域名解析。  **取值范围**： true：已加入域名解析。 false：未加入域名解析。

        :param enable: The enable of this DnsIpResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def ip_address(self):
        r"""Gets the ip_address of this DnsIpResponse.

        **参数解释**：ip地址。可以是ipv4地址也可以是ipv6地址。  **约束限制**：必须是负载均衡器的私网地址或者公网地址。

        :return: The ip_address of this DnsIpResponse.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this DnsIpResponse.

        **参数解释**：ip地址。可以是ipv4地址也可以是ipv6地址。  **约束限制**：必须是负载均衡器的私网地址或者公网地址。

        :param ip_address: The ip_address of this DnsIpResponse.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def type(self):
        r"""Gets the type of this DnsIpResponse.

        **参数解释**：地址类型。  **取值范围**： vip：私网ip。 eip：公网ip。

        :return: The type of this DnsIpResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DnsIpResponse.

        **参数解释**：地址类型。  **取值范围**： vip：私网ip。 eip：公网ip。

        :param type: The type of this DnsIpResponse.
        :type type: str
        """
        self._type = type

    @property
    def domain_name(self):
        r"""Gets the domain_name of this DnsIpResponse.

        **参数解释**：ip对应的域名。  **约束限制**： - 如果ip为私网类型，则这里为负载均衡实例的私网域名 - 如果ip为公网类型，则这里为负载均衡实例的公网域名

        :return: The domain_name of this DnsIpResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this DnsIpResponse.

        **参数解释**：ip对应的域名。  **约束限制**： - 如果ip为私网类型，则这里为负载均衡实例的私网域名 - 如果ip为公网类型，则这里为负载均衡实例的公网域名

        :param domain_name: The domain_name of this DnsIpResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def created_at(self):
        r"""Gets the created_at of this DnsIpResponse.

        创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :return: The created_at of this DnsIpResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DnsIpResponse.

        创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :param created_at: The created_at of this DnsIpResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DnsIpResponse.

        更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :return: The updated_at of this DnsIpResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DnsIpResponse.

        更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。

        :param updated_at: The updated_at of this DnsIpResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, DnsIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
