# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCheckRuleFixFailDetailRequest:

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
        'host_id': 'str',
        'check_name': 'str',
        'check_rule_id': 'str',
        'standard': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'check_name': 'check_name',
        'check_rule_id': 'check_rule_id',
        'standard': 'standard'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, check_name=None, check_rule_id=None, standard=None):
        r"""ShowCheckRuleFixFailDetailRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param host_id: **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param check_name: **参数解释** : \&quot;配置检查（基线）的名称，例如SSH、CentOS 7、Windows\&quot;。 **约束限制** : 不涉及 **取值范围** : 字符长度1-256位 **默认取值** : 不涉及 
        :type check_name: str
        :param check_rule_id: **参数解释**:  检查项ID，值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules **约束限制**: 不涉及 **取值范围**: 字符长度0-255位 **默认取值**: 不涉及
        :type check_rule_id: str
        :param standard: **参数解释**: 标准类型。 **约束限制**: 不涉及 **取值范围**: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准  **默认取值**: 不涉及 
        :type standard: str
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._check_name = None
        self._check_rule_id = None
        self._standard = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_id is not None:
            self.host_id = host_id
        if check_name is not None:
            self.check_name = check_name
        self.check_rule_id = check_rule_id
        if standard is not None:
            self.standard = standard

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowCheckRuleFixFailDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowCheckRuleFixFailDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowCheckRuleFixFailDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowCheckRuleFixFailDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ShowCheckRuleFixFailDetailRequest.

        **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ShowCheckRuleFixFailDetailRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ShowCheckRuleFixFailDetailRequest.

        **参数解释**: 服务器的唯一标识ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ShowCheckRuleFixFailDetailRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def check_name(self):
        r"""Gets the check_name of this ShowCheckRuleFixFailDetailRequest.

        **参数解释** : \"配置检查（基线）的名称，例如SSH、CentOS 7、Windows\"。 **约束限制** : 不涉及 **取值范围** : 字符长度1-256位 **默认取值** : 不涉及 

        :return: The check_name of this ShowCheckRuleFixFailDetailRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ShowCheckRuleFixFailDetailRequest.

        **参数解释** : \"配置检查（基线）的名称，例如SSH、CentOS 7、Windows\"。 **约束限制** : 不涉及 **取值范围** : 字符长度1-256位 **默认取值** : 不涉及 

        :param check_name: The check_name of this ShowCheckRuleFixFailDetailRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this ShowCheckRuleFixFailDetailRequest.

        **参数解释**:  检查项ID，值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules **约束限制**: 不涉及 **取值范围**: 字符长度0-255位 **默认取值**: 不涉及

        :return: The check_rule_id of this ShowCheckRuleFixFailDetailRequest.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this ShowCheckRuleFixFailDetailRequest.

        **参数解释**:  检查项ID，值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules **约束限制**: 不涉及 **取值范围**: 字符长度0-255位 **默认取值**: 不涉及

        :param check_rule_id: The check_rule_id of this ShowCheckRuleFixFailDetailRequest.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def standard(self):
        r"""Gets the standard of this ShowCheckRuleFixFailDetailRequest.

        **参数解释**: 标准类型。 **约束限制**: 不涉及 **取值范围**: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准  **默认取值**: 不涉及 

        :return: The standard of this ShowCheckRuleFixFailDetailRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ShowCheckRuleFixFailDetailRequest.

        **参数解释**: 标准类型。 **约束限制**: 不涉及 **取值范围**: - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard : 通用安全标准  **默认取值**: 不涉及 

        :param standard: The standard of this ShowCheckRuleFixFailDetailRequest.
        :type standard: str
        """
        self._standard = standard

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
        if not isinstance(other, ShowCheckRuleFixFailDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
