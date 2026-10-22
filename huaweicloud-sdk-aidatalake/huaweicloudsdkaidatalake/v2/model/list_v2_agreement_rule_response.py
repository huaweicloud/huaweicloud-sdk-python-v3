# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2AgreementRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreement_rules': 'list[V2AgreementRule]',
        'total': 'int'
    }

    attribute_map = {
        'agreement_rules': 'agreement_rules',
        'total': 'total'
    }

    def __init__(self, agreement_rules=None, total=None):
        r"""ListV2AgreementRuleResponse

        The model defined in huaweicloud sdk

        :param agreement_rules: **参数解释**：系统协议列表，每个元素为一个V2AgreementRule对象，包含协议名称、展示名称、版本、链接等信息。
        :type agreement_rules: list[:class:`huaweicloudsdkaidatalake.v2.V2AgreementRule`]
        :param total: **参数解释**：系统协议总数。 **取值范围**：0~1000。
        :type total: int
        """
        
        super().__init__()

        self._agreement_rules = None
        self._total = None
        self.discriminator = None

        if agreement_rules is not None:
            self.agreement_rules = agreement_rules
        if total is not None:
            self.total = total

    @property
    def agreement_rules(self):
        r"""Gets the agreement_rules of this ListV2AgreementRuleResponse.

        **参数解释**：系统协议列表，每个元素为一个V2AgreementRule对象，包含协议名称、展示名称、版本、链接等信息。

        :return: The agreement_rules of this ListV2AgreementRuleResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2AgreementRule`]
        """
        return self._agreement_rules

    @agreement_rules.setter
    def agreement_rules(self, agreement_rules):
        r"""Sets the agreement_rules of this ListV2AgreementRuleResponse.

        **参数解释**：系统协议列表，每个元素为一个V2AgreementRule对象，包含协议名称、展示名称、版本、链接等信息。

        :param agreement_rules: The agreement_rules of this ListV2AgreementRuleResponse.
        :type agreement_rules: list[:class:`huaweicloudsdkaidatalake.v2.V2AgreementRule`]
        """
        self._agreement_rules = agreement_rules

    @property
    def total(self):
        r"""Gets the total of this ListV2AgreementRuleResponse.

        **参数解释**：系统协议总数。 **取值范围**：0~1000。

        :return: The total of this ListV2AgreementRuleResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2AgreementRuleResponse.

        **参数解释**：系统协议总数。 **取值范围**：0~1000。

        :param total: The total of this ListV2AgreementRuleResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListV2AgreementRuleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2AgreementRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
