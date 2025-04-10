# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'rule_language': 'str',
        'rule_name': 'str',
        'rule_severity': 'str',
        'rule_tages': 'str',
        'checked': 'str',
        'rule_config_list': 'list[RuleConfig]'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'rule_language': 'rule_language',
        'rule_name': 'rule_name',
        'rule_severity': 'rule_severity',
        'rule_tages': 'rule_tages',
        'checked': 'checked',
        'rule_config_list': 'rule_config_list'
    }

    def __init__(self, rule_id=None, rule_language=None, rule_name=None, rule_severity=None, rule_tages=None, checked=None, rule_config_list=None):
        r"""RuleItem

        The model defined in huaweicloud sdk

        :param rule_id: 规则id
        :type rule_id: str
        :param rule_language: 规则所属语言
        :type rule_language: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param rule_severity: 规则问题级别
        :type rule_severity: str
        :param rule_tages: 规则标签
        :type rule_tages: str
        :param checked: 规则状态0：未启用，1：已启用
        :type checked: str
        :param rule_config_list: 规则配置参数阈值相关信息
        :type rule_config_list: list[:class:`huaweicloudsdkcodeartscheck.v2.RuleConfig`]
        """
        
        

        self._rule_id = None
        self._rule_language = None
        self._rule_name = None
        self._rule_severity = None
        self._rule_tages = None
        self._checked = None
        self._rule_config_list = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_language is not None:
            self.rule_language = rule_language
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_severity is not None:
            self.rule_severity = rule_severity
        if rule_tages is not None:
            self.rule_tages = rule_tages
        if checked is not None:
            self.checked = checked
        if rule_config_list is not None:
            self.rule_config_list = rule_config_list

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleItem.

        规则id

        :return: The rule_id of this RuleItem.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleItem.

        规则id

        :param rule_id: The rule_id of this RuleItem.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_language(self):
        r"""Gets the rule_language of this RuleItem.

        规则所属语言

        :return: The rule_language of this RuleItem.
        :rtype: str
        """
        return self._rule_language

    @rule_language.setter
    def rule_language(self, rule_language):
        r"""Sets the rule_language of this RuleItem.

        规则所属语言

        :param rule_language: The rule_language of this RuleItem.
        :type rule_language: str
        """
        self._rule_language = rule_language

    @property
    def rule_name(self):
        r"""Gets the rule_name of this RuleItem.

        规则名称

        :return: The rule_name of this RuleItem.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this RuleItem.

        规则名称

        :param rule_name: The rule_name of this RuleItem.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_severity(self):
        r"""Gets the rule_severity of this RuleItem.

        规则问题级别

        :return: The rule_severity of this RuleItem.
        :rtype: str
        """
        return self._rule_severity

    @rule_severity.setter
    def rule_severity(self, rule_severity):
        r"""Sets the rule_severity of this RuleItem.

        规则问题级别

        :param rule_severity: The rule_severity of this RuleItem.
        :type rule_severity: str
        """
        self._rule_severity = rule_severity

    @property
    def rule_tages(self):
        r"""Gets the rule_tages of this RuleItem.

        规则标签

        :return: The rule_tages of this RuleItem.
        :rtype: str
        """
        return self._rule_tages

    @rule_tages.setter
    def rule_tages(self, rule_tages):
        r"""Sets the rule_tages of this RuleItem.

        规则标签

        :param rule_tages: The rule_tages of this RuleItem.
        :type rule_tages: str
        """
        self._rule_tages = rule_tages

    @property
    def checked(self):
        r"""Gets the checked of this RuleItem.

        规则状态0：未启用，1：已启用

        :return: The checked of this RuleItem.
        :rtype: str
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        r"""Sets the checked of this RuleItem.

        规则状态0：未启用，1：已启用

        :param checked: The checked of this RuleItem.
        :type checked: str
        """
        self._checked = checked

    @property
    def rule_config_list(self):
        r"""Gets the rule_config_list of this RuleItem.

        规则配置参数阈值相关信息

        :return: The rule_config_list of this RuleItem.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.RuleConfig`]
        """
        return self._rule_config_list

    @rule_config_list.setter
    def rule_config_list(self, rule_config_list):
        r"""Sets the rule_config_list of this RuleItem.

        规则配置参数阈值相关信息

        :param rule_config_list: The rule_config_list of this RuleItem.
        :type rule_config_list: list[:class:`huaweicloudsdkcodeartscheck.v2.RuleConfig`]
        """
        self._rule_config_list = rule_config_list

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
        if not isinstance(other, RuleItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
