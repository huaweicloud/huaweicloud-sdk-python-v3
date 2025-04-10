# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulCheckerRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checker_rule': 'str',
        'checker_entry': 'str',
        'checker_result': 'str',
        'checker_stack': 'str',
        'privacy_policy_evidences': 'str',
        '_pass': 'bool',
        'rectify_suggestion': 'str'
    }

    attribute_map = {
        'checker_rule': 'checker_rule',
        'checker_entry': 'checker_entry',
        'checker_result': 'checker_result',
        'checker_stack': 'checker_stack',
        'privacy_policy_evidences': 'privacy_policy_evidences',
        '_pass': 'pass',
        'rectify_suggestion': 'rectify_suggestion'
    }

    def __init__(self, checker_rule=None, checker_entry=None, checker_result=None, checker_stack=None, privacy_policy_evidences=None, _pass=None, rectify_suggestion=None):
        r"""VulCheckerRule

        The model defined in huaweicloud sdk

        :param checker_rule: 检测项
        :type checker_rule: str
        :param checker_entry: 规范检测项条目
        :type checker_entry: str
        :param checker_result: 规则检测项结果
        :type checker_result: str
        :param checker_stack: 调用栈信息
        :type checker_stack: str
        :param privacy_policy_evidences: 隐私声明
        :type privacy_policy_evidences: str
        :param _pass: 是否通过
        :type _pass: bool
        :param rectify_suggestion: 修复建议
        :type rectify_suggestion: str
        """
        
        

        self._checker_rule = None
        self._checker_entry = None
        self._checker_result = None
        self._checker_stack = None
        self._privacy_policy_evidences = None
        self.__pass = None
        self._rectify_suggestion = None
        self.discriminator = None

        if checker_rule is not None:
            self.checker_rule = checker_rule
        if checker_entry is not None:
            self.checker_entry = checker_entry
        if checker_result is not None:
            self.checker_result = checker_result
        if checker_stack is not None:
            self.checker_stack = checker_stack
        if privacy_policy_evidences is not None:
            self.privacy_policy_evidences = privacy_policy_evidences
        if _pass is not None:
            self._pass = _pass
        if rectify_suggestion is not None:
            self.rectify_suggestion = rectify_suggestion

    @property
    def checker_rule(self):
        r"""Gets the checker_rule of this VulCheckerRule.

        检测项

        :return: The checker_rule of this VulCheckerRule.
        :rtype: str
        """
        return self._checker_rule

    @checker_rule.setter
    def checker_rule(self, checker_rule):
        r"""Sets the checker_rule of this VulCheckerRule.

        检测项

        :param checker_rule: The checker_rule of this VulCheckerRule.
        :type checker_rule: str
        """
        self._checker_rule = checker_rule

    @property
    def checker_entry(self):
        r"""Gets the checker_entry of this VulCheckerRule.

        规范检测项条目

        :return: The checker_entry of this VulCheckerRule.
        :rtype: str
        """
        return self._checker_entry

    @checker_entry.setter
    def checker_entry(self, checker_entry):
        r"""Sets the checker_entry of this VulCheckerRule.

        规范检测项条目

        :param checker_entry: The checker_entry of this VulCheckerRule.
        :type checker_entry: str
        """
        self._checker_entry = checker_entry

    @property
    def checker_result(self):
        r"""Gets the checker_result of this VulCheckerRule.

        规则检测项结果

        :return: The checker_result of this VulCheckerRule.
        :rtype: str
        """
        return self._checker_result

    @checker_result.setter
    def checker_result(self, checker_result):
        r"""Sets the checker_result of this VulCheckerRule.

        规则检测项结果

        :param checker_result: The checker_result of this VulCheckerRule.
        :type checker_result: str
        """
        self._checker_result = checker_result

    @property
    def checker_stack(self):
        r"""Gets the checker_stack of this VulCheckerRule.

        调用栈信息

        :return: The checker_stack of this VulCheckerRule.
        :rtype: str
        """
        return self._checker_stack

    @checker_stack.setter
    def checker_stack(self, checker_stack):
        r"""Sets the checker_stack of this VulCheckerRule.

        调用栈信息

        :param checker_stack: The checker_stack of this VulCheckerRule.
        :type checker_stack: str
        """
        self._checker_stack = checker_stack

    @property
    def privacy_policy_evidences(self):
        r"""Gets the privacy_policy_evidences of this VulCheckerRule.

        隐私声明

        :return: The privacy_policy_evidences of this VulCheckerRule.
        :rtype: str
        """
        return self._privacy_policy_evidences

    @privacy_policy_evidences.setter
    def privacy_policy_evidences(self, privacy_policy_evidences):
        r"""Sets the privacy_policy_evidences of this VulCheckerRule.

        隐私声明

        :param privacy_policy_evidences: The privacy_policy_evidences of this VulCheckerRule.
        :type privacy_policy_evidences: str
        """
        self._privacy_policy_evidences = privacy_policy_evidences

    @property
    def _pass(self):
        r"""Gets the _pass of this VulCheckerRule.

        是否通过

        :return: The _pass of this VulCheckerRule.
        :rtype: bool
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        r"""Sets the _pass of this VulCheckerRule.

        是否通过

        :param _pass: The _pass of this VulCheckerRule.
        :type _pass: bool
        """
        self.__pass = _pass

    @property
    def rectify_suggestion(self):
        r"""Gets the rectify_suggestion of this VulCheckerRule.

        修复建议

        :return: The rectify_suggestion of this VulCheckerRule.
        :rtype: str
        """
        return self._rectify_suggestion

    @rectify_suggestion.setter
    def rectify_suggestion(self, rectify_suggestion):
        r"""Sets the rectify_suggestion of this VulCheckerRule.

        修复建议

        :param rectify_suggestion: The rectify_suggestion of this VulCheckerRule.
        :type rectify_suggestion: str
        """
        self._rectify_suggestion = rectify_suggestion

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
        if not isinstance(other, VulCheckerRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
