# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_address_id': 'str',
        'domain_name': 'str',
        'description': 'str',
        'dns_ips': 'list[str]'
    }

    attribute_map = {
        'domain_address_id': 'domain_address_id',
        'domain_name': 'domain_name',
        'description': 'description',
        'dns_ips': 'dns_ips'
    }

    def __init__(self, domain_address_id=None, domain_name=None, description=None, dns_ips=None):
        """DomainInfo

        The model defined in huaweicloud sdk

        :param domain_address_id: 域名地址id
        :type domain_address_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param description: 描述
        :type description: str
        :param dns_ips: 域名服务器列表
        :type dns_ips: list[str]
        """
        
        

        self._domain_address_id = None
        self._domain_name = None
        self._description = None
        self._dns_ips = None
        self.discriminator = None

        if domain_address_id is not None:
            self.domain_address_id = domain_address_id
        if domain_name is not None:
            self.domain_name = domain_name
        if description is not None:
            self.description = description
        if dns_ips is not None:
            self.dns_ips = dns_ips

    @property
    def domain_address_id(self):
        """Gets the domain_address_id of this DomainInfo.

        域名地址id

        :return: The domain_address_id of this DomainInfo.
        :rtype: str
        """
        return self._domain_address_id

    @domain_address_id.setter
    def domain_address_id(self, domain_address_id):
        """Sets the domain_address_id of this DomainInfo.

        域名地址id

        :param domain_address_id: The domain_address_id of this DomainInfo.
        :type domain_address_id: str
        """
        self._domain_address_id = domain_address_id

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainInfo.

        域名

        :return: The domain_name of this DomainInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainInfo.

        域名

        :param domain_name: The domain_name of this DomainInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def description(self):
        """Gets the description of this DomainInfo.

        描述

        :return: The description of this DomainInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DomainInfo.

        描述

        :param description: The description of this DomainInfo.
        :type description: str
        """
        self._description = description

    @property
    def dns_ips(self):
        """Gets the dns_ips of this DomainInfo.

        域名服务器列表

        :return: The dns_ips of this DomainInfo.
        :rtype: list[str]
        """
        return self._dns_ips

    @dns_ips.setter
    def dns_ips(self, dns_ips):
        """Sets the dns_ips of this DomainInfo.

        域名服务器列表

        :param dns_ips: The dns_ips of this DomainInfo.
        :type dns_ips: list[str]
        """
        self._dns_ips = dns_ips

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
        if not isinstance(other, DomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
