# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Oauth2Discovery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'discovery_url': 'str',
        'authorization_server_metadata': 'Oauth2AuthorizationServerMetadata'
    }

    attribute_map = {
        'discovery_url': 'discovery_url',
        'authorization_server_metadata': 'authorization_server_metadata'
    }

    def __init__(self, discovery_url=None, authorization_server_metadata=None):
        r"""Oauth2Discovery

        The model defined in huaweicloud sdk

        :param discovery_url: This URL is used to fetch OpenID Connect configuration.
        :type discovery_url: str
        :param authorization_server_metadata: 
        :type authorization_server_metadata: :class:`huaweicloudsdkagentidentity.v1.Oauth2AuthorizationServerMetadata`
        """
        
        

        self._discovery_url = None
        self._authorization_server_metadata = None
        self.discriminator = None

        if discovery_url is not None:
            self.discovery_url = discovery_url
        if authorization_server_metadata is not None:
            self.authorization_server_metadata = authorization_server_metadata

    @property
    def discovery_url(self):
        r"""Gets the discovery_url of this Oauth2Discovery.

        This URL is used to fetch OpenID Connect configuration.

        :return: The discovery_url of this Oauth2Discovery.
        :rtype: str
        """
        return self._discovery_url

    @discovery_url.setter
    def discovery_url(self, discovery_url):
        r"""Sets the discovery_url of this Oauth2Discovery.

        This URL is used to fetch OpenID Connect configuration.

        :param discovery_url: The discovery_url of this Oauth2Discovery.
        :type discovery_url: str
        """
        self._discovery_url = discovery_url

    @property
    def authorization_server_metadata(self):
        r"""Gets the authorization_server_metadata of this Oauth2Discovery.

        :return: The authorization_server_metadata of this Oauth2Discovery.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.Oauth2AuthorizationServerMetadata`
        """
        return self._authorization_server_metadata

    @authorization_server_metadata.setter
    def authorization_server_metadata(self, authorization_server_metadata):
        r"""Sets the authorization_server_metadata of this Oauth2Discovery.

        :param authorization_server_metadata: The authorization_server_metadata of this Oauth2Discovery.
        :type authorization_server_metadata: :class:`huaweicloudsdkagentidentity.v1.Oauth2AuthorizationServerMetadata`
        """
        self._authorization_server_metadata = authorization_server_metadata

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
        if not isinstance(other, Oauth2Discovery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
