# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaselineOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_time': 'int',
        'host_num': 'int',
        'failed_host_num': 'int',
        'check_type_num': 'int',
        'check_rule_num': 'int',
        'check_rule_pass_rate': 'int',
        'cn_standard_check_rule_pass_rate': 'int',
        'hw_standard_check_rule_pass_rate': 'int',
        'check_rule_failed_num': 'int',
        'check_rule_high_risk': 'int',
        'check_rule_medium_risk': 'int',
        'check_rule_low_risk': 'int',
        'weak_pwd_total_host': 'int',
        'weak_pwd_risk': 'int',
        'weak_pwd_normal': 'int',
        'weak_pwd_not_protected': 'int',
        'host_risks': 'list[HostRiskNumInfoResponseInfo]',
        'weak_pwd_risk_hosts': 'list[HostWeakPwdRiskNumInfoResponseInfo]'
    }

    attribute_map = {
        'scan_time': 'scan_time',
        'host_num': 'host_num',
        'failed_host_num': 'failed_host_num',
        'check_type_num': 'check_type_num',
        'check_rule_num': 'check_rule_num',
        'check_rule_pass_rate': 'check_rule_pass_rate',
        'cn_standard_check_rule_pass_rate': 'cn_standard_check_rule_pass_rate',
        'hw_standard_check_rule_pass_rate': 'hw_standard_check_rule_pass_rate',
        'check_rule_failed_num': 'check_rule_failed_num',
        'check_rule_high_risk': 'check_rule_high_risk',
        'check_rule_medium_risk': 'check_rule_medium_risk',
        'check_rule_low_risk': 'check_rule_low_risk',
        'weak_pwd_total_host': 'weak_pwd_total_host',
        'weak_pwd_risk': 'weak_pwd_risk',
        'weak_pwd_normal': 'weak_pwd_normal',
        'weak_pwd_not_protected': 'weak_pwd_not_protected',
        'host_risks': 'host_risks',
        'weak_pwd_risk_hosts': 'weak_pwd_risk_hosts'
    }

    def __init__(self, scan_time=None, host_num=None, failed_host_num=None, check_type_num=None, check_rule_num=None, check_rule_pass_rate=None, cn_standard_check_rule_pass_rate=None, hw_standard_check_rule_pass_rate=None, check_rule_failed_num=None, check_rule_high_risk=None, check_rule_medium_risk=None, check_rule_low_risk=None, weak_pwd_total_host=None, weak_pwd_risk=None, weak_pwd_normal=None, weak_pwd_not_protected=None, host_risks=None, weak_pwd_risk_hosts=None):
        r"""ShowBaselineOverviewResponse

        The model defined in huaweicloud sdk

        :param scan_time: **参数解释**: 最新检测时间(ms)。 **取值范围**: 取值0-9223372036854775807 
        :type scan_time: int
        :param host_num: **参数解释**: 检查服务器数量。 **取值范围**: 取值0-2147483647 
        :type host_num: int
        :param failed_host_num: **参数解释**: 未通过主机数。 **取值范围**: 取值0-2147483647 
        :type failed_host_num: int
        :param check_type_num: **参数解释**: 检测基线数量。例如共检测了SSH、CentOS 7这2个配置检测（基线）类型，值就是2。 **取值范围**: 取值0-2147483647 
        :type check_type_num: int
        :param check_rule_num: **参数解释**: 基线检测项（检测规则）数量。例如SSH基线检测了17条规则，CentOS 7基线检测了60条规则，值就是17+60&#x3D;77。 **取值范围**: 取值0-2147483647 
        :type check_rule_num: int
        :param check_rule_pass_rate: **参数解释**: 基线检查项通过率。 **取值范围**: 取值0-2147483647 
        :type check_rule_pass_rate: int
        :param cn_standard_check_rule_pass_rate: **参数解释**: 云安全实践基线检查项通过率。 **取值范围**: 取值0-2147483647 
        :type cn_standard_check_rule_pass_rate: int
        :param hw_standard_check_rule_pass_rate: **参数解释**: 等保合规基线检查项通过率。 **取值范围**: 取值0-2147483647 
        :type hw_standard_check_rule_pass_rate: int
        :param check_rule_failed_num: **参数解释**: 未通过的检查项数量。 **取值范围**: 取值0-2147483647 
        :type check_rule_failed_num: int
        :param check_rule_high_risk: **参数解释**: 高危检查项数量。 **取值范围**: 取值0-2147483647 
        :type check_rule_high_risk: int
        :param check_rule_medium_risk: **参数解释**: 中危检查项数量。 **取值范围**: 取值0-2147483647 
        :type check_rule_medium_risk: int
        :param check_rule_low_risk: **参数解释**: 低危检查项数量。 **取值范围**: 取值0-2147483647 
        :type check_rule_low_risk: int
        :param weak_pwd_total_host: **参数解释**: 弱口令检测主机总数。 **取值范围**: 取值0-2147483647 
        :type weak_pwd_total_host: int
        :param weak_pwd_risk: **参数解释**: 弱口令检测结果：有弱口令的主机数。 **取值范围**: 取值0-2147483647 
        :type weak_pwd_risk: int
        :param weak_pwd_normal: **参数解释**: 弱口令检测结果：无弱口令的主机数。 **取值范围**: 取值0-2147483647 
        :type weak_pwd_normal: int
        :param weak_pwd_not_protected: **参数解释**: 弱口令检测结果：未开启防护的主机数。 **取值范围**: 取值0-2147483647 
        :type weak_pwd_not_protected: int
        :param host_risks: 服务器风险TOP5列表
        :type host_risks: list[:class:`huaweicloudsdkhss.v5.HostRiskNumInfoResponseInfo`]
        :param weak_pwd_risk_hosts: 主机弱口令风险TOP5列表
        :type weak_pwd_risk_hosts: list[:class:`huaweicloudsdkhss.v5.HostWeakPwdRiskNumInfoResponseInfo`]
        """
        
        super().__init__()

        self._scan_time = None
        self._host_num = None
        self._failed_host_num = None
        self._check_type_num = None
        self._check_rule_num = None
        self._check_rule_pass_rate = None
        self._cn_standard_check_rule_pass_rate = None
        self._hw_standard_check_rule_pass_rate = None
        self._check_rule_failed_num = None
        self._check_rule_high_risk = None
        self._check_rule_medium_risk = None
        self._check_rule_low_risk = None
        self._weak_pwd_total_host = None
        self._weak_pwd_risk = None
        self._weak_pwd_normal = None
        self._weak_pwd_not_protected = None
        self._host_risks = None
        self._weak_pwd_risk_hosts = None
        self.discriminator = None

        if scan_time is not None:
            self.scan_time = scan_time
        if host_num is not None:
            self.host_num = host_num
        if failed_host_num is not None:
            self.failed_host_num = failed_host_num
        if check_type_num is not None:
            self.check_type_num = check_type_num
        if check_rule_num is not None:
            self.check_rule_num = check_rule_num
        if check_rule_pass_rate is not None:
            self.check_rule_pass_rate = check_rule_pass_rate
        if cn_standard_check_rule_pass_rate is not None:
            self.cn_standard_check_rule_pass_rate = cn_standard_check_rule_pass_rate
        if hw_standard_check_rule_pass_rate is not None:
            self.hw_standard_check_rule_pass_rate = hw_standard_check_rule_pass_rate
        if check_rule_failed_num is not None:
            self.check_rule_failed_num = check_rule_failed_num
        if check_rule_high_risk is not None:
            self.check_rule_high_risk = check_rule_high_risk
        if check_rule_medium_risk is not None:
            self.check_rule_medium_risk = check_rule_medium_risk
        if check_rule_low_risk is not None:
            self.check_rule_low_risk = check_rule_low_risk
        if weak_pwd_total_host is not None:
            self.weak_pwd_total_host = weak_pwd_total_host
        if weak_pwd_risk is not None:
            self.weak_pwd_risk = weak_pwd_risk
        if weak_pwd_normal is not None:
            self.weak_pwd_normal = weak_pwd_normal
        if weak_pwd_not_protected is not None:
            self.weak_pwd_not_protected = weak_pwd_not_protected
        if host_risks is not None:
            self.host_risks = host_risks
        if weak_pwd_risk_hosts is not None:
            self.weak_pwd_risk_hosts = weak_pwd_risk_hosts

    @property
    def scan_time(self):
        r"""Gets the scan_time of this ShowBaselineOverviewResponse.

        **参数解释**: 最新检测时间(ms)。 **取值范围**: 取值0-9223372036854775807 

        :return: The scan_time of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this ShowBaselineOverviewResponse.

        **参数解释**: 最新检测时间(ms)。 **取值范围**: 取值0-9223372036854775807 

        :param scan_time: The scan_time of this ShowBaselineOverviewResponse.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def host_num(self):
        r"""Gets the host_num of this ShowBaselineOverviewResponse.

        **参数解释**: 检查服务器数量。 **取值范围**: 取值0-2147483647 

        :return: The host_num of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ShowBaselineOverviewResponse.

        **参数解释**: 检查服务器数量。 **取值范围**: 取值0-2147483647 

        :param host_num: The host_num of this ShowBaselineOverviewResponse.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def failed_host_num(self):
        r"""Gets the failed_host_num of this ShowBaselineOverviewResponse.

        **参数解释**: 未通过主机数。 **取值范围**: 取值0-2147483647 

        :return: The failed_host_num of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._failed_host_num

    @failed_host_num.setter
    def failed_host_num(self, failed_host_num):
        r"""Sets the failed_host_num of this ShowBaselineOverviewResponse.

        **参数解释**: 未通过主机数。 **取值范围**: 取值0-2147483647 

        :param failed_host_num: The failed_host_num of this ShowBaselineOverviewResponse.
        :type failed_host_num: int
        """
        self._failed_host_num = failed_host_num

    @property
    def check_type_num(self):
        r"""Gets the check_type_num of this ShowBaselineOverviewResponse.

        **参数解释**: 检测基线数量。例如共检测了SSH、CentOS 7这2个配置检测（基线）类型，值就是2。 **取值范围**: 取值0-2147483647 

        :return: The check_type_num of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._check_type_num

    @check_type_num.setter
    def check_type_num(self, check_type_num):
        r"""Sets the check_type_num of this ShowBaselineOverviewResponse.

        **参数解释**: 检测基线数量。例如共检测了SSH、CentOS 7这2个配置检测（基线）类型，值就是2。 **取值范围**: 取值0-2147483647 

        :param check_type_num: The check_type_num of this ShowBaselineOverviewResponse.
        :type check_type_num: int
        """
        self._check_type_num = check_type_num

    @property
    def check_rule_num(self):
        r"""Gets the check_rule_num of this ShowBaselineOverviewResponse.

        **参数解释**: 基线检测项（检测规则）数量。例如SSH基线检测了17条规则，CentOS 7基线检测了60条规则，值就是17+60=77。 **取值范围**: 取值0-2147483647 

        :return: The check_rule_num of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._check_rule_num

    @check_rule_num.setter
    def check_rule_num(self, check_rule_num):
        r"""Sets the check_rule_num of this ShowBaselineOverviewResponse.

        **参数解释**: 基线检测项（检测规则）数量。例如SSH基线检测了17条规则，CentOS 7基线检测了60条规则，值就是17+60=77。 **取值范围**: 取值0-2147483647 

        :param check_rule_num: The check_rule_num of this ShowBaselineOverviewResponse.
        :type check_rule_num: int
        """
        self._check_rule_num = check_rule_num

    @property
    def check_rule_pass_rate(self):
        r"""Gets the check_rule_pass_rate of this ShowBaselineOverviewResponse.

        **参数解释**: 基线检查项通过率。 **取值范围**: 取值0-2147483647 

        :return: The check_rule_pass_rate of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._check_rule_pass_rate

    @check_rule_pass_rate.setter
    def check_rule_pass_rate(self, check_rule_pass_rate):
        r"""Sets the check_rule_pass_rate of this ShowBaselineOverviewResponse.

        **参数解释**: 基线检查项通过率。 **取值范围**: 取值0-2147483647 

        :param check_rule_pass_rate: The check_rule_pass_rate of this ShowBaselineOverviewResponse.
        :type check_rule_pass_rate: int
        """
        self._check_rule_pass_rate = check_rule_pass_rate

    @property
    def cn_standard_check_rule_pass_rate(self):
        r"""Gets the cn_standard_check_rule_pass_rate of this ShowBaselineOverviewResponse.

        **参数解释**: 云安全实践基线检查项通过率。 **取值范围**: 取值0-2147483647 

        :return: The cn_standard_check_rule_pass_rate of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._cn_standard_check_rule_pass_rate

    @cn_standard_check_rule_pass_rate.setter
    def cn_standard_check_rule_pass_rate(self, cn_standard_check_rule_pass_rate):
        r"""Sets the cn_standard_check_rule_pass_rate of this ShowBaselineOverviewResponse.

        **参数解释**: 云安全实践基线检查项通过率。 **取值范围**: 取值0-2147483647 

        :param cn_standard_check_rule_pass_rate: The cn_standard_check_rule_pass_rate of this ShowBaselineOverviewResponse.
        :type cn_standard_check_rule_pass_rate: int
        """
        self._cn_standard_check_rule_pass_rate = cn_standard_check_rule_pass_rate

    @property
    def hw_standard_check_rule_pass_rate(self):
        r"""Gets the hw_standard_check_rule_pass_rate of this ShowBaselineOverviewResponse.

        **参数解释**: 等保合规基线检查项通过率。 **取值范围**: 取值0-2147483647 

        :return: The hw_standard_check_rule_pass_rate of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._hw_standard_check_rule_pass_rate

    @hw_standard_check_rule_pass_rate.setter
    def hw_standard_check_rule_pass_rate(self, hw_standard_check_rule_pass_rate):
        r"""Sets the hw_standard_check_rule_pass_rate of this ShowBaselineOverviewResponse.

        **参数解释**: 等保合规基线检查项通过率。 **取值范围**: 取值0-2147483647 

        :param hw_standard_check_rule_pass_rate: The hw_standard_check_rule_pass_rate of this ShowBaselineOverviewResponse.
        :type hw_standard_check_rule_pass_rate: int
        """
        self._hw_standard_check_rule_pass_rate = hw_standard_check_rule_pass_rate

    @property
    def check_rule_failed_num(self):
        r"""Gets the check_rule_failed_num of this ShowBaselineOverviewResponse.

        **参数解释**: 未通过的检查项数量。 **取值范围**: 取值0-2147483647 

        :return: The check_rule_failed_num of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._check_rule_failed_num

    @check_rule_failed_num.setter
    def check_rule_failed_num(self, check_rule_failed_num):
        r"""Sets the check_rule_failed_num of this ShowBaselineOverviewResponse.

        **参数解释**: 未通过的检查项数量。 **取值范围**: 取值0-2147483647 

        :param check_rule_failed_num: The check_rule_failed_num of this ShowBaselineOverviewResponse.
        :type check_rule_failed_num: int
        """
        self._check_rule_failed_num = check_rule_failed_num

    @property
    def check_rule_high_risk(self):
        r"""Gets the check_rule_high_risk of this ShowBaselineOverviewResponse.

        **参数解释**: 高危检查项数量。 **取值范围**: 取值0-2147483647 

        :return: The check_rule_high_risk of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._check_rule_high_risk

    @check_rule_high_risk.setter
    def check_rule_high_risk(self, check_rule_high_risk):
        r"""Sets the check_rule_high_risk of this ShowBaselineOverviewResponse.

        **参数解释**: 高危检查项数量。 **取值范围**: 取值0-2147483647 

        :param check_rule_high_risk: The check_rule_high_risk of this ShowBaselineOverviewResponse.
        :type check_rule_high_risk: int
        """
        self._check_rule_high_risk = check_rule_high_risk

    @property
    def check_rule_medium_risk(self):
        r"""Gets the check_rule_medium_risk of this ShowBaselineOverviewResponse.

        **参数解释**: 中危检查项数量。 **取值范围**: 取值0-2147483647 

        :return: The check_rule_medium_risk of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._check_rule_medium_risk

    @check_rule_medium_risk.setter
    def check_rule_medium_risk(self, check_rule_medium_risk):
        r"""Sets the check_rule_medium_risk of this ShowBaselineOverviewResponse.

        **参数解释**: 中危检查项数量。 **取值范围**: 取值0-2147483647 

        :param check_rule_medium_risk: The check_rule_medium_risk of this ShowBaselineOverviewResponse.
        :type check_rule_medium_risk: int
        """
        self._check_rule_medium_risk = check_rule_medium_risk

    @property
    def check_rule_low_risk(self):
        r"""Gets the check_rule_low_risk of this ShowBaselineOverviewResponse.

        **参数解释**: 低危检查项数量。 **取值范围**: 取值0-2147483647 

        :return: The check_rule_low_risk of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._check_rule_low_risk

    @check_rule_low_risk.setter
    def check_rule_low_risk(self, check_rule_low_risk):
        r"""Sets the check_rule_low_risk of this ShowBaselineOverviewResponse.

        **参数解释**: 低危检查项数量。 **取值范围**: 取值0-2147483647 

        :param check_rule_low_risk: The check_rule_low_risk of this ShowBaselineOverviewResponse.
        :type check_rule_low_risk: int
        """
        self._check_rule_low_risk = check_rule_low_risk

    @property
    def weak_pwd_total_host(self):
        r"""Gets the weak_pwd_total_host of this ShowBaselineOverviewResponse.

        **参数解释**: 弱口令检测主机总数。 **取值范围**: 取值0-2147483647 

        :return: The weak_pwd_total_host of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._weak_pwd_total_host

    @weak_pwd_total_host.setter
    def weak_pwd_total_host(self, weak_pwd_total_host):
        r"""Sets the weak_pwd_total_host of this ShowBaselineOverviewResponse.

        **参数解释**: 弱口令检测主机总数。 **取值范围**: 取值0-2147483647 

        :param weak_pwd_total_host: The weak_pwd_total_host of this ShowBaselineOverviewResponse.
        :type weak_pwd_total_host: int
        """
        self._weak_pwd_total_host = weak_pwd_total_host

    @property
    def weak_pwd_risk(self):
        r"""Gets the weak_pwd_risk of this ShowBaselineOverviewResponse.

        **参数解释**: 弱口令检测结果：有弱口令的主机数。 **取值范围**: 取值0-2147483647 

        :return: The weak_pwd_risk of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._weak_pwd_risk

    @weak_pwd_risk.setter
    def weak_pwd_risk(self, weak_pwd_risk):
        r"""Sets the weak_pwd_risk of this ShowBaselineOverviewResponse.

        **参数解释**: 弱口令检测结果：有弱口令的主机数。 **取值范围**: 取值0-2147483647 

        :param weak_pwd_risk: The weak_pwd_risk of this ShowBaselineOverviewResponse.
        :type weak_pwd_risk: int
        """
        self._weak_pwd_risk = weak_pwd_risk

    @property
    def weak_pwd_normal(self):
        r"""Gets the weak_pwd_normal of this ShowBaselineOverviewResponse.

        **参数解释**: 弱口令检测结果：无弱口令的主机数。 **取值范围**: 取值0-2147483647 

        :return: The weak_pwd_normal of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._weak_pwd_normal

    @weak_pwd_normal.setter
    def weak_pwd_normal(self, weak_pwd_normal):
        r"""Sets the weak_pwd_normal of this ShowBaselineOverviewResponse.

        **参数解释**: 弱口令检测结果：无弱口令的主机数。 **取值范围**: 取值0-2147483647 

        :param weak_pwd_normal: The weak_pwd_normal of this ShowBaselineOverviewResponse.
        :type weak_pwd_normal: int
        """
        self._weak_pwd_normal = weak_pwd_normal

    @property
    def weak_pwd_not_protected(self):
        r"""Gets the weak_pwd_not_protected of this ShowBaselineOverviewResponse.

        **参数解释**: 弱口令检测结果：未开启防护的主机数。 **取值范围**: 取值0-2147483647 

        :return: The weak_pwd_not_protected of this ShowBaselineOverviewResponse.
        :rtype: int
        """
        return self._weak_pwd_not_protected

    @weak_pwd_not_protected.setter
    def weak_pwd_not_protected(self, weak_pwd_not_protected):
        r"""Sets the weak_pwd_not_protected of this ShowBaselineOverviewResponse.

        **参数解释**: 弱口令检测结果：未开启防护的主机数。 **取值范围**: 取值0-2147483647 

        :param weak_pwd_not_protected: The weak_pwd_not_protected of this ShowBaselineOverviewResponse.
        :type weak_pwd_not_protected: int
        """
        self._weak_pwd_not_protected = weak_pwd_not_protected

    @property
    def host_risks(self):
        r"""Gets the host_risks of this ShowBaselineOverviewResponse.

        服务器风险TOP5列表

        :return: The host_risks of this ShowBaselineOverviewResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostRiskNumInfoResponseInfo`]
        """
        return self._host_risks

    @host_risks.setter
    def host_risks(self, host_risks):
        r"""Sets the host_risks of this ShowBaselineOverviewResponse.

        服务器风险TOP5列表

        :param host_risks: The host_risks of this ShowBaselineOverviewResponse.
        :type host_risks: list[:class:`huaweicloudsdkhss.v5.HostRiskNumInfoResponseInfo`]
        """
        self._host_risks = host_risks

    @property
    def weak_pwd_risk_hosts(self):
        r"""Gets the weak_pwd_risk_hosts of this ShowBaselineOverviewResponse.

        主机弱口令风险TOP5列表

        :return: The weak_pwd_risk_hosts of this ShowBaselineOverviewResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostWeakPwdRiskNumInfoResponseInfo`]
        """
        return self._weak_pwd_risk_hosts

    @weak_pwd_risk_hosts.setter
    def weak_pwd_risk_hosts(self, weak_pwd_risk_hosts):
        r"""Sets the weak_pwd_risk_hosts of this ShowBaselineOverviewResponse.

        主机弱口令风险TOP5列表

        :param weak_pwd_risk_hosts: The weak_pwd_risk_hosts of this ShowBaselineOverviewResponse.
        :type weak_pwd_risk_hosts: list[:class:`huaweicloudsdkhss.v5.HostWeakPwdRiskNumInfoResponseInfo`]
        """
        self._weak_pwd_risk_hosts = weak_pwd_risk_hosts

    def to_dict(self):
        import warnings
        warnings.warn("ShowBaselineOverviewResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowBaselineOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
