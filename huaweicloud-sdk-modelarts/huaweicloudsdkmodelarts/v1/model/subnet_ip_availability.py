# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubnetIpAvailability:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidr': 'str',
        'ip_version': 'int',
        'used_ips': 'int',
        'total_ips': 'int'
    }

    attribute_map = {
        'cidr': 'cidr',
        'ip_version': 'ipVersion',
        'used_ips': 'usedIps',
        'total_ips': 'totalIps'
    }

    def __init__(self, cidr=None, ip_version=None, used_ips=None, total_ips=None):
        r"""SubnetIpAvailability

        The model defined in huaweicloud sdk

        :param cidr: **参数解释**：子网的cidr。 **取值范围**：不涉及。
        :type cidr: str
        :param ip_version: **参数解释**：网络版本。 **取值范围**：可选值如下： - 4：代表ipV4
        :type ip_version: int
        :param used_ips: **参数解释**：已使用的IP数量。 **取值范围**：不涉及。
        :type used_ips: int
        :param total_ips: **参数解释**：子网中总的IP数量。 **取值范围**：不涉及。
        :type total_ips: int
        """
        
        

        self._cidr = None
        self._ip_version = None
        self._used_ips = None
        self._total_ips = None
        self.discriminator = None

        self.cidr = cidr
        self.ip_version = ip_version
        self.used_ips = used_ips
        if total_ips is not None:
            self.total_ips = total_ips

    @property
    def cidr(self):
        r"""Gets the cidr of this SubnetIpAvailability.

        **参数解释**：子网的cidr。 **取值范围**：不涉及。

        :return: The cidr of this SubnetIpAvailability.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this SubnetIpAvailability.

        **参数解释**：子网的cidr。 **取值范围**：不涉及。

        :param cidr: The cidr of this SubnetIpAvailability.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def ip_version(self):
        r"""Gets the ip_version of this SubnetIpAvailability.

        **参数解释**：网络版本。 **取值范围**：可选值如下： - 4：代表ipV4

        :return: The ip_version of this SubnetIpAvailability.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this SubnetIpAvailability.

        **参数解释**：网络版本。 **取值范围**：可选值如下： - 4：代表ipV4

        :param ip_version: The ip_version of this SubnetIpAvailability.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def used_ips(self):
        r"""Gets the used_ips of this SubnetIpAvailability.

        **参数解释**：已使用的IP数量。 **取值范围**：不涉及。

        :return: The used_ips of this SubnetIpAvailability.
        :rtype: int
        """
        return self._used_ips

    @used_ips.setter
    def used_ips(self, used_ips):
        r"""Sets the used_ips of this SubnetIpAvailability.

        **参数解释**：已使用的IP数量。 **取值范围**：不涉及。

        :param used_ips: The used_ips of this SubnetIpAvailability.
        :type used_ips: int
        """
        self._used_ips = used_ips

    @property
    def total_ips(self):
        r"""Gets the total_ips of this SubnetIpAvailability.

        **参数解释**：子网中总的IP数量。 **取值范围**：不涉及。

        :return: The total_ips of this SubnetIpAvailability.
        :rtype: int
        """
        return self._total_ips

    @total_ips.setter
    def total_ips(self, total_ips):
        r"""Sets the total_ips of this SubnetIpAvailability.

        **参数解释**：子网中总的IP数量。 **取值范围**：不涉及。

        :param total_ips: The total_ips of this SubnetIpAvailability.
        :type total_ips: int
        """
        self._total_ips = total_ips

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
        if not isinstance(other, SubnetIpAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
