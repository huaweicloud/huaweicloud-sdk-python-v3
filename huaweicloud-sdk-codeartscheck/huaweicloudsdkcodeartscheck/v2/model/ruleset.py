# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Ruleset:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'template_name': 'str',
        'language': 'str',
        'is_default': 'str',
        'rule_ids': 'str',
        'uncheck_ids': 'str',
        'template_id': 'str',
        'custom_attributes': 'list[CustomAttributes]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'template_name': 'template_name',
        'language': 'language',
        'is_default': 'is_default',
        'rule_ids': 'rule_ids',
        'uncheck_ids': 'uncheck_ids',
        'template_id': 'template_id',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, project_id=None, template_name=None, language=None, is_default=None, rule_ids=None, uncheck_ids=None, template_id=None, custom_attributes=None):
        r"""Ruleset

        The model defined in huaweicloud sdk

        :param project_id: **参数解释:** 项目的32位UUID，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束限制:** 不涉及。 **取值范围:** 长度为[1~32]个字符。 **默认取值:** 不涉及。
        :type project_id: str
        :param template_name: **参数解释:** 新规则集名称。 **约束限制:** 不能含有任意中英文，数字，点，连字符-及下划线_以外的特殊字符。 **取值范围:** 任意中英文，数字，点，连字符-及下划线_。长度为[1~128]个字符。 **默认取值:** 不涉及。
        :type template_name: str
        :param language: **参数解释:** 规则集语言。 **约束限制:** 只能选择当前系统上支持的语言。 **取值范围:** 只能传一种语言。当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES **默认取值:** 不涉及。
        :type language: str
        :param is_default: **参数解释:** 是否基于已存在的规则集创建新规则集。 **约束限制:** 只能填0或1。 **取值范围:** - 0：新建空白规则集。 - 1：基于已存在的规则集创建新规则集。 **默认取值:** 不涉及。
        :type is_default: str
        :param rule_ids: **参数解释:** 新启用规则ID集合，启用多条规则时，id用英文逗号相连。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则ID。 **约束限制:** 规则ID为32位UUID，多个ID之间用英文逗号分隔。例如：\&quot;00034fc32ee045388365d42ca4e07fe1,002c2eda6d6c11edab16fa163e0fa374\&quot;。 **取值范围:** 长度为[1~4000]个字符。 **默认取值:** 不涉及。
        :type rule_ids: str
        :param uncheck_ids: **参数解释:** 新关闭规则ID集合，多个ID用英文逗号相连。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则ID。 **约束限制:** 规则ID为32位UUID，多个ID之间用英文逗号分隔。例如：\&quot;00034fc32ee045388365d42ca4e07fe1,002c2eda6d6c11edab16fa163e0fa374\&quot;。 **取值范围:** 长度为[1~4000]个字符。 **默认取值:** 不涉及。
        :type uncheck_ids: str
        :param template_id: **参数解释:** 规则集ID。当is_default参数为1时，该参数需要传参。可调用[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取已存在的规则集ID。 **约束限制:** 32位UUID。例如：\&quot;da303d80d2594faca60dbcc2e29c18aa\&quot;。 **取值范围:** 不涉及。 **默认取值:** 不涉及。
        :type template_id: str
        :param custom_attributes: 自定义规则参数项，支持修改规则阈值。
        :type custom_attributes: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomAttributes`]
        """
        
        

        self._project_id = None
        self._template_name = None
        self._language = None
        self._is_default = None
        self._rule_ids = None
        self._uncheck_ids = None
        self._template_id = None
        self._custom_attributes = None
        self.discriminator = None

        self.project_id = project_id
        self.template_name = template_name
        self.language = language
        self.is_default = is_default
        if rule_ids is not None:
            self.rule_ids = rule_ids
        if uncheck_ids is not None:
            self.uncheck_ids = uncheck_ids
        if template_id is not None:
            self.template_id = template_id
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes

    @property
    def project_id(self):
        r"""Gets the project_id of this Ruleset.

        **参数解释:** 项目的32位UUID，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束限制:** 不涉及。 **取值范围:** 长度为[1~32]个字符。 **默认取值:** 不涉及。

        :return: The project_id of this Ruleset.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Ruleset.

        **参数解释:** 项目的32位UUID，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束限制:** 不涉及。 **取值范围:** 长度为[1~32]个字符。 **默认取值:** 不涉及。

        :param project_id: The project_id of this Ruleset.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def template_name(self):
        r"""Gets the template_name of this Ruleset.

        **参数解释:** 新规则集名称。 **约束限制:** 不能含有任意中英文，数字，点，连字符-及下划线_以外的特殊字符。 **取值范围:** 任意中英文，数字，点，连字符-及下划线_。长度为[1~128]个字符。 **默认取值:** 不涉及。

        :return: The template_name of this Ruleset.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this Ruleset.

        **参数解释:** 新规则集名称。 **约束限制:** 不能含有任意中英文，数字，点，连字符-及下划线_以外的特殊字符。 **取值范围:** 任意中英文，数字，点，连字符-及下划线_。长度为[1~128]个字符。 **默认取值:** 不涉及。

        :param template_name: The template_name of this Ruleset.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def language(self):
        r"""Gets the language of this Ruleset.

        **参数解释:** 规则集语言。 **约束限制:** 只能选择当前系统上支持的语言。 **取值范围:** 只能传一种语言。当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES **默认取值:** 不涉及。

        :return: The language of this Ruleset.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this Ruleset.

        **参数解释:** 规则集语言。 **约束限制:** 只能选择当前系统上支持的语言。 **取值范围:** 只能传一种语言。当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES **默认取值:** 不涉及。

        :param language: The language of this Ruleset.
        :type language: str
        """
        self._language = language

    @property
    def is_default(self):
        r"""Gets the is_default of this Ruleset.

        **参数解释:** 是否基于已存在的规则集创建新规则集。 **约束限制:** 只能填0或1。 **取值范围:** - 0：新建空白规则集。 - 1：基于已存在的规则集创建新规则集。 **默认取值:** 不涉及。

        :return: The is_default of this Ruleset.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this Ruleset.

        **参数解释:** 是否基于已存在的规则集创建新规则集。 **约束限制:** 只能填0或1。 **取值范围:** - 0：新建空白规则集。 - 1：基于已存在的规则集创建新规则集。 **默认取值:** 不涉及。

        :param is_default: The is_default of this Ruleset.
        :type is_default: str
        """
        self._is_default = is_default

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this Ruleset.

        **参数解释:** 新启用规则ID集合，启用多条规则时，id用英文逗号相连。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则ID。 **约束限制:** 规则ID为32位UUID，多个ID之间用英文逗号分隔。例如：\"00034fc32ee045388365d42ca4e07fe1,002c2eda6d6c11edab16fa163e0fa374\"。 **取值范围:** 长度为[1~4000]个字符。 **默认取值:** 不涉及。

        :return: The rule_ids of this Ruleset.
        :rtype: str
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this Ruleset.

        **参数解释:** 新启用规则ID集合，启用多条规则时，id用英文逗号相连。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则ID。 **约束限制:** 规则ID为32位UUID，多个ID之间用英文逗号分隔。例如：\"00034fc32ee045388365d42ca4e07fe1,002c2eda6d6c11edab16fa163e0fa374\"。 **取值范围:** 长度为[1~4000]个字符。 **默认取值:** 不涉及。

        :param rule_ids: The rule_ids of this Ruleset.
        :type rule_ids: str
        """
        self._rule_ids = rule_ids

    @property
    def uncheck_ids(self):
        r"""Gets the uncheck_ids of this Ruleset.

        **参数解释:** 新关闭规则ID集合，多个ID用英文逗号相连。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则ID。 **约束限制:** 规则ID为32位UUID，多个ID之间用英文逗号分隔。例如：\"00034fc32ee045388365d42ca4e07fe1,002c2eda6d6c11edab16fa163e0fa374\"。 **取值范围:** 长度为[1~4000]个字符。 **默认取值:** 不涉及。

        :return: The uncheck_ids of this Ruleset.
        :rtype: str
        """
        return self._uncheck_ids

    @uncheck_ids.setter
    def uncheck_ids(self, uncheck_ids):
        r"""Sets the uncheck_ids of this Ruleset.

        **参数解释:** 新关闭规则ID集合，多个ID用英文逗号相连。可调用[[获取规则列表接口](https://support.huaweicloud.com/api-codecheck/ListRules.html)](tag:hws)[[获取规则列表接口](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRules.html)](tag:hws_hk)[获取规则列表接口](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取规则ID。 **约束限制:** 规则ID为32位UUID，多个ID之间用英文逗号分隔。例如：\"00034fc32ee045388365d42ca4e07fe1,002c2eda6d6c11edab16fa163e0fa374\"。 **取值范围:** 长度为[1~4000]个字符。 **默认取值:** 不涉及。

        :param uncheck_ids: The uncheck_ids of this Ruleset.
        :type uncheck_ids: str
        """
        self._uncheck_ids = uncheck_ids

    @property
    def template_id(self):
        r"""Gets the template_id of this Ruleset.

        **参数解释:** 规则集ID。当is_default参数为1时，该参数需要传参。可调用[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取已存在的规则集ID。 **约束限制:** 32位UUID。例如：\"da303d80d2594faca60dbcc2e29c18aa\"。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :return: The template_id of this Ruleset.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this Ruleset.

        **参数解释:** 规则集ID。当is_default参数为1时，该参数需要传参。可调用[[查询规则集列表](https://support.huaweicloud.com/api-codecheck/ListRulesets.html)](tag:hws)[[查询规则集列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ListRulesets.html)](tag:hws_hk)[查询规则集列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)获取已存在的规则集ID。 **约束限制:** 32位UUID。例如：\"da303d80d2594faca60dbcc2e29c18aa\"。 **取值范围:** 不涉及。 **默认取值:** 不涉及。

        :param template_id: The template_id of this Ruleset.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def custom_attributes(self):
        r"""Gets the custom_attributes of this Ruleset.

        自定义规则参数项，支持修改规则阈值。

        :return: The custom_attributes of this Ruleset.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomAttributes`]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        r"""Sets the custom_attributes of this Ruleset.

        自定义规则参数项，支持修改规则阈值。

        :param custom_attributes: The custom_attributes of this Ruleset.
        :type custom_attributes: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomAttributes`]
        """
        self._custom_attributes = custom_attributes

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
        if not isinstance(other, Ruleset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
