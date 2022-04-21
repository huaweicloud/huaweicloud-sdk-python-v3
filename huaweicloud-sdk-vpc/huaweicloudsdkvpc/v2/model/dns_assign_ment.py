# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnsAssignMent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'hostname': 'str',
        'ip_address': 'str',
        'fqdn': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'ip_address': 'ip_address',
        'fqdn': 'fqdn'
    }

    def __init__(self, hostname=None, ip_address=None, fqdn=None):
        """DnsAssignMent

        The model defined in huaweicloud sdk

        :param hostname: 端口hostname
        :type hostname: str
        :param ip_address: 端口IP地址
        :type ip_address: str
        :param fqdn: 端口内网fqdn
        :type fqdn: str
        """
        
        

        self._hostname = None
        self._ip_address = None
        self._fqdn = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if ip_address is not None:
            self.ip_address = ip_address
        if fqdn is not None:
            self.fqdn = fqdn

    @property
    def hostname(self):
        """Gets the hostname of this DnsAssignMent.

        端口hostname

        :return: The hostname of this DnsAssignMent.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DnsAssignMent.

        端口hostname

        :param hostname: The hostname of this DnsAssignMent.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def ip_address(self):
        """Gets the ip_address of this DnsAssignMent.

        端口IP地址

        :return: The ip_address of this DnsAssignMent.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DnsAssignMent.

        端口IP地址

        :param ip_address: The ip_address of this DnsAssignMent.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def fqdn(self):
        """Gets the fqdn of this DnsAssignMent.

        端口内网fqdn

        :return: The fqdn of this DnsAssignMent.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this DnsAssignMent.

        端口内网fqdn

        :param fqdn: The fqdn of this DnsAssignMent.
        :type fqdn: str
        """
        self._fqdn = fqdn

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
        if not isinstance(other, DnsAssignMent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
