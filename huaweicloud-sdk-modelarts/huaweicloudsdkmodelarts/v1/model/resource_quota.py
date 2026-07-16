# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceQuota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'quota': 'str',
        'used': 'str'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, type=None, quota=None, used=None):
        r"""ResourceQuota

        The model defined in huaweicloud sdk

        :param type: **参数解释**：资源类型 **取值范围**：可选值如下： -  VPC：虚拟私有云。 -  SUBNET：子网。 -  SECURITY_GROUP：安全组。 -  SECURITY_GROUP_RULE：安全组规则。 -  PUBLIC_IP：公网IP。 -  VPC_PEER：VPC对端链接个数。 -  FIREWALL：防火墙。 -  SHARE_BANDWIDTH：共享带宽。 -  SHARE_BANDWIDTH_IP：共享带宽IP。 -  LOADBALANCER：负载均衡。 -  LISTENER：监听器。 -  PHYSICAL_CONNECT：物理连接。 -  VIRTUAL_INTERFACE：虚拟接口。 -  VPC_CONTAIN_ROUTETABLE：VPC包含的路由表。 -  ROUTETABLE_CONTAIN_ROUTES：路由表包含的路由。
        :type type: str
        :param quota: **参数解释**： 资源配额上限。 **取值范围**： 不涉及。
        :type quota: str
        :param used: **参数解释**： 已使用配额。 **取值范围**： 不涉及。
        :type used: str
        """
        
        

        self._type = None
        self._quota = None
        self._used = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if quota is not None:
            self.quota = quota
        if used is not None:
            self.used = used

    @property
    def type(self):
        r"""Gets the type of this ResourceQuota.

        **参数解释**：资源类型 **取值范围**：可选值如下： -  VPC：虚拟私有云。 -  SUBNET：子网。 -  SECURITY_GROUP：安全组。 -  SECURITY_GROUP_RULE：安全组规则。 -  PUBLIC_IP：公网IP。 -  VPC_PEER：VPC对端链接个数。 -  FIREWALL：防火墙。 -  SHARE_BANDWIDTH：共享带宽。 -  SHARE_BANDWIDTH_IP：共享带宽IP。 -  LOADBALANCER：负载均衡。 -  LISTENER：监听器。 -  PHYSICAL_CONNECT：物理连接。 -  VIRTUAL_INTERFACE：虚拟接口。 -  VPC_CONTAIN_ROUTETABLE：VPC包含的路由表。 -  ROUTETABLE_CONTAIN_ROUTES：路由表包含的路由。

        :return: The type of this ResourceQuota.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceQuota.

        **参数解释**：资源类型 **取值范围**：可选值如下： -  VPC：虚拟私有云。 -  SUBNET：子网。 -  SECURITY_GROUP：安全组。 -  SECURITY_GROUP_RULE：安全组规则。 -  PUBLIC_IP：公网IP。 -  VPC_PEER：VPC对端链接个数。 -  FIREWALL：防火墙。 -  SHARE_BANDWIDTH：共享带宽。 -  SHARE_BANDWIDTH_IP：共享带宽IP。 -  LOADBALANCER：负载均衡。 -  LISTENER：监听器。 -  PHYSICAL_CONNECT：物理连接。 -  VIRTUAL_INTERFACE：虚拟接口。 -  VPC_CONTAIN_ROUTETABLE：VPC包含的路由表。 -  ROUTETABLE_CONTAIN_ROUTES：路由表包含的路由。

        :param type: The type of this ResourceQuota.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        r"""Gets the quota of this ResourceQuota.

        **参数解释**： 资源配额上限。 **取值范围**： 不涉及。

        :return: The quota of this ResourceQuota.
        :rtype: str
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ResourceQuota.

        **参数解释**： 资源配额上限。 **取值范围**： 不涉及。

        :param quota: The quota of this ResourceQuota.
        :type quota: str
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this ResourceQuota.

        **参数解释**： 已使用配额。 **取值范围**： 不涉及。

        :return: The used of this ResourceQuota.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this ResourceQuota.

        **参数解释**： 已使用配额。 **取值范围**： 不涉及。

        :param used: The used of this ResourceQuota.
        :type used: str
        """
        self._used = used

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
        if not isinstance(other, ResourceQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
