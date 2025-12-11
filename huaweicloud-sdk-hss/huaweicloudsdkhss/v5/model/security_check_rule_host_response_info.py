# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckRuleHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'check_name': 'str',
        'baseline_name': 'str',
        'host_public_ip': 'str',
        'host_private_ip': 'str',
        'scan_time': 'int',
        'failed_num': 'int',
        'passed_num': 'int',
        'diff_description': 'str',
        'description': 'str',
        'host_type': 'str',
        'enable_fix': 'int',
        'enable_verify': 'bool',
        'enable_click': 'bool',
        'cancel_ignore_enable_click': 'bool',
        'result_type': 'str',
        'fix_failed_reason': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'check_name': 'check_name',
        'baseline_name': 'baseline_name',
        'host_public_ip': 'host_public_ip',
        'host_private_ip': 'host_private_ip',
        'scan_time': 'scan_time',
        'failed_num': 'failed_num',
        'passed_num': 'passed_num',
        'diff_description': 'diff_description',
        'description': 'description',
        'host_type': 'host_type',
        'enable_fix': 'enable_fix',
        'enable_verify': 'enable_verify',
        'enable_click': 'enable_click',
        'cancel_ignore_enable_click': 'cancel_ignore_enable_click',
        'result_type': 'result_type',
        'fix_failed_reason': 'fix_failed_reason',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, host_id=None, host_name=None, check_name=None, baseline_name=None, host_public_ip=None, host_private_ip=None, scan_time=None, failed_num=None, passed_num=None, diff_description=None, description=None, host_type=None, enable_fix=None, enable_verify=None, enable_click=None, cancel_ignore_enable_click=None, result_type=None, fix_failed_reason=None, cluster_id=None):
        r"""SecurityCheckRuleHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param check_name: **参数解释** 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **取值范围** 字符长度0-256位
        :type check_name: str
        :param baseline_name: **参数解释** 基线的名称，例如SSH 应用基线检查、CentOS 7 系统基线检查、Windows 系统基线检查 **取值范围** 字符长度0-256位
        :type baseline_name: str
        :param host_public_ip: **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128位 
        :type host_public_ip: str
        :param host_private_ip: **参数解释** 服务器私有IP **取值范围** 字符长度0-256位
        :type host_private_ip: str
        :param scan_time: **参数解释** 扫描时间(ms) **取值范围** 取值0-9223372036854775807
        :type scan_time: int
        :param failed_num: **参数解释** 风险项数量 **取值范围** 取值0-2147483647
        :type failed_num: int
        :param passed_num: **参数解释** 通过项数量 **取值范围** 取值0-2147483647
        :type passed_num: int
        :param diff_description: **参数解释** 差异化展示提示信息 **取值范围** 字符长度0-512位
        :type diff_description: str
        :param description: **参数解释** 忽略或加白的备注 **取值范围** 字符长度0-1024位
        :type description: str
        :param host_type: **参数解释** 主机类型，当主机为cce类型时，返回cce **取值范围** - cce
        :type host_type: str
        :param enable_fix: **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持
        :type enable_fix: int
        :param enable_verify: **参数解释** 该检查项是否可验证，要求为Linux且agent版本&gt;&#x3D;3.2.24 **取值范围** - true  : 可验证 - false : 不可验证
        :type enable_verify: bool
        :param enable_click: **参数解释** 该检查项的修复&amp;忽略&amp;验证按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击
        :type enable_click: bool
        :param cancel_ignore_enable_click: **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击
        :type cancel_ignore_enable_click: bool
        :param result_type: **参数解释** 检测结果类型 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白(表示检测失败，但已进行加白)
        :type result_type: str
        :param fix_failed_reason: **参数解释** 修复失败原因 **取值范围** 字符长度0-256位
        :type fix_failed_reason: str
        :param cluster_id: **参数解释** 集群ID **取值范围** 字符长度0-64位
        :type cluster_id: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._check_name = None
        self._baseline_name = None
        self._host_public_ip = None
        self._host_private_ip = None
        self._scan_time = None
        self._failed_num = None
        self._passed_num = None
        self._diff_description = None
        self._description = None
        self._host_type = None
        self._enable_fix = None
        self._enable_verify = None
        self._enable_click = None
        self._cancel_ignore_enable_click = None
        self._result_type = None
        self._fix_failed_reason = None
        self._cluster_id = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if check_name is not None:
            self.check_name = check_name
        if baseline_name is not None:
            self.baseline_name = baseline_name
        if host_public_ip is not None:
            self.host_public_ip = host_public_ip
        if host_private_ip is not None:
            self.host_private_ip = host_private_ip
        if scan_time is not None:
            self.scan_time = scan_time
        if failed_num is not None:
            self.failed_num = failed_num
        if passed_num is not None:
            self.passed_num = passed_num
        if diff_description is not None:
            self.diff_description = diff_description
        if description is not None:
            self.description = description
        if host_type is not None:
            self.host_type = host_type
        if enable_fix is not None:
            self.enable_fix = enable_fix
        if enable_verify is not None:
            self.enable_verify = enable_verify
        if enable_click is not None:
            self.enable_click = enable_click
        if cancel_ignore_enable_click is not None:
            self.cancel_ignore_enable_click = cancel_ignore_enable_click
        if result_type is not None:
            self.result_type = result_type
        if fix_failed_reason is not None:
            self.fix_failed_reason = fix_failed_reason
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def host_id(self):
        r"""Gets the host_id of this SecurityCheckRuleHostResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this SecurityCheckRuleHostResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this SecurityCheckRuleHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this SecurityCheckRuleHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this SecurityCheckRuleHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this SecurityCheckRuleHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def check_name(self):
        r"""Gets the check_name of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **取值范围** 字符长度0-256位

        :return: The check_name of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **取值范围** 字符长度0-256位

        :param check_name: The check_name of this SecurityCheckRuleHostResponseInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def baseline_name(self):
        r"""Gets the baseline_name of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 基线的名称，例如SSH 应用基线检查、CentOS 7 系统基线检查、Windows 系统基线检查 **取值范围** 字符长度0-256位

        :return: The baseline_name of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._baseline_name

    @baseline_name.setter
    def baseline_name(self, baseline_name):
        r"""Sets the baseline_name of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 基线的名称，例如SSH 应用基线检查、CentOS 7 系统基线检查、Windows 系统基线检查 **取值范围** 字符长度0-256位

        :param baseline_name: The baseline_name of this SecurityCheckRuleHostResponseInfo.
        :type baseline_name: str
        """
        self._baseline_name = baseline_name

    @property
    def host_public_ip(self):
        r"""Gets the host_public_ip of this SecurityCheckRuleHostResponseInfo.

        **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128位 

        :return: The host_public_ip of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._host_public_ip

    @host_public_ip.setter
    def host_public_ip(self, host_public_ip):
        r"""Sets the host_public_ip of this SecurityCheckRuleHostResponseInfo.

        **参数解释**: 服务器公网IP **取值范围**: 字符长度0-128位 

        :param host_public_ip: The host_public_ip of this SecurityCheckRuleHostResponseInfo.
        :type host_public_ip: str
        """
        self._host_public_ip = host_public_ip

    @property
    def host_private_ip(self):
        r"""Gets the host_private_ip of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 服务器私有IP **取值范围** 字符长度0-256位

        :return: The host_private_ip of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._host_private_ip

    @host_private_ip.setter
    def host_private_ip(self, host_private_ip):
        r"""Sets the host_private_ip of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 服务器私有IP **取值范围** 字符长度0-256位

        :param host_private_ip: The host_private_ip of this SecurityCheckRuleHostResponseInfo.
        :type host_private_ip: str
        """
        self._host_private_ip = host_private_ip

    @property
    def scan_time(self):
        r"""Gets the scan_time of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 扫描时间(ms) **取值范围** 取值0-9223372036854775807

        :return: The scan_time of this SecurityCheckRuleHostResponseInfo.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 扫描时间(ms) **取值范围** 取值0-9223372036854775807

        :param scan_time: The scan_time of this SecurityCheckRuleHostResponseInfo.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def failed_num(self):
        r"""Gets the failed_num of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 风险项数量 **取值范围** 取值0-2147483647

        :return: The failed_num of this SecurityCheckRuleHostResponseInfo.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 风险项数量 **取值范围** 取值0-2147483647

        :param failed_num: The failed_num of this SecurityCheckRuleHostResponseInfo.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def passed_num(self):
        r"""Gets the passed_num of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 通过项数量 **取值范围** 取值0-2147483647

        :return: The passed_num of this SecurityCheckRuleHostResponseInfo.
        :rtype: int
        """
        return self._passed_num

    @passed_num.setter
    def passed_num(self, passed_num):
        r"""Sets the passed_num of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 通过项数量 **取值范围** 取值0-2147483647

        :param passed_num: The passed_num of this SecurityCheckRuleHostResponseInfo.
        :type passed_num: int
        """
        self._passed_num = passed_num

    @property
    def diff_description(self):
        r"""Gets the diff_description of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 差异化展示提示信息 **取值范围** 字符长度0-512位

        :return: The diff_description of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._diff_description

    @diff_description.setter
    def diff_description(self, diff_description):
        r"""Sets the diff_description of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 差异化展示提示信息 **取值范围** 字符长度0-512位

        :param diff_description: The diff_description of this SecurityCheckRuleHostResponseInfo.
        :type diff_description: str
        """
        self._diff_description = diff_description

    @property
    def description(self):
        r"""Gets the description of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 忽略或加白的备注 **取值范围** 字符长度0-1024位

        :return: The description of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 忽略或加白的备注 **取值范围** 字符长度0-1024位

        :param description: The description of this SecurityCheckRuleHostResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def host_type(self):
        r"""Gets the host_type of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 主机类型，当主机为cce类型时，返回cce **取值范围** - cce

        :return: The host_type of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 主机类型，当主机为cce类型时，返回cce **取值范围** - cce

        :param host_type: The host_type of this SecurityCheckRuleHostResponseInfo.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def enable_fix(self):
        r"""Gets the enable_fix of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持

        :return: The enable_fix of this SecurityCheckRuleHostResponseInfo.
        :rtype: int
        """
        return self._enable_fix

    @enable_fix.setter
    def enable_fix(self, enable_fix):
        r"""Sets the enable_fix of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 是否支持一键修复 **取值范围** - 1 : 支持一键修复 - 0 : 不支持

        :param enable_fix: The enable_fix of this SecurityCheckRuleHostResponseInfo.
        :type enable_fix: int
        """
        self._enable_fix = enable_fix

    @property
    def enable_verify(self):
        r"""Gets the enable_verify of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 该检查项是否可验证，要求为Linux且agent版本>=3.2.24 **取值范围** - true  : 可验证 - false : 不可验证

        :return: The enable_verify of this SecurityCheckRuleHostResponseInfo.
        :rtype: bool
        """
        return self._enable_verify

    @enable_verify.setter
    def enable_verify(self, enable_verify):
        r"""Sets the enable_verify of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 该检查项是否可验证，要求为Linux且agent版本>=3.2.24 **取值范围** - true  : 可验证 - false : 不可验证

        :param enable_verify: The enable_verify of this SecurityCheckRuleHostResponseInfo.
        :type enable_verify: bool
        """
        self._enable_verify = enable_verify

    @property
    def enable_click(self):
        r"""Gets the enable_click of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 该检查项的修复&忽略&验证按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :return: The enable_click of this SecurityCheckRuleHostResponseInfo.
        :rtype: bool
        """
        return self._enable_click

    @enable_click.setter
    def enable_click(self, enable_click):
        r"""Sets the enable_click of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 该检查项的修复&忽略&验证按钮是否可单击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :param enable_click: The enable_click of this SecurityCheckRuleHostResponseInfo.
        :type enable_click: bool
        """
        self._enable_click = enable_click

    @property
    def cancel_ignore_enable_click(self):
        r"""Gets the cancel_ignore_enable_click of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :return: The cancel_ignore_enable_click of this SecurityCheckRuleHostResponseInfo.
        :rtype: bool
        """
        return self._cancel_ignore_enable_click

    @cancel_ignore_enable_click.setter
    def cancel_ignore_enable_click(self, cancel_ignore_enable_click):
        r"""Sets the cancel_ignore_enable_click of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 已忽略检查项是否可点击 **取值范围** - true  : 按钮可单击 - false : 按钮不可单击

        :param cancel_ignore_enable_click: The cancel_ignore_enable_click of this SecurityCheckRuleHostResponseInfo.
        :type cancel_ignore_enable_click: bool
        """
        self._cancel_ignore_enable_click = cancel_ignore_enable_click

    @property
    def result_type(self):
        r"""Gets the result_type of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 检测结果类型 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白(表示检测失败，但已进行加白)

        :return: The result_type of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        r"""Sets the result_type of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 检测结果类型 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白(表示检测失败，但已进行加白)

        :param result_type: The result_type of this SecurityCheckRuleHostResponseInfo.
        :type result_type: str
        """
        self._result_type = result_type

    @property
    def fix_failed_reason(self):
        r"""Gets the fix_failed_reason of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 修复失败原因 **取值范围** 字符长度0-256位

        :return: The fix_failed_reason of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._fix_failed_reason

    @fix_failed_reason.setter
    def fix_failed_reason(self, fix_failed_reason):
        r"""Sets the fix_failed_reason of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 修复失败原因 **取值范围** 字符长度0-256位

        :param fix_failed_reason: The fix_failed_reason of this SecurityCheckRuleHostResponseInfo.
        :type fix_failed_reason: str
        """
        self._fix_failed_reason = fix_failed_reason

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 集群ID **取值范围** 字符长度0-64位

        :return: The cluster_id of this SecurityCheckRuleHostResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this SecurityCheckRuleHostResponseInfo.

        **参数解释** 集群ID **取值范围** 字符长度0-64位

        :param cluster_id: The cluster_id of this SecurityCheckRuleHostResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, SecurityCheckRuleHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
