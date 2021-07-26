# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OsFederationInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'identity_provider': 'IdpIdInfo',
        'protocol': 'ProtocolIdInfo',
        'groups': 'list[object]'
    }

    attribute_map = {
        'identity_provider': 'identity_provider',
        'protocol': 'protocol',
        'groups': 'groups'
    }

    def __init__(self, identity_provider=None, protocol=None, groups=None):
        """OsFederationInfo - a model defined in huaweicloud sdk"""
        
        

        self._identity_provider = None
        self._protocol = None
        self._groups = None
        self.discriminator = None

        self.identity_provider = identity_provider
        self.protocol = protocol
        self.groups = groups

    @property
    def identity_provider(self):
        """Gets the identity_provider of this OsFederationInfo.


        :return: The identity_provider of this OsFederationInfo.
        :rtype: IdpIdInfo
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """Sets the identity_provider of this OsFederationInfo.


        :param identity_provider: The identity_provider of this OsFederationInfo.
        :type: IdpIdInfo
        """
        self._identity_provider = identity_provider

    @property
    def protocol(self):
        """Gets the protocol of this OsFederationInfo.


        :return: The protocol of this OsFederationInfo.
        :rtype: ProtocolIdInfo
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this OsFederationInfo.


        :param protocol: The protocol of this OsFederationInfo.
        :type: ProtocolIdInfo
        """
        self._protocol = protocol

    @property
    def groups(self):
        """Gets the groups of this OsFederationInfo.

        用户组信息

        :return: The groups of this OsFederationInfo.
        :rtype: list[object]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this OsFederationInfo.

        用户组信息

        :param groups: The groups of this OsFederationInfo.
        :type: list[object]
        """
        self._groups = groups

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OsFederationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
