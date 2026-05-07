# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomRuleConfigDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'hash_type': 'str',
        'auto_block': 'int',
        'is_all_host': 'bool',
        'rule_type': 'str',
        'rule_values': 'list[str]',
        'agent_ids': 'list[str]'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'hash_type': 'hash_type',
        'auto_block': 'auto_block',
        'is_all_host': 'is_all_host',
        'rule_type': 'rule_type',
        'rule_values': 'rule_values',
        'agent_ids': 'agent_ids'
    }

    def __init__(self, rule_id=None, hash_type=None, auto_block=None, is_all_host=None, rule_type=None, rule_values=None, agent_ids=None):
        r"""ListCustomRuleConfigDetailResponse

        The model defined in huaweicloud sdk

        :param rule_id: **参数解释**： 规则ID **取值范围**： 字符长度1-36位 
        :type rule_id: str
        :param hash_type: **参数解释**： hash类型 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum 
        :type hash_type: str
        :param auto_block: **参数解释**： 是否自动阻断告警 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警 
        :type auto_block: int
        :param is_all_host: **参数解释**: 是否选择所有主机 **取值范围**: - true：是 - false：否 
        :type is_all_host: bool
        :param rule_type: **参数解释**： 规则类型 **取值范围**： - black_hash：黑hash 
        :type rule_type: str
        :param rule_values: **参数解释**： 规则集列表 **取值范围**: 1-1000个规则值 
        :type rule_values: list[str]
        :param agent_ids: **参数解释**: agent列表 **取值范围**: 字符长度1-64位 
        :type agent_ids: list[str]
        """
        
        super().__init__()

        self._rule_id = None
        self._hash_type = None
        self._auto_block = None
        self._is_all_host = None
        self._rule_type = None
        self._rule_values = None
        self._agent_ids = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if hash_type is not None:
            self.hash_type = hash_type
        if auto_block is not None:
            self.auto_block = auto_block
        if is_all_host is not None:
            self.is_all_host = is_all_host
        if rule_type is not None:
            self.rule_type = rule_type
        if rule_values is not None:
            self.rule_values = rule_values
        if agent_ids is not None:
            self.agent_ids = agent_ids

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ListCustomRuleConfigDetailResponse.

        **参数解释**： 规则ID **取值范围**： 字符长度1-36位 

        :return: The rule_id of this ListCustomRuleConfigDetailResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ListCustomRuleConfigDetailResponse.

        **参数解释**： 规则ID **取值范围**： 字符长度1-36位 

        :param rule_id: The rule_id of this ListCustomRuleConfigDetailResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def hash_type(self):
        r"""Gets the hash_type of this ListCustomRuleConfigDetailResponse.

        **参数解释**： hash类型 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum 

        :return: The hash_type of this ListCustomRuleConfigDetailResponse.
        :rtype: str
        """
        return self._hash_type

    @hash_type.setter
    def hash_type(self, hash_type):
        r"""Sets the hash_type of this ListCustomRuleConfigDetailResponse.

        **参数解释**： hash类型 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum 

        :param hash_type: The hash_type of this ListCustomRuleConfigDetailResponse.
        :type hash_type: str
        """
        self._hash_type = hash_type

    @property
    def auto_block(self):
        r"""Gets the auto_block of this ListCustomRuleConfigDetailResponse.

        **参数解释**： 是否自动阻断告警 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警 

        :return: The auto_block of this ListCustomRuleConfigDetailResponse.
        :rtype: int
        """
        return self._auto_block

    @auto_block.setter
    def auto_block(self, auto_block):
        r"""Sets the auto_block of this ListCustomRuleConfigDetailResponse.

        **参数解释**： 是否自动阻断告警 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警 

        :param auto_block: The auto_block of this ListCustomRuleConfigDetailResponse.
        :type auto_block: int
        """
        self._auto_block = auto_block

    @property
    def is_all_host(self):
        r"""Gets the is_all_host of this ListCustomRuleConfigDetailResponse.

        **参数解释**: 是否选择所有主机 **取值范围**: - true：是 - false：否 

        :return: The is_all_host of this ListCustomRuleConfigDetailResponse.
        :rtype: bool
        """
        return self._is_all_host

    @is_all_host.setter
    def is_all_host(self, is_all_host):
        r"""Sets the is_all_host of this ListCustomRuleConfigDetailResponse.

        **参数解释**: 是否选择所有主机 **取值范围**: - true：是 - false：否 

        :param is_all_host: The is_all_host of this ListCustomRuleConfigDetailResponse.
        :type is_all_host: bool
        """
        self._is_all_host = is_all_host

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ListCustomRuleConfigDetailResponse.

        **参数解释**： 规则类型 **取值范围**： - black_hash：黑hash 

        :return: The rule_type of this ListCustomRuleConfigDetailResponse.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ListCustomRuleConfigDetailResponse.

        **参数解释**： 规则类型 **取值范围**： - black_hash：黑hash 

        :param rule_type: The rule_type of this ListCustomRuleConfigDetailResponse.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def rule_values(self):
        r"""Gets the rule_values of this ListCustomRuleConfigDetailResponse.

        **参数解释**： 规则集列表 **取值范围**: 1-1000个规则值 

        :return: The rule_values of this ListCustomRuleConfigDetailResponse.
        :rtype: list[str]
        """
        return self._rule_values

    @rule_values.setter
    def rule_values(self, rule_values):
        r"""Sets the rule_values of this ListCustomRuleConfigDetailResponse.

        **参数解释**： 规则集列表 **取值范围**: 1-1000个规则值 

        :param rule_values: The rule_values of this ListCustomRuleConfigDetailResponse.
        :type rule_values: list[str]
        """
        self._rule_values = rule_values

    @property
    def agent_ids(self):
        r"""Gets the agent_ids of this ListCustomRuleConfigDetailResponse.

        **参数解释**: agent列表 **取值范围**: 字符长度1-64位 

        :return: The agent_ids of this ListCustomRuleConfigDetailResponse.
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        r"""Sets the agent_ids of this ListCustomRuleConfigDetailResponse.

        **参数解释**: agent列表 **取值范围**: 字符长度1-64位 

        :param agent_ids: The agent_ids of this ListCustomRuleConfigDetailResponse.
        :type agent_ids: list[str]
        """
        self._agent_ids = agent_ids

    def to_dict(self):
        import warnings
        warnings.warn("ListCustomRuleConfigDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCustomRuleConfigDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
