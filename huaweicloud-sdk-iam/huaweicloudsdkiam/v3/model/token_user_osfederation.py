# coding: utf-8

import pprint
import re

import six





class TokenUserOsfederation:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'groups': 'list[OsfederationGroups]',
        'identity_provider': 'OsfederationIdentityprovider',
        'protocol': 'OsfederationProtocol'
    }

    attribute_map = {
        'groups': 'groups',
        'identity_provider': 'identity_provider',
        'protocol': 'protocol'
    }

    def __init__(self, groups=None, identity_provider=None, protocol=None):
        """TokenUserOsfederation - a model defined in huaweicloud sdk"""
        
        

        self._groups = None
        self._identity_provider = None
        self._protocol = None
        self.discriminator = None

        self.groups = groups
        self.identity_provider = identity_provider
        self.protocol = protocol

    @property
    def groups(self):
        """Gets the groups of this TokenUserOsfederation.

        用户组信息列表。

        :return: The groups of this TokenUserOsfederation.
        :rtype: list[OsfederationGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this TokenUserOsfederation.

        用户组信息列表。

        :param groups: The groups of this TokenUserOsfederation.
        :type: list[OsfederationGroups]
        """
        self._groups = groups

    @property
    def identity_provider(self):
        """Gets the identity_provider of this TokenUserOsfederation.


        :return: The identity_provider of this TokenUserOsfederation.
        :rtype: OsfederationIdentityprovider
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """Sets the identity_provider of this TokenUserOsfederation.


        :param identity_provider: The identity_provider of this TokenUserOsfederation.
        :type: OsfederationIdentityprovider
        """
        self._identity_provider = identity_provider

    @property
    def protocol(self):
        """Gets the protocol of this TokenUserOsfederation.


        :return: The protocol of this TokenUserOsfederation.
        :rtype: OsfederationProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TokenUserOsfederation.


        :param protocol: The protocol of this TokenUserOsfederation.
        :type: OsfederationProtocol
        """
        self._protocol = protocol

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
        if not isinstance(other, TokenUserOsfederation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
