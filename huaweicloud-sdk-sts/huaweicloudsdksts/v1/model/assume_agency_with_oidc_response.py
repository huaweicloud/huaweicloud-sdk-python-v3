# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumeAgencyWithOIDCResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_identity': 'str',
        'assumed_agency': 'AssumedAgencyWithFederationDto',
        'credentials': 'CredentialsDto',
        'audience': 'str',
        'provider': 'str',
        'subject_from_id_token': 'str'
    }

    attribute_map = {
        'source_identity': 'source_identity',
        'assumed_agency': 'assumed_agency',
        'credentials': 'credentials',
        'audience': 'audience',
        'provider': 'provider',
        'subject_from_id_token': 'subject_from_id_token'
    }

    def __init__(self, source_identity=None, assumed_agency=None, credentials=None, audience=None, provider=None, subject_from_id_token=None):
        r"""AssumeAgencyWithOIDCResponse

        The model defined in huaweicloud sdk

        :param source_identity: **参数解释**： 身份提供商返回的OIDC令牌中所申明的身份。  **取值范围**： 不涉及。 
        :type source_identity: str
        :param assumed_agency: 
        :type assumed_agency: :class:`huaweicloudsdksts.v1.AssumedAgencyWithFederationDto`
        :param credentials: 
        :type credentials: :class:`huaweicloudsdksts.v1.CredentialsDto`
        :param audience: **参数解释**： OIDC令牌的预期受众（也称为客户端ID），通常是分发给应用程序的客户端标识符。  **取值范围**： 不涉及。 
        :type audience: str
        :param provider: **参数解释**： 身份提供商的URN。  **取值范围**： 不涉及。 
        :type provider: str
        :param subject_from_id_token: **参数解释**： 由身份提供商返回的唯一用户标识符，即OIDC令牌中的sub(Subject)声明的值。  **取值范围**： 不涉及。 
        :type subject_from_id_token: str
        """
        
        super().__init__()

        self._source_identity = None
        self._assumed_agency = None
        self._credentials = None
        self._audience = None
        self._provider = None
        self._subject_from_id_token = None
        self.discriminator = None

        if source_identity is not None:
            self.source_identity = source_identity
        if assumed_agency is not None:
            self.assumed_agency = assumed_agency
        if credentials is not None:
            self.credentials = credentials
        if audience is not None:
            self.audience = audience
        if provider is not None:
            self.provider = provider
        if subject_from_id_token is not None:
            self.subject_from_id_token = subject_from_id_token

    @property
    def source_identity(self):
        r"""Gets the source_identity of this AssumeAgencyWithOIDCResponse.

        **参数解释**： 身份提供商返回的OIDC令牌中所申明的身份。  **取值范围**： 不涉及。 

        :return: The source_identity of this AssumeAgencyWithOIDCResponse.
        :rtype: str
        """
        return self._source_identity

    @source_identity.setter
    def source_identity(self, source_identity):
        r"""Sets the source_identity of this AssumeAgencyWithOIDCResponse.

        **参数解释**： 身份提供商返回的OIDC令牌中所申明的身份。  **取值范围**： 不涉及。 

        :param source_identity: The source_identity of this AssumeAgencyWithOIDCResponse.
        :type source_identity: str
        """
        self._source_identity = source_identity

    @property
    def assumed_agency(self):
        r"""Gets the assumed_agency of this AssumeAgencyWithOIDCResponse.

        :return: The assumed_agency of this AssumeAgencyWithOIDCResponse.
        :rtype: :class:`huaweicloudsdksts.v1.AssumedAgencyWithFederationDto`
        """
        return self._assumed_agency

    @assumed_agency.setter
    def assumed_agency(self, assumed_agency):
        r"""Sets the assumed_agency of this AssumeAgencyWithOIDCResponse.

        :param assumed_agency: The assumed_agency of this AssumeAgencyWithOIDCResponse.
        :type assumed_agency: :class:`huaweicloudsdksts.v1.AssumedAgencyWithFederationDto`
        """
        self._assumed_agency = assumed_agency

    @property
    def credentials(self):
        r"""Gets the credentials of this AssumeAgencyWithOIDCResponse.

        :return: The credentials of this AssumeAgencyWithOIDCResponse.
        :rtype: :class:`huaweicloudsdksts.v1.CredentialsDto`
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        r"""Sets the credentials of this AssumeAgencyWithOIDCResponse.

        :param credentials: The credentials of this AssumeAgencyWithOIDCResponse.
        :type credentials: :class:`huaweicloudsdksts.v1.CredentialsDto`
        """
        self._credentials = credentials

    @property
    def audience(self):
        r"""Gets the audience of this AssumeAgencyWithOIDCResponse.

        **参数解释**： OIDC令牌的预期受众（也称为客户端ID），通常是分发给应用程序的客户端标识符。  **取值范围**： 不涉及。 

        :return: The audience of this AssumeAgencyWithOIDCResponse.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        r"""Sets the audience of this AssumeAgencyWithOIDCResponse.

        **参数解释**： OIDC令牌的预期受众（也称为客户端ID），通常是分发给应用程序的客户端标识符。  **取值范围**： 不涉及。 

        :param audience: The audience of this AssumeAgencyWithOIDCResponse.
        :type audience: str
        """
        self._audience = audience

    @property
    def provider(self):
        r"""Gets the provider of this AssumeAgencyWithOIDCResponse.

        **参数解释**： 身份提供商的URN。  **取值范围**： 不涉及。 

        :return: The provider of this AssumeAgencyWithOIDCResponse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this AssumeAgencyWithOIDCResponse.

        **参数解释**： 身份提供商的URN。  **取值范围**： 不涉及。 

        :param provider: The provider of this AssumeAgencyWithOIDCResponse.
        :type provider: str
        """
        self._provider = provider

    @property
    def subject_from_id_token(self):
        r"""Gets the subject_from_id_token of this AssumeAgencyWithOIDCResponse.

        **参数解释**： 由身份提供商返回的唯一用户标识符，即OIDC令牌中的sub(Subject)声明的值。  **取值范围**： 不涉及。 

        :return: The subject_from_id_token of this AssumeAgencyWithOIDCResponse.
        :rtype: str
        """
        return self._subject_from_id_token

    @subject_from_id_token.setter
    def subject_from_id_token(self, subject_from_id_token):
        r"""Sets the subject_from_id_token of this AssumeAgencyWithOIDCResponse.

        **参数解释**： 由身份提供商返回的唯一用户标识符，即OIDC令牌中的sub(Subject)声明的值。  **取值范围**： 不涉及。 

        :param subject_from_id_token: The subject_from_id_token of this AssumeAgencyWithOIDCResponse.
        :type subject_from_id_token: str
        """
        self._subject_from_id_token = subject_from_id_token

    def to_dict(self):
        import warnings
        warnings.warn("AssumeAgencyWithOIDCResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, AssumeAgencyWithOIDCResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
