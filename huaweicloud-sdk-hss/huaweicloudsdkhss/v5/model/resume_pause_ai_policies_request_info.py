# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResumePauseAiPoliciesRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'policy_id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'policy_id': 'policy_id'
    }

    def __init__(self, enabled=None, policy_id=None):
        r"""ResumePauseAiPoliciesRequestInfo

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**: 是否启用 **约束限制**: 必填 **取值范围**: - false：否 - true：是  **默认取值**: 不涉及 
        :type enabled: bool
        :param policy_id: **参数解释**: 策略ID **约束限制**: 必填 **取值范围**: 字符长度1-20位 **默认取值**: 不涉及 
        :type policy_id: str
        """
        
        

        self._enabled = None
        self._policy_id = None
        self.discriminator = None

        self.enabled = enabled
        self.policy_id = policy_id

    @property
    def enabled(self):
        r"""Gets the enabled of this ResumePauseAiPoliciesRequestInfo.

        **参数解释**: 是否启用 **约束限制**: 必填 **取值范围**: - false：否 - true：是  **默认取值**: 不涉及 

        :return: The enabled of this ResumePauseAiPoliciesRequestInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ResumePauseAiPoliciesRequestInfo.

        **参数解释**: 是否启用 **约束限制**: 必填 **取值范围**: - false：否 - true：是  **默认取值**: 不涉及 

        :param enabled: The enabled of this ResumePauseAiPoliciesRequestInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ResumePauseAiPoliciesRequestInfo.

        **参数解释**: 策略ID **约束限制**: 必填 **取值范围**: 字符长度1-20位 **默认取值**: 不涉及 

        :return: The policy_id of this ResumePauseAiPoliciesRequestInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ResumePauseAiPoliciesRequestInfo.

        **参数解释**: 策略ID **约束限制**: 必填 **取值范围**: 字符长度1-20位 **默认取值**: 不涉及 

        :param policy_id: The policy_id of this ResumePauseAiPoliciesRequestInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

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
        if not isinstance(other, ResumePauseAiPoliciesRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
