# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostCheckRulesResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_rule_id': 'str',
        'check_rule_name': 'str',
        'tag': 'str',
        'severity': 'str',
        'result_type': 'str',
        'rule_params': 'list[CheckRuleFixParamInfo]',
        'scan_time': 'int',
        'host_type': 'str',
        'diff_description': 'str',
        'description': 'str',
        'enable_fix': 'int',
        'enable_click': 'bool',
        'enable_verify': 'bool',
        'cancel_ignore_enable_click': 'bool',
        'fix_failed_reason': 'str'
    }

    attribute_map = {
        'check_rule_id': 'check_rule_id',
        'check_rule_name': 'check_rule_name',
        'tag': 'tag',
        'severity': 'severity',
        'result_type': 'result_type',
        'rule_params': 'rule_params',
        'scan_time': 'scan_time',
        'host_type': 'host_type',
        'diff_description': 'diff_description',
        'description': 'description',
        'enable_fix': 'enable_fix',
        'enable_click': 'enable_click',
        'enable_verify': 'enable_verify',
        'cancel_ignore_enable_click': 'cancel_ignore_enable_click',
        'fix_failed_reason': 'fix_failed_reason'
    }

    def __init__(self, check_rule_id=None, check_rule_name=None, tag=None, severity=None, result_type=None, rule_params=None, scan_time=None, host_type=None, diff_description=None, description=None, enable_fix=None, enable_click=None, enable_verify=None, cancel_ignore_enable_click=None, fix_failed_reason=None):
        r"""HostCheckRulesResponseInfo

        The model defined in huaweicloud sdk

        :param check_rule_id: **参数解释** 检查项id **取值范围** 字符长度0-256位
        :type check_rule_id: str
        :param check_rule_name: **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-65534位
        :type check_rule_name: str
        :param tag: 基线检查中检查项的检查类型 - 访问控制 - 服务配置
        :type tag: str
        :param severity: 风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危
        :type severity: str
        :param result_type: **参数解释** 检测结果类型 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白
        :type result_type: str
        :param rule_params: **参数解释** 支持传递参数修复的检查项可传递参数的范围，只有支持传递参数修复的检查项才返回此数据
        :type rule_params: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixParamInfo`]
        :param scan_time: **参数解释** 检查项扫描时间(ms) **取值范围** 不涉及
        :type scan_time: int
        :param host_type: **参数解释** 主机类型，是cce则返回cce，否则返回null **取值范围** - cce
        :type host_type: str
        :param diff_description: **参数解释** 差异化展示提示信息 **取值范围** 字符长度0-2048位
        :type diff_description: str
        :param description: **参数解释** 忽略或加白的描述 **取值范围** 字符长度0-512位
        :type description: str
        :param enable_fix: **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持
        :type enable_fix: int
        :param enable_click: **参数解释** 该检查项的修复 &amp; 验证 按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击
        :type enable_click: bool
        :param enable_verify: **参数解释** 该检查项是否可验证，要求为Linux且agent版本&gt;&#x3D;3.2.24 **取值范围** - true  : 可验证 - false : 不可验证
        :type enable_verify: bool
        :param cancel_ignore_enable_click: **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击
        :type cancel_ignore_enable_click: bool
        :param fix_failed_reason: **参数解释** 修复失败原因 **取值范围** 不涉及
        :type fix_failed_reason: str
        """
        
        

        self._check_rule_id = None
        self._check_rule_name = None
        self._tag = None
        self._severity = None
        self._result_type = None
        self._rule_params = None
        self._scan_time = None
        self._host_type = None
        self._diff_description = None
        self._description = None
        self._enable_fix = None
        self._enable_click = None
        self._enable_verify = None
        self._cancel_ignore_enable_click = None
        self._fix_failed_reason = None
        self.discriminator = None

        if check_rule_id is not None:
            self.check_rule_id = check_rule_id
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if tag is not None:
            self.tag = tag
        if severity is not None:
            self.severity = severity
        if result_type is not None:
            self.result_type = result_type
        if rule_params is not None:
            self.rule_params = rule_params
        if scan_time is not None:
            self.scan_time = scan_time
        if host_type is not None:
            self.host_type = host_type
        if diff_description is not None:
            self.diff_description = diff_description
        if description is not None:
            self.description = description
        if enable_fix is not None:
            self.enable_fix = enable_fix
        if enable_click is not None:
            self.enable_click = enable_click
        if enable_verify is not None:
            self.enable_verify = enable_verify
        if cancel_ignore_enable_click is not None:
            self.cancel_ignore_enable_click = cancel_ignore_enable_click
        if fix_failed_reason is not None:
            self.fix_failed_reason = fix_failed_reason

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this HostCheckRulesResponseInfo.

        **参数解释** 检查项id **取值范围** 字符长度0-256位

        :return: The check_rule_id of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this HostCheckRulesResponseInfo.

        **参数解释** 检查项id **取值范围** 字符长度0-256位

        :param check_rule_id: The check_rule_id of this HostCheckRulesResponseInfo.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this HostCheckRulesResponseInfo.

        **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-65534位

        :return: The check_rule_name of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this HostCheckRulesResponseInfo.

        **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-65534位

        :param check_rule_name: The check_rule_name of this HostCheckRulesResponseInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def tag(self):
        r"""Gets the tag of this HostCheckRulesResponseInfo.

        基线检查中检查项的检查类型 - 访问控制 - 服务配置

        :return: The tag of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this HostCheckRulesResponseInfo.

        基线检查中检查项的检查类型 - 访问控制 - 服务配置

        :param tag: The tag of this HostCheckRulesResponseInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def severity(self):
        r"""Gets the severity of this HostCheckRulesResponseInfo.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :return: The severity of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this HostCheckRulesResponseInfo.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :param severity: The severity of this HostCheckRulesResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def result_type(self):
        r"""Gets the result_type of this HostCheckRulesResponseInfo.

        **参数解释** 检测结果类型 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白

        :return: The result_type of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        r"""Sets the result_type of this HostCheckRulesResponseInfo.

        **参数解释** 检测结果类型 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白

        :param result_type: The result_type of this HostCheckRulesResponseInfo.
        :type result_type: str
        """
        self._result_type = result_type

    @property
    def rule_params(self):
        r"""Gets the rule_params of this HostCheckRulesResponseInfo.

        **参数解释** 支持传递参数修复的检查项可传递参数的范围，只有支持传递参数修复的检查项才返回此数据

        :return: The rule_params of this HostCheckRulesResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixParamInfo`]
        """
        return self._rule_params

    @rule_params.setter
    def rule_params(self, rule_params):
        r"""Sets the rule_params of this HostCheckRulesResponseInfo.

        **参数解释** 支持传递参数修复的检查项可传递参数的范围，只有支持传递参数修复的检查项才返回此数据

        :param rule_params: The rule_params of this HostCheckRulesResponseInfo.
        :type rule_params: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixParamInfo`]
        """
        self._rule_params = rule_params

    @property
    def scan_time(self):
        r"""Gets the scan_time of this HostCheckRulesResponseInfo.

        **参数解释** 检查项扫描时间(ms) **取值范围** 不涉及

        :return: The scan_time of this HostCheckRulesResponseInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this HostCheckRulesResponseInfo.

        **参数解释** 检查项扫描时间(ms) **取值范围** 不涉及

        :param scan_time: The scan_time of this HostCheckRulesResponseInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def host_type(self):
        r"""Gets the host_type of this HostCheckRulesResponseInfo.

        **参数解释** 主机类型，是cce则返回cce，否则返回null **取值范围** - cce

        :return: The host_type of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this HostCheckRulesResponseInfo.

        **参数解释** 主机类型，是cce则返回cce，否则返回null **取值范围** - cce

        :param host_type: The host_type of this HostCheckRulesResponseInfo.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def diff_description(self):
        r"""Gets the diff_description of this HostCheckRulesResponseInfo.

        **参数解释** 差异化展示提示信息 **取值范围** 字符长度0-2048位

        :return: The diff_description of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._diff_description

    @diff_description.setter
    def diff_description(self, diff_description):
        r"""Sets the diff_description of this HostCheckRulesResponseInfo.

        **参数解释** 差异化展示提示信息 **取值范围** 字符长度0-2048位

        :param diff_description: The diff_description of this HostCheckRulesResponseInfo.
        :type diff_description: str
        """
        self._diff_description = diff_description

    @property
    def description(self):
        r"""Gets the description of this HostCheckRulesResponseInfo.

        **参数解释** 忽略或加白的描述 **取值范围** 字符长度0-512位

        :return: The description of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HostCheckRulesResponseInfo.

        **参数解释** 忽略或加白的描述 **取值范围** 字符长度0-512位

        :param description: The description of this HostCheckRulesResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def enable_fix(self):
        r"""Gets the enable_fix of this HostCheckRulesResponseInfo.

        **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持

        :return: The enable_fix of this HostCheckRulesResponseInfo.
        :rtype: int
        """
        return self._enable_fix

    @enable_fix.setter
    def enable_fix(self, enable_fix):
        r"""Sets the enable_fix of this HostCheckRulesResponseInfo.

        **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持

        :param enable_fix: The enable_fix of this HostCheckRulesResponseInfo.
        :type enable_fix: int
        """
        self._enable_fix = enable_fix

    @property
    def enable_click(self):
        r"""Gets the enable_click of this HostCheckRulesResponseInfo.

        **参数解释** 该检查项的修复 & 验证 按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :return: The enable_click of this HostCheckRulesResponseInfo.
        :rtype: bool
        """
        return self._enable_click

    @enable_click.setter
    def enable_click(self, enable_click):
        r"""Sets the enable_click of this HostCheckRulesResponseInfo.

        **参数解释** 该检查项的修复 & 验证 按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :param enable_click: The enable_click of this HostCheckRulesResponseInfo.
        :type enable_click: bool
        """
        self._enable_click = enable_click

    @property
    def enable_verify(self):
        r"""Gets the enable_verify of this HostCheckRulesResponseInfo.

        **参数解释** 该检查项是否可验证，要求为Linux且agent版本>=3.2.24 **取值范围** - true  : 可验证 - false : 不可验证

        :return: The enable_verify of this HostCheckRulesResponseInfo.
        :rtype: bool
        """
        return self._enable_verify

    @enable_verify.setter
    def enable_verify(self, enable_verify):
        r"""Sets the enable_verify of this HostCheckRulesResponseInfo.

        **参数解释** 该检查项是否可验证，要求为Linux且agent版本>=3.2.24 **取值范围** - true  : 可验证 - false : 不可验证

        :param enable_verify: The enable_verify of this HostCheckRulesResponseInfo.
        :type enable_verify: bool
        """
        self._enable_verify = enable_verify

    @property
    def cancel_ignore_enable_click(self):
        r"""Gets the cancel_ignore_enable_click of this HostCheckRulesResponseInfo.

        **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :return: The cancel_ignore_enable_click of this HostCheckRulesResponseInfo.
        :rtype: bool
        """
        return self._cancel_ignore_enable_click

    @cancel_ignore_enable_click.setter
    def cancel_ignore_enable_click(self, cancel_ignore_enable_click):
        r"""Sets the cancel_ignore_enable_click of this HostCheckRulesResponseInfo.

        **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :param cancel_ignore_enable_click: The cancel_ignore_enable_click of this HostCheckRulesResponseInfo.
        :type cancel_ignore_enable_click: bool
        """
        self._cancel_ignore_enable_click = cancel_ignore_enable_click

    @property
    def fix_failed_reason(self):
        r"""Gets the fix_failed_reason of this HostCheckRulesResponseInfo.

        **参数解释** 修复失败原因 **取值范围** 不涉及

        :return: The fix_failed_reason of this HostCheckRulesResponseInfo.
        :rtype: str
        """
        return self._fix_failed_reason

    @fix_failed_reason.setter
    def fix_failed_reason(self, fix_failed_reason):
        r"""Sets the fix_failed_reason of this HostCheckRulesResponseInfo.

        **参数解释** 修复失败原因 **取值范围** 不涉及

        :param fix_failed_reason: The fix_failed_reason of this HostCheckRulesResponseInfo.
        :type fix_failed_reason: str
        """
        self._fix_failed_reason = fix_failed_reason

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
        if not isinstance(other, HostCheckRulesResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
