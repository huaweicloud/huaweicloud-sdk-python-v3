# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumeAgencyWithSAMLReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duration_seconds': 'int',
        'policy': 'str',
        'policy_ids': 'list[str]',
        'provider_urn': 'str',
        'agency_urn': 'str',
        'saml_assertion': 'str'
    }

    attribute_map = {
        'duration_seconds': 'duration_seconds',
        'policy': 'policy',
        'policy_ids': 'policy_ids',
        'provider_urn': 'provider_urn',
        'agency_urn': 'agency_urn',
        'saml_assertion': 'saml_assertion'
    }

    def __init__(self, duration_seconds=None, policy=None, policy_ids=None, provider_urn=None, agency_urn=None, saml_assertion=None):
        r"""AssumeAgencyWithSAMLReqBody

        The model defined in huaweicloud sdk

        :param duration_seconds: **参数解释**： 获得的临时安全凭证的有效时间（单位：秒）。  **约束限制**： 获得的临时安全凭证的有效时间（单位：秒）。请注意，该时间需要小于信任委托本身设置的最大会话持续时间。同时最终的会话持续时间以duration_seconds，  SAML身份验证响应中SessionNotOnOrAfter值和SessionDuration值三者中较短的一个为准。  **取值范围**： 取值范围为[900,43200]。  **默认取值**： 默认值为3600。 
        :type duration_seconds: int
        :param policy: **参数解释**： 自定义策略，限制本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。  **约束限制**： 本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。 长度范围为[2,2048]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 
        :type policy: str
        :param policy_ids: **参数解释**： 预置策略列表，限制本次会话获得的临时安全凭证的权限范围不会超过该预置策略指定的权限。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 
        :type policy_ids: list[str]
        :param provider_urn: **参数解释**： SAML提供商的URN。  **约束限制**： 长度范围为[0,1500]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 
        :type provider_urn: str
        :param agency_urn: **参数解释**： 目标信任委托的URN。  **约束限制**： 长度范围为[0,1500]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 
        :type agency_urn: str
        :param saml_assertion: **参数解释**： 由SAML身份提供商提供的Base64编码的SAML身份验证响应。  **约束限制**： 长度范围为[4,100000]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 
        :type saml_assertion: str
        """
        
        

        self._duration_seconds = None
        self._policy = None
        self._policy_ids = None
        self._provider_urn = None
        self._agency_urn = None
        self._saml_assertion = None
        self.discriminator = None

        if duration_seconds is not None:
            self.duration_seconds = duration_seconds
        if policy is not None:
            self.policy = policy
        if policy_ids is not None:
            self.policy_ids = policy_ids
        self.provider_urn = provider_urn
        self.agency_urn = agency_urn
        self.saml_assertion = saml_assertion

    @property
    def duration_seconds(self):
        r"""Gets the duration_seconds of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 获得的临时安全凭证的有效时间（单位：秒）。  **约束限制**： 获得的临时安全凭证的有效时间（单位：秒）。请注意，该时间需要小于信任委托本身设置的最大会话持续时间。同时最终的会话持续时间以duration_seconds，  SAML身份验证响应中SessionNotOnOrAfter值和SessionDuration值三者中较短的一个为准。  **取值范围**： 取值范围为[900,43200]。  **默认取值**： 默认值为3600。 

        :return: The duration_seconds of this AssumeAgencyWithSAMLReqBody.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        r"""Sets the duration_seconds of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 获得的临时安全凭证的有效时间（单位：秒）。  **约束限制**： 获得的临时安全凭证的有效时间（单位：秒）。请注意，该时间需要小于信任委托本身设置的最大会话持续时间。同时最终的会话持续时间以duration_seconds，  SAML身份验证响应中SessionNotOnOrAfter值和SessionDuration值三者中较短的一个为准。  **取值范围**： 取值范围为[900,43200]。  **默认取值**： 默认值为3600。 

        :param duration_seconds: The duration_seconds of this AssumeAgencyWithSAMLReqBody.
        :type duration_seconds: int
        """
        self._duration_seconds = duration_seconds

    @property
    def policy(self):
        r"""Gets the policy of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 自定义策略，限制本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。  **约束限制**： 本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。 长度范围为[2,2048]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :return: The policy of this AssumeAgencyWithSAMLReqBody.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 自定义策略，限制本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。  **约束限制**： 本次会话获得的临时安全凭证的权限范围不会超过该自定义策略指定的权限。 长度范围为[2,2048]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :param policy: The policy of this AssumeAgencyWithSAMLReqBody.
        :type policy: str
        """
        self._policy = policy

    @property
    def policy_ids(self):
        r"""Gets the policy_ids of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 预置策略列表，限制本次会话获得的临时安全凭证的权限范围不会超过该预置策略指定的权限。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :return: The policy_ids of this AssumeAgencyWithSAMLReqBody.
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        r"""Sets the policy_ids of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 预置策略列表，限制本次会话获得的临时安全凭证的权限范围不会超过该预置策略指定的权限。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :param policy_ids: The policy_ids of this AssumeAgencyWithSAMLReqBody.
        :type policy_ids: list[str]
        """
        self._policy_ids = policy_ids

    @property
    def provider_urn(self):
        r"""Gets the provider_urn of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： SAML提供商的URN。  **约束限制**： 长度范围为[0,1500]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :return: The provider_urn of this AssumeAgencyWithSAMLReqBody.
        :rtype: str
        """
        return self._provider_urn

    @provider_urn.setter
    def provider_urn(self, provider_urn):
        r"""Sets the provider_urn of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： SAML提供商的URN。  **约束限制**： 长度范围为[0,1500]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :param provider_urn: The provider_urn of this AssumeAgencyWithSAMLReqBody.
        :type provider_urn: str
        """
        self._provider_urn = provider_urn

    @property
    def agency_urn(self):
        r"""Gets the agency_urn of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 目标信任委托的URN。  **约束限制**： 长度范围为[0,1500]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :return: The agency_urn of this AssumeAgencyWithSAMLReqBody.
        :rtype: str
        """
        return self._agency_urn

    @agency_urn.setter
    def agency_urn(self, agency_urn):
        r"""Sets the agency_urn of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 目标信任委托的URN。  **约束限制**： 长度范围为[0,1500]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :param agency_urn: The agency_urn of this AssumeAgencyWithSAMLReqBody.
        :type agency_urn: str
        """
        self._agency_urn = agency_urn

    @property
    def saml_assertion(self):
        r"""Gets the saml_assertion of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 由SAML身份提供商提供的Base64编码的SAML身份验证响应。  **约束限制**： 长度范围为[4,100000]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :return: The saml_assertion of this AssumeAgencyWithSAMLReqBody.
        :rtype: str
        """
        return self._saml_assertion

    @saml_assertion.setter
    def saml_assertion(self, saml_assertion):
        r"""Sets the saml_assertion of this AssumeAgencyWithSAMLReqBody.

        **参数解释**： 由SAML身份提供商提供的Base64编码的SAML身份验证响应。  **约束限制**： 长度范围为[4,100000]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :param saml_assertion: The saml_assertion of this AssumeAgencyWithSAMLReqBody.
        :type saml_assertion: str
        """
        self._saml_assertion = saml_assertion

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
        if not isinstance(other, AssumeAgencyWithSAMLReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
