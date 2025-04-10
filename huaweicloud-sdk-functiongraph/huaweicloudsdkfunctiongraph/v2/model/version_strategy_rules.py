# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionStrategyRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_type': 'str',
        'param': 'str',
        'op': 'str',
        'value': 'str'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'param': 'param',
        'op': 'op',
        'value': 'value'
    }

    def __init__(self, rule_type=None, param=None, op=None, value=None):
        r"""VersionStrategyRules

        The model defined in huaweicloud sdk

        :param rule_type: 参数类型。
        :type rule_type: str
        :param param: 规则参数名, 只支持大小写字母，数字，下划线，中划线。
        :type param: str
        :param op: 规则匹配操作符，目前仅需支持 &#x3D; 或者in。
        :type op: str
        :param value: 规则值，如果op为in，则为逗号分隔的多值字符串
        :type value: str
        """
        
        

        self._rule_type = None
        self._param = None
        self._op = None
        self._value = None
        self.discriminator = None

        if rule_type is not None:
            self.rule_type = rule_type
        if param is not None:
            self.param = param
        if op is not None:
            self.op = op
        if value is not None:
            self.value = value

    @property
    def rule_type(self):
        r"""Gets the rule_type of this VersionStrategyRules.

        参数类型。

        :return: The rule_type of this VersionStrategyRules.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this VersionStrategyRules.

        参数类型。

        :param rule_type: The rule_type of this VersionStrategyRules.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def param(self):
        r"""Gets the param of this VersionStrategyRules.

        规则参数名, 只支持大小写字母，数字，下划线，中划线。

        :return: The param of this VersionStrategyRules.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        r"""Sets the param of this VersionStrategyRules.

        规则参数名, 只支持大小写字母，数字，下划线，中划线。

        :param param: The param of this VersionStrategyRules.
        :type param: str
        """
        self._param = param

    @property
    def op(self):
        r"""Gets the op of this VersionStrategyRules.

        规则匹配操作符，目前仅需支持 = 或者in。

        :return: The op of this VersionStrategyRules.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        r"""Sets the op of this VersionStrategyRules.

        规则匹配操作符，目前仅需支持 = 或者in。

        :param op: The op of this VersionStrategyRules.
        :type op: str
        """
        self._op = op

    @property
    def value(self):
        r"""Gets the value of this VersionStrategyRules.

        规则值，如果op为in，则为逗号分隔的多值字符串

        :return: The value of this VersionStrategyRules.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this VersionStrategyRules.

        规则值，如果op为in，则为逗号分隔的多值字符串

        :param value: The value of this VersionStrategyRules.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, VersionStrategyRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
