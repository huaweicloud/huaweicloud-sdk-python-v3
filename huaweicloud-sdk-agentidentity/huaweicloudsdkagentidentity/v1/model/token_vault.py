# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TokenVault:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token_vault_id': 'str',
        'kms_configuration': 'KmsConfiguration',
        'updated_at': 'datetime',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'token_vault_id': 'token_vault_id',
        'kms_configuration': 'kms_configuration',
        'updated_at': 'updated_at',
        'tags': 'tags'
    }

    def __init__(self, token_vault_id=None, kms_configuration=None, updated_at=None, tags=None):
        r"""TokenVault

        The model defined in huaweicloud sdk

        :param token_vault_id: The unique identifier of the token vault.
        :type token_vault_id: str
        :param kms_configuration: 
        :type kms_configuration: :class:`huaweicloudsdkagentidentity.v1.KmsConfiguration`
        :param updated_at: Timestamp in RFC 3339 format (UTC)
        :type updated_at: datetime
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._token_vault_id = None
        self._kms_configuration = None
        self._updated_at = None
        self._tags = None
        self.discriminator = None

        self.token_vault_id = token_vault_id
        self.kms_configuration = kms_configuration
        self.updated_at = updated_at
        if tags is not None:
            self.tags = tags

    @property
    def token_vault_id(self):
        r"""Gets the token_vault_id of this TokenVault.

        The unique identifier of the token vault.

        :return: The token_vault_id of this TokenVault.
        :rtype: str
        """
        return self._token_vault_id

    @token_vault_id.setter
    def token_vault_id(self, token_vault_id):
        r"""Sets the token_vault_id of this TokenVault.

        The unique identifier of the token vault.

        :param token_vault_id: The token_vault_id of this TokenVault.
        :type token_vault_id: str
        """
        self._token_vault_id = token_vault_id

    @property
    def kms_configuration(self):
        r"""Gets the kms_configuration of this TokenVault.

        :return: The kms_configuration of this TokenVault.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.KmsConfiguration`
        """
        return self._kms_configuration

    @kms_configuration.setter
    def kms_configuration(self, kms_configuration):
        r"""Sets the kms_configuration of this TokenVault.

        :param kms_configuration: The kms_configuration of this TokenVault.
        :type kms_configuration: :class:`huaweicloudsdkagentidentity.v1.KmsConfiguration`
        """
        self._kms_configuration = kms_configuration

    @property
    def updated_at(self):
        r"""Gets the updated_at of this TokenVault.

        Timestamp in RFC 3339 format (UTC)

        :return: The updated_at of this TokenVault.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this TokenVault.

        Timestamp in RFC 3339 format (UTC)

        :param updated_at: The updated_at of this TokenVault.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this TokenVault.

        自定义标签列表。

        :return: The tags of this TokenVault.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TokenVault.

        自定义标签列表。

        :param tags: The tags of this TokenVault.
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
        if not isinstance(other, TokenVault):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
