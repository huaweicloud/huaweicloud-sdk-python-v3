# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRulesResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag': 'str',
        'check_rule_name': 'str',
        'check_rule_id': 'str',
        'severity': 'str',
        'check_type': 'str',
        'check_type_name': 'str',
        'standard': 'str',
        'host_num': 'int',
        'failed_num': 'int',
        'scan_time': 'int',
        'statistics_scan_result': 'str',
        'enable_fix': 'int',
        'enable_click': 'bool',
        'cancel_ignore_enable_click': 'bool',
        'rule_params': 'list[CheckRuleFixParamInfo]'
    }

    attribute_map = {
        'tag': 'tag',
        'check_rule_name': 'check_rule_name',
        'check_rule_id': 'check_rule_id',
        'severity': 'severity',
        'check_type': 'check_type',
        'check_type_name': 'check_type_name',
        'standard': 'standard',
        'host_num': 'host_num',
        'failed_num': 'failed_num',
        'scan_time': 'scan_time',
        'statistics_scan_result': 'statistics_scan_result',
        'enable_fix': 'enable_fix',
        'enable_click': 'enable_click',
        'cancel_ignore_enable_click': 'cancel_ignore_enable_click',
        'rule_params': 'rule_params'
    }

    def __init__(self, tag=None, check_rule_name=None, check_rule_id=None, severity=None, check_type=None, check_type_name=None, standard=None, host_num=None, failed_num=None, scan_time=None, statistics_scan_result=None, enable_fix=None, enable_click=None, cancel_ignore_enable_click=None, rule_params=None):
        r"""CheckRulesResponseInfo

        The model defined in huaweicloud sdk

        :param tag: **参数解释** 基线检查项的类型 **取值范围** 字符长度0-256位
        :type tag: str
        :param check_rule_name: **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-2048位
        :type check_rule_name: str
        :param check_rule_id: **参数解释** 检查项ID **取值范围** 字符长度0-64位
        :type check_rule_id: str
        :param severity: **参数解释** 风险等级，包含如下: **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危
        :type severity: str
        :param check_type: **参数解释** 配置检查（基线）的类型,Linux系统支持的基线一般check_type和check_name相同,例如SSH、CentOS 7。 Windows系统支持的基线一般check_type和check_name不相同，例如check_name为Windows的配置检查（基线），它的check_type包含Windows Server 2019 R2、Windows Server 2016 R2等。 **取值范围** 字符长度0-256位
        :type check_type: str
        :param check_type_name: **参数解释** 配置检查（基线）的类型名称, 一般为check_type + 系统基线检查|应用基线检查 **取值范围** 字符长度0-256位
        :type check_type_name: str
        :param standard: **参数解释** 标准类型，包含如下3种 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准
        :type standard: str
        :param host_num: **参数解释** 受影响的服务器的数量，进行了当前基线检测的服务器数量 **取值范围** 取值0-2147483647
        :type host_num: int
        :param failed_num: **参数解释** 此检测项失败，且未忽略且未加白的主机数 **取值范围** 取值0-2147483647
        :type failed_num: int
        :param scan_time: 最新检测时间(ms)
        :type scan_time: int
        :param statistics_scan_result: **参数解释** 检查项统计结果： **取值范围** - pass      : 已通过，表示此检查项涉及的主机，全部检查通过。 - failed    : 未通过，表示此检查项涉及的主机，存在检查不通过，且不通过的主机中，存在未处理(忽略、加白)主机。 - processed : 已处理，表示此检查项涉及的主机，存在未通过，但所有的未通过主机均已处理(忽略、加白)。
        :type statistics_scan_result: str
        :param enable_fix: **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持
        :type enable_fix: int
        :param enable_click: **参数解释** 该检查项的 修复 &amp; 验证 按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击
        :type enable_click: bool
        :param cancel_ignore_enable_click: **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击
        :type cancel_ignore_enable_click: bool
        :param rule_params: **参数解释** 支持传递参数修复的检查项可传递参数的范围，只有支持传递参数修复的检查项才返回此数据
        :type rule_params: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixParamInfo`]
        """
        
        

        self._tag = None
        self._check_rule_name = None
        self._check_rule_id = None
        self._severity = None
        self._check_type = None
        self._check_type_name = None
        self._standard = None
        self._host_num = None
        self._failed_num = None
        self._scan_time = None
        self._statistics_scan_result = None
        self._enable_fix = None
        self._enable_click = None
        self._cancel_ignore_enable_click = None
        self._rule_params = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if check_rule_id is not None:
            self.check_rule_id = check_rule_id
        if severity is not None:
            self.severity = severity
        if check_type is not None:
            self.check_type = check_type
        if check_type_name is not None:
            self.check_type_name = check_type_name
        if standard is not None:
            self.standard = standard
        if host_num is not None:
            self.host_num = host_num
        if failed_num is not None:
            self.failed_num = failed_num
        if scan_time is not None:
            self.scan_time = scan_time
        if statistics_scan_result is not None:
            self.statistics_scan_result = statistics_scan_result
        if enable_fix is not None:
            self.enable_fix = enable_fix
        if enable_click is not None:
            self.enable_click = enable_click
        if cancel_ignore_enable_click is not None:
            self.cancel_ignore_enable_click = cancel_ignore_enable_click
        if rule_params is not None:
            self.rule_params = rule_params

    @property
    def tag(self):
        r"""Gets the tag of this CheckRulesResponseInfo.

        **参数解释** 基线检查项的类型 **取值范围** 字符长度0-256位

        :return: The tag of this CheckRulesResponseInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this CheckRulesResponseInfo.

        **参数解释** 基线检查项的类型 **取值范围** 字符长度0-256位

        :param tag: The tag of this CheckRulesResponseInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this CheckRulesResponseInfo.

        **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-2048位

        :return: The check_rule_name of this CheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this CheckRulesResponseInfo.

        **参数解释** 检查项（检查规则）名称 **取值范围** 字符长度0-2048位

        :param check_rule_name: The check_rule_name of this CheckRulesResponseInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this CheckRulesResponseInfo.

        **参数解释** 检查项ID **取值范围** 字符长度0-64位

        :return: The check_rule_id of this CheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this CheckRulesResponseInfo.

        **参数解释** 检查项ID **取值范围** 字符长度0-64位

        :param check_rule_id: The check_rule_id of this CheckRulesResponseInfo.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def severity(self):
        r"""Gets the severity of this CheckRulesResponseInfo.

        **参数解释** 风险等级，包含如下: **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危

        :return: The severity of this CheckRulesResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this CheckRulesResponseInfo.

        **参数解释** 风险等级，包含如下: **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危

        :param severity: The severity of this CheckRulesResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def check_type(self):
        r"""Gets the check_type of this CheckRulesResponseInfo.

        **参数解释** 配置检查（基线）的类型,Linux系统支持的基线一般check_type和check_name相同,例如SSH、CentOS 7。 Windows系统支持的基线一般check_type和check_name不相同，例如check_name为Windows的配置检查（基线），它的check_type包含Windows Server 2019 R2、Windows Server 2016 R2等。 **取值范围** 字符长度0-256位

        :return: The check_type of this CheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this CheckRulesResponseInfo.

        **参数解释** 配置检查（基线）的类型,Linux系统支持的基线一般check_type和check_name相同,例如SSH、CentOS 7。 Windows系统支持的基线一般check_type和check_name不相同，例如check_name为Windows的配置检查（基线），它的check_type包含Windows Server 2019 R2、Windows Server 2016 R2等。 **取值范围** 字符长度0-256位

        :param check_type: The check_type of this CheckRulesResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def check_type_name(self):
        r"""Gets the check_type_name of this CheckRulesResponseInfo.

        **参数解释** 配置检查（基线）的类型名称, 一般为check_type + 系统基线检查|应用基线检查 **取值范围** 字符长度0-256位

        :return: The check_type_name of this CheckRulesResponseInfo.
        :rtype: str
        """
        return self._check_type_name

    @check_type_name.setter
    def check_type_name(self, check_type_name):
        r"""Sets the check_type_name of this CheckRulesResponseInfo.

        **参数解释** 配置检查（基线）的类型名称, 一般为check_type + 系统基线检查|应用基线检查 **取值范围** 字符长度0-256位

        :param check_type_name: The check_type_name of this CheckRulesResponseInfo.
        :type check_type_name: str
        """
        self._check_type_name = check_type_name

    @property
    def standard(self):
        r"""Gets the standard of this CheckRulesResponseInfo.

        **参数解释** 标准类型，包含如下3种 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准

        :return: The standard of this CheckRulesResponseInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this CheckRulesResponseInfo.

        **参数解释** 标准类型，包含如下3种 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准

        :param standard: The standard of this CheckRulesResponseInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def host_num(self):
        r"""Gets the host_num of this CheckRulesResponseInfo.

        **参数解释** 受影响的服务器的数量，进行了当前基线检测的服务器数量 **取值范围** 取值0-2147483647

        :return: The host_num of this CheckRulesResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this CheckRulesResponseInfo.

        **参数解释** 受影响的服务器的数量，进行了当前基线检测的服务器数量 **取值范围** 取值0-2147483647

        :param host_num: The host_num of this CheckRulesResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this CheckRulesResponseInfo.

        **参数解释** 此检测项失败，且未忽略且未加白的主机数 **取值范围** 取值0-2147483647

        :return: The failed_num of this CheckRulesResponseInfo.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this CheckRulesResponseInfo.

        **参数解释** 此检测项失败，且未忽略且未加白的主机数 **取值范围** 取值0-2147483647

        :param failed_num: The failed_num of this CheckRulesResponseInfo.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def scan_time(self):
        r"""Gets the scan_time of this CheckRulesResponseInfo.

        最新检测时间(ms)

        :return: The scan_time of this CheckRulesResponseInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this CheckRulesResponseInfo.

        最新检测时间(ms)

        :param scan_time: The scan_time of this CheckRulesResponseInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def statistics_scan_result(self):
        r"""Gets the statistics_scan_result of this CheckRulesResponseInfo.

        **参数解释** 检查项统计结果： **取值范围** - pass      : 已通过，表示此检查项涉及的主机，全部检查通过。 - failed    : 未通过，表示此检查项涉及的主机，存在检查不通过，且不通过的主机中，存在未处理(忽略、加白)主机。 - processed : 已处理，表示此检查项涉及的主机，存在未通过，但所有的未通过主机均已处理(忽略、加白)。

        :return: The statistics_scan_result of this CheckRulesResponseInfo.
        :rtype: str
        """
        return self._statistics_scan_result

    @statistics_scan_result.setter
    def statistics_scan_result(self, statistics_scan_result):
        r"""Sets the statistics_scan_result of this CheckRulesResponseInfo.

        **参数解释** 检查项统计结果： **取值范围** - pass      : 已通过，表示此检查项涉及的主机，全部检查通过。 - failed    : 未通过，表示此检查项涉及的主机，存在检查不通过，且不通过的主机中，存在未处理(忽略、加白)主机。 - processed : 已处理，表示此检查项涉及的主机，存在未通过，但所有的未通过主机均已处理(忽略、加白)。

        :param statistics_scan_result: The statistics_scan_result of this CheckRulesResponseInfo.
        :type statistics_scan_result: str
        """
        self._statistics_scan_result = statistics_scan_result

    @property
    def enable_fix(self):
        r"""Gets the enable_fix of this CheckRulesResponseInfo.

        **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持

        :return: The enable_fix of this CheckRulesResponseInfo.
        :rtype: int
        """
        return self._enable_fix

    @enable_fix.setter
    def enable_fix(self, enable_fix):
        r"""Sets the enable_fix of this CheckRulesResponseInfo.

        **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持

        :param enable_fix: The enable_fix of this CheckRulesResponseInfo.
        :type enable_fix: int
        """
        self._enable_fix = enable_fix

    @property
    def enable_click(self):
        r"""Gets the enable_click of this CheckRulesResponseInfo.

        **参数解释** 该检查项的 修复 & 验证 按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :return: The enable_click of this CheckRulesResponseInfo.
        :rtype: bool
        """
        return self._enable_click

    @enable_click.setter
    def enable_click(self, enable_click):
        r"""Sets the enable_click of this CheckRulesResponseInfo.

        **参数解释** 该检查项的 修复 & 验证 按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :param enable_click: The enable_click of this CheckRulesResponseInfo.
        :type enable_click: bool
        """
        self._enable_click = enable_click

    @property
    def cancel_ignore_enable_click(self):
        r"""Gets the cancel_ignore_enable_click of this CheckRulesResponseInfo.

        **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :return: The cancel_ignore_enable_click of this CheckRulesResponseInfo.
        :rtype: bool
        """
        return self._cancel_ignore_enable_click

    @cancel_ignore_enable_click.setter
    def cancel_ignore_enable_click(self, cancel_ignore_enable_click):
        r"""Sets the cancel_ignore_enable_click of this CheckRulesResponseInfo.

        **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :param cancel_ignore_enable_click: The cancel_ignore_enable_click of this CheckRulesResponseInfo.
        :type cancel_ignore_enable_click: bool
        """
        self._cancel_ignore_enable_click = cancel_ignore_enable_click

    @property
    def rule_params(self):
        r"""Gets the rule_params of this CheckRulesResponseInfo.

        **参数解释** 支持传递参数修复的检查项可传递参数的范围，只有支持传递参数修复的检查项才返回此数据

        :return: The rule_params of this CheckRulesResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CheckRuleFixParamInfo`]
        """
        return self._rule_params

    @rule_params.setter
    def rule_params(self, rule_params):
        r"""Sets the rule_params of this CheckRulesResponseInfo.

        **参数解释** 支持传递参数修复的检查项可传递参数的范围，只有支持传递参数修复的检查项才返回此数据

        :param rule_params: The rule_params of this CheckRulesResponseInfo.
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
        if not isinstance(other, CheckRulesResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
