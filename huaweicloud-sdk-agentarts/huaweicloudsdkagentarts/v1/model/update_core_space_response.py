# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreSpaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'message_ttl_hours': 'int',
        'memory_extract_enabled': 'bool',
        'memory_extract_idle_seconds': 'int',
        'memory_extract_max_tokens': 'int',
        'memory_extract_max_messages': 'int',
        'memory_strategies_builtin': 'list[CoreSpaceBuiltinMemoryStrategy]',
        'memory_strategies_customized': 'list[CoreSpaceMemoryStrategy]',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'private_access': 'CoreSpaceNetwork',
        'public_access': 'CoreSpaceNetwork',
        'api_key': 'ShowCoreSpaceApiKeyResponseBody',
        'encryption_config': 'EncryptionConfig',
        'tags': 'list[CoreSpaceTag]',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'message_ttl_hours': 'message_ttl_hours',
        'memory_extract_enabled': 'memory_extract_enabled',
        'memory_extract_idle_seconds': 'memory_extract_idle_seconds',
        'memory_extract_max_tokens': 'memory_extract_max_tokens',
        'memory_extract_max_messages': 'memory_extract_max_messages',
        'memory_strategies_builtin': 'memory_strategies_builtin',
        'memory_strategies_customized': 'memory_strategies_customized',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'private_access': 'private_access',
        'public_access': 'public_access',
        'api_key': 'api_key',
        'encryption_config': 'encryption_config',
        'tags': 'tags',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, message_ttl_hours=None, memory_extract_enabled=None, memory_extract_idle_seconds=None, memory_extract_max_tokens=None, memory_extract_max_messages=None, memory_strategies_builtin=None, memory_strategies_customized=None, vpc_id=None, subnet_id=None, private_access=None, public_access=None, api_key=None, encryption_config=None, tags=None, status=None, created_at=None, updated_at=None):
        r"""UpdateCoreSpaceResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 记忆库 ID，唯一标识一个记忆库，可通过\&quot;创建Space\&quot;接口获取。 **取值范围：** 不涉及。 
        :type id: str
        :param name: **参数解释：** 记忆库名称。 **取值范围：** 不涉及。 
        :type name: str
        :param description: **参数解释：** 记忆库描述。 **取值范围：** 不涉及。 
        :type description: str
        :param message_ttl_hours: **参数解释：** 短期记忆过期时间（小时）。 **取值范围：** 不涉及。 
        :type message_ttl_hours: int
        :param memory_extract_enabled: **参数解释：** 是否开启长期记忆抽取。 **取值范围：** - true: 已开启 - false: 未开启 
        :type memory_extract_enabled: bool
        :param memory_extract_idle_seconds: **参数解释：** 长期记忆抽取空闲时间（秒）。 **取值范围：** 不涉及。 
        :type memory_extract_idle_seconds: int
        :param memory_extract_max_tokens: **参数解释：** 长期记忆抽取最大累计 token 数。 **取值范围：** 不涉及。 
        :type memory_extract_max_tokens: int
        :param memory_extract_max_messages: **参数解释：** 长期记忆抽取最大累计 message 数。 **取值范围：** 不涉及。 
        :type memory_extract_max_messages: int
        :param memory_strategies_builtin: **参数解释：** 内置策略列表。 **取值范围：** 不涉及。 
        :type memory_strategies_builtin: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceBuiltinMemoryStrategy`]
        :param memory_strategies_customized: **参数解释：** 该记忆库关联的用户自定义记忆策略列表（完整数据）。 **取值范围：** 不涉及。 
        :type memory_strategies_customized: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategy`]
        :param vpc_id: **参数解释：** 租户 VPC ID，获取方式：[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)。 **取值范围：** 不涉及。 
        :type vpc_id: str
        :param subnet_id: **参数解释：** 租户子网 ID，获取方式：[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 **取值范围：** 不涉及。 
        :type subnet_id: str
        :param private_access: 
        :type private_access: :class:`huaweicloudsdkagentarts.v1.CoreSpaceNetwork`
        :param public_access: 
        :type public_access: :class:`huaweicloudsdkagentarts.v1.CoreSpaceNetwork`
        :param api_key: 
        :type api_key: :class:`huaweicloudsdkagentarts.v1.ShowCoreSpaceApiKeyResponseBody`
        :param encryption_config: 
        :type encryption_config: :class:`huaweicloudsdkagentarts.v1.EncryptionConfig`
        :param tags: **参数解释：** 库标签列表。 **取值范围：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        :param status: **参数解释：** Space 状态。 **取值范围：** - creating: 创建中 - running: 运行中 - deleted: 已删除 - create_failed: 创建失败 
        :type status: str
        :param created_at: **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type updated_at: datetime
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._message_ttl_hours = None
        self._memory_extract_enabled = None
        self._memory_extract_idle_seconds = None
        self._memory_extract_max_tokens = None
        self._memory_extract_max_messages = None
        self._memory_strategies_builtin = None
        self._memory_strategies_customized = None
        self._vpc_id = None
        self._subnet_id = None
        self._private_access = None
        self._public_access = None
        self._api_key = None
        self._encryption_config = None
        self._tags = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if message_ttl_hours is not None:
            self.message_ttl_hours = message_ttl_hours
        if memory_extract_enabled is not None:
            self.memory_extract_enabled = memory_extract_enabled
        if memory_extract_idle_seconds is not None:
            self.memory_extract_idle_seconds = memory_extract_idle_seconds
        if memory_extract_max_tokens is not None:
            self.memory_extract_max_tokens = memory_extract_max_tokens
        if memory_extract_max_messages is not None:
            self.memory_extract_max_messages = memory_extract_max_messages
        if memory_strategies_builtin is not None:
            self.memory_strategies_builtin = memory_strategies_builtin
        if memory_strategies_customized is not None:
            self.memory_strategies_customized = memory_strategies_customized
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if private_access is not None:
            self.private_access = private_access
        if public_access is not None:
            self.public_access = public_access
        if api_key is not None:
            self.api_key = api_key
        if encryption_config is not None:
            self.encryption_config = encryption_config
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this UpdateCoreSpaceResponse.

        **参数解释：** 记忆库 ID，唯一标识一个记忆库，可通过\"创建Space\"接口获取。 **取值范围：** 不涉及。 

        :return: The id of this UpdateCoreSpaceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateCoreSpaceResponse.

        **参数解释：** 记忆库 ID，唯一标识一个记忆库，可通过\"创建Space\"接口获取。 **取值范围：** 不涉及。 

        :param id: The id of this UpdateCoreSpaceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateCoreSpaceResponse.

        **参数解释：** 记忆库名称。 **取值范围：** 不涉及。 

        :return: The name of this UpdateCoreSpaceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCoreSpaceResponse.

        **参数解释：** 记忆库名称。 **取值范围：** 不涉及。 

        :param name: The name of this UpdateCoreSpaceResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateCoreSpaceResponse.

        **参数解释：** 记忆库描述。 **取值范围：** 不涉及。 

        :return: The description of this UpdateCoreSpaceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCoreSpaceResponse.

        **参数解释：** 记忆库描述。 **取值范围：** 不涉及。 

        :param description: The description of this UpdateCoreSpaceResponse.
        :type description: str
        """
        self._description = description

    @property
    def message_ttl_hours(self):
        r"""Gets the message_ttl_hours of this UpdateCoreSpaceResponse.

        **参数解释：** 短期记忆过期时间（小时）。 **取值范围：** 不涉及。 

        :return: The message_ttl_hours of this UpdateCoreSpaceResponse.
        :rtype: int
        """
        return self._message_ttl_hours

    @message_ttl_hours.setter
    def message_ttl_hours(self, message_ttl_hours):
        r"""Sets the message_ttl_hours of this UpdateCoreSpaceResponse.

        **参数解释：** 短期记忆过期时间（小时）。 **取值范围：** 不涉及。 

        :param message_ttl_hours: The message_ttl_hours of this UpdateCoreSpaceResponse.
        :type message_ttl_hours: int
        """
        self._message_ttl_hours = message_ttl_hours

    @property
    def memory_extract_enabled(self):
        r"""Gets the memory_extract_enabled of this UpdateCoreSpaceResponse.

        **参数解释：** 是否开启长期记忆抽取。 **取值范围：** - true: 已开启 - false: 未开启 

        :return: The memory_extract_enabled of this UpdateCoreSpaceResponse.
        :rtype: bool
        """
        return self._memory_extract_enabled

    @memory_extract_enabled.setter
    def memory_extract_enabled(self, memory_extract_enabled):
        r"""Sets the memory_extract_enabled of this UpdateCoreSpaceResponse.

        **参数解释：** 是否开启长期记忆抽取。 **取值范围：** - true: 已开启 - false: 未开启 

        :param memory_extract_enabled: The memory_extract_enabled of this UpdateCoreSpaceResponse.
        :type memory_extract_enabled: bool
        """
        self._memory_extract_enabled = memory_extract_enabled

    @property
    def memory_extract_idle_seconds(self):
        r"""Gets the memory_extract_idle_seconds of this UpdateCoreSpaceResponse.

        **参数解释：** 长期记忆抽取空闲时间（秒）。 **取值范围：** 不涉及。 

        :return: The memory_extract_idle_seconds of this UpdateCoreSpaceResponse.
        :rtype: int
        """
        return self._memory_extract_idle_seconds

    @memory_extract_idle_seconds.setter
    def memory_extract_idle_seconds(self, memory_extract_idle_seconds):
        r"""Sets the memory_extract_idle_seconds of this UpdateCoreSpaceResponse.

        **参数解释：** 长期记忆抽取空闲时间（秒）。 **取值范围：** 不涉及。 

        :param memory_extract_idle_seconds: The memory_extract_idle_seconds of this UpdateCoreSpaceResponse.
        :type memory_extract_idle_seconds: int
        """
        self._memory_extract_idle_seconds = memory_extract_idle_seconds

    @property
    def memory_extract_max_tokens(self):
        r"""Gets the memory_extract_max_tokens of this UpdateCoreSpaceResponse.

        **参数解释：** 长期记忆抽取最大累计 token 数。 **取值范围：** 不涉及。 

        :return: The memory_extract_max_tokens of this UpdateCoreSpaceResponse.
        :rtype: int
        """
        return self._memory_extract_max_tokens

    @memory_extract_max_tokens.setter
    def memory_extract_max_tokens(self, memory_extract_max_tokens):
        r"""Sets the memory_extract_max_tokens of this UpdateCoreSpaceResponse.

        **参数解释：** 长期记忆抽取最大累计 token 数。 **取值范围：** 不涉及。 

        :param memory_extract_max_tokens: The memory_extract_max_tokens of this UpdateCoreSpaceResponse.
        :type memory_extract_max_tokens: int
        """
        self._memory_extract_max_tokens = memory_extract_max_tokens

    @property
    def memory_extract_max_messages(self):
        r"""Gets the memory_extract_max_messages of this UpdateCoreSpaceResponse.

        **参数解释：** 长期记忆抽取最大累计 message 数。 **取值范围：** 不涉及。 

        :return: The memory_extract_max_messages of this UpdateCoreSpaceResponse.
        :rtype: int
        """
        return self._memory_extract_max_messages

    @memory_extract_max_messages.setter
    def memory_extract_max_messages(self, memory_extract_max_messages):
        r"""Sets the memory_extract_max_messages of this UpdateCoreSpaceResponse.

        **参数解释：** 长期记忆抽取最大累计 message 数。 **取值范围：** 不涉及。 

        :param memory_extract_max_messages: The memory_extract_max_messages of this UpdateCoreSpaceResponse.
        :type memory_extract_max_messages: int
        """
        self._memory_extract_max_messages = memory_extract_max_messages

    @property
    def memory_strategies_builtin(self):
        r"""Gets the memory_strategies_builtin of this UpdateCoreSpaceResponse.

        **参数解释：** 内置策略列表。 **取值范围：** 不涉及。 

        :return: The memory_strategies_builtin of this UpdateCoreSpaceResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceBuiltinMemoryStrategy`]
        """
        return self._memory_strategies_builtin

    @memory_strategies_builtin.setter
    def memory_strategies_builtin(self, memory_strategies_builtin):
        r"""Sets the memory_strategies_builtin of this UpdateCoreSpaceResponse.

        **参数解释：** 内置策略列表。 **取值范围：** 不涉及。 

        :param memory_strategies_builtin: The memory_strategies_builtin of this UpdateCoreSpaceResponse.
        :type memory_strategies_builtin: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceBuiltinMemoryStrategy`]
        """
        self._memory_strategies_builtin = memory_strategies_builtin

    @property
    def memory_strategies_customized(self):
        r"""Gets the memory_strategies_customized of this UpdateCoreSpaceResponse.

        **参数解释：** 该记忆库关联的用户自定义记忆策略列表（完整数据）。 **取值范围：** 不涉及。 

        :return: The memory_strategies_customized of this UpdateCoreSpaceResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategy`]
        """
        return self._memory_strategies_customized

    @memory_strategies_customized.setter
    def memory_strategies_customized(self, memory_strategies_customized):
        r"""Sets the memory_strategies_customized of this UpdateCoreSpaceResponse.

        **参数解释：** 该记忆库关联的用户自定义记忆策略列表（完整数据）。 **取值范围：** 不涉及。 

        :param memory_strategies_customized: The memory_strategies_customized of this UpdateCoreSpaceResponse.
        :type memory_strategies_customized: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategy`]
        """
        self._memory_strategies_customized = memory_strategies_customized

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UpdateCoreSpaceResponse.

        **参数解释：** 租户 VPC ID，获取方式：[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)。 **取值范围：** 不涉及。 

        :return: The vpc_id of this UpdateCoreSpaceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UpdateCoreSpaceResponse.

        **参数解释：** 租户 VPC ID，获取方式：[查询VPC列表](https://support.huaweicloud.com/api-vpc/vpc_apiv3_0003.html)。 **取值范围：** 不涉及。 

        :param vpc_id: The vpc_id of this UpdateCoreSpaceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this UpdateCoreSpaceResponse.

        **参数解释：** 租户子网 ID，获取方式：[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 **取值范围：** 不涉及。 

        :return: The subnet_id of this UpdateCoreSpaceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this UpdateCoreSpaceResponse.

        **参数解释：** 租户子网 ID，获取方式：[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)。 **取值范围：** 不涉及。 

        :param subnet_id: The subnet_id of this UpdateCoreSpaceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def private_access(self):
        r"""Gets the private_access of this UpdateCoreSpaceResponse.

        :return: The private_access of this UpdateCoreSpaceResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreSpaceNetwork`
        """
        return self._private_access

    @private_access.setter
    def private_access(self, private_access):
        r"""Sets the private_access of this UpdateCoreSpaceResponse.

        :param private_access: The private_access of this UpdateCoreSpaceResponse.
        :type private_access: :class:`huaweicloudsdkagentarts.v1.CoreSpaceNetwork`
        """
        self._private_access = private_access

    @property
    def public_access(self):
        r"""Gets the public_access of this UpdateCoreSpaceResponse.

        :return: The public_access of this UpdateCoreSpaceResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreSpaceNetwork`
        """
        return self._public_access

    @public_access.setter
    def public_access(self, public_access):
        r"""Sets the public_access of this UpdateCoreSpaceResponse.

        :param public_access: The public_access of this UpdateCoreSpaceResponse.
        :type public_access: :class:`huaweicloudsdkagentarts.v1.CoreSpaceNetwork`
        """
        self._public_access = public_access

    @property
    def api_key(self):
        r"""Gets the api_key of this UpdateCoreSpaceResponse.

        :return: The api_key of this UpdateCoreSpaceResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ShowCoreSpaceApiKeyResponseBody`
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this UpdateCoreSpaceResponse.

        :param api_key: The api_key of this UpdateCoreSpaceResponse.
        :type api_key: :class:`huaweicloudsdkagentarts.v1.ShowCoreSpaceApiKeyResponseBody`
        """
        self._api_key = api_key

    @property
    def encryption_config(self):
        r"""Gets the encryption_config of this UpdateCoreSpaceResponse.

        :return: The encryption_config of this UpdateCoreSpaceResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EncryptionConfig`
        """
        return self._encryption_config

    @encryption_config.setter
    def encryption_config(self, encryption_config):
        r"""Sets the encryption_config of this UpdateCoreSpaceResponse.

        :param encryption_config: The encryption_config of this UpdateCoreSpaceResponse.
        :type encryption_config: :class:`huaweicloudsdkagentarts.v1.EncryptionConfig`
        """
        self._encryption_config = encryption_config

    @property
    def tags(self):
        r"""Gets the tags of this UpdateCoreSpaceResponse.

        **参数解释：** 库标签列表。 **取值范围：** 不涉及。 

        :return: The tags of this UpdateCoreSpaceResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateCoreSpaceResponse.

        **参数解释：** 库标签列表。 **取值范围：** 不涉及。 

        :param tags: The tags of this UpdateCoreSpaceResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        """
        self._tags = tags

    @property
    def status(self):
        r"""Gets the status of this UpdateCoreSpaceResponse.

        **参数解释：** Space 状态。 **取值范围：** - creating: 创建中 - running: 运行中 - deleted: 已删除 - create_failed: 创建失败 

        :return: The status of this UpdateCoreSpaceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateCoreSpaceResponse.

        **参数解释：** Space 状态。 **取值范围：** - creating: 创建中 - running: 运行中 - deleted: 已删除 - create_failed: 创建失败 

        :param status: The status of this UpdateCoreSpaceResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateCoreSpaceResponse.

        **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The created_at of this UpdateCoreSpaceResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateCoreSpaceResponse.

        **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param created_at: The created_at of this UpdateCoreSpaceResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateCoreSpaceResponse.

        **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The updated_at of this UpdateCoreSpaceResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateCoreSpaceResponse.

        **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param updated_at: The updated_at of this UpdateCoreSpaceResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("UpdateCoreSpaceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateCoreSpaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
