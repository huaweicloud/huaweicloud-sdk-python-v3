# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SystemDefaultDnsConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_dns_record_set_ttl': 'int',
        'private_domain_name_enable': 'bool',
        'public_domain_name_enable': 'bool',
        'private_dns_record_set_ttl': 'int'
    }

    attribute_map = {
        'public_dns_record_set_ttl': 'public_dns_record_set_ttl',
        'private_domain_name_enable': 'private_domain_name_enable',
        'public_domain_name_enable': 'public_domain_name_enable',
        'private_dns_record_set_ttl': 'private_dns_record_set_ttl'
    }

    def __init__(self, public_dns_record_set_ttl=None, private_domain_name_enable=None, public_domain_name_enable=None, private_dns_record_set_ttl=None):
        r"""SystemDefaultDnsConfigRequestBody

        The model defined in huaweicloud sdk

        :param public_dns_record_set_ttl: **参数解释**：公网解析记录集超时时间。解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些  **约束限制**：不涉及  **取值范围**：1-2147483647  **默认取值**：300
        :type public_dns_record_set_ttl: int
        :param private_domain_name_enable: **参数解释**：是否配置私网域名。  **约束限制**：不涉及  **取值范围**： true：开启私网域名 false：关闭私网域名  **默认取值**：false
        :type private_domain_name_enable: bool
        :param public_domain_name_enable: **参数解释**：是否配置公网域名。  **约束限制**：不涉及  **取值范围**： true：开启公网域名 false：关闭公网域名  **默认取值**：false
        :type public_domain_name_enable: bool
        :param private_dns_record_set_ttl: **参数解释**：私网解析记录集超时时间。解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。  **约束限制**：不涉及  **取值范围**：1-2147483647  **默认取值**：300
        :type private_dns_record_set_ttl: int
        """
        
        

        self._public_dns_record_set_ttl = None
        self._private_domain_name_enable = None
        self._public_domain_name_enable = None
        self._private_dns_record_set_ttl = None
        self.discriminator = None

        if public_dns_record_set_ttl is not None:
            self.public_dns_record_set_ttl = public_dns_record_set_ttl
        if private_domain_name_enable is not None:
            self.private_domain_name_enable = private_domain_name_enable
        if public_domain_name_enable is not None:
            self.public_domain_name_enable = public_domain_name_enable
        if private_dns_record_set_ttl is not None:
            self.private_dns_record_set_ttl = private_dns_record_set_ttl

    @property
    def public_dns_record_set_ttl(self):
        r"""Gets the public_dns_record_set_ttl of this SystemDefaultDnsConfigRequestBody.

        **参数解释**：公网解析记录集超时时间。解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些  **约束限制**：不涉及  **取值范围**：1-2147483647  **默认取值**：300

        :return: The public_dns_record_set_ttl of this SystemDefaultDnsConfigRequestBody.
        :rtype: int
        """
        return self._public_dns_record_set_ttl

    @public_dns_record_set_ttl.setter
    def public_dns_record_set_ttl(self, public_dns_record_set_ttl):
        r"""Sets the public_dns_record_set_ttl of this SystemDefaultDnsConfigRequestBody.

        **参数解释**：公网解析记录集超时时间。解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些  **约束限制**：不涉及  **取值范围**：1-2147483647  **默认取值**：300

        :param public_dns_record_set_ttl: The public_dns_record_set_ttl of this SystemDefaultDnsConfigRequestBody.
        :type public_dns_record_set_ttl: int
        """
        self._public_dns_record_set_ttl = public_dns_record_set_ttl

    @property
    def private_domain_name_enable(self):
        r"""Gets the private_domain_name_enable of this SystemDefaultDnsConfigRequestBody.

        **参数解释**：是否配置私网域名。  **约束限制**：不涉及  **取值范围**： true：开启私网域名 false：关闭私网域名  **默认取值**：false

        :return: The private_domain_name_enable of this SystemDefaultDnsConfigRequestBody.
        :rtype: bool
        """
        return self._private_domain_name_enable

    @private_domain_name_enable.setter
    def private_domain_name_enable(self, private_domain_name_enable):
        r"""Sets the private_domain_name_enable of this SystemDefaultDnsConfigRequestBody.

        **参数解释**：是否配置私网域名。  **约束限制**：不涉及  **取值范围**： true：开启私网域名 false：关闭私网域名  **默认取值**：false

        :param private_domain_name_enable: The private_domain_name_enable of this SystemDefaultDnsConfigRequestBody.
        :type private_domain_name_enable: bool
        """
        self._private_domain_name_enable = private_domain_name_enable

    @property
    def public_domain_name_enable(self):
        r"""Gets the public_domain_name_enable of this SystemDefaultDnsConfigRequestBody.

        **参数解释**：是否配置公网域名。  **约束限制**：不涉及  **取值范围**： true：开启公网域名 false：关闭公网域名  **默认取值**：false

        :return: The public_domain_name_enable of this SystemDefaultDnsConfigRequestBody.
        :rtype: bool
        """
        return self._public_domain_name_enable

    @public_domain_name_enable.setter
    def public_domain_name_enable(self, public_domain_name_enable):
        r"""Sets the public_domain_name_enable of this SystemDefaultDnsConfigRequestBody.

        **参数解释**：是否配置公网域名。  **约束限制**：不涉及  **取值范围**： true：开启公网域名 false：关闭公网域名  **默认取值**：false

        :param public_domain_name_enable: The public_domain_name_enable of this SystemDefaultDnsConfigRequestBody.
        :type public_domain_name_enable: bool
        """
        self._public_domain_name_enable = public_domain_name_enable

    @property
    def private_dns_record_set_ttl(self):
        r"""Gets the private_dns_record_set_ttl of this SystemDefaultDnsConfigRequestBody.

        **参数解释**：私网解析记录集超时时间。解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。  **约束限制**：不涉及  **取值范围**：1-2147483647  **默认取值**：300

        :return: The private_dns_record_set_ttl of this SystemDefaultDnsConfigRequestBody.
        :rtype: int
        """
        return self._private_dns_record_set_ttl

    @private_dns_record_set_ttl.setter
    def private_dns_record_set_ttl(self, private_dns_record_set_ttl):
        r"""Sets the private_dns_record_set_ttl of this SystemDefaultDnsConfigRequestBody.

        **参数解释**：私网解析记录集超时时间。解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。如果您的服务地址经常更换，建议TTL值设置相对小些，反之，建议设置相对大些。  **约束限制**：不涉及  **取值范围**：1-2147483647  **默认取值**：300

        :param private_dns_record_set_ttl: The private_dns_record_set_ttl of this SystemDefaultDnsConfigRequestBody.
        :type private_dns_record_set_ttl: int
        """
        self._private_dns_record_set_ttl = private_dns_record_set_ttl

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
        if not isinstance(other, SystemDefaultDnsConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
