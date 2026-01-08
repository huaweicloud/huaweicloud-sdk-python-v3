# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Saml2AuthConfig:

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
        'access_server_address': 'str',
        'unique_user_identifier': 'str',
        'idp_metadata_info': 'IdpMetadataInfo'
    }

    attribute_map = {
        'identity_provider': 'identity_provider',
        'access_server_address': 'access_server_address',
        'unique_user_identifier': 'unique_user_identifier',
        'idp_metadata_info': 'idp_metadata_info'
    }

    def __init__(self, identity_provider=None, access_server_address=None, unique_user_identifier=None, idp_metadata_info=None):
        r"""Saml2AuthConfig

        The model defined in huaweicloud sdk

        :param identity_provider: 身份提供者名称。
        :type identity_provider: str
        :param access_server_address: 接入服务器地址。
        :type access_server_address: str
        :param unique_user_identifier: 唯一用户标识符。
        :type unique_user_identifier: str
        :param idp_metadata_info: 
        :type idp_metadata_info: :class:`huaweicloudsdkworkspace.v2.IdpMetadataInfo`
        """
        
        

        self._identity_provider = None
        self._access_server_address = None
        self._unique_user_identifier = None
        self._idp_metadata_info = None
        self.discriminator = None

        if identity_provider is not None:
            self.identity_provider = identity_provider
        if access_server_address is not None:
            self.access_server_address = access_server_address
        if unique_user_identifier is not None:
            self.unique_user_identifier = unique_user_identifier
        if idp_metadata_info is not None:
            self.idp_metadata_info = idp_metadata_info

    @property
    def identity_provider(self):
        r"""Gets the identity_provider of this Saml2AuthConfig.

        身份提供者名称。

        :return: The identity_provider of this Saml2AuthConfig.
        :rtype: str
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        r"""Sets the identity_provider of this Saml2AuthConfig.

        身份提供者名称。

        :param identity_provider: The identity_provider of this Saml2AuthConfig.
        :type identity_provider: str
        """
        self._identity_provider = identity_provider

    @property
    def access_server_address(self):
        r"""Gets the access_server_address of this Saml2AuthConfig.

        接入服务器地址。

        :return: The access_server_address of this Saml2AuthConfig.
        :rtype: str
        """
        return self._access_server_address

    @access_server_address.setter
    def access_server_address(self, access_server_address):
        r"""Sets the access_server_address of this Saml2AuthConfig.

        接入服务器地址。

        :param access_server_address: The access_server_address of this Saml2AuthConfig.
        :type access_server_address: str
        """
        self._access_server_address = access_server_address

    @property
    def unique_user_identifier(self):
        r"""Gets the unique_user_identifier of this Saml2AuthConfig.

        唯一用户标识符。

        :return: The unique_user_identifier of this Saml2AuthConfig.
        :rtype: str
        """
        return self._unique_user_identifier

    @unique_user_identifier.setter
    def unique_user_identifier(self, unique_user_identifier):
        r"""Sets the unique_user_identifier of this Saml2AuthConfig.

        唯一用户标识符。

        :param unique_user_identifier: The unique_user_identifier of this Saml2AuthConfig.
        :type unique_user_identifier: str
        """
        self._unique_user_identifier = unique_user_identifier

    @property
    def idp_metadata_info(self):
        r"""Gets the idp_metadata_info of this Saml2AuthConfig.

        :return: The idp_metadata_info of this Saml2AuthConfig.
        :rtype: :class:`huaweicloudsdkworkspace.v2.IdpMetadataInfo`
        """
        return self._idp_metadata_info

    @idp_metadata_info.setter
    def idp_metadata_info(self, idp_metadata_info):
        r"""Sets the idp_metadata_info of this Saml2AuthConfig.

        :param idp_metadata_info: The idp_metadata_info of this Saml2AuthConfig.
        :type idp_metadata_info: :class:`huaweicloudsdkworkspace.v2.IdpMetadataInfo`
        """
        self._idp_metadata_info = idp_metadata_info

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
        if not isinstance(other, Saml2AuthConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
