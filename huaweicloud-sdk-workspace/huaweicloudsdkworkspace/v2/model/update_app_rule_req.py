# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppRuleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'rule': 'Rule'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'rule': 'rule'
    }

    def __init__(self, name=None, description=None, rule=None):
        r"""UpdateAppRuleReq

        The model defined in huaweicloud sdk

        :param name: 规则名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度1~64个字符。
        :type name: str
        :param description: 规则描述： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。
        :type description: str
        :param rule: 
        :type rule: :class:`huaweicloudsdkworkspace.v2.Rule`
        """
        
        

        self._name = None
        self._description = None
        self._rule = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if rule is not None:
            self.rule = rule

    @property
    def name(self):
        r"""Gets the name of this UpdateAppRuleReq.

        规则名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度1~64个字符。

        :return: The name of this UpdateAppRuleReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateAppRuleReq.

        规则名称： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度1~64个字符。

        :param name: The name of this UpdateAppRuleReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateAppRuleReq.

        规则描述： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。

        :return: The description of this UpdateAppRuleReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAppRuleReq.

        规则描述： 1. 名称允许可见字符或空格，不可为全空格。 2. 长度0~128个字符。

        :param description: The description of this UpdateAppRuleReq.
        :type description: str
        """
        self._description = description

    @property
    def rule(self):
        r"""Gets the rule of this UpdateAppRuleReq.

        :return: The rule of this UpdateAppRuleReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Rule`
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this UpdateAppRuleReq.

        :param rule: The rule of this UpdateAppRuleReq.
        :type rule: :class:`huaweicloudsdkworkspace.v2.Rule`
        """
        self._rule = rule

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
        if not isinstance(other, UpdateAppRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
