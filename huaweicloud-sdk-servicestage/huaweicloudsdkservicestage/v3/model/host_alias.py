# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostAlias:

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
        'hostnames': 'list[str]'
    }

    attribute_map = {
        'ip': 'ip',
        'hostnames': 'hostnames'
    }

    def __init__(self, ip=None, hostnames=None):
        """HostAlias

        The model defined in huaweicloud sdk

        :param ip: 
        :type ip: str
        :param hostnames: 
        :type hostnames: list[str]
        """
        
        

        self._ip = None
        self._hostnames = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if hostnames is not None:
            self.hostnames = hostnames

    @property
    def ip(self):
        """Gets the ip of this HostAlias.

        :return: The ip of this HostAlias.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this HostAlias.

        :param ip: The ip of this HostAlias.
        :type ip: str
        """
        self._ip = ip

    @property
    def hostnames(self):
        """Gets the hostnames of this HostAlias.

        :return: The hostnames of this HostAlias.
        :rtype: list[str]
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """Sets the hostnames of this HostAlias.

        :param hostnames: The hostnames of this HostAlias.
        :type hostnames: list[str]
        """
        self._hostnames = hostnames

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
        if not isinstance(other, HostAlias):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
