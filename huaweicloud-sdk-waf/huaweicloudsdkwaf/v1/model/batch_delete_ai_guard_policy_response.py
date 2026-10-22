# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAiGuardPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_ids': 'list[str]'
    }

    attribute_map = {
        'policy_ids': 'policy_ids'
    }

    def __init__(self, policy_ids=None):
        r"""BatchDeleteAiGuardPolicyResponse

        The model defined in huaweicloud sdk

        :param policy_ids: 已删除的策略 ID 列表
        :type policy_ids: list[str]
        """
        
        super().__init__()

        self._policy_ids = None
        self.discriminator = None

        if policy_ids is not None:
            self.policy_ids = policy_ids

    @property
    def policy_ids(self):
        r"""Gets the policy_ids of this BatchDeleteAiGuardPolicyResponse.

        已删除的策略 ID 列表

        :return: The policy_ids of this BatchDeleteAiGuardPolicyResponse.
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        r"""Sets the policy_ids of this BatchDeleteAiGuardPolicyResponse.

        已删除的策略 ID 列表

        :param policy_ids: The policy_ids of this BatchDeleteAiGuardPolicyResponse.
        :type policy_ids: list[str]
        """
        self._policy_ids = policy_ids

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteAiGuardPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteAiGuardPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
