# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreSpaceNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'ip': 'ip'
    }

    def __init__(self, domain_name=None, ip=None):
        r"""CoreSpaceNetwork

        The model defined in huaweicloud sdk

        :param domain_name: **参数解释：** 访问域名。 **取值范围：** 不涉及。 
        :type domain_name: str
        :param ip: **参数解释：** IP 地址。 **取值范围：** 不涉及。 
        :type ip: str
        """
        
        

        self._domain_name = None
        self._ip = None
        self.discriminator = None

        self.domain_name = domain_name
        self.ip = ip

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CoreSpaceNetwork.

        **参数解释：** 访问域名。 **取值范围：** 不涉及。 

        :return: The domain_name of this CoreSpaceNetwork.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CoreSpaceNetwork.

        **参数解释：** 访问域名。 **取值范围：** 不涉及。 

        :param domain_name: The domain_name of this CoreSpaceNetwork.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def ip(self):
        r"""Gets the ip of this CoreSpaceNetwork.

        **参数解释：** IP 地址。 **取值范围：** 不涉及。 

        :return: The ip of this CoreSpaceNetwork.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this CoreSpaceNetwork.

        **参数解释：** IP 地址。 **取值范围：** 不涉及。 

        :param ip: The ip of this CoreSpaceNetwork.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, CoreSpaceNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
