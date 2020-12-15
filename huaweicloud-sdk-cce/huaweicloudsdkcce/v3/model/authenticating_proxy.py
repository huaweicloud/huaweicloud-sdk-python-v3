# coding: utf-8

import pprint
import re

import six





class AuthenticatingProxy:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ca': 'str'
    }

    attribute_map = {
        'ca': 'ca'
    }

    def __init__(self, ca=None):
        """AuthenticatingProxy - a model defined in huaweicloud sdk"""
        
        

        self._ca = None
        self.discriminator = None

        if ca is not None:
            self.ca = ca

    @property
    def ca(self):
        """Gets the ca of this AuthenticatingProxy.

        authenticating_proxy模式配置的x509格式CA证书(base64编码)。 最大长度：1M

        :return: The ca of this AuthenticatingProxy.
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this AuthenticatingProxy.

        authenticating_proxy模式配置的x509格式CA证书(base64编码)。 最大长度：1M

        :param ca: The ca of this AuthenticatingProxy.
        :type: str
        """
        self._ca = ca

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
        if not isinstance(other, AuthenticatingProxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
