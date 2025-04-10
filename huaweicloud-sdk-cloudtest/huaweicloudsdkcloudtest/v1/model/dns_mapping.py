# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnsMapping:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dns': 'list[DnsMappingNode]'
    }

    attribute_map = {
        'dns': 'dns'
    }

    def __init__(self, dns=None):
        r"""DnsMapping

        The model defined in huaweicloud sdk

        :param dns: 
        :type dns: list[:class:`huaweicloudsdkcloudtest.v1.DnsMappingNode`]
        """
        
        

        self._dns = None
        self.discriminator = None

        if dns is not None:
            self.dns = dns

    @property
    def dns(self):
        r"""Gets the dns of this DnsMapping.

        :return: The dns of this DnsMapping.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.DnsMappingNode`]
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        r"""Sets the dns of this DnsMapping.

        :param dns: The dns of this DnsMapping.
        :type dns: list[:class:`huaweicloudsdkcloudtest.v1.DnsMappingNode`]
        """
        self._dns = dns

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
        if not isinstance(other, DnsMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
