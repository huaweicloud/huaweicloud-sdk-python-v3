# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAiGuardRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_ids': 'list[str]'
    }

    attribute_map = {
        'rule_ids': 'rule_ids'
    }

    def __init__(self, rule_ids=None):
        r"""BatchDeleteAiGuardRuleResponse

        The model defined in huaweicloud sdk

        :param rule_ids: 已删除的规则ID列表
        :type rule_ids: list[str]
        """
        
        super().__init__()

        self._rule_ids = None
        self.discriminator = None

        if rule_ids is not None:
            self.rule_ids = rule_ids

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this BatchDeleteAiGuardRuleResponse.

        已删除的规则ID列表

        :return: The rule_ids of this BatchDeleteAiGuardRuleResponse.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this BatchDeleteAiGuardRuleResponse.

        已删除的规则ID列表

        :param rule_ids: The rule_ids of this BatchDeleteAiGuardRuleResponse.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteAiGuardRuleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteAiGuardRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
