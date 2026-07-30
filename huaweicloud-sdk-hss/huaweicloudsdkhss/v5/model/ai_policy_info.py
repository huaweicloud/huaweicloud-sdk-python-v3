# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiPolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'enabled': 'bool',
        'policy_group_id': 'str',
        'content': 'str',
        'description': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'enabled': 'enabled',
        'policy_group_id': 'policy_group_id',
        'content': 'content',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, policy_id=None, policy_name=None, enabled=None, policy_group_id=None, content=None, description=None, create_time=None, update_time=None):
        r"""AiPolicyInfo

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释**: 策略ID **取值范围**: 字符长度1-20位 
        :type policy_id: str
        :param policy_name: **参数解释**: 策略名称 **取值范围**： - 0: 意图行为一致性检测 - 1: 命令执行控制 - 2: 文件访问控制 - 3: 敏感信息检测 - 4: 角色限定 
        :type policy_name: str
        :param enabled: **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 
        :type enabled: bool
        :param policy_group_id: **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 
        :type policy_group_id: str
        :param content: **参数解释**: 策略详情 **取值范围**: 字符长度0-65535位 
        :type content: str
        :param description: **参数解释**: 策略描述 **取值范围**: 字符长度1-256位 
        :type description: str
        :param create_time: **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type create_time: int
        :param update_time: **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type update_time: int
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._enabled = None
        self._policy_group_id = None
        self._content = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if enabled is not None:
            self.enabled = enabled
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if content is not None:
            self.content = content
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AiPolicyInfo.

        **参数解释**: 策略ID **取值范围**: 字符长度1-20位 

        :return: The policy_id of this AiPolicyInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AiPolicyInfo.

        **参数解释**: 策略ID **取值范围**: 字符长度1-20位 

        :param policy_id: The policy_id of this AiPolicyInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AiPolicyInfo.

        **参数解释**: 策略名称 **取值范围**： - 0: 意图行为一致性检测 - 1: 命令执行控制 - 2: 文件访问控制 - 3: 敏感信息检测 - 4: 角色限定 

        :return: The policy_name of this AiPolicyInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AiPolicyInfo.

        **参数解释**: 策略名称 **取值范围**： - 0: 意图行为一致性检测 - 1: 命令执行控制 - 2: 文件访问控制 - 3: 敏感信息检测 - 4: 角色限定 

        :param policy_name: The policy_name of this AiPolicyInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def enabled(self):
        r"""Gets the enabled of this AiPolicyInfo.

        **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 

        :return: The enabled of this AiPolicyInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this AiPolicyInfo.

        **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 

        :param enabled: The enabled of this AiPolicyInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this AiPolicyInfo.

        **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 

        :return: The policy_group_id of this AiPolicyInfo.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this AiPolicyInfo.

        **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 

        :param policy_group_id: The policy_group_id of this AiPolicyInfo.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def content(self):
        r"""Gets the content of this AiPolicyInfo.

        **参数解释**: 策略详情 **取值范围**: 字符长度0-65535位 

        :return: The content of this AiPolicyInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this AiPolicyInfo.

        **参数解释**: 策略详情 **取值范围**: 字符长度0-65535位 

        :param content: The content of this AiPolicyInfo.
        :type content: str
        """
        self._content = content

    @property
    def description(self):
        r"""Gets the description of this AiPolicyInfo.

        **参数解释**: 策略描述 **取值范围**: 字符长度1-256位 

        :return: The description of this AiPolicyInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AiPolicyInfo.

        **参数解释**: 策略描述 **取值范围**: 字符长度1-256位 

        :param description: The description of this AiPolicyInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this AiPolicyInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The create_time of this AiPolicyInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AiPolicyInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this AiPolicyInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AiPolicyInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The update_time of this AiPolicyInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AiPolicyInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param update_time: The update_time of this AiPolicyInfo.
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
        if not isinstance(other, AiPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
