# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizedDns:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_set_dns': 'bool',
        'set_dns_action': 'str',
        'dns_ip': 'str'
    }

    attribute_map = {
        'is_set_dns': 'is_set_dns',
        'set_dns_action': 'set_dns_action',
        'dns_ip': 'dns_ip'
    }

    def __init__(self, is_set_dns=None, set_dns_action=None, dns_ip=None):
        r"""CustomizedDns

        The model defined in huaweicloud sdk

        :param is_set_dns: 是否设置客户自定义DNS。
        :type is_set_dns: bool
        :param set_dns_action: 设置客户自定义DNS的行为。 - add：新增客户自定义DNS IP。 - keep：保持客户自定义DNS IP。 - update：更新客户自定义DNS IP（当DNS IP变化时更新生效）。 - recover：还原系统默认DNS IP（还原时可能会导致域名解析失败，请谨慎操作）。
        :type set_dns_action: str
        :param dns_ip: 设置客户自定义DNS IP。
        :type dns_ip: str
        """
        
        

        self._is_set_dns = None
        self._set_dns_action = None
        self._dns_ip = None
        self.discriminator = None

        self.is_set_dns = is_set_dns
        self.set_dns_action = set_dns_action
        self.dns_ip = dns_ip

    @property
    def is_set_dns(self):
        r"""Gets the is_set_dns of this CustomizedDns.

        是否设置客户自定义DNS。

        :return: The is_set_dns of this CustomizedDns.
        :rtype: bool
        """
        return self._is_set_dns

    @is_set_dns.setter
    def is_set_dns(self, is_set_dns):
        r"""Sets the is_set_dns of this CustomizedDns.

        是否设置客户自定义DNS。

        :param is_set_dns: The is_set_dns of this CustomizedDns.
        :type is_set_dns: bool
        """
        self._is_set_dns = is_set_dns

    @property
    def set_dns_action(self):
        r"""Gets the set_dns_action of this CustomizedDns.

        设置客户自定义DNS的行为。 - add：新增客户自定义DNS IP。 - keep：保持客户自定义DNS IP。 - update：更新客户自定义DNS IP（当DNS IP变化时更新生效）。 - recover：还原系统默认DNS IP（还原时可能会导致域名解析失败，请谨慎操作）。

        :return: The set_dns_action of this CustomizedDns.
        :rtype: str
        """
        return self._set_dns_action

    @set_dns_action.setter
    def set_dns_action(self, set_dns_action):
        r"""Sets the set_dns_action of this CustomizedDns.

        设置客户自定义DNS的行为。 - add：新增客户自定义DNS IP。 - keep：保持客户自定义DNS IP。 - update：更新客户自定义DNS IP（当DNS IP变化时更新生效）。 - recover：还原系统默认DNS IP（还原时可能会导致域名解析失败，请谨慎操作）。

        :param set_dns_action: The set_dns_action of this CustomizedDns.
        :type set_dns_action: str
        """
        self._set_dns_action = set_dns_action

    @property
    def dns_ip(self):
        r"""Gets the dns_ip of this CustomizedDns.

        设置客户自定义DNS IP。

        :return: The dns_ip of this CustomizedDns.
        :rtype: str
        """
        return self._dns_ip

    @dns_ip.setter
    def dns_ip(self, dns_ip):
        r"""Sets the dns_ip of this CustomizedDns.

        设置客户自定义DNS IP。

        :param dns_ip: The dns_ip of this CustomizedDns.
        :type dns_ip: str
        """
        self._dns_ip = dns_ip

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
        if not isinstance(other, CustomizedDns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
