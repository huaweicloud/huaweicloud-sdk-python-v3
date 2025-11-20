# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckPolicyDetailInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'check_rule_id': 'str',
        'check_rule_name': 'str',
        'check_rule_type': 'int',
        'check_type': 'str',
        'severity': 'str',
        'level': 'str',
        'checked': 'bool',
        'rule_params': 'list[CheckRuleFixParamInfo]'
    }

    attribute_map = {
        'key': 'key',
        'check_rule_id': 'check_rule_id',
        'check_rule_name': 'check_rule_name',
        'check_rule_type': 'check_rule_type',
        'check_type': 'check_type',
        'severity': 'severity',
        'level': 'level',
        'checked': 'checked',
        'rule_params': 'rule_params'
    }

    def __init__(self, key=None, check_rule_id=None, check_rule_name=None, check_rule_type=None, check_type=None, severity=None, level=None, checked=None, rule_params=None):
        r"""SecurityCheckPolicyDetailInfoResponseInfo

        The model defined in huaweicloud sdk

        :param key: **参数解释** 检查项唯一值 **取值范围** 字符长度0-256位
        :type key: str
        :param check_rule_id: **参数解释** 检查项id **取值范围** 字符长度0-256位
        :type check_rule_id: str
        :param check_rule_name: **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-65534位
        :type check_rule_name: str
        :param check_rule_type: **参数解释** 检查项类型是否是数值类型 **取值范围** - 1 : 是 - 0 : 不是
        :type check_rule_type: int
        :param check_type: **参数解释** 配置检查（基线）的类型，例如SSH、CentOS 7、Windows **取值范围** 字符长度0-256位
        :type check_type: str
        :param severity: **参数解释** 检查项的风险程度 **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危
        :type severity: str
        :param level: **参数解释** 配置检查（基线）检查项的版本信息 **取值范围** 字符长度0-32位
        :type level: str
        :param checked: **参数解释** 检查项是否被选中 **取值范围** - true  : 被选中 - false : 未被选中
        :type checked: bool
        :param rule_params: **参数解释** 可自定义配置的参数
        :type rule_params: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixParamInfo`]
        """
        
        

        self._key = None
        self._check_rule_id = None
        self._check_rule_name = None
        self._check_rule_type = None
        self._check_type = None
        self._severity = None
        self._level = None
        self._checked = None
        self._rule_params = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if check_rule_id is not None:
            self.check_rule_id = check_rule_id
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if check_rule_type is not None:
            self.check_rule_type = check_rule_type
        if check_type is not None:
            self.check_type = check_type
        if severity is not None:
            self.severity = severity
        if level is not None:
            self.level = level
        if checked is not None:
            self.checked = checked
        if rule_params is not None:
            self.rule_params = rule_params

    @property
    def key(self):
        r"""Gets the key of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项唯一值 **取值范围** 字符长度0-256位

        :return: The key of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项唯一值 **取值范围** 字符长度0-256位

        :param key: The key of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type key: str
        """
        self._key = key

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项id **取值范围** 字符长度0-256位

        :return: The check_rule_id of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项id **取值范围** 字符长度0-256位

        :param check_rule_id: The check_rule_id of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-65534位

        :return: The check_rule_name of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-65534位

        :param check_rule_name: The check_rule_name of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def check_rule_type(self):
        r"""Gets the check_rule_type of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项类型是否是数值类型 **取值范围** - 1 : 是 - 0 : 不是

        :return: The check_rule_type of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: int
        """
        return self._check_rule_type

    @check_rule_type.setter
    def check_rule_type(self, check_rule_type):
        r"""Sets the check_rule_type of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项类型是否是数值类型 **取值范围** - 1 : 是 - 0 : 不是

        :param check_rule_type: The check_rule_type of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type check_rule_type: int
        """
        self._check_rule_type = check_rule_type

    @property
    def check_type(self):
        r"""Gets the check_type of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 配置检查（基线）的类型，例如SSH、CentOS 7、Windows **取值范围** 字符长度0-256位

        :return: The check_type of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 配置检查（基线）的类型，例如SSH、CentOS 7、Windows **取值范围** 字符长度0-256位

        :param check_type: The check_type of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def severity(self):
        r"""Gets the severity of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项的风险程度 **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危

        :return: The severity of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项的风险程度 **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危

        :param severity: The severity of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def level(self):
        r"""Gets the level of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 配置检查（基线）检查项的版本信息 **取值范围** 字符长度0-32位

        :return: The level of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 配置检查（基线）检查项的版本信息 **取值范围** 字符长度0-32位

        :param level: The level of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type level: str
        """
        self._level = level

    @property
    def checked(self):
        r"""Gets the checked of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项是否被选中 **取值范围** - true  : 被选中 - false : 未被选中

        :return: The checked of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        r"""Sets the checked of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 检查项是否被选中 **取值范围** - true  : 被选中 - false : 未被选中

        :param checked: The checked of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type checked: bool
        """
        self._checked = checked

    @property
    def rule_params(self):
        r"""Gets the rule_params of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 可自定义配置的参数

        :return: The rule_params of this SecurityCheckPolicyDetailInfoResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixParamInfo`]
        """
        return self._rule_params

    @rule_params.setter
    def rule_params(self, rule_params):
        r"""Sets the rule_params of this SecurityCheckPolicyDetailInfoResponseInfo.

        **参数解释** 可自定义配置的参数

        :param rule_params: The rule_params of this SecurityCheckPolicyDetailInfoResponseInfo.
        :type rule_params: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixParamInfo`]
        """
        self._rule_params = rule_params

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
        if not isinstance(other, SecurityCheckPolicyDetailInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
