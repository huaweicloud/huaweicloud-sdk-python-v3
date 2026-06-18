# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumeAgencyWithSAMLResponse(SdkResponse):

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
        'issuer': 'str',
        'name_qualifier': 'str',
        'subject': 'str',
        'subject_type': 'str'
    }

    attribute_map = {
        'source_identity': 'source_identity',
        'assumed_agency': 'assumed_agency',
        'credentials': 'credentials',
        'audience': 'audience',
        'issuer': 'issuer',
        'name_qualifier': 'name_qualifier',
        'subject': 'subject',
        'subject_type': 'subject_type'
    }

    def __init__(self, source_identity=None, assumed_agency=None, credentials=None, audience=None, issuer=None, name_qualifier=None, subject=None, subject_type=None):
        r"""AssumeAgencyWithSAMLResponse

        The model defined in huaweicloud sdk

        :param source_identity: **参数解释**： SAML断言中SourceIdentity属性值所申明的身份。  **约束限制**： 不涉及。 
        :type source_identity: str
        :param assumed_agency: 
        :type assumed_agency: :class:`huaweicloudsdksts.v1.AssumedAgencyWithFederationDto`
        :param credentials: 
        :type credentials: :class:`huaweicloudsdksts.v1.CredentialsDto`
        :param audience: **参数解释**：  SAML断言中SubjectConfirmationData元素的Recipient属性值。  **约束限制**： 不涉及。 
        :type audience: str
        :param issuer: **参数解释**： SAML断言中Issuer元素的值。  **约束限制**： 不涉及。 
        :type issuer: str
        :param name_qualifier: **参数解释**： 以下三部分的哈希值：issuer、华为云账号的Account ID以及IAM中SAML提供商的名称（URN的最后一部分）。name_qualifier和subject的组合可用于唯一标识用户。下面的伪代码展示了哈希值的计算方式：BASE64 ( SHA1 ( \&quot;https://example.com/saml\&quot; + \&quot;8c1eef3a241945f69c3d3axxxxxxxxxx\&quot; + \&quot;/MySAMLIdPName\&quot; ) )  **约束限制**： 不涉及。 
        :type name_qualifier: str
        :param subject: **参数解释**：  SAML断言中Subject元素的NameID元素的值。  **约束限制**： 不涉及。 
        :type subject: str
        :param subject_type: **参数解释**：  NameID的格式，由SAML断言中NameID元素的Format属性定义。格式的典型示例是transient（临时）或persistent（持久）。 如果该格式包含前缀urn:oasis:names:tc:SAML:2.0:nameid-format，该前缀将被移除。例如，urn:oasis:names:tc:SAML:2.0:nameid-format:transient将作为transient返回。如果格式包含任何其他前缀，则直接返回该格式而不作任何修改。  **约束限制**： 不涉及。 
        :type subject_type: str
        """
        
        super().__init__()

        self._source_identity = None
        self._assumed_agency = None
        self._credentials = None
        self._audience = None
        self._issuer = None
        self._name_qualifier = None
        self._subject = None
        self._subject_type = None
        self.discriminator = None

        if source_identity is not None:
            self.source_identity = source_identity
        if assumed_agency is not None:
            self.assumed_agency = assumed_agency
        if credentials is not None:
            self.credentials = credentials
        if audience is not None:
            self.audience = audience
        if issuer is not None:
            self.issuer = issuer
        if name_qualifier is not None:
            self.name_qualifier = name_qualifier
        if subject is not None:
            self.subject = subject
        if subject_type is not None:
            self.subject_type = subject_type

    @property
    def source_identity(self):
        r"""Gets the source_identity of this AssumeAgencyWithSAMLResponse.

        **参数解释**： SAML断言中SourceIdentity属性值所申明的身份。  **约束限制**： 不涉及。 

        :return: The source_identity of this AssumeAgencyWithSAMLResponse.
        :rtype: str
        """
        return self._source_identity

    @source_identity.setter
    def source_identity(self, source_identity):
        r"""Sets the source_identity of this AssumeAgencyWithSAMLResponse.

        **参数解释**： SAML断言中SourceIdentity属性值所申明的身份。  **约束限制**： 不涉及。 

        :param source_identity: The source_identity of this AssumeAgencyWithSAMLResponse.
        :type source_identity: str
        """
        self._source_identity = source_identity

    @property
    def assumed_agency(self):
        r"""Gets the assumed_agency of this AssumeAgencyWithSAMLResponse.

        :return: The assumed_agency of this AssumeAgencyWithSAMLResponse.
        :rtype: :class:`huaweicloudsdksts.v1.AssumedAgencyWithFederationDto`
        """
        return self._assumed_agency

    @assumed_agency.setter
    def assumed_agency(self, assumed_agency):
        r"""Sets the assumed_agency of this AssumeAgencyWithSAMLResponse.

        :param assumed_agency: The assumed_agency of this AssumeAgencyWithSAMLResponse.
        :type assumed_agency: :class:`huaweicloudsdksts.v1.AssumedAgencyWithFederationDto`
        """
        self._assumed_agency = assumed_agency

    @property
    def credentials(self):
        r"""Gets the credentials of this AssumeAgencyWithSAMLResponse.

        :return: The credentials of this AssumeAgencyWithSAMLResponse.
        :rtype: :class:`huaweicloudsdksts.v1.CredentialsDto`
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        r"""Sets the credentials of this AssumeAgencyWithSAMLResponse.

        :param credentials: The credentials of this AssumeAgencyWithSAMLResponse.
        :type credentials: :class:`huaweicloudsdksts.v1.CredentialsDto`
        """
        self._credentials = credentials

    @property
    def audience(self):
        r"""Gets the audience of this AssumeAgencyWithSAMLResponse.

        **参数解释**：  SAML断言中SubjectConfirmationData元素的Recipient属性值。  **约束限制**： 不涉及。 

        :return: The audience of this AssumeAgencyWithSAMLResponse.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        r"""Sets the audience of this AssumeAgencyWithSAMLResponse.

        **参数解释**：  SAML断言中SubjectConfirmationData元素的Recipient属性值。  **约束限制**： 不涉及。 

        :param audience: The audience of this AssumeAgencyWithSAMLResponse.
        :type audience: str
        """
        self._audience = audience

    @property
    def issuer(self):
        r"""Gets the issuer of this AssumeAgencyWithSAMLResponse.

        **参数解释**： SAML断言中Issuer元素的值。  **约束限制**： 不涉及。 

        :return: The issuer of this AssumeAgencyWithSAMLResponse.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        r"""Sets the issuer of this AssumeAgencyWithSAMLResponse.

        **参数解释**： SAML断言中Issuer元素的值。  **约束限制**： 不涉及。 

        :param issuer: The issuer of this AssumeAgencyWithSAMLResponse.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def name_qualifier(self):
        r"""Gets the name_qualifier of this AssumeAgencyWithSAMLResponse.

        **参数解释**： 以下三部分的哈希值：issuer、华为云账号的Account ID以及IAM中SAML提供商的名称（URN的最后一部分）。name_qualifier和subject的组合可用于唯一标识用户。下面的伪代码展示了哈希值的计算方式：BASE64 ( SHA1 ( \"https://example.com/saml\" + \"8c1eef3a241945f69c3d3axxxxxxxxxx\" + \"/MySAMLIdPName\" ) )  **约束限制**： 不涉及。 

        :return: The name_qualifier of this AssumeAgencyWithSAMLResponse.
        :rtype: str
        """
        return self._name_qualifier

    @name_qualifier.setter
    def name_qualifier(self, name_qualifier):
        r"""Sets the name_qualifier of this AssumeAgencyWithSAMLResponse.

        **参数解释**： 以下三部分的哈希值：issuer、华为云账号的Account ID以及IAM中SAML提供商的名称（URN的最后一部分）。name_qualifier和subject的组合可用于唯一标识用户。下面的伪代码展示了哈希值的计算方式：BASE64 ( SHA1 ( \"https://example.com/saml\" + \"8c1eef3a241945f69c3d3axxxxxxxxxx\" + \"/MySAMLIdPName\" ) )  **约束限制**： 不涉及。 

        :param name_qualifier: The name_qualifier of this AssumeAgencyWithSAMLResponse.
        :type name_qualifier: str
        """
        self._name_qualifier = name_qualifier

    @property
    def subject(self):
        r"""Gets the subject of this AssumeAgencyWithSAMLResponse.

        **参数解释**：  SAML断言中Subject元素的NameID元素的值。  **约束限制**： 不涉及。 

        :return: The subject of this AssumeAgencyWithSAMLResponse.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this AssumeAgencyWithSAMLResponse.

        **参数解释**：  SAML断言中Subject元素的NameID元素的值。  **约束限制**： 不涉及。 

        :param subject: The subject of this AssumeAgencyWithSAMLResponse.
        :type subject: str
        """
        self._subject = subject

    @property
    def subject_type(self):
        r"""Gets the subject_type of this AssumeAgencyWithSAMLResponse.

        **参数解释**：  NameID的格式，由SAML断言中NameID元素的Format属性定义。格式的典型示例是transient（临时）或persistent（持久）。 如果该格式包含前缀urn:oasis:names:tc:SAML:2.0:nameid-format，该前缀将被移除。例如，urn:oasis:names:tc:SAML:2.0:nameid-format:transient将作为transient返回。如果格式包含任何其他前缀，则直接返回该格式而不作任何修改。  **约束限制**： 不涉及。 

        :return: The subject_type of this AssumeAgencyWithSAMLResponse.
        :rtype: str
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        r"""Sets the subject_type of this AssumeAgencyWithSAMLResponse.

        **参数解释**：  NameID的格式，由SAML断言中NameID元素的Format属性定义。格式的典型示例是transient（临时）或persistent（持久）。 如果该格式包含前缀urn:oasis:names:tc:SAML:2.0:nameid-format，该前缀将被移除。例如，urn:oasis:names:tc:SAML:2.0:nameid-format:transient将作为transient返回。如果格式包含任何其他前缀，则直接返回该格式而不作任何修改。  **约束限制**： 不涉及。 

        :param subject_type: The subject_type of this AssumeAgencyWithSAMLResponse.
        :type subject_type: str
        """
        self._subject_type = subject_type

    def to_dict(self):
        import warnings
        warnings.warn("AssumeAgencyWithSAMLResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, AssumeAgencyWithSAMLResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
