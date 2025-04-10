# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnsAssignment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fqdn': 'str',
        'hostname': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'fqdn': 'fqdn',
        'hostname': 'hostname',
        'ip_address': 'ip_address'
    }

    def __init__(self, fqdn=None, hostname=None, ip_address=None):
        r"""DnsAssignment

        The model defined in huaweicloud sdk

        :param fqdn: 端口内网fqdn
        :type fqdn: str
        :param hostname: 端口hostname
        :type hostname: str
        :param ip_address: 端口IP地址
        :type ip_address: str
        """
        
        

        self._fqdn = None
        self._hostname = None
        self._ip_address = None
        self.discriminator = None

        if fqdn is not None:
            self.fqdn = fqdn
        if hostname is not None:
            self.hostname = hostname
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def fqdn(self):
        r"""Gets the fqdn of this DnsAssignment.

        端口内网fqdn

        :return: The fqdn of this DnsAssignment.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        r"""Sets the fqdn of this DnsAssignment.

        端口内网fqdn

        :param fqdn: The fqdn of this DnsAssignment.
        :type fqdn: str
        """
        self._fqdn = fqdn

    @property
    def hostname(self):
        r"""Gets the hostname of this DnsAssignment.

        端口hostname

        :return: The hostname of this DnsAssignment.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        r"""Sets the hostname of this DnsAssignment.

        端口hostname

        :param hostname: The hostname of this DnsAssignment.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def ip_address(self):
        r"""Gets the ip_address of this DnsAssignment.

        端口IP地址

        :return: The ip_address of this DnsAssignment.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this DnsAssignment.

        端口IP地址

        :param ip_address: The ip_address of this DnsAssignment.
        :type ip_address: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, DnsAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
