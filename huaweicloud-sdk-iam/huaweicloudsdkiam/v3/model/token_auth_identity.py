# coding: utf-8

import pprint
import re

import six





class TokenAuthIdentity:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'methods': 'list[str]',
        'token': 'IdentityToken',
        'policy': 'ServicePolicy'
    }

    attribute_map = {
        'methods': 'methods',
        'token': 'token',
        'policy': 'policy'
    }

    def __init__(self, methods=None, token=None, policy=None):
        """TokenAuthIdentity - a model defined in huaweicloud sdk"""
        
        

        self._methods = None
        self._token = None
        self._policy = None
        self.discriminator = None

        self.methods = methods
        if token is not None:
            self.token = token
        if policy is not None:
            self.policy = policy

    @property
    def methods(self):
        """Gets the methods of this TokenAuthIdentity.

        认证方法，该字段内容为[\"token\"]。

        :return: The methods of this TokenAuthIdentity.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this TokenAuthIdentity.

        认证方法，该字段内容为[\"token\"]。

        :param methods: The methods of this TokenAuthIdentity.
        :type: list[str]
        """
        self._methods = methods

    @property
    def token(self):
        """Gets the token of this TokenAuthIdentity.


        :return: The token of this TokenAuthIdentity.
        :rtype: IdentityToken
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TokenAuthIdentity.


        :param token: The token of this TokenAuthIdentity.
        :type: IdentityToken
        """
        self._token = token

    @property
    def policy(self):
        """Gets the policy of this TokenAuthIdentity.


        :return: The policy of this TokenAuthIdentity.
        :rtype: ServicePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this TokenAuthIdentity.


        :param policy: The policy of this TokenAuthIdentity.
        :type: ServicePolicy
        """
        self._policy = policy

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
        if not isinstance(other, TokenAuthIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
