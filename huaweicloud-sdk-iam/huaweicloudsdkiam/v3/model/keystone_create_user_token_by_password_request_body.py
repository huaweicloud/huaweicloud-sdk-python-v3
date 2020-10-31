# coding: utf-8

import pprint
import re

import six





class KeystoneCreateUserTokenByPasswordRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auth': 'PwdAuth'
    }

    attribute_map = {
        'auth': 'auth'
    }

    def __init__(self, auth=None):
        """KeystoneCreateUserTokenByPasswordRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._auth = None
        self.discriminator = None

        self.auth = auth

    @property
    def auth(self):
        """Gets the auth of this KeystoneCreateUserTokenByPasswordRequestBody.


        :return: The auth of this KeystoneCreateUserTokenByPasswordRequestBody.
        :rtype: PwdAuth
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this KeystoneCreateUserTokenByPasswordRequestBody.


        :param auth: The auth of this KeystoneCreateUserTokenByPasswordRequestBody.
        :type: PwdAuth
        """
        self._auth = auth

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
        if not isinstance(other, KeystoneCreateUserTokenByPasswordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
