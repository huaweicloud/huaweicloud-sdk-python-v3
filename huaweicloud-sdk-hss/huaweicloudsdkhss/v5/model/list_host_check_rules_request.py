# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostCheckRulesRequest:

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
        'host_id': 'str',
        'policy_group_id': 'str',
        'result_type': 'str',
        'standard': 'str',
        'check_name': 'str',
        'check_rule_name': 'str',
        'tag': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_id': 'host_id',
        'policy_group_id': 'policy_group_id',
        'result_type': 'result_type',
        'standard': 'standard',
        'check_name': 'check_name',
        'check_rule_name': 'check_rule_name',
        'tag': 'tag',
        'severity': 'severity'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, host_id=None, policy_group_id=None, result_type=None, standard=None, check_name=None, check_rule_name=None, tag=None, severity=None):
        r"""ListHostCheckRulesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_id: **参数解释** 主机ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及
        :type host_id: str
        :param policy_group_id: **参数解释** 策略组ID **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及
        :type policy_group_id: str
        :param result_type: **参数解释** 检测结果类型 **约束限制** 不涉及 **取值范围** - safe：已通过 - unhandled： 未处理 - ignored：已忽略 - fixing：修复中 - fix-failed：修复失败 - verifying：验证中 - add_to_whitelist：已加白  **默认取值** 不涉及
        :type result_type: str
        :param standard: **参数解释** 基线分类 **约束限制** 不涉及 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及
        :type standard: str
        :param check_name: **参数解释** 配置检查（基线）的名称，如SSH、CentOS 7、Windows **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及
        :type check_name: str
        :param check_rule_name: **参数解释** 检查项（检查规则）名称，支持模糊匹配 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及
        :type check_rule_name: str
        :param tag: **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及
        :type tag: str
        :param severity: **参数解释** 风险等级 **约束限制** 不涉及 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值** 不涉及
        :type severity: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_id = None
        self._policy_group_id = None
        self._result_type = None
        self._standard = None
        self._check_name = None
        self._check_rule_name = None
        self._tag = None
        self._severity = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.host_id = host_id
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if result_type is not None:
            self.result_type = result_type
        self.standard = standard
        self.check_name = check_name
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if tag is not None:
            self.tag = tag
        if severity is not None:
            self.severity = severity

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHostCheckRulesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHostCheckRulesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListHostCheckRulesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListHostCheckRulesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListHostCheckRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHostCheckRulesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListHostCheckRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHostCheckRulesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListHostCheckRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHostCheckRulesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListHostCheckRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_id(self):
        r"""Gets the host_id of this ListHostCheckRulesRequest.

        **参数解释** 主机ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及

        :return: The host_id of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListHostCheckRulesRequest.

        **参数解释** 主机ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及

        :param host_id: The host_id of this ListHostCheckRulesRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListHostCheckRulesRequest.

        **参数解释** 策略组ID **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及

        :return: The policy_group_id of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListHostCheckRulesRequest.

        **参数解释** 策略组ID **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及

        :param policy_group_id: The policy_group_id of this ListHostCheckRulesRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def result_type(self):
        r"""Gets the result_type of this ListHostCheckRulesRequest.

        **参数解释** 检测结果类型 **约束限制** 不涉及 **取值范围** - safe：已通过 - unhandled： 未处理 - ignored：已忽略 - fixing：修复中 - fix-failed：修复失败 - verifying：验证中 - add_to_whitelist：已加白  **默认取值** 不涉及

        :return: The result_type of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        r"""Sets the result_type of this ListHostCheckRulesRequest.

        **参数解释** 检测结果类型 **约束限制** 不涉及 **取值范围** - safe：已通过 - unhandled： 未处理 - ignored：已忽略 - fixing：修复中 - fix-failed：修复失败 - verifying：验证中 - add_to_whitelist：已加白  **默认取值** 不涉及

        :param result_type: The result_type of this ListHostCheckRulesRequest.
        :type result_type: str
        """
        self._result_type = result_type

    @property
    def standard(self):
        r"""Gets the standard of this ListHostCheckRulesRequest.

        **参数解释** 基线分类 **约束限制** 不涉及 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及

        :return: The standard of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListHostCheckRulesRequest.

        **参数解释** 基线分类 **约束限制** 不涉及 **取值范围** - cn_standard：等保合规标准 - hw_standard：云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及

        :param standard: The standard of this ListHostCheckRulesRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def check_name(self):
        r"""Gets the check_name of this ListHostCheckRulesRequest.

        **参数解释** 配置检查（基线）的名称，如SSH、CentOS 7、Windows **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及

        :return: The check_name of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ListHostCheckRulesRequest.

        **参数解释** 配置检查（基线）的名称，如SSH、CentOS 7、Windows **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及

        :param check_name: The check_name of this ListHostCheckRulesRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this ListHostCheckRulesRequest.

        **参数解释** 检查项（检查规则）名称，支持模糊匹配 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及

        :return: The check_rule_name of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this ListHostCheckRulesRequest.

        **参数解释** 检查项（检查规则）名称，支持模糊匹配 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及

        :param check_rule_name: The check_rule_name of this ListHostCheckRulesRequest.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def tag(self):
        r"""Gets the tag of this ListHostCheckRulesRequest.

        **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :return: The tag of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListHostCheckRulesRequest.

        **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :param tag: The tag of this ListHostCheckRulesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def severity(self):
        r"""Gets the severity of this ListHostCheckRulesRequest.

        **参数解释** 风险等级 **约束限制** 不涉及 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值** 不涉及

        :return: The severity of this ListHostCheckRulesRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListHostCheckRulesRequest.

        **参数解释** 风险等级 **约束限制** 不涉及 **取值范围** - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急  **默认取值** 不涉及

        :param severity: The severity of this ListHostCheckRulesRequest.
        :type severity: str
        """
        self._severity = severity

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
        if not isinstance(other, ListHostCheckRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
