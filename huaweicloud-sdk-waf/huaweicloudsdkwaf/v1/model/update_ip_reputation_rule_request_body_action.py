# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIpReputationRuleRequestBodyAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str'
    }

    attribute_map = {
        'category': 'category'
    }

    def __init__(self, category=None):
        r"""UpdateIpReputationRuleRequestBodyAction

        The model defined in huaweicloud sdk

        :param category: **参数解释：** 动作类型（如captcha表示验证码） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type category: str
        """
        
        

        self._category = None
        self.discriminator = None

        if category is not None:
            self.category = category

    @property
    def category(self):
        r"""Gets the category of this UpdateIpReputationRuleRequestBodyAction.

        **参数解释：** 动作类型（如captcha表示验证码） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The category of this UpdateIpReputationRuleRequestBodyAction.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this UpdateIpReputationRuleRequestBodyAction.

        **参数解释：** 动作类型（如captcha表示验证码） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param category: The category of this UpdateIpReputationRuleRequestBodyAction.
        :type category: str
        """
        self._category = category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateIpReputationRuleRequestBodyAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
