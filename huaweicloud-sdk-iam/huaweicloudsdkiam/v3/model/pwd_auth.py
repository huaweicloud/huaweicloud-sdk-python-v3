# coding: utf-8

import pprint
import re

import six





class PwdAuth:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'identity': 'PwdIdentity',
        'scope': 'AuthScope'
    }

    attribute_map = {
        'identity': 'identity',
        'scope': 'scope'
    }

    def __init__(self, identity=None, scope=None):
        """PwdAuth - a model defined in huaweicloud sdk"""
        
        

        self._identity = None
        self._scope = None
        self.discriminator = None

        self.identity = identity
        self.scope = scope

    @property
    def identity(self):
        """Gets the identity of this PwdAuth.


        :return: The identity of this PwdAuth.
        :rtype: PwdIdentity
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this PwdAuth.


        :param identity: The identity of this PwdAuth.
        :type: PwdIdentity
        """
        self._identity = identity

    @property
    def scope(self):
        """Gets the scope of this PwdAuth.


        :return: The scope of this PwdAuth.
        :rtype: AuthScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PwdAuth.


        :param scope: The scope of this PwdAuth.
        :type: AuthScope
        """
        self._scope = scope

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
        if not isinstance(other, PwdAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
