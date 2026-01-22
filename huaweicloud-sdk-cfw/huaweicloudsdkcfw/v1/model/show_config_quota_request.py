# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigQuotaRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'config_type': 'str',
        'set_id': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'config_type': 'config_type',
        'set_id': 'set_id'
    }

    def __init__(self, fw_instance_id=None, config_type=None, set_id=None):
        r"""ShowConfigQuotaRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param config_type: **参数解释**： 防火墙配额类型 **约束限制**： 不涉及 **取值范围**：   ACL：ACL规则配额   DNS_DOMAIN_SET：网络域名组配额   DOMAIN：域名组域名成员配额   DOMAIN_DEVICE：域名设备配额   DNS_DOMAIN_SET_PARSE_IP：网络域名组解析IP配额   APPLICATION_DOMAIN_SET：应用域名组配额   APPLICATION_DOMAIN_SET_ITEM：应用域名组域名成员配额   APPLICATION_DOMAIN_SET_ITEM_DEVICE：应用域名组设备配额   ADDR_SET：地址组配额   ADDR_SET_ITEM：地址组IP地址成员配额   ADDR_SET_ITEM_DEVICE：地址组IP地址设备配额   SERV_SET：服务组配额   SERV_SET_ITEM：服务组服务成员配额   SERV_SET_ITEM_DEVICE：服务组服务设备配额   BLACKLIST：黑名单配额   WHITELIST：白名单配额   PRIVATE_NETWORK_SEGMENT：私网网段配额 **默认取值**： 不涉及
        :type config_type: str
        :param set_id: **参数解释**： 组Id，查询IP地址组地址成员配额，域名组域名成员配额，服务组服务成员配额时必传，地址组id，可通过查询地址组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得，域名组id，可通过查询域名组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得，服务组id，可通过获取服务组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type set_id: str
        """
        
        

        self._fw_instance_id = None
        self._config_type = None
        self._set_id = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        self.config_type = config_type
        if set_id is not None:
            self.set_id = set_id

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ShowConfigQuotaRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ShowConfigQuotaRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ShowConfigQuotaRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ShowConfigQuotaRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def config_type(self):
        r"""Gets the config_type of this ShowConfigQuotaRequest.

        **参数解释**： 防火墙配额类型 **约束限制**： 不涉及 **取值范围**：   ACL：ACL规则配额   DNS_DOMAIN_SET：网络域名组配额   DOMAIN：域名组域名成员配额   DOMAIN_DEVICE：域名设备配额   DNS_DOMAIN_SET_PARSE_IP：网络域名组解析IP配额   APPLICATION_DOMAIN_SET：应用域名组配额   APPLICATION_DOMAIN_SET_ITEM：应用域名组域名成员配额   APPLICATION_DOMAIN_SET_ITEM_DEVICE：应用域名组设备配额   ADDR_SET：地址组配额   ADDR_SET_ITEM：地址组IP地址成员配额   ADDR_SET_ITEM_DEVICE：地址组IP地址设备配额   SERV_SET：服务组配额   SERV_SET_ITEM：服务组服务成员配额   SERV_SET_ITEM_DEVICE：服务组服务设备配额   BLACKLIST：黑名单配额   WHITELIST：白名单配额   PRIVATE_NETWORK_SEGMENT：私网网段配额 **默认取值**： 不涉及

        :return: The config_type of this ShowConfigQuotaRequest.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        r"""Sets the config_type of this ShowConfigQuotaRequest.

        **参数解释**： 防火墙配额类型 **约束限制**： 不涉及 **取值范围**：   ACL：ACL规则配额   DNS_DOMAIN_SET：网络域名组配额   DOMAIN：域名组域名成员配额   DOMAIN_DEVICE：域名设备配额   DNS_DOMAIN_SET_PARSE_IP：网络域名组解析IP配额   APPLICATION_DOMAIN_SET：应用域名组配额   APPLICATION_DOMAIN_SET_ITEM：应用域名组域名成员配额   APPLICATION_DOMAIN_SET_ITEM_DEVICE：应用域名组设备配额   ADDR_SET：地址组配额   ADDR_SET_ITEM：地址组IP地址成员配额   ADDR_SET_ITEM_DEVICE：地址组IP地址设备配额   SERV_SET：服务组配额   SERV_SET_ITEM：服务组服务成员配额   SERV_SET_ITEM_DEVICE：服务组服务设备配额   BLACKLIST：黑名单配额   WHITELIST：白名单配额   PRIVATE_NETWORK_SEGMENT：私网网段配额 **默认取值**： 不涉及

        :param config_type: The config_type of this ShowConfigQuotaRequest.
        :type config_type: str
        """
        self._config_type = config_type

    @property
    def set_id(self):
        r"""Gets the set_id of this ShowConfigQuotaRequest.

        **参数解释**： 组Id，查询IP地址组地址成员配额，域名组域名成员配额，服务组服务成员配额时必传，地址组id，可通过查询地址组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得，域名组id，可通过查询域名组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得，服务组id，可通过获取服务组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The set_id of this ShowConfigQuotaRequest.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        r"""Sets the set_id of this ShowConfigQuotaRequest.

        **参数解释**： 组Id，查询IP地址组地址成员配额，域名组域名成员配额，服务组服务成员配额时必传，地址组id，可通过查询地址组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得，域名组id，可通过查询域名组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得，服务组id，可通过获取服务组列表接口查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param set_id: The set_id of this ShowConfigQuotaRequest.
        :type set_id: str
        """
        self._set_id = set_id

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
        if not isinstance(other, ShowConfigQuotaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
