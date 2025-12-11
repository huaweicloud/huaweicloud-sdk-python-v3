# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllRiskConfigCheckRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'check_type': 'str',
        'standard': 'str',
        'statistics_scan_result': 'str',
        'check_rule_name': 'str',
        'severity': 'str',
        'cluster_id': 'str',
        'tag': 'str',
        'policy_group_id': 'str',
        'statistics_flag': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'check_type': 'check_type',
        'standard': 'standard',
        'statistics_scan_result': 'statistics_scan_result',
        'check_rule_name': 'check_rule_name',
        'severity': 'severity',
        'cluster_id': 'cluster_id',
        'tag': 'tag',
        'policy_group_id': 'policy_group_id',
        'statistics_flag': 'statistics_flag'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, check_type=None, standard=None, statistics_scan_result=None, check_rule_name=None, severity=None, cluster_id=None, tag=None, policy_group_id=None, statistics_flag=None):
        r"""ListAllRiskConfigCheckRulesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param check_type: **参数解释** 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及
        :type check_type: str
        :param standard: **参数解释** 标准类型 **约束限制** 不涉及 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及
        :type standard: str
        :param statistics_scan_result: **参数解释** 统计结果类型 **约束限制** 不涉及 **取值范围** - pass：已通过，表示查看主机全部通过的检查项 - failed：未通过，表示查看主机全部未通过 &amp; 全部未处理的检查项 - processed：已处理，表示查看主机存在未通过 &amp; 未通过主机已全部处理(忽略、加白)的检查项  **默认取值** 不涉及
        :type statistics_scan_result: str
        :param check_rule_name: **参数解释** 检查项（检查规则）名称，支持模糊匹配 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及
        :type check_rule_name: str
        :param severity: **参数解释** 风险等级 **约束限制** 不涉及 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 **默认取值** 不涉及
        :type severity: str
        :param cluster_id: **参数解释** 集群ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及
        :type cluster_id: str
        :param tag: **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及
        :type tag: str
        :param policy_group_id: **参数解释** 策略组ID，不赋值时，查租户所有主机，host_id存在时，此值无效 **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及
        :type policy_group_id: str
        :param statistics_flag: **参数解释** 是否从统计维度展示数据 **约束限制** 不涉及 **取值范围** - false : 不从统计维度展示 - true  : 从统计维度展示  **默认取值** false
        :type statistics_flag: bool
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._check_type = None
        self._standard = None
        self._statistics_scan_result = None
        self._check_rule_name = None
        self._severity = None
        self._cluster_id = None
        self._tag = None
        self._policy_group_id = None
        self._statistics_flag = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard
        if statistics_scan_result is not None:
            self.statistics_scan_result = statistics_scan_result
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if severity is not None:
            self.severity = severity
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if tag is not None:
            self.tag = tag
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if statistics_flag is not None:
            self.statistics_flag = statistics_flag

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAllRiskConfigCheckRulesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAllRiskConfigCheckRulesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAllRiskConfigCheckRulesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAllRiskConfigCheckRulesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListAllRiskConfigCheckRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAllRiskConfigCheckRulesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListAllRiskConfigCheckRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAllRiskConfigCheckRulesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAllRiskConfigCheckRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAllRiskConfigCheckRulesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAllRiskConfigCheckRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def check_type(self):
        r"""Gets the check_type of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :return: The check_type of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :param check_type: The check_type of this ListAllRiskConfigCheckRulesRequest.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 标准类型 **约束限制** 不涉及 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及

        :return: The standard of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 标准类型 **约束限制** 不涉及 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及

        :param standard: The standard of this ListAllRiskConfigCheckRulesRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def statistics_scan_result(self):
        r"""Gets the statistics_scan_result of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 统计结果类型 **约束限制** 不涉及 **取值范围** - pass：已通过，表示查看主机全部通过的检查项 - failed：未通过，表示查看主机全部未通过 & 全部未处理的检查项 - processed：已处理，表示查看主机存在未通过 & 未通过主机已全部处理(忽略、加白)的检查项  **默认取值** 不涉及

        :return: The statistics_scan_result of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._statistics_scan_result

    @statistics_scan_result.setter
    def statistics_scan_result(self, statistics_scan_result):
        r"""Sets the statistics_scan_result of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 统计结果类型 **约束限制** 不涉及 **取值范围** - pass：已通过，表示查看主机全部通过的检查项 - failed：未通过，表示查看主机全部未通过 & 全部未处理的检查项 - processed：已处理，表示查看主机存在未通过 & 未通过主机已全部处理(忽略、加白)的检查项  **默认取值** 不涉及

        :param statistics_scan_result: The statistics_scan_result of this ListAllRiskConfigCheckRulesRequest.
        :type statistics_scan_result: str
        """
        self._statistics_scan_result = statistics_scan_result

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 检查项（检查规则）名称，支持模糊匹配 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及

        :return: The check_rule_name of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 检查项（检查规则）名称，支持模糊匹配 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及

        :param check_rule_name: The check_rule_name of this ListAllRiskConfigCheckRulesRequest.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def severity(self):
        r"""Gets the severity of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 风险等级 **约束限制** 不涉及 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 **默认取值** 不涉及

        :return: The severity of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 风险等级 **约束限制** 不涉及 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 **默认取值** 不涉及

        :param severity: The severity of this ListAllRiskConfigCheckRulesRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 集群ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及

        :return: The cluster_id of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 集群ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及

        :param cluster_id: The cluster_id of this ListAllRiskConfigCheckRulesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def tag(self):
        r"""Gets the tag of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :return: The tag of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :param tag: The tag of this ListAllRiskConfigCheckRulesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 策略组ID，不赋值时，查租户所有主机，host_id存在时，此值无效 **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及

        :return: The policy_group_id of this ListAllRiskConfigCheckRulesRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 策略组ID，不赋值时，查租户所有主机，host_id存在时，此值无效 **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及

        :param policy_group_id: The policy_group_id of this ListAllRiskConfigCheckRulesRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def statistics_flag(self):
        r"""Gets the statistics_flag of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 是否从统计维度展示数据 **约束限制** 不涉及 **取值范围** - false : 不从统计维度展示 - true  : 从统计维度展示  **默认取值** false

        :return: The statistics_flag of this ListAllRiskConfigCheckRulesRequest.
        :rtype: bool
        """
        return self._statistics_flag

    @statistics_flag.setter
    def statistics_flag(self, statistics_flag):
        r"""Sets the statistics_flag of this ListAllRiskConfigCheckRulesRequest.

        **参数解释** 是否从统计维度展示数据 **约束限制** 不涉及 **取值范围** - false : 不从统计维度展示 - true  : 从统计维度展示  **默认取值** false

        :param statistics_flag: The statistics_flag of this ListAllRiskConfigCheckRulesRequest.
        :type statistics_flag: bool
        """
        self._statistics_flag = statistics_flag

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
        if not isinstance(other, ListAllRiskConfigCheckRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
