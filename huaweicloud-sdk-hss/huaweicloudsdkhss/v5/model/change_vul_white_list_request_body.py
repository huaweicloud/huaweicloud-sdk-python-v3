# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeVulWhiteListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_type': 'str',
        'host_ids': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'host_ids': 'host_ids',
        'description': 'description'
    }

    def __init__(self, rule_type=None, host_ids=None, description=None):
        r"""ChangeVulWhiteListRequestBody

        The model defined in huaweicloud sdk

        :param rule_type: **参数解释**： 白名单规则类型 **约束限制**： 不涉及 **取值范围**： - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机  **默认取值**： 不涉及 
        :type rule_type: str
        :param host_ids: **参数解释**： 白名单应用的主机ID列表，rule_type为specific_host时必填 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type host_ids: list[str]
        :param description: **参数解释**： 白名单的描述信息 **约束限制**： 不涉及 **取值范围**： 字符长度0-1024 **默认取值**： 不涉及 
        :type description: str
        """
        
        

        self._rule_type = None
        self._host_ids = None
        self._description = None
        self.discriminator = None

        self.rule_type = rule_type
        if host_ids is not None:
            self.host_ids = host_ids
        if description is not None:
            self.description = description

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ChangeVulWhiteListRequestBody.

        **参数解释**： 白名单规则类型 **约束限制**： 不涉及 **取值范围**： - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机  **默认取值**： 不涉及 

        :return: The rule_type of this ChangeVulWhiteListRequestBody.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ChangeVulWhiteListRequestBody.

        **参数解释**： 白名单规则类型 **约束限制**： 不涉及 **取值范围**： - all_host：白名单应用于全部主机 - specific_host：白名单应用于指定主机  **默认取值**： 不涉及 

        :param rule_type: The rule_type of this ChangeVulWhiteListRequestBody.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def host_ids(self):
        r"""Gets the host_ids of this ChangeVulWhiteListRequestBody.

        **参数解释**： 白名单应用的主机ID列表，rule_type为specific_host时必填 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The host_ids of this ChangeVulWhiteListRequestBody.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this ChangeVulWhiteListRequestBody.

        **参数解释**： 白名单应用的主机ID列表，rule_type为specific_host时必填 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param host_ids: The host_ids of this ChangeVulWhiteListRequestBody.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def description(self):
        r"""Gets the description of this ChangeVulWhiteListRequestBody.

        **参数解释**： 白名单的描述信息 **约束限制**： 不涉及 **取值范围**： 字符长度0-1024 **默认取值**： 不涉及 

        :return: The description of this ChangeVulWhiteListRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ChangeVulWhiteListRequestBody.

        **参数解释**： 白名单的描述信息 **约束限制**： 不涉及 **取值范围**： 字符长度0-1024 **默认取值**： 不涉及 

        :param description: The description of this ChangeVulWhiteListRequestBody.
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
        if not isinstance(other, ChangeVulWhiteListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
