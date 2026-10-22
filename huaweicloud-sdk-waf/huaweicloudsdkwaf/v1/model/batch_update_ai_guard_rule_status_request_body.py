# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateAiGuardRuleStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_ids': 'list[str]',
        'status': 'str',
        'template_ids': 'list[str]'
    }

    attribute_map = {
        'rule_ids': 'rule_ids',
        'status': 'status',
        'template_ids': 'template_ids'
    }

    def __init__(self, rule_ids=None, status=None, template_ids=None):
        r"""BatchUpdateAiGuardRuleStatusRequestBody

        The model defined in huaweicloud sdk

        :param rule_ids: 规则ID列表
        :type rule_ids: list[str]
        :param status: 规则状态，可选：enable(启用), disable(禁用)，当disable时，只有rule_ids，而enable时至少有rule_ids或者temlate_ids
        :type status: str
        :param template_ids: 系统规则的id
        :type template_ids: list[str]
        """
        
        

        self._rule_ids = None
        self._status = None
        self._template_ids = None
        self.discriminator = None

        if rule_ids is not None:
            self.rule_ids = rule_ids
        self.status = status
        if template_ids is not None:
            self.template_ids = template_ids

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this BatchUpdateAiGuardRuleStatusRequestBody.

        规则ID列表

        :return: The rule_ids of this BatchUpdateAiGuardRuleStatusRequestBody.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this BatchUpdateAiGuardRuleStatusRequestBody.

        规则ID列表

        :param rule_ids: The rule_ids of this BatchUpdateAiGuardRuleStatusRequestBody.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

    @property
    def status(self):
        r"""Gets the status of this BatchUpdateAiGuardRuleStatusRequestBody.

        规则状态，可选：enable(启用), disable(禁用)，当disable时，只有rule_ids，而enable时至少有rule_ids或者temlate_ids

        :return: The status of this BatchUpdateAiGuardRuleStatusRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchUpdateAiGuardRuleStatusRequestBody.

        规则状态，可选：enable(启用), disable(禁用)，当disable时，只有rule_ids，而enable时至少有rule_ids或者temlate_ids

        :param status: The status of this BatchUpdateAiGuardRuleStatusRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def template_ids(self):
        r"""Gets the template_ids of this BatchUpdateAiGuardRuleStatusRequestBody.

        系统规则的id

        :return: The template_ids of this BatchUpdateAiGuardRuleStatusRequestBody.
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        r"""Sets the template_ids of this BatchUpdateAiGuardRuleStatusRequestBody.

        系统规则的id

        :param template_ids: The template_ids of this BatchUpdateAiGuardRuleStatusRequestBody.
        :type template_ids: list[str]
        """
        self._template_ids = template_ids

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
        if not isinstance(other, BatchUpdateAiGuardRuleStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
