# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddVulWhiteListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_type': 'str',
        'vul_ids': 'list[str]',
        'rule_type': 'str',
        'host_ids': 'list[str]',
        'with_ignore': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'vul_type': 'vul_type',
        'vul_ids': 'vul_ids',
        'rule_type': 'rule_type',
        'host_ids': 'host_ids',
        'with_ignore': 'with_ignore',
        'description': 'description'
    }

    def __init__(self, vul_type=None, vul_ids=None, rule_type=None, host_ids=None, with_ignore=None, description=None):
        r"""AddVulWhiteListRequestBody

        The model defined in huaweicloud sdk

        :param vul_type: **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及 
        :type vul_type: str
        :param vul_ids: **参数解释**: 漏洞ID列表 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 
        :type vul_ids: list[str]
        :param rule_type: **参数解释**: 白名单规则类型 **约束限制**: 不涉及 **取值范围**: - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机  **默认取值**: 不涉及 
        :type rule_type: str
        :param host_ids: **参数解释**: 主机ID列表，当rule_type为specific_host时，该字段必填 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值2000 **默认取值**: 不涉及 
        :type host_ids: list[str]
        :param with_ignore: **参数解释**: 是否忽略当前已扫描出的漏洞 **约束限制**: 不涉及 **取值范围**: - true：忽略 - false：不忽略 **默认取值**: true 
        :type with_ignore: bool
        :param description: **参数解释**: 白名单的描述信息 **约束限制**: 不涉及 **取值范围**: 字符长度0-1000 **默认取值**: 不涉及 
        :type description: str
        """
        
        

        self._vul_type = None
        self._vul_ids = None
        self._rule_type = None
        self._host_ids = None
        self._with_ignore = None
        self._description = None
        self.discriminator = None

        self.vul_type = vul_type
        self.vul_ids = vul_ids
        self.rule_type = rule_type
        if host_ids is not None:
            self.host_ids = host_ids
        if with_ignore is not None:
            self.with_ignore = with_ignore
        if description is not None:
            self.description = description

    @property
    def vul_type(self):
        r"""Gets the vul_type of this AddVulWhiteListRequestBody.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及 

        :return: The vul_type of this AddVulWhiteListRequestBody.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this AddVulWhiteListRequestBody.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及 

        :param vul_type: The vul_type of this AddVulWhiteListRequestBody.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def vul_ids(self):
        r"""Gets the vul_ids of this AddVulWhiteListRequestBody.

        **参数解释**: 漏洞ID列表 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 

        :return: The vul_ids of this AddVulWhiteListRequestBody.
        :rtype: list[str]
        """
        return self._vul_ids

    @vul_ids.setter
    def vul_ids(self, vul_ids):
        r"""Sets the vul_ids of this AddVulWhiteListRequestBody.

        **参数解释**: 漏洞ID列表 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值500 **默认取值**: 不涉及 

        :param vul_ids: The vul_ids of this AddVulWhiteListRequestBody.
        :type vul_ids: list[str]
        """
        self._vul_ids = vul_ids

    @property
    def rule_type(self):
        r"""Gets the rule_type of this AddVulWhiteListRequestBody.

        **参数解释**: 白名单规则类型 **约束限制**: 不涉及 **取值范围**: - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机  **默认取值**: 不涉及 

        :return: The rule_type of this AddVulWhiteListRequestBody.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this AddVulWhiteListRequestBody.

        **参数解释**: 白名单规则类型 **约束限制**: 不涉及 **取值范围**: - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机  **默认取值**: 不涉及 

        :param rule_type: The rule_type of this AddVulWhiteListRequestBody.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def host_ids(self):
        r"""Gets the host_ids of this AddVulWhiteListRequestBody.

        **参数解释**: 主机ID列表，当rule_type为specific_host时，该字段必填 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值2000 **默认取值**: 不涉及 

        :return: The host_ids of this AddVulWhiteListRequestBody.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this AddVulWhiteListRequestBody.

        **参数解释**: 主机ID列表，当rule_type为specific_host时，该字段必填 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值2000 **默认取值**: 不涉及 

        :param host_ids: The host_ids of this AddVulWhiteListRequestBody.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def with_ignore(self):
        r"""Gets the with_ignore of this AddVulWhiteListRequestBody.

        **参数解释**: 是否忽略当前已扫描出的漏洞 **约束限制**: 不涉及 **取值范围**: - true：忽略 - false：不忽略 **默认取值**: true 

        :return: The with_ignore of this AddVulWhiteListRequestBody.
        :rtype: bool
        """
        return self._with_ignore

    @with_ignore.setter
    def with_ignore(self, with_ignore):
        r"""Sets the with_ignore of this AddVulWhiteListRequestBody.

        **参数解释**: 是否忽略当前已扫描出的漏洞 **约束限制**: 不涉及 **取值范围**: - true：忽略 - false：不忽略 **默认取值**: true 

        :param with_ignore: The with_ignore of this AddVulWhiteListRequestBody.
        :type with_ignore: bool
        """
        self._with_ignore = with_ignore

    @property
    def description(self):
        r"""Gets the description of this AddVulWhiteListRequestBody.

        **参数解释**: 白名单的描述信息 **约束限制**: 不涉及 **取值范围**: 字符长度0-1000 **默认取值**: 不涉及 

        :return: The description of this AddVulWhiteListRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddVulWhiteListRequestBody.

        **参数解释**: 白名单的描述信息 **约束限制**: 不涉及 **取值范围**: 字符长度0-1000 **默认取值**: 不涉及 

        :param description: The description of this AddVulWhiteListRequestBody.
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
        if not isinstance(other, AddVulWhiteListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
