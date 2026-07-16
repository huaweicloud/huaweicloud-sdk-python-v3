# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreSpaceSummary:

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
        'status': 'str',
        'memory_strategy_count': 'int',
        'message_ttl_days': 'int',
        'tags': 'list[CoreSpaceTag]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'memory_strategy_count': 'memory_strategy_count',
        'message_ttl_days': 'message_ttl_days',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, status=None, memory_strategy_count=None, message_ttl_days=None, tags=None, created_at=None, updated_at=None):
        r"""CoreSpaceSummary

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 记忆库 ID，唯一标识一个记忆库，可通过\&quot;创建Space\&quot;接口获取。 **取值范围：** 不涉及。 
        :type id: str
        :param name: **参数解释：** Space 名称。 **取值范围：** 不涉及。 
        :type name: str
        :param description: **参数解释：** Space 描述。 **取值范围：** 不涉及。 
        :type description: str
        :param status: **参数解释：** 记忆库状态。 **取值范围：** - creating: 创建中 - running: 运行中 - deleted: 已删除 - create_failed: 创建失败 
        :type status: str
        :param memory_strategy_count: **参数解释：** 关联的记忆策略数目（个）。 **取值范围：** 不涉及。 
        :type memory_strategy_count: int
        :param message_ttl_days: **参数解释：** 短期记忆过期时间（天），由 message_ttl_hours 换算。 **取值范围：** 不涉及。 
        :type message_ttl_days: int
        :param tags: **参数解释：** 库标签列表。 **取值范围：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        :param created_at: **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._memory_strategy_count = None
        self._message_ttl_days = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.status = status
        self.memory_strategy_count = memory_strategy_count
        self.message_ttl_days = message_ttl_days
        if tags is not None:
            self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this CoreSpaceSummary.

        **参数解释：** 记忆库 ID，唯一标识一个记忆库，可通过\"创建Space\"接口获取。 **取值范围：** 不涉及。 

        :return: The id of this CoreSpaceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CoreSpaceSummary.

        **参数解释：** 记忆库 ID，唯一标识一个记忆库，可通过\"创建Space\"接口获取。 **取值范围：** 不涉及。 

        :param id: The id of this CoreSpaceSummary.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CoreSpaceSummary.

        **参数解释：** Space 名称。 **取值范围：** 不涉及。 

        :return: The name of this CoreSpaceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CoreSpaceSummary.

        **参数解释：** Space 名称。 **取值范围：** 不涉及。 

        :param name: The name of this CoreSpaceSummary.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CoreSpaceSummary.

        **参数解释：** Space 描述。 **取值范围：** 不涉及。 

        :return: The description of this CoreSpaceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CoreSpaceSummary.

        **参数解释：** Space 描述。 **取值范围：** 不涉及。 

        :param description: The description of this CoreSpaceSummary.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CoreSpaceSummary.

        **参数解释：** 记忆库状态。 **取值范围：** - creating: 创建中 - running: 运行中 - deleted: 已删除 - create_failed: 创建失败 

        :return: The status of this CoreSpaceSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CoreSpaceSummary.

        **参数解释：** 记忆库状态。 **取值范围：** - creating: 创建中 - running: 运行中 - deleted: 已删除 - create_failed: 创建失败 

        :param status: The status of this CoreSpaceSummary.
        :type status: str
        """
        self._status = status

    @property
    def memory_strategy_count(self):
        r"""Gets the memory_strategy_count of this CoreSpaceSummary.

        **参数解释：** 关联的记忆策略数目（个）。 **取值范围：** 不涉及。 

        :return: The memory_strategy_count of this CoreSpaceSummary.
        :rtype: int
        """
        return self._memory_strategy_count

    @memory_strategy_count.setter
    def memory_strategy_count(self, memory_strategy_count):
        r"""Sets the memory_strategy_count of this CoreSpaceSummary.

        **参数解释：** 关联的记忆策略数目（个）。 **取值范围：** 不涉及。 

        :param memory_strategy_count: The memory_strategy_count of this CoreSpaceSummary.
        :type memory_strategy_count: int
        """
        self._memory_strategy_count = memory_strategy_count

    @property
    def message_ttl_days(self):
        r"""Gets the message_ttl_days of this CoreSpaceSummary.

        **参数解释：** 短期记忆过期时间（天），由 message_ttl_hours 换算。 **取值范围：** 不涉及。 

        :return: The message_ttl_days of this CoreSpaceSummary.
        :rtype: int
        """
        return self._message_ttl_days

    @message_ttl_days.setter
    def message_ttl_days(self, message_ttl_days):
        r"""Sets the message_ttl_days of this CoreSpaceSummary.

        **参数解释：** 短期记忆过期时间（天），由 message_ttl_hours 换算。 **取值范围：** 不涉及。 

        :param message_ttl_days: The message_ttl_days of this CoreSpaceSummary.
        :type message_ttl_days: int
        """
        self._message_ttl_days = message_ttl_days

    @property
    def tags(self):
        r"""Gets the tags of this CoreSpaceSummary.

        **参数解释：** 库标签列表。 **取值范围：** 不涉及。 

        :return: The tags of this CoreSpaceSummary.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CoreSpaceSummary.

        **参数解释：** 库标签列表。 **取值范围：** 不涉及。 

        :param tags: The tags of this CoreSpaceSummary.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreSpaceSummary.

        **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The created_at of this CoreSpaceSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreSpaceSummary.

        **参数解释：** 记录的创建时间，由系统自动生成，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param created_at: The created_at of this CoreSpaceSummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreSpaceSummary.

        **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The updated_at of this CoreSpaceSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreSpaceSummary.

        **参数解释：** 记录的最近更新时间，由系统自动更新，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param updated_at: The updated_at of this CoreSpaceSummary.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CoreSpaceSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
