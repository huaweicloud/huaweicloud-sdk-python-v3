# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubnetExtraDhcpOpt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'opt_name': 'str',
        'opt_value': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'opt_name': 'opt_name',
        'opt_value': 'opt_value',
        'ip_version': 'ip_version'
    }

    def __init__(self, opt_name=None, opt_value=None, ip_version=None):
        r"""SubnetExtraDhcpOpt

        The model defined in huaweicloud sdk

        :param opt_name: **参数解释**： 子网配置的NTP地址、DNS域名或租约到期时间的名称。 **取值范围**： - 42：表示子网ntp地址。 - 15：表示DNS配置的域名，用于向DNS服务器获取IP地址。 - 51：表示IPv4子网租约到期时间。 - 651：表示IPv6子网租约到期时间。
        :type opt_name: str
        :param opt_value: **参数解释**： 子网配置的NTP地址、DNS域名或租约到期时间。 **取值范围**： - opt_name配置为“42”，则表示是子网ntp地址，目前只支持IPv4地址，每个IP地址以逗号隔开，IP地址个数不能超过4个，不能存在相同地址。 - opt_name配置为“15”，则该值表示是DNS配置的域名，用于向DNS服务器获取IP地址。域名只能由字母，数字，中划线组成，中划线不能在开头或末尾。域名可以包含多个字符串，单个字符串不超过63个字符，字符串间以点分隔。域名长度不超过254个字符。 - opt_name配置为“51”，则该值表示是IPv4子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~175200，比如5h，默认值为87600h。 - opt_name配置为“651”，则该值表示是IPv6子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~175200，比如5h，默认值为2h。
        :type opt_value: str
        :param ip_version: **参数解释**： 子网的IP版本。 **取值范围**： - 4：默认值，IPv4。 - 6：IPv6，只有opt_name是“651”时，ip_version为6。
        :type ip_version: int
        """
        
        

        self._opt_name = None
        self._opt_value = None
        self._ip_version = None
        self.discriminator = None

        self.opt_name = opt_name
        self.opt_value = opt_value
        self.ip_version = ip_version

    @property
    def opt_name(self):
        r"""Gets the opt_name of this SubnetExtraDhcpOpt.

        **参数解释**： 子网配置的NTP地址、DNS域名或租约到期时间的名称。 **取值范围**： - 42：表示子网ntp地址。 - 15：表示DNS配置的域名，用于向DNS服务器获取IP地址。 - 51：表示IPv4子网租约到期时间。 - 651：表示IPv6子网租约到期时间。

        :return: The opt_name of this SubnetExtraDhcpOpt.
        :rtype: str
        """
        return self._opt_name

    @opt_name.setter
    def opt_name(self, opt_name):
        r"""Sets the opt_name of this SubnetExtraDhcpOpt.

        **参数解释**： 子网配置的NTP地址、DNS域名或租约到期时间的名称。 **取值范围**： - 42：表示子网ntp地址。 - 15：表示DNS配置的域名，用于向DNS服务器获取IP地址。 - 51：表示IPv4子网租约到期时间。 - 651：表示IPv6子网租约到期时间。

        :param opt_name: The opt_name of this SubnetExtraDhcpOpt.
        :type opt_name: str
        """
        self._opt_name = opt_name

    @property
    def opt_value(self):
        r"""Gets the opt_value of this SubnetExtraDhcpOpt.

        **参数解释**： 子网配置的NTP地址、DNS域名或租约到期时间。 **取值范围**： - opt_name配置为“42”，则表示是子网ntp地址，目前只支持IPv4地址，每个IP地址以逗号隔开，IP地址个数不能超过4个，不能存在相同地址。 - opt_name配置为“15”，则该值表示是DNS配置的域名，用于向DNS服务器获取IP地址。域名只能由字母，数字，中划线组成，中划线不能在开头或末尾。域名可以包含多个字符串，单个字符串不超过63个字符，字符串间以点分隔。域名长度不超过254个字符。 - opt_name配置为“51”，则该值表示是IPv4子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~175200，比如5h，默认值为87600h。 - opt_name配置为“651”，则该值表示是IPv6子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~175200，比如5h，默认值为2h。

        :return: The opt_value of this SubnetExtraDhcpOpt.
        :rtype: str
        """
        return self._opt_value

    @opt_value.setter
    def opt_value(self, opt_value):
        r"""Sets the opt_value of this SubnetExtraDhcpOpt.

        **参数解释**： 子网配置的NTP地址、DNS域名或租约到期时间。 **取值范围**： - opt_name配置为“42”，则表示是子网ntp地址，目前只支持IPv4地址，每个IP地址以逗号隔开，IP地址个数不能超过4个，不能存在相同地址。 - opt_name配置为“15”，则该值表示是DNS配置的域名，用于向DNS服务器获取IP地址。域名只能由字母，数字，中划线组成，中划线不能在开头或末尾。域名可以包含多个字符串，单个字符串不超过63个字符，字符串间以点分隔。域名长度不超过254个字符。 - opt_name配置为“51”，则该值表示是IPv4子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~175200，比如5h，默认值为87600h。 - opt_name配置为“651”，则该值表示是IPv6子网租约到期时间，取值格式有两种，取-1，表示无限租约；数字+h，数字范围是1~175200，比如5h，默认值为2h。

        :param opt_value: The opt_value of this SubnetExtraDhcpOpt.
        :type opt_value: str
        """
        self._opt_value = opt_value

    @property
    def ip_version(self):
        r"""Gets the ip_version of this SubnetExtraDhcpOpt.

        **参数解释**： 子网的IP版本。 **取值范围**： - 4：默认值，IPv4。 - 6：IPv6，只有opt_name是“651”时，ip_version为6。

        :return: The ip_version of this SubnetExtraDhcpOpt.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this SubnetExtraDhcpOpt.

        **参数解释**： 子网的IP版本。 **取值范围**： - 4：默认值，IPv4。 - 6：IPv6，只有opt_name是“651”时，ip_version为6。

        :param ip_version: The ip_version of this SubnetExtraDhcpOpt.
        :type ip_version: int
        """
        self._ip_version = ip_version

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
        if not isinstance(other, SubnetExtraDhcpOpt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
