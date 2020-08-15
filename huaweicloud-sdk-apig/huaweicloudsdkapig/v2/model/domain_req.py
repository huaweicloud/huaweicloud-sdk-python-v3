# coding: utf-8

import pprint
import re

import six





class DomainReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url_domain': 'str'
    }

    attribute_map = {
        'url_domain': 'url_domain'
    }

    def __init__(self, url_domain=None):
        """DomainReq - a model defined in huaweicloud sdk"""
        
        

        self._url_domain = None
        self.discriminator = None

        self.url_domain = url_domain

    @property
    def url_domain(self):
        """Gets the url_domain of this DomainReq.

        自定义域名。长度为0-255位的字符串，需要符合域名规范。

        :return: The url_domain of this DomainReq.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this DomainReq.

        自定义域名。长度为0-255位的字符串，需要符合域名规范。

        :param url_domain: The url_domain of this DomainReq.
        :type: str
        """
        self._url_domain = url_domain

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DomainReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
