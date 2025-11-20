# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDefaultSecurityCheckPolicyDetailsRequest:

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
        'support_os': 'str',
        'check_type': 'str',
        'standard': 'str',
        'tag': 'str',
        'check_rule_name': 'str',
        'severity': 'str',
        'level': 'str',
        'group_id': 'str',
        'checked': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'support_os': 'support_os',
        'check_type': 'check_type',
        'standard': 'standard',
        'tag': 'tag',
        'check_rule_name': 'check_rule_name',
        'severity': 'severity',
        'level': 'level',
        'group_id': 'group_id',
        'checked': 'checked'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, support_os=None, check_type=None, standard=None, tag=None, check_rule_name=None, severity=None, level=None, group_id=None, checked=None):
        r"""ShowDefaultSecurityCheckPolicyDetailsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param support_os: **参数解释** 策略支持的操作系统类型 **约束限制** 不涉及 **取值范围** - Linux : Linux操作系统 - Windows : Windows操作系统  **默认取值** Linux
        :type support_os: str
        :param check_type: **参数解释** 配置检查（基线）的类型,例如SSH、CentOS 7、Windows Server 2019 R2、Windows Server 2016 R2、MySQL5-Windows、weakpwd、pwdcomplexity **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及
        :type check_type: str
        :param standard: **参数解释** 标准类型 **约束限制** 不涉及 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard: 通用安全标准  **默认取值** 不涉及
        :type standard: str
        :param tag: **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及
        :type tag: str
        :param check_rule_name: **参数解释** 配置检查（基线）检查项的名称 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及
        :type check_rule_name: str
        :param severity: **参数解释** 配置检查（基线）检查项的风险程度 **约束限制** 不涉及 **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危  **默认取值** 不涉及
        :type severity: str
        :param level: **参数解释** 配置检查（基线）检查项的版本信息 **约束限制** 不涉及 **取值范围** 字符长度0-32位 **默认取值** 不涉及
        :type level: str
        :param group_id: **参数解释** 策略组ID **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及
        :type group_id: str
        :param checked: **参数解释** 默认是否被选中 **约束限制** 不涉及 **取值范围** false : 不选中 true  : 默认  **默认取值** true
        :type checked: bool
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._support_os = None
        self._check_type = None
        self._standard = None
        self._tag = None
        self._check_rule_name = None
        self._severity = None
        self._level = None
        self._group_id = None
        self._checked = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        self.support_os = support_os
        if check_type is not None:
            self.check_type = check_type
        self.standard = standard
        if tag is not None:
            self.tag = tag
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if severity is not None:
            self.severity = severity
        if level is not None:
            self.level = level
        if group_id is not None:
            self.group_id = group_id
        if checked is not None:
            self.checked = checked

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def support_os(self):
        r"""Gets the support_os of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 策略支持的操作系统类型 **约束限制** 不涉及 **取值范围** - Linux : Linux操作系统 - Windows : Windows操作系统  **默认取值** Linux

        :return: The support_os of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 策略支持的操作系统类型 **约束限制** 不涉及 **取值范围** - Linux : Linux操作系统 - Windows : Windows操作系统  **默认取值** Linux

        :param support_os: The support_os of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def check_type(self):
        r"""Gets the check_type of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 配置检查（基线）的类型,例如SSH、CentOS 7、Windows Server 2019 R2、Windows Server 2016 R2、MySQL5-Windows、weakpwd、pwdcomplexity **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :return: The check_type of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 配置检查（基线）的类型,例如SSH、CentOS 7、Windows Server 2019 R2、Windows Server 2016 R2、MySQL5-Windows、weakpwd、pwdcomplexity **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :param check_type: The check_type of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 标准类型 **约束限制** 不涉及 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard: 通用安全标准  **默认取值** 不涉及

        :return: The standard of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 标准类型 **约束限制** 不涉及 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard: 通用安全标准  **默认取值** 不涉及

        :param standard: The standard of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def tag(self):
        r"""Gets the tag of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :return: The tag of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 基线检查项的类型 **约束限制** 不涉及 **取值范围** 字符长度0-256位 **默认取值** 不涉及

        :param tag: The tag of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 配置检查（基线）检查项的名称 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及

        :return: The check_rule_name of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 配置检查（基线）检查项的名称 **约束限制** 不涉及 **取值范围** 字符长度0-2048位 **默认取值** 不涉及

        :param check_rule_name: The check_rule_name of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def severity(self):
        r"""Gets the severity of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 配置检查（基线）检查项的风险程度 **约束限制** 不涉及 **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危  **默认取值** 不涉及

        :return: The severity of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 配置检查（基线）检查项的风险程度 **约束限制** 不涉及 **取值范围** - Low    : 低危 - Medium : 中危 - High   : 高危  **默认取值** 不涉及

        :param severity: The severity of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def level(self):
        r"""Gets the level of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 配置检查（基线）检查项的版本信息 **约束限制** 不涉及 **取值范围** 字符长度0-32位 **默认取值** 不涉及

        :return: The level of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 配置检查（基线）检查项的版本信息 **约束限制** 不涉及 **取值范围** 字符长度0-32位 **默认取值** 不涉及

        :param level: The level of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type level: str
        """
        self._level = level

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 策略组ID **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及

        :return: The group_id of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 策略组ID **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及

        :param group_id: The group_id of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def checked(self):
        r"""Gets the checked of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 默认是否被选中 **约束限制** 不涉及 **取值范围** false : 不选中 true  : 默认  **默认取值** true

        :return: The checked of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        r"""Sets the checked of this ShowDefaultSecurityCheckPolicyDetailsRequest.

        **参数解释** 默认是否被选中 **约束限制** 不涉及 **取值范围** false : 不选中 true  : 默认  **默认取值** true

        :param checked: The checked of this ShowDefaultSecurityCheckPolicyDetailsRequest.
        :type checked: bool
        """
        self._checked = checked

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
        if not isinstance(other, ShowDefaultSecurityCheckPolicyDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
