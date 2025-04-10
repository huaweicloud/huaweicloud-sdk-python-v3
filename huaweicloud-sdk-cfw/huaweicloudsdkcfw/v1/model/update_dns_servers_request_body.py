# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDnsServersRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dns_server': 'list[UpdateDnsServersRequestBodyDnsServer]',
        'health_check_domain_name': 'str'
    }

    attribute_map = {
        'dns_server': 'dns_server',
        'health_check_domain_name': 'health_check_domain_name'
    }

    def __init__(self, dns_server=None, health_check_domain_name=None):
        r"""UpdateDnsServersRequestBody

        The model defined in huaweicloud sdk

        :param dns_server: DNS服务器列表
        :type dns_server: list[:class:`huaweicloudsdkcfw.v1.UpdateDnsServersRequestBodyDnsServer`]
        :param health_check_domain_name: 健康检查域名，可通过[查询dns服务器列表接口](ListDnsServers.xml)查询获得，通过返回值中的data.health_check_domain_name（.表示各对象之间层级的区分）获得。
        :type health_check_domain_name: str
        """
        
        

        self._dns_server = None
        self._health_check_domain_name = None
        self.discriminator = None

        self.dns_server = dns_server
        if health_check_domain_name is not None:
            self.health_check_domain_name = health_check_domain_name

    @property
    def dns_server(self):
        r"""Gets the dns_server of this UpdateDnsServersRequestBody.

        DNS服务器列表

        :return: The dns_server of this UpdateDnsServersRequestBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.UpdateDnsServersRequestBodyDnsServer`]
        """
        return self._dns_server

    @dns_server.setter
    def dns_server(self, dns_server):
        r"""Sets the dns_server of this UpdateDnsServersRequestBody.

        DNS服务器列表

        :param dns_server: The dns_server of this UpdateDnsServersRequestBody.
        :type dns_server: list[:class:`huaweicloudsdkcfw.v1.UpdateDnsServersRequestBodyDnsServer`]
        """
        self._dns_server = dns_server

    @property
    def health_check_domain_name(self):
        r"""Gets the health_check_domain_name of this UpdateDnsServersRequestBody.

        健康检查域名，可通过[查询dns服务器列表接口](ListDnsServers.xml)查询获得，通过返回值中的data.health_check_domain_name（.表示各对象之间层级的区分）获得。

        :return: The health_check_domain_name of this UpdateDnsServersRequestBody.
        :rtype: str
        """
        return self._health_check_domain_name

    @health_check_domain_name.setter
    def health_check_domain_name(self, health_check_domain_name):
        r"""Sets the health_check_domain_name of this UpdateDnsServersRequestBody.

        健康检查域名，可通过[查询dns服务器列表接口](ListDnsServers.xml)查询获得，通过返回值中的data.health_check_domain_name（.表示各对象之间层级的区分）获得。

        :param health_check_domain_name: The health_check_domain_name of this UpdateDnsServersRequestBody.
        :type health_check_domain_name: str
        """
        self._health_check_domain_name = health_check_domain_name

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
        if not isinstance(other, UpdateDnsServersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
