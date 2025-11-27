# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateAntileakageRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'category': 'str',
        'contents': 'list[str]',
        'action': 'LeakageListInfoAction',
        'description': 'str',
        'policy_rule_ids': 'list[PolicyRuleIdRequestBodyPolicyRuleIds]'
    }

    attribute_map = {
        'url': 'url',
        'category': 'category',
        'contents': 'contents',
        'action': 'action',
        'description': 'description',
        'policy_rule_ids': 'policy_rule_ids'
    }

    def __init__(self, url=None, category=None, contents=None, action=None, description=None, policy_rule_ids=None):
        r"""BatchUpdateAntileakageRuleRequestBody

        The model defined in huaweicloud sdk

        :param url: 规则应用的url
        :type url: str
        :param category: 类别（响应码：code，敏感信息：sensitive）
        :type category: str
        :param contents: 内容（http状态码：400 、401、402 、 403 、404 、 405 、500 、501 、502 、503、 504 、507；手机：phone、身份证号：id_card、邮箱：email）
        :type contents: list[str]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.LeakageListInfoAction`
        :param description: 规则描述
        :type description: str
        :param policy_rule_ids: **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        
        

        self._url = None
        self._category = None
        self._contents = None
        self._action = None
        self._description = None
        self._policy_rule_ids = None
        self.discriminator = None

        self.url = url
        self.category = category
        self.contents = contents
        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        if policy_rule_ids is not None:
            self.policy_rule_ids = policy_rule_ids

    @property
    def url(self):
        r"""Gets the url of this BatchUpdateAntileakageRuleRequestBody.

        规则应用的url

        :return: The url of this BatchUpdateAntileakageRuleRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this BatchUpdateAntileakageRuleRequestBody.

        规则应用的url

        :param url: The url of this BatchUpdateAntileakageRuleRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def category(self):
        r"""Gets the category of this BatchUpdateAntileakageRuleRequestBody.

        类别（响应码：code，敏感信息：sensitive）

        :return: The category of this BatchUpdateAntileakageRuleRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this BatchUpdateAntileakageRuleRequestBody.

        类别（响应码：code，敏感信息：sensitive）

        :param category: The category of this BatchUpdateAntileakageRuleRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def contents(self):
        r"""Gets the contents of this BatchUpdateAntileakageRuleRequestBody.

        内容（http状态码：400 、401、402 、 403 、404 、 405 、500 、501 、502 、503、 504 、507；手机：phone、身份证号：id_card、邮箱：email）

        :return: The contents of this BatchUpdateAntileakageRuleRequestBody.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this BatchUpdateAntileakageRuleRequestBody.

        内容（http状态码：400 、401、402 、 403 、404 、 405 、500 、501 、502 、503、 504 、507；手机：phone、身份证号：id_card、邮箱：email）

        :param contents: The contents of this BatchUpdateAntileakageRuleRequestBody.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def action(self):
        r"""Gets the action of this BatchUpdateAntileakageRuleRequestBody.

        :return: The action of this BatchUpdateAntileakageRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.LeakageListInfoAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchUpdateAntileakageRuleRequestBody.

        :param action: The action of this BatchUpdateAntileakageRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.LeakageListInfoAction`
        """
        self._action = action

    @property
    def description(self):
        r"""Gets the description of this BatchUpdateAntileakageRuleRequestBody.

        规则描述

        :return: The description of this BatchUpdateAntileakageRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchUpdateAntileakageRuleRequestBody.

        规则描述

        :param description: The description of this BatchUpdateAntileakageRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def policy_rule_ids(self):
        r"""Gets the policy_rule_ids of this BatchUpdateAntileakageRuleRequestBody.

        **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_rule_ids of this BatchUpdateAntileakageRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        return self._policy_rule_ids

    @policy_rule_ids.setter
    def policy_rule_ids(self, policy_rule_ids):
        r"""Sets the policy_rule_ids of this BatchUpdateAntileakageRuleRequestBody.

        **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_rule_ids: The policy_rule_ids of this BatchUpdateAntileakageRuleRequestBody.
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        self._policy_rule_ids = policy_rule_ids

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
        if not isinstance(other, BatchUpdateAntileakageRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
