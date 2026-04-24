# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Oauth2CredentialProviderSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'urn': 'str',
        'credential_provider_vendor': 'CredentialProviderVendor',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'urn': 'urn',
        'credential_provider_vendor': 'credential_provider_vendor',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags'
    }

    def __init__(self, name=None, urn=None, credential_provider_vendor=None, created_at=None, updated_at=None, tags=None):
        r"""Oauth2CredentialProviderSummary

        The model defined in huaweicloud sdk

        :param name: The name of the credential provider.
        :type name: str
        :param urn: 凭证提供者的唯一资源名称（URN）。
        :type urn: str
        :param credential_provider_vendor: 
        :type credential_provider_vendor: :class:`huaweicloudsdkagentidentity.v1.CredentialProviderVendor`
        :param created_at: Timestamp in RFC 3339 format (UTC)
        :type created_at: datetime
        :param updated_at: Timestamp in RFC 3339 format (UTC)
        :type updated_at: datetime
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._name = None
        self._urn = None
        self._credential_provider_vendor = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.urn = urn
        self.credential_provider_vendor = credential_provider_vendor
        self.created_at = created_at
        self.updated_at = updated_at
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this Oauth2CredentialProviderSummary.

        The name of the credential provider.

        :return: The name of this Oauth2CredentialProviderSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Oauth2CredentialProviderSummary.

        The name of the credential provider.

        :param name: The name of this Oauth2CredentialProviderSummary.
        :type name: str
        """
        self._name = name

    @property
    def urn(self):
        r"""Gets the urn of this Oauth2CredentialProviderSummary.

        凭证提供者的唯一资源名称（URN）。

        :return: The urn of this Oauth2CredentialProviderSummary.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this Oauth2CredentialProviderSummary.

        凭证提供者的唯一资源名称（URN）。

        :param urn: The urn of this Oauth2CredentialProviderSummary.
        :type urn: str
        """
        self._urn = urn

    @property
    def credential_provider_vendor(self):
        r"""Gets the credential_provider_vendor of this Oauth2CredentialProviderSummary.

        :return: The credential_provider_vendor of this Oauth2CredentialProviderSummary.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CredentialProviderVendor`
        """
        return self._credential_provider_vendor

    @credential_provider_vendor.setter
    def credential_provider_vendor(self, credential_provider_vendor):
        r"""Sets the credential_provider_vendor of this Oauth2CredentialProviderSummary.

        :param credential_provider_vendor: The credential_provider_vendor of this Oauth2CredentialProviderSummary.
        :type credential_provider_vendor: :class:`huaweicloudsdkagentidentity.v1.CredentialProviderVendor`
        """
        self._credential_provider_vendor = credential_provider_vendor

    @property
    def created_at(self):
        r"""Gets the created_at of this Oauth2CredentialProviderSummary.

        Timestamp in RFC 3339 format (UTC)

        :return: The created_at of this Oauth2CredentialProviderSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Oauth2CredentialProviderSummary.

        Timestamp in RFC 3339 format (UTC)

        :param created_at: The created_at of this Oauth2CredentialProviderSummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Oauth2CredentialProviderSummary.

        Timestamp in RFC 3339 format (UTC)

        :return: The updated_at of this Oauth2CredentialProviderSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Oauth2CredentialProviderSummary.

        Timestamp in RFC 3339 format (UTC)

        :param updated_at: The updated_at of this Oauth2CredentialProviderSummary.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this Oauth2CredentialProviderSummary.

        自定义标签列表。

        :return: The tags of this Oauth2CredentialProviderSummary.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Oauth2CredentialProviderSummary.

        自定义标签列表。

        :param tags: The tags of this Oauth2CredentialProviderSummary.
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, Oauth2CredentialProviderSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
