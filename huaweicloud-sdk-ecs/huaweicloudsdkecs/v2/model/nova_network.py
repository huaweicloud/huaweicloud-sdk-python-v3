# coding: utf-8

import pprint
import re

import six





class NovaNetwork:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'addr': 'str',
        'version': 'int',
        'os_ext_ips_ma_cmac_addr': 'str',
        'os_ext_ip_stype': 'str'
    }

    attribute_map = {
        'addr': 'addr',
        'version': 'version',
        'os_ext_ips_ma_cmac_addr': 'OS-EXT-IPS-MAC:mac_addr',
        'os_ext_ip_stype': 'OS-EXT-IPS:type'
    }

    def __init__(self, addr=None, version=None, os_ext_ips_ma_cmac_addr=None, os_ext_ip_stype=None):
        """NovaNetwork - a model defined in huaweicloud sdk"""
        
        

        self._addr = None
        self._version = None
        self._os_ext_ips_ma_cmac_addr = None
        self._os_ext_ip_stype = None
        self.discriminator = None

        self.addr = addr
        self.version = version
        self.os_ext_ips_ma_cmac_addr = os_ext_ips_ma_cmac_addr
        self.os_ext_ip_stype = os_ext_ip_stype

    @property
    def addr(self):
        """Gets the addr of this NovaNetwork.

        IP地址。

        :return: The addr of this NovaNetwork.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this NovaNetwork.

        IP地址。

        :param addr: The addr of this NovaNetwork.
        :type: str
        """
        self._addr = addr

    @property
    def version(self):
        """Gets the version of this NovaNetwork.

        IP地址类型，值为4或6。  4：IP地址类型是IPv4 6：IP地址类型是IPv6

        :return: The version of this NovaNetwork.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NovaNetwork.

        IP地址类型，值为4或6。  4：IP地址类型是IPv4 6：IP地址类型是IPv6

        :param version: The version of this NovaNetwork.
        :type: int
        """
        self._version = version

    @property
    def os_ext_ips_ma_cmac_addr(self):
        """Gets the os_ext_ips_ma_cmac_addr of this NovaNetwork.

        扩展属性，MAC地址。

        :return: The os_ext_ips_ma_cmac_addr of this NovaNetwork.
        :rtype: str
        """
        return self._os_ext_ips_ma_cmac_addr

    @os_ext_ips_ma_cmac_addr.setter
    def os_ext_ips_ma_cmac_addr(self, os_ext_ips_ma_cmac_addr):
        """Sets the os_ext_ips_ma_cmac_addr of this NovaNetwork.

        扩展属性，MAC地址。

        :param os_ext_ips_ma_cmac_addr: The os_ext_ips_ma_cmac_addr of this NovaNetwork.
        :type: str
        """
        self._os_ext_ips_ma_cmac_addr = os_ext_ips_ma_cmac_addr

    @property
    def os_ext_ip_stype(self):
        """Gets the os_ext_ip_stype of this NovaNetwork.

        扩展属性，分配IP地址方式。

        :return: The os_ext_ip_stype of this NovaNetwork.
        :rtype: str
        """
        return self._os_ext_ip_stype

    @os_ext_ip_stype.setter
    def os_ext_ip_stype(self, os_ext_ip_stype):
        """Sets the os_ext_ip_stype of this NovaNetwork.

        扩展属性，分配IP地址方式。

        :param os_ext_ip_stype: The os_ext_ip_stype of this NovaNetwork.
        :type: str
        """
        self._os_ext_ip_stype = os_ext_ip_stype

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
