# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyDnsNameRequestBody:

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
        """ModifyDnsNameRequestBody

        The model defined in huaweicloud sdk

        :param dns_name: 新域名的前缀，校验规则是^[0-9a-zA-Z]{8,64}$
        :type dns_name: str
        """
        
        

        self._dns_name = None
        self.discriminator = None

        self.dns_name = dns_name

    @property
    def dns_name(self):
        """Gets the dns_name of this ModifyDnsNameRequestBody.

        新域名的前缀，校验规则是^[0-9a-zA-Z]{8,64}$

        :return: The dns_name of this ModifyDnsNameRequestBody.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this ModifyDnsNameRequestBody.

        新域名的前缀，校验规则是^[0-9a-zA-Z]{8,64}$

        :param dns_name: The dns_name of this ModifyDnsNameRequestBody.
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
        if not isinstance(other, ModifyDnsNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
