# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Nics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interface': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'interface': 'interface',
        'ip': 'ip'
    }

    def __init__(self, interface=None, ip=None):
        """Nics

        The model defined in huaweicloud sdk

        :param interface: 边缘节点网卡名称
        :type interface: str
        :param ip: 上述网卡对应的IPv4地址
        :type ip: str
        """
        
        

        self._interface = None
        self._ip = None
        self.discriminator = None

        if interface is not None:
            self.interface = interface
        if ip is not None:
            self.ip = ip

    @property
    def interface(self):
        """Gets the interface of this Nics.

        边缘节点网卡名称

        :return: The interface of this Nics.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this Nics.

        边缘节点网卡名称

        :param interface: The interface of this Nics.
        :type interface: str
        """
        self._interface = interface

    @property
    def ip(self):
        """Gets the ip of this Nics.

        上述网卡对应的IPv4地址

        :return: The ip of this Nics.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Nics.

        上述网卡对应的IPv4地址

        :param ip: The ip of this Nics.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, Nics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
