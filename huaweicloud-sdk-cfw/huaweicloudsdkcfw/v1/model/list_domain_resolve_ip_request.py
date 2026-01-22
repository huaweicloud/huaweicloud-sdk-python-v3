# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainResolveIpRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address_type': 'str',
        'domain_address_id': 'str',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'address_type': 'address_type',
        'domain_address_id': 'domain_address_id',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, address_type=None, domain_address_id=None, fw_instance_id=None):
        r"""ListDomainResolveIpRequest

        The model defined in huaweicloud sdk

        :param address_type: **参数解释**： 解析ip类型IPV4或IPV6 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type address_type: str
        :param domain_address_id: **参数解释**： 域名id **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type domain_address_id: str
        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        """
        
        

        self._address_type = None
        self._domain_address_id = None
        self._fw_instance_id = None
        self.discriminator = None

        if address_type is not None:
            self.address_type = address_type
        self.domain_address_id = domain_address_id
        self.fw_instance_id = fw_instance_id

    @property
    def address_type(self):
        r"""Gets the address_type of this ListDomainResolveIpRequest.

        **参数解释**： 解析ip类型IPV4或IPV6 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The address_type of this ListDomainResolveIpRequest.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this ListDomainResolveIpRequest.

        **参数解释**： 解析ip类型IPV4或IPV6 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param address_type: The address_type of this ListDomainResolveIpRequest.
        :type address_type: str
        """
        self._address_type = address_type

    @property
    def domain_address_id(self):
        r"""Gets the domain_address_id of this ListDomainResolveIpRequest.

        **参数解释**： 域名id **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The domain_address_id of this ListDomainResolveIpRequest.
        :rtype: str
        """
        return self._domain_address_id

    @domain_address_id.setter
    def domain_address_id(self, domain_address_id):
        r"""Sets the domain_address_id of this ListDomainResolveIpRequest.

        **参数解释**： 域名id **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param domain_address_id: The domain_address_id of this ListDomainResolveIpRequest.
        :type domain_address_id: str
        """
        self._domain_address_id = domain_address_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListDomainResolveIpRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ListDomainResolveIpRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListDomainResolveIpRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ListDomainResolveIpRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

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
        if not isinstance(other, ListDomainResolveIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
