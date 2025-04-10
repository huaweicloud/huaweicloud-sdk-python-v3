# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainIpv6SwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'is_ipv6': 'bool'
    }

    attribute_map = {
        'domain': 'domain',
        'is_ipv6': 'is_ipv6'
    }

    def __init__(self, domain=None, is_ipv6=None):
        r"""DomainIpv6SwitchReq

        The model defined in huaweicloud sdk

        :param domain: 域名
        :type domain: str
        :param is_ipv6: IPV6开关配置，默认关闭，true为开启，false为关闭
        :type is_ipv6: bool
        """
        
        

        self._domain = None
        self._is_ipv6 = None
        self.discriminator = None

        self.domain = domain
        if is_ipv6 is not None:
            self.is_ipv6 = is_ipv6

    @property
    def domain(self):
        r"""Gets the domain of this DomainIpv6SwitchReq.

        域名

        :return: The domain of this DomainIpv6SwitchReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this DomainIpv6SwitchReq.

        域名

        :param domain: The domain of this DomainIpv6SwitchReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def is_ipv6(self):
        r"""Gets the is_ipv6 of this DomainIpv6SwitchReq.

        IPV6开关配置，默认关闭，true为开启，false为关闭

        :return: The is_ipv6 of this DomainIpv6SwitchReq.
        :rtype: bool
        """
        return self._is_ipv6

    @is_ipv6.setter
    def is_ipv6(self, is_ipv6):
        r"""Sets the is_ipv6 of this DomainIpv6SwitchReq.

        IPV6开关配置，默认关闭，true为开启，false为关闭

        :param is_ipv6: The is_ipv6 of this DomainIpv6SwitchReq.
        :type is_ipv6: bool
        """
        self._is_ipv6 = is_ipv6

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DomainIpv6SwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
