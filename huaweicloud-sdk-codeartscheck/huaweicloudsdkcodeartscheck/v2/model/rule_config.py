# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'rule_id': 'str',
        'default_value': 'str',
        'option_value': 'str',
        'option_key': 'str',
        'option_name': 'str',
        'template_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'rule_id': 'rule_id',
        'default_value': 'default_value',
        'option_value': 'option_value',
        'option_key': 'option_key',
        'option_name': 'option_name',
        'template_id': 'template_id',
        'description': 'description'
    }

    def __init__(self, id=None, rule_id=None, default_value=None, option_value=None, option_key=None, option_name=None, template_id=None, description=None):
        r"""RuleConfig

        The model defined in huaweicloud sdk

        :param id: **参数解释:** 规则配置ID。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。
        :type id: int
        :param rule_id: **参数解释:** 工具规则ID，即可配置阈值规则的各种阈值对应的ID，当前无便利手段获取，请联系客服咨询。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。
        :type rule_id: str
        :param default_value: **参数解释:** 配置参数默认阈值。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。
        :type default_value: str
        :param option_value: **参数解释:** 配置参数新阈值。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。
        :type option_value: str
        :param option_key: **参数解释:** 当前规则配置项key。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 需要和规则ID相匹配。 **取值范围:** 不涉及。 **默认取值:** 不涉及。
        :type option_key: str
        :param option_name: **参数解释:** 当前规则配置项key。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 需要和规则ID相匹配。 **取值范围:** 不涉及。 **默认取值:** 不涉及。
        :type option_name: str
        :param template_id: **参数解释:** 规则集ID。可调用[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则集ID。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。
        :type template_id: str
        :param description: **参数解释:** 配置参数的描述。可不填。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。
        :type description: str
        """
        
        

        self._id = None
        self._rule_id = None
        self._default_value = None
        self._option_value = None
        self._option_key = None
        self._option_name = None
        self._template_id = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if rule_id is not None:
            self.rule_id = rule_id
        if default_value is not None:
            self.default_value = default_value
        if option_value is not None:
            self.option_value = option_value
        if option_key is not None:
            self.option_key = option_key
        if option_name is not None:
            self.option_name = option_name
        if template_id is not None:
            self.template_id = template_id
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this RuleConfig.

        **参数解释:** 规则配置ID。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。

        :return: The id of this RuleConfig.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RuleConfig.

        **参数解释:** 规则配置ID。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。

        :param id: The id of this RuleConfig.
        :type id: int
        """
        self._id = id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleConfig.

        **参数解释:** 工具规则ID，即可配置阈值规则的各种阈值对应的ID，当前无便利手段获取，请联系客服咨询。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。

        :return: The rule_id of this RuleConfig.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleConfig.

        **参数解释:** 工具规则ID，即可配置阈值规则的各种阈值对应的ID，当前无便利手段获取，请联系客服咨询。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。

        :param rule_id: The rule_id of this RuleConfig.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def default_value(self):
        r"""Gets the default_value of this RuleConfig.

        **参数解释:** 配置参数默认阈值。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :return: The default_value of this RuleConfig.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this RuleConfig.

        **参数解释:** 配置参数默认阈值。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :param default_value: The default_value of this RuleConfig.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def option_value(self):
        r"""Gets the option_value of this RuleConfig.

        **参数解释:** 配置参数新阈值。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :return: The option_value of this RuleConfig.
        :rtype: str
        """
        return self._option_value

    @option_value.setter
    def option_value(self, option_value):
        r"""Sets the option_value of this RuleConfig.

        **参数解释:** 配置参数新阈值。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :param option_value: The option_value of this RuleConfig.
        :type option_value: str
        """
        self._option_value = option_value

    @property
    def option_key(self):
        r"""Gets the option_key of this RuleConfig.

        **参数解释:** 当前规则配置项key。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 需要和规则ID相匹配。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :return: The option_key of this RuleConfig.
        :rtype: str
        """
        return self._option_key

    @option_key.setter
    def option_key(self, option_key):
        r"""Sets the option_key of this RuleConfig.

        **参数解释:** 当前规则配置项key。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 需要和规则ID相匹配。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :param option_key: The option_key of this RuleConfig.
        :type option_key: str
        """
        self._option_key = option_key

    @property
    def option_name(self):
        r"""Gets the option_name of this RuleConfig.

        **参数解释:** 当前规则配置项key。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 需要和规则ID相匹配。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :return: The option_name of this RuleConfig.
        :rtype: str
        """
        return self._option_name

    @option_name.setter
    def option_name(self, option_name):
        r"""Sets the option_name of this RuleConfig.

        **参数解释:** 当前规则配置项key。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则配置ID。 **约束限制:** 需要和规则ID相匹配。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :param option_name: The option_name of this RuleConfig.
        :type option_name: str
        """
        self._option_name = option_name

    @property
    def template_id(self):
        r"""Gets the template_id of this RuleConfig.

        **参数解释:** 规则集ID。可调用[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则集ID。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。

        :return: The template_id of this RuleConfig.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this RuleConfig.

        **参数解释:** 规则集ID。可调用[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则集ID。 **约束限制:** 不涉及。 **取值范围:** 32位UUID。 **默认取值:** 不涉及。

        :param template_id: The template_id of this RuleConfig.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def description(self):
        r"""Gets the description of this RuleConfig.

        **参数解释:** 配置参数的描述。可不填。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :return: The description of this RuleConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RuleConfig.

        **参数解释:** 配置参数的描述。可不填。 **约束限制:** 不涉及。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :param description: The description of this RuleConfig.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RuleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
