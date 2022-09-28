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
        'addr': 'str',
        'version': 'str',
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
        """AddressInfo

        The model defined in huaweicloud sdk

        :param addr: IP地址信息。
        :type addr: str
        :param version: IP地址类型，值为4或6，分别表示IPV4和IPV6。
        :type version: str
        :param os_ext_ips_ma_cmac_addr: MAC地址。
        :type os_ext_ips_ma_cmac_addr: str
        :param os_ext_ip_stype: IP地址分配方式。 -fixed  私有IP地址。 -floating 浮动IP地址。
        :type os_ext_ip_stype: str
        """
        
        

        self._addr = None
        self._version = None
        self._os_ext_ips_ma_cmac_addr = None
        self._os_ext_ip_stype = None
        self.discriminator = None

        if addr is not None:
            self.addr = addr
        if version is not None:
            self.version = version
        if os_ext_ips_ma_cmac_addr is not None:
            self.os_ext_ips_ma_cmac_addr = os_ext_ips_ma_cmac_addr
        if os_ext_ip_stype is not None:
            self.os_ext_ip_stype = os_ext_ip_stype

    @property
    def addr(self):
        """Gets the addr of this AddressInfo.

        IP地址信息。

        :return: The addr of this AddressInfo.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this AddressInfo.

        IP地址信息。

        :param addr: The addr of this AddressInfo.
        :type addr: str
        """
        self._addr = addr

    @property
    def version(self):
        """Gets the version of this AddressInfo.

        IP地址类型，值为4或6，分别表示IPV4和IPV6。

        :return: The version of this AddressInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AddressInfo.

        IP地址类型，值为4或6，分别表示IPV4和IPV6。

        :param version: The version of this AddressInfo.
        :type version: str
        """
        self._version = version

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
        :type os_ext_ips_ma_cmac_addr: str
        """
        self._os_ext_ips_ma_cmac_addr = os_ext_ips_ma_cmac_addr

    @property
    def os_ext_ip_stype(self):
        """Gets the os_ext_ip_stype of this AddressInfo.

        IP地址分配方式。 -fixed  私有IP地址。 -floating 浮动IP地址。

        :return: The os_ext_ip_stype of this AddressInfo.
        :rtype: str
        """
        return self._os_ext_ip_stype

    @os_ext_ip_stype.setter
    def os_ext_ip_stype(self, os_ext_ip_stype):
        """Sets the os_ext_ip_stype of this AddressInfo.

        IP地址分配方式。 -fixed  私有IP地址。 -floating 浮动IP地址。

        :param os_ext_ip_stype: The os_ext_ip_stype of this AddressInfo.
        :type os_ext_ip_stype: str
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
        if not isinstance(other, AddressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
