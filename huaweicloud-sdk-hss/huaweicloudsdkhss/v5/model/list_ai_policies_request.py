# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_id': 'str'
    }

    attribute_map = {
        'policy_group_id': 'policy_group_id'
    }

    def __init__(self, policy_group_id=None):
        r"""ListAiPoliciesRequest

        The model defined in huaweicloud sdk

        :param policy_group_id: **参数解释**： 策略组ID **约束限制**： 不涉及 **取值范围**： 字符长度1-20位 **默认取值**： 不涉及 
        :type policy_group_id: str
        """
        
        

        self._policy_group_id = None
        self.discriminator = None

        self.policy_group_id = policy_group_id

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListAiPoliciesRequest.

        **参数解释**： 策略组ID **约束限制**： 不涉及 **取值范围**： 字符长度1-20位 **默认取值**： 不涉及 

        :return: The policy_group_id of this ListAiPoliciesRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListAiPoliciesRequest.

        **参数解释**： 策略组ID **约束限制**： 不涉及 **取值范围**： 字符长度1-20位 **默认取值**： 不涉及 

        :param policy_group_id: The policy_group_id of this ListAiPoliciesRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

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
        if not isinstance(other, ListAiPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
