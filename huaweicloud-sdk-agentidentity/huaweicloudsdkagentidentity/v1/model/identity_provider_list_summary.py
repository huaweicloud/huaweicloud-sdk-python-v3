# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentityProviderListSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_provider': 'str',
        'display_name': 'str',
        'oauth2_discovery': 'Oauth2Discovery'
    }

    attribute_map = {
        'identity_provider': 'identity_provider',
        'display_name': 'display_name',
        'oauth2_discovery': 'oauth2_discovery'
    }

    def __init__(self, identity_provider=None, display_name=None, oauth2_discovery=None):
        r"""IdentityProviderListSummary

        The model defined in huaweicloud sdk

        :param identity_provider: Identity provider code.
        :type identity_provider: str
        :param display_name: Display name of the identity provider.
        :type display_name: str
        :param oauth2_discovery: 
        :type oauth2_discovery: :class:`huaweicloudsdkagentidentity.v1.Oauth2Discovery`
        """
        
        

        self._identity_provider = None
        self._display_name = None
        self._oauth2_discovery = None
        self.discriminator = None

        self.identity_provider = identity_provider
        self.display_name = display_name
        self.oauth2_discovery = oauth2_discovery

    @property
    def identity_provider(self):
        r"""Gets the identity_provider of this IdentityProviderListSummary.

        Identity provider code.

        :return: The identity_provider of this IdentityProviderListSummary.
        :rtype: str
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        r"""Sets the identity_provider of this IdentityProviderListSummary.

        Identity provider code.

        :param identity_provider: The identity_provider of this IdentityProviderListSummary.
        :type identity_provider: str
        """
        self._identity_provider = identity_provider

    @property
    def display_name(self):
        r"""Gets the display_name of this IdentityProviderListSummary.

        Display name of the identity provider.

        :return: The display_name of this IdentityProviderListSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this IdentityProviderListSummary.

        Display name of the identity provider.

        :param display_name: The display_name of this IdentityProviderListSummary.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def oauth2_discovery(self):
        r"""Gets the oauth2_discovery of this IdentityProviderListSummary.

        :return: The oauth2_discovery of this IdentityProviderListSummary.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.Oauth2Discovery`
        """
        return self._oauth2_discovery

    @oauth2_discovery.setter
    def oauth2_discovery(self, oauth2_discovery):
        r"""Sets the oauth2_discovery of this IdentityProviderListSummary.

        :param oauth2_discovery: The oauth2_discovery of this IdentityProviderListSummary.
        :type oauth2_discovery: :class:`huaweicloudsdkagentidentity.v1.Oauth2Discovery`
        """
        self._oauth2_discovery = oauth2_discovery

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IdentityProviderListSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
