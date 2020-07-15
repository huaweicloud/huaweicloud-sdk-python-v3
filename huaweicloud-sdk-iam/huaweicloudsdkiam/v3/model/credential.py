# coding: utf-8

import pprint
import re

import six





class Credential:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'expires_at': 'str',
        'access': 'str',
        'secret': 'str',
        'securitytoken': 'str'
    }

    attribute_map = {
        'expires_at': 'expires_at',
        'access': 'access',
        'secret': 'secret',
        'securitytoken': 'securitytoken'
    }

    def __init__(self, expires_at=None, access=None, secret=None, securitytoken=None):
        """Credential - a model defined in huaweicloud sdk"""
        
        

        self._expires_at = None
        self._access = None
        self._secret = None
        self._securitytoken = None
        self.discriminator = None

        self.expires_at = expires_at
        self.access = access
        self.secret = secret
        self.securitytoken = securitytoken

    @property
    def expires_at(self):
        """Gets the expires_at of this Credential.

        AK/SK和securitytoken的过期时间。

        :return: The expires_at of this Credential.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Credential.

        AK/SK和securitytoken的过期时间。

        :param expires_at: The expires_at of this Credential.
        :type: str
        """
        self._expires_at = expires_at

    @property
    def access(self):
        """Gets the access of this Credential.

        获取的AK。

        :return: The access of this Credential.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this Credential.

        获取的AK。

        :param access: The access of this Credential.
        :type: str
        """
        self._access = access

    @property
    def secret(self):
        """Gets the secret of this Credential.

        获取的SK。

        :return: The secret of this Credential.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this Credential.

        获取的SK。

        :param secret: The secret of this Credential.
        :type: str
        """
        self._secret = secret

    @property
    def securitytoken(self):
        """Gets the securitytoken of this Credential.

        securitytoken是将所获的AK、SK等信息进行加密后的字符串。

        :return: The securitytoken of this Credential.
        :rtype: str
        """
        return self._securitytoken

    @securitytoken.setter
    def securitytoken(self, securitytoken):
        """Sets the securitytoken of this Credential.

        securitytoken是将所获的AK、SK等信息进行加密后的字符串。

        :param securitytoken: The securitytoken of this Credential.
        :type: str
        """
        self._securitytoken = securitytoken

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
        if not isinstance(other, Credential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
