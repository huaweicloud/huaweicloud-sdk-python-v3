# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'addr': 'str',
        'os_ext_ip_stype': 'str',
        'os_ext_ips_ma_cmac_addr': 'str',
        'os_ext_ip_sport_id': 'str'
    }

    attribute_map = {
        'version': 'version',
        'addr': 'addr',
        'os_ext_ip_stype': 'OS-EXT-IPS:type',
        'os_ext_ips_ma_cmac_addr': 'OS-EXT-IPS-MAC:mac_addr',
        'os_ext_ip_sport_id': 'OS-EXT-IPS:port_id'
    }

    def __init__(self, version=None, addr=None, os_ext_ip_stype=None, os_ext_ips_ma_cmac_addr=None, os_ext_ip_sport_id=None):
        """AddressInfo - a model defined in huaweicloud sdk"""
        
        

        self._version = None
        self._addr = None
        self._os_ext_ip_stype = None
        self._os_ext_ips_ma_cmac_addr = None
        self._os_ext_ip_sport_id = None
        self.discriminator = None

        self.version = version
        self.addr = addr
        if os_ext_ip_stype is not None:
            self.os_ext_ip_stype = os_ext_ip_stype
        if os_ext_ips_ma_cmac_addr is not None:
            self.os_ext_ips_ma_cmac_addr = os_ext_ips_ma_cmac_addr
        if os_ext_ip_sport_id is not None:
            self.os_ext_ip_sport_id = os_ext_ip_sport_id

    @property
    def version(self):
        """Gets the version of this AddressInfo.

        IP地址版本。4：代表IPv4。6：代表IPv6。

        :return: The version of this AddressInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AddressInfo.

        IP地址版本。4：代表IPv4。6：代表IPv6。

        :param version: The version of this AddressInfo.
        :type: str
        """
        self._version = version

    @property
    def addr(self):
        """Gets the addr of this AddressInfo.

        IP地址

        :return: The addr of this AddressInfo.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this AddressInfo.

        IP地址

        :param addr: The addr of this AddressInfo.
        :type: str
        """
        self._addr = addr

    @property
    def os_ext_ip_stype(self):
        """Gets the os_ext_ip_stype of this AddressInfo.

        IP地址类型。fixed：代表私有IP地址。floating：代表浮动IP地址。

        :return: The os_ext_ip_stype of this AddressInfo.
        :rtype: str
        """
        return self._os_ext_ip_stype

    @os_ext_ip_stype.setter
    def os_ext_ip_stype(self, os_ext_ip_stype):
        """Sets the os_ext_ip_stype of this AddressInfo.

        IP地址类型。fixed：代表私有IP地址。floating：代表浮动IP地址。

        :param os_ext_ip_stype: The os_ext_ip_stype of this AddressInfo.
        :type: str
        """
        self._os_ext_ip_stype = os_ext_ip_stype

    @property
    def os_ext_ips_ma_cmac_addr(self):
        """Gets the os_ext_ips_ma_cmac_addr of this AddressInfo.

        MAC地址。

        :return: The os_ext_ips_ma_cmac_addr of this AddressInfo.
        :rtype: str
        """
        return self._os_ext_ips_ma_cmac_addr

    @os_ext_ips_ma_cmac_addr.setter
    def os_ext_ips_ma_cmac_addr(self, os_ext_ips_ma_cmac_addr):
        """Sets the os_ext_ips_ma_cmac_addr of this AddressInfo.

        MAC地址。

        :param os_ext_ips_ma_cmac_addr: The os_ext_ips_ma_cmac_addr of this AddressInfo.
        :type: str
        """
        self._os_ext_ips_ma_cmac_addr = os_ext_ips_ma_cmac_addr

    @property
    def os_ext_ip_sport_id(self):
        """Gets the os_ext_ip_sport_id of this AddressInfo.

        IP地址对应的端口ID

        :return: The os_ext_ip_sport_id of this AddressInfo.
        :rtype: str
        """
        return self._os_ext_ip_sport_id

    @os_ext_ip_sport_id.setter
    def os_ext_ip_sport_id(self, os_ext_ip_sport_id):
        """Sets the os_ext_ip_sport_id of this AddressInfo.

        IP地址对应的端口ID

        :param os_ext_ip_sport_id: The os_ext_ip_sport_id of this AddressInfo.
        :type: str
        """
        self._os_ext_ip_sport_id = os_ext_ip_sport_id

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
