# coding: utf-8

import pprint
import re

import six





class IdpToken:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'issued_at': 'str',
        'expires_at': 'str',
        'methods': 'list[str]',
        'user': 'UnscopedTokenUser'
    }

    attribute_map = {
        'issued_at': 'issued_at',
        'expires_at': 'expires_at',
        'methods': 'methods',
        'user': 'user'
    }

    def __init__(self, issued_at=None, expires_at=None, methods=None, user=None):
        """IdpToken - a model defined in huaweicloud sdk"""
        
        

        self._issued_at = None
        self._expires_at = None
        self._methods = None
        self._user = None
        self.discriminator = None

        self.issued_at = issued_at
        self.expires_at = expires_at
        self.methods = methods
        self.user = user

    @property
    def issued_at(self):
        """Gets the issued_at of this IdpToken.

        token产生时间。

        :return: The issued_at of this IdpToken.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this IdpToken.

        token产生时间。

        :param issued_at: The issued_at of this IdpToken.
        :type: str
        """
        self._issued_at = issued_at

    @property
    def expires_at(self):
        """Gets the expires_at of this IdpToken.

        token到期时间。

        :return: The expires_at of this IdpToken.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this IdpToken.

        token到期时间。

        :param expires_at: The expires_at of this IdpToken.
        :type: str
        """
        self._expires_at = expires_at

    @property
    def methods(self):
        """Gets the methods of this IdpToken.

        获取token的方式。

        :return: The methods of this IdpToken.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this IdpToken.

        获取token的方式。

        :param methods: The methods of this IdpToken.
        :type: list[str]
        """
        self._methods = methods

    @property
    def user(self):
        """Gets the user of this IdpToken.


        :return: The user of this IdpToken.
        :rtype: UnscopedTokenUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this IdpToken.


        :param user: The user of this IdpToken.
        :type: UnscopedTokenUser
        """
        self._user = user

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
        if not isinstance(other, IdpToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
