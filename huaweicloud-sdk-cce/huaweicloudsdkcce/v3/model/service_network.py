# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'i_pv4_cidr': 'str',
        'i_pv6_cidr': 'str'
    }

    attribute_map = {
        'i_pv4_cidr': 'IPv4CIDR',
        'i_pv6_cidr': 'IPv6CIDR'
    }

    def __init__(self, i_pv4_cidr=None, i_pv6_cidr=None):
        r"""ServiceNetwork

        The model defined in huaweicloud sdk

        :param i_pv4_cidr: **参数解释：** kubernetes clusterIP IPv4 CIDR取值范围。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 默认为\&quot;10.247.0.0/16\&quot;。 
        :type i_pv4_cidr: str
        :param i_pv6_cidr: **参数解释：** kubernetes clusterIP IPv6 CIDR取值范围。 **约束限制：** 仅开启IPV6双栈的Turbo集群支持配置IPv6服务网段。 **取值范围：** 不涉及 **默认取值：** Turbo集群默认为\&quot;fc00::/112\&quot; CCE集群默认为\&quot;fd00:1234::/120\&quot; 
        :type i_pv6_cidr: str
        """
        
        

        self._i_pv4_cidr = None
        self._i_pv6_cidr = None
        self.discriminator = None

        if i_pv4_cidr is not None:
            self.i_pv4_cidr = i_pv4_cidr
        if i_pv6_cidr is not None:
            self.i_pv6_cidr = i_pv6_cidr

    @property
    def i_pv4_cidr(self):
        r"""Gets the i_pv4_cidr of this ServiceNetwork.

        **参数解释：** kubernetes clusterIP IPv4 CIDR取值范围。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 默认为\"10.247.0.0/16\"。 

        :return: The i_pv4_cidr of this ServiceNetwork.
        :rtype: str
        """
        return self._i_pv4_cidr

    @i_pv4_cidr.setter
    def i_pv4_cidr(self, i_pv4_cidr):
        r"""Sets the i_pv4_cidr of this ServiceNetwork.

        **参数解释：** kubernetes clusterIP IPv4 CIDR取值范围。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 默认为\"10.247.0.0/16\"。 

        :param i_pv4_cidr: The i_pv4_cidr of this ServiceNetwork.
        :type i_pv4_cidr: str
        """
        self._i_pv4_cidr = i_pv4_cidr

    @property
    def i_pv6_cidr(self):
        r"""Gets the i_pv6_cidr of this ServiceNetwork.

        **参数解释：** kubernetes clusterIP IPv6 CIDR取值范围。 **约束限制：** 仅开启IPV6双栈的Turbo集群支持配置IPv6服务网段。 **取值范围：** 不涉及 **默认取值：** Turbo集群默认为\"fc00::/112\" CCE集群默认为\"fd00:1234::/120\" 

        :return: The i_pv6_cidr of this ServiceNetwork.
        :rtype: str
        """
        return self._i_pv6_cidr

    @i_pv6_cidr.setter
    def i_pv6_cidr(self, i_pv6_cidr):
        r"""Sets the i_pv6_cidr of this ServiceNetwork.

        **参数解释：** kubernetes clusterIP IPv6 CIDR取值范围。 **约束限制：** 仅开启IPV6双栈的Turbo集群支持配置IPv6服务网段。 **取值范围：** 不涉及 **默认取值：** Turbo集群默认为\"fc00::/112\" CCE集群默认为\"fd00:1234::/120\" 

        :param i_pv6_cidr: The i_pv6_cidr of this ServiceNetwork.
        :type i_pv6_cidr: str
        """
        self._i_pv6_cidr = i_pv6_cidr

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
        if not isinstance(other, ServiceNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
