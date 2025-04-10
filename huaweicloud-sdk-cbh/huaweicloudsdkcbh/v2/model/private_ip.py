# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'slave_ip': 'str',
        'floating_ip': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'slave_ip': 'slave_ip',
        'floating_ip': 'floating_ip'
    }

    def __init__(self, ip=None, slave_ip=None, floating_ip=None):
        r"""PrivateIp

        The model defined in huaweicloud sdk

        :param ip: 私网IP地址。
        :type ip: str
        :param slave_ip: 备机私网IP地址。
        :type slave_ip: str
        :param floating_ip: 浮动IP地址。
        :type floating_ip: str
        """
        
        

        self._ip = None
        self._slave_ip = None
        self._floating_ip = None
        self.discriminator = None

        self.ip = ip
        if slave_ip is not None:
            self.slave_ip = slave_ip
        if floating_ip is not None:
            self.floating_ip = floating_ip

    @property
    def ip(self):
        r"""Gets the ip of this PrivateIp.

        私网IP地址。

        :return: The ip of this PrivateIp.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this PrivateIp.

        私网IP地址。

        :param ip: The ip of this PrivateIp.
        :type ip: str
        """
        self._ip = ip

    @property
    def slave_ip(self):
        r"""Gets the slave_ip of this PrivateIp.

        备机私网IP地址。

        :return: The slave_ip of this PrivateIp.
        :rtype: str
        """
        return self._slave_ip

    @slave_ip.setter
    def slave_ip(self, slave_ip):
        r"""Sets the slave_ip of this PrivateIp.

        备机私网IP地址。

        :param slave_ip: The slave_ip of this PrivateIp.
        :type slave_ip: str
        """
        self._slave_ip = slave_ip

    @property
    def floating_ip(self):
        r"""Gets the floating_ip of this PrivateIp.

        浮动IP地址。

        :return: The floating_ip of this PrivateIp.
        :rtype: str
        """
        return self._floating_ip

    @floating_ip.setter
    def floating_ip(self, floating_ip):
        r"""Sets the floating_ip of this PrivateIp.

        浮动IP地址。

        :param floating_ip: The floating_ip of this PrivateIp.
        :type floating_ip: str
        """
        self._floating_ip = floating_ip

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
        if not isinstance(other, PrivateIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
