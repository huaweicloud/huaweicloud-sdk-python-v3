# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServerNicAllowedAddressPairs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_address': 'str',
        'mac_address': 'str'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'mac_address': 'mac_address'
    }

    def __init__(self, ip_address=None, mac_address=None):
        r"""CreateServerNicAllowedAddressPairs

        The model defined in huaweicloud sdk

        :param ip_address: IP地址 不支持0.0.0.0/0 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。
        :type ip_address: str
        :param mac_address: MAC地址
        :type mac_address: str
        """
        
        

        self._ip_address = None
        self._mac_address = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address

    @property
    def ip_address(self):
        r"""Gets the ip_address of this CreateServerNicAllowedAddressPairs.

        IP地址 不支持0.0.0.0/0 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。

        :return: The ip_address of this CreateServerNicAllowedAddressPairs.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this CreateServerNicAllowedAddressPairs.

        IP地址 不支持0.0.0.0/0 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。

        :param ip_address: The ip_address of this CreateServerNicAllowedAddressPairs.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def mac_address(self):
        r"""Gets the mac_address of this CreateServerNicAllowedAddressPairs.

        MAC地址

        :return: The mac_address of this CreateServerNicAllowedAddressPairs.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        r"""Sets the mac_address of this CreateServerNicAllowedAddressPairs.

        MAC地址

        :param mac_address: The mac_address of this CreateServerNicAllowedAddressPairs.
        :type mac_address: str
        """
        self._mac_address = mac_address

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
        if not isinstance(other, CreateServerNicAllowedAddressPairs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
