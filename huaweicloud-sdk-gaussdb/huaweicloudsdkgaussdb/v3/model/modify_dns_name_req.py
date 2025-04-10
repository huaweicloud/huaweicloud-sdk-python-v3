# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyDnsNameReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dns_name': 'str'
    }

    attribute_map = {
        'dns_name': 'dns_name'
    }

    def __init__(self, dns_name=None):
        r"""ModifyDnsNameReq

        The model defined in huaweicloud sdk

        :param dns_name: 新域名的前缀，取值范围如下：8~63个字符之间，可以包含小写字母、数字，不能包含其他特殊字符。
        :type dns_name: str
        """
        
        

        self._dns_name = None
        self.discriminator = None

        self.dns_name = dns_name

    @property
    def dns_name(self):
        r"""Gets the dns_name of this ModifyDnsNameReq.

        新域名的前缀，取值范围如下：8~63个字符之间，可以包含小写字母、数字，不能包含其他特殊字符。

        :return: The dns_name of this ModifyDnsNameReq.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        r"""Sets the dns_name of this ModifyDnsNameReq.

        新域名的前缀，取值范围如下：8~63个字符之间，可以包含小写字母、数字，不能包含其他特殊字符。

        :param dns_name: The dns_name of this ModifyDnsNameReq.
        :type dns_name: str
        """
        self._dns_name = dns_name

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
        if not isinstance(other, ModifyDnsNameReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
