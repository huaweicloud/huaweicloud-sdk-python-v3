# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowZoneNameServerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_hw_dns': 'bool',
        'include_hw_dns': 'bool',
        'dns_servers': 'list[str]',
        'expected_dns_servers': 'list[str]',
        'domain_name': 'str'
    }

    attribute_map = {
        'all_hw_dns': 'all_hw_dns',
        'include_hw_dns': 'include_hw_dns',
        'dns_servers': 'dns_servers',
        'expected_dns_servers': 'expected_dns_servers',
        'domain_name': 'domain_name'
    }

    def __init__(self, all_hw_dns=None, include_hw_dns=None, dns_servers=None, expected_dns_servers=None, domain_name=None):
        r"""ShowZoneNameServerResponse

        The model defined in huaweicloud sdk

        :param all_hw_dns: **参数解释：** 是否全部为华为云DNS服务器地址。 **取值范围：** 不涉及。
        :type all_hw_dns: bool
        :param include_hw_dns: **参数解释：** 是否包含华为云DNS服务器地址。  **取值范围：** 不涉及。
        :type include_hw_dns: bool
        :param dns_servers: **参数解释：** DNS服务器地址。 **取值范围：** 不涉及。
        :type dns_servers: list[str]
        :param expected_dns_servers: **参数解释：** 期望的DNS服务器地址。 **取值范围：** 不涉及。
        :type expected_dns_servers: list[str]
        :param domain_name: **参数解释：** 公网域名。 **取值范围：** 不涉及。
        :type domain_name: str
        """
        
        super().__init__()

        self._all_hw_dns = None
        self._include_hw_dns = None
        self._dns_servers = None
        self._expected_dns_servers = None
        self._domain_name = None
        self.discriminator = None

        if all_hw_dns is not None:
            self.all_hw_dns = all_hw_dns
        if include_hw_dns is not None:
            self.include_hw_dns = include_hw_dns
        if dns_servers is not None:
            self.dns_servers = dns_servers
        if expected_dns_servers is not None:
            self.expected_dns_servers = expected_dns_servers
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def all_hw_dns(self):
        r"""Gets the all_hw_dns of this ShowZoneNameServerResponse.

        **参数解释：** 是否全部为华为云DNS服务器地址。 **取值范围：** 不涉及。

        :return: The all_hw_dns of this ShowZoneNameServerResponse.
        :rtype: bool
        """
        return self._all_hw_dns

    @all_hw_dns.setter
    def all_hw_dns(self, all_hw_dns):
        r"""Sets the all_hw_dns of this ShowZoneNameServerResponse.

        **参数解释：** 是否全部为华为云DNS服务器地址。 **取值范围：** 不涉及。

        :param all_hw_dns: The all_hw_dns of this ShowZoneNameServerResponse.
        :type all_hw_dns: bool
        """
        self._all_hw_dns = all_hw_dns

    @property
    def include_hw_dns(self):
        r"""Gets the include_hw_dns of this ShowZoneNameServerResponse.

        **参数解释：** 是否包含华为云DNS服务器地址。  **取值范围：** 不涉及。

        :return: The include_hw_dns of this ShowZoneNameServerResponse.
        :rtype: bool
        """
        return self._include_hw_dns

    @include_hw_dns.setter
    def include_hw_dns(self, include_hw_dns):
        r"""Sets the include_hw_dns of this ShowZoneNameServerResponse.

        **参数解释：** 是否包含华为云DNS服务器地址。  **取值范围：** 不涉及。

        :param include_hw_dns: The include_hw_dns of this ShowZoneNameServerResponse.
        :type include_hw_dns: bool
        """
        self._include_hw_dns = include_hw_dns

    @property
    def dns_servers(self):
        r"""Gets the dns_servers of this ShowZoneNameServerResponse.

        **参数解释：** DNS服务器地址。 **取值范围：** 不涉及。

        :return: The dns_servers of this ShowZoneNameServerResponse.
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        r"""Sets the dns_servers of this ShowZoneNameServerResponse.

        **参数解释：** DNS服务器地址。 **取值范围：** 不涉及。

        :param dns_servers: The dns_servers of this ShowZoneNameServerResponse.
        :type dns_servers: list[str]
        """
        self._dns_servers = dns_servers

    @property
    def expected_dns_servers(self):
        r"""Gets the expected_dns_servers of this ShowZoneNameServerResponse.

        **参数解释：** 期望的DNS服务器地址。 **取值范围：** 不涉及。

        :return: The expected_dns_servers of this ShowZoneNameServerResponse.
        :rtype: list[str]
        """
        return self._expected_dns_servers

    @expected_dns_servers.setter
    def expected_dns_servers(self, expected_dns_servers):
        r"""Sets the expected_dns_servers of this ShowZoneNameServerResponse.

        **参数解释：** 期望的DNS服务器地址。 **取值范围：** 不涉及。

        :param expected_dns_servers: The expected_dns_servers of this ShowZoneNameServerResponse.
        :type expected_dns_servers: list[str]
        """
        self._expected_dns_servers = expected_dns_servers

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowZoneNameServerResponse.

        **参数解释：** 公网域名。 **取值范围：** 不涉及。

        :return: The domain_name of this ShowZoneNameServerResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowZoneNameServerResponse.

        **参数解释：** 公网域名。 **取值范围：** 不涉及。

        :param domain_name: The domain_name of this ShowZoneNameServerResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    def to_dict(self):
        import warnings
        warnings.warn("ShowZoneNameServerResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowZoneNameServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
