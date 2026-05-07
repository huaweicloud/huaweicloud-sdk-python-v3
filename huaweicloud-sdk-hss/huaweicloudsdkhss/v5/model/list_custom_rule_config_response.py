# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomRuleConfigResponse:

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
        'host_num': 'int',
        'rule_name': 'str',
        'rule_status': 'int',
        'rule_type': 'str',
        'auto_block': 'int',
        'hash_type': 'str',
        'is_all_host': 'bool',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'host_num': 'host_num',
        'rule_name': 'rule_name',
        'rule_status': 'rule_status',
        'rule_type': 'rule_type',
        'auto_block': 'auto_block',
        'hash_type': 'hash_type',
        'is_all_host': 'is_all_host',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, rule_id=None, host_num=None, rule_name=None, rule_status=None, rule_type=None, auto_block=None, hash_type=None, is_all_host=None, create_time=None, update_time=None):
        r"""ListCustomRuleConfigResponse

        The model defined in huaweicloud sdk

        :param rule_id: **参数解释**： 规则ID **取值范围**： 字符长度1-36位 
        :type rule_id: str
        :param host_num: **参数解释**: 防护主机数量。 **取值范围**: 最小值1，最大值2000000 
        :type host_num: int
        :param rule_name: **参数解释**： 规则名称 **取值范围**： 字符长度1-64位 
        :type rule_name: str
        :param rule_status: **参数解释**： 规则状态 **取值范围**: - 0：停用 - 1：启用 
        :type rule_status: int
        :param rule_type: **参数解释**： 规则类型 **取值范围**： - black_hash：黑hash 
        :type rule_type: str
        :param auto_block: **参数解释**： 是否自动阻断告警 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警 
        :type auto_block: int
        :param hash_type: **参数解释**： hash类型 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum 
        :type hash_type: str
        :param is_all_host: **参数解释**: 是否选择所有主机 **取值范围**: - true：是 - false：否 
        :type is_all_host: bool
        :param create_time: **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type create_time: int
        :param update_time: **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type update_time: int
        """
        
        

        self._rule_id = None
        self._host_num = None
        self._rule_name = None
        self._rule_status = None
        self._rule_type = None
        self._auto_block = None
        self._hash_type = None
        self._is_all_host = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if host_num is not None:
            self.host_num = host_num
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_status is not None:
            self.rule_status = rule_status
        if rule_type is not None:
            self.rule_type = rule_type
        if auto_block is not None:
            self.auto_block = auto_block
        if hash_type is not None:
            self.hash_type = hash_type
        if is_all_host is not None:
            self.is_all_host = is_all_host
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ListCustomRuleConfigResponse.

        **参数解释**： 规则ID **取值范围**： 字符长度1-36位 

        :return: The rule_id of this ListCustomRuleConfigResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ListCustomRuleConfigResponse.

        **参数解释**： 规则ID **取值范围**： 字符长度1-36位 

        :param rule_id: The rule_id of this ListCustomRuleConfigResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def host_num(self):
        r"""Gets the host_num of this ListCustomRuleConfigResponse.

        **参数解释**: 防护主机数量。 **取值范围**: 最小值1，最大值2000000 

        :return: The host_num of this ListCustomRuleConfigResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ListCustomRuleConfigResponse.

        **参数解释**: 防护主机数量。 **取值范围**: 最小值1，最大值2000000 

        :param host_num: The host_num of this ListCustomRuleConfigResponse.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ListCustomRuleConfigResponse.

        **参数解释**： 规则名称 **取值范围**： 字符长度1-64位 

        :return: The rule_name of this ListCustomRuleConfigResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ListCustomRuleConfigResponse.

        **参数解释**： 规则名称 **取值范围**： 字符长度1-64位 

        :param rule_name: The rule_name of this ListCustomRuleConfigResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_status(self):
        r"""Gets the rule_status of this ListCustomRuleConfigResponse.

        **参数解释**： 规则状态 **取值范围**: - 0：停用 - 1：启用 

        :return: The rule_status of this ListCustomRuleConfigResponse.
        :rtype: int
        """
        return self._rule_status

    @rule_status.setter
    def rule_status(self, rule_status):
        r"""Sets the rule_status of this ListCustomRuleConfigResponse.

        **参数解释**： 规则状态 **取值范围**: - 0：停用 - 1：启用 

        :param rule_status: The rule_status of this ListCustomRuleConfigResponse.
        :type rule_status: int
        """
        self._rule_status = rule_status

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ListCustomRuleConfigResponse.

        **参数解释**： 规则类型 **取值范围**： - black_hash：黑hash 

        :return: The rule_type of this ListCustomRuleConfigResponse.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ListCustomRuleConfigResponse.

        **参数解释**： 规则类型 **取值范围**： - black_hash：黑hash 

        :param rule_type: The rule_type of this ListCustomRuleConfigResponse.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def auto_block(self):
        r"""Gets the auto_block of this ListCustomRuleConfigResponse.

        **参数解释**： 是否自动阻断告警 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警 

        :return: The auto_block of this ListCustomRuleConfigResponse.
        :rtype: int
        """
        return self._auto_block

    @auto_block.setter
    def auto_block(self, auto_block):
        r"""Sets the auto_block of this ListCustomRuleConfigResponse.

        **参数解释**： 是否自动阻断告警 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警 

        :param auto_block: The auto_block of this ListCustomRuleConfigResponse.
        :type auto_block: int
        """
        self._auto_block = auto_block

    @property
    def hash_type(self):
        r"""Gets the hash_type of this ListCustomRuleConfigResponse.

        **参数解释**： hash类型 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum 

        :return: The hash_type of this ListCustomRuleConfigResponse.
        :rtype: str
        """
        return self._hash_type

    @hash_type.setter
    def hash_type(self, hash_type):
        r"""Sets the hash_type of this ListCustomRuleConfigResponse.

        **参数解释**： hash类型 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum 

        :param hash_type: The hash_type of this ListCustomRuleConfigResponse.
        :type hash_type: str
        """
        self._hash_type = hash_type

    @property
    def is_all_host(self):
        r"""Gets the is_all_host of this ListCustomRuleConfigResponse.

        **参数解释**: 是否选择所有主机 **取值范围**: - true：是 - false：否 

        :return: The is_all_host of this ListCustomRuleConfigResponse.
        :rtype: bool
        """
        return self._is_all_host

    @is_all_host.setter
    def is_all_host(self, is_all_host):
        r"""Sets the is_all_host of this ListCustomRuleConfigResponse.

        **参数解释**: 是否选择所有主机 **取值范围**: - true：是 - false：否 

        :param is_all_host: The is_all_host of this ListCustomRuleConfigResponse.
        :type is_all_host: bool
        """
        self._is_all_host = is_all_host

    @property
    def create_time(self):
        r"""Gets the create_time of this ListCustomRuleConfigResponse.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The create_time of this ListCustomRuleConfigResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListCustomRuleConfigResponse.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this ListCustomRuleConfigResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListCustomRuleConfigResponse.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The update_time of this ListCustomRuleConfigResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListCustomRuleConfigResponse.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param update_time: The update_time of this ListCustomRuleConfigResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ListCustomRuleConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
