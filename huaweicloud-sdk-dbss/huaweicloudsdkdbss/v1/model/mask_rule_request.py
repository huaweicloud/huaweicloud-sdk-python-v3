# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MaskRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mask_regex': 'str',
        'mask_value': 'str',
        'rule_name': 'str'
    }

    attribute_map = {
        'mask_regex': 'mask_regex',
        'mask_value': 'mask_value',
        'rule_name': 'rule_name'
    }

    def __init__(self, mask_regex=None, mask_value=None, rule_name=None):
        r"""MaskRuleRequest

        The model defined in huaweicloud sdk

        :param mask_regex: 匹配正则
        :type mask_regex: str
        :param mask_value: 脱敏值
        :type mask_value: str
        :param rule_name: 隐私数据保护规则名称
        :type rule_name: str
        """
        
        

        self._mask_regex = None
        self._mask_value = None
        self._rule_name = None
        self.discriminator = None

        self.mask_regex = mask_regex
        self.mask_value = mask_value
        self.rule_name = rule_name

    @property
    def mask_regex(self):
        r"""Gets the mask_regex of this MaskRuleRequest.

        匹配正则

        :return: The mask_regex of this MaskRuleRequest.
        :rtype: str
        """
        return self._mask_regex

    @mask_regex.setter
    def mask_regex(self, mask_regex):
        r"""Sets the mask_regex of this MaskRuleRequest.

        匹配正则

        :param mask_regex: The mask_regex of this MaskRuleRequest.
        :type mask_regex: str
        """
        self._mask_regex = mask_regex

    @property
    def mask_value(self):
        r"""Gets the mask_value of this MaskRuleRequest.

        脱敏值

        :return: The mask_value of this MaskRuleRequest.
        :rtype: str
        """
        return self._mask_value

    @mask_value.setter
    def mask_value(self, mask_value):
        r"""Sets the mask_value of this MaskRuleRequest.

        脱敏值

        :param mask_value: The mask_value of this MaskRuleRequest.
        :type mask_value: str
        """
        self._mask_value = mask_value

    @property
    def rule_name(self):
        r"""Gets the rule_name of this MaskRuleRequest.

        隐私数据保护规则名称

        :return: The rule_name of this MaskRuleRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this MaskRuleRequest.

        隐私数据保护规则名称

        :param rule_name: The rule_name of this MaskRuleRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

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
        if not isinstance(other, MaskRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
