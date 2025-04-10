# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpInfo:

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
        'subnet_mask': 'str'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'subnet_mask': 'subnet_mask'
    }

    def __init__(self, ip_address=None, subnet_mask=None):
        r"""IpInfo

        The model defined in huaweicloud sdk

        :param ip_address: ip地址。
        :type ip_address: str
        :param subnet_mask: 子网掩码。
        :type subnet_mask: str
        """
        
        

        self._ip_address = None
        self._subnet_mask = None
        self.discriminator = None

        self.ip_address = ip_address
        self.subnet_mask = subnet_mask

    @property
    def ip_address(self):
        r"""Gets the ip_address of this IpInfo.

        ip地址。

        :return: The ip_address of this IpInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this IpInfo.

        ip地址。

        :param ip_address: The ip_address of this IpInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def subnet_mask(self):
        r"""Gets the subnet_mask of this IpInfo.

        子网掩码。

        :return: The subnet_mask of this IpInfo.
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        r"""Sets the subnet_mask of this IpInfo.

        子网掩码。

        :param subnet_mask: The subnet_mask of this IpInfo.
        :type subnet_mask: str
        """
        self._subnet_mask = subnet_mask

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
        if not isinstance(other, IpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
