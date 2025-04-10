# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeerAddress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_port': 'str',
        'ip_port': 'str'
    }

    attribute_map = {
        'domain_port': 'domain_port',
        'ip_port': 'ip_port'
    }

    def __init__(self, domain_port=None, ip_port=None):
        r"""PeerAddress

        The model defined in huaweicloud sdk

        :param domain_port: 域名地址
        :type domain_port: str
        :param ip_port: IP地址
        :type ip_port: str
        """
        
        

        self._domain_port = None
        self._ip_port = None
        self.discriminator = None

        if domain_port is not None:
            self.domain_port = domain_port
        if ip_port is not None:
            self.ip_port = ip_port

    @property
    def domain_port(self):
        r"""Gets the domain_port of this PeerAddress.

        域名地址

        :return: The domain_port of this PeerAddress.
        :rtype: str
        """
        return self._domain_port

    @domain_port.setter
    def domain_port(self, domain_port):
        r"""Sets the domain_port of this PeerAddress.

        域名地址

        :param domain_port: The domain_port of this PeerAddress.
        :type domain_port: str
        """
        self._domain_port = domain_port

    @property
    def ip_port(self):
        r"""Gets the ip_port of this PeerAddress.

        IP地址

        :return: The ip_port of this PeerAddress.
        :rtype: str
        """
        return self._ip_port

    @ip_port.setter
    def ip_port(self, ip_port):
        r"""Sets the ip_port of this PeerAddress.

        IP地址

        :param ip_port: The ip_port of this PeerAddress.
        :type ip_port: str
        """
        self._ip_port = ip_port

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
        if not isinstance(other, PeerAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
