# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreSpaceMemoryStrategy:

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
        'type': 'str',
        'origin_type': 'str',
        'steps': 'list[CoreSpaceMemoryStrategyStep]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'origin_type': 'origin_type',
        'steps': 'steps',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, type=None, origin_type=None, steps=None, created_at=None, updated_at=None):
        r"""CoreSpaceMemoryStrategy

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 策略 ID。 **取值范围：** 不涉及。 
        :type id: str
        :param name: **参数解释：** 策略名称。 **取值范围：** 不涉及。 
        :type name: str
        :param type: **参数解释：** 策略类型。 当前包含 4 种内置策略： - **semantic**：语义记忆提取（extraction → consolidation） - **user_preference**：用户偏好提取（extraction → consolidation） - **summary**：会话摘要生成（consolidation） - **episodic**：情景记忆提取（extraction → consolidation → reflection）        **取值范围：** 不涉及。 
        :type type: str
        :param origin_type: **参数解释：** 策略来源类型。 **取值范围：** - builtin: 系统内置 - user: 用户自定义 
        :type origin_type: str
        :param steps: **参数解释：** 策略步骤列表。 **取值范围：** 0-20个。 
        :type steps: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategyStep`]
        :param created_at: **参数解释：** 创建时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 更新时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._origin_type = None
        self._steps = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        self.origin_type = origin_type
        if steps is not None:
            self.steps = steps
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略 ID。 **取值范围：** 不涉及。 

        :return: The id of this CoreSpaceMemoryStrategy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略 ID。 **取值范围：** 不涉及。 

        :param id: The id of this CoreSpaceMemoryStrategy.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略名称。 **取值范围：** 不涉及。 

        :return: The name of this CoreSpaceMemoryStrategy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略名称。 **取值范围：** 不涉及。 

        :param name: The name of this CoreSpaceMemoryStrategy.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略类型。 当前包含 4 种内置策略： - **semantic**：语义记忆提取（extraction → consolidation） - **user_preference**：用户偏好提取（extraction → consolidation） - **summary**：会话摘要生成（consolidation） - **episodic**：情景记忆提取（extraction → consolidation → reflection）        **取值范围：** 不涉及。 

        :return: The type of this CoreSpaceMemoryStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略类型。 当前包含 4 种内置策略： - **semantic**：语义记忆提取（extraction → consolidation） - **user_preference**：用户偏好提取（extraction → consolidation） - **summary**：会话摘要生成（consolidation） - **episodic**：情景记忆提取（extraction → consolidation → reflection）        **取值范围：** 不涉及。 

        :param type: The type of this CoreSpaceMemoryStrategy.
        :type type: str
        """
        self._type = type

    @property
    def origin_type(self):
        r"""Gets the origin_type of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略来源类型。 **取值范围：** - builtin: 系统内置 - user: 用户自定义 

        :return: The origin_type of this CoreSpaceMemoryStrategy.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        r"""Sets the origin_type of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略来源类型。 **取值范围：** - builtin: 系统内置 - user: 用户自定义 

        :param origin_type: The origin_type of this CoreSpaceMemoryStrategy.
        :type origin_type: str
        """
        self._origin_type = origin_type

    @property
    def steps(self):
        r"""Gets the steps of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略步骤列表。 **取值范围：** 0-20个。 

        :return: The steps of this CoreSpaceMemoryStrategy.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategyStep`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this CoreSpaceMemoryStrategy.

        **参数解释：** 策略步骤列表。 **取值范围：** 0-20个。 

        :param steps: The steps of this CoreSpaceMemoryStrategy.
        :type steps: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategyStep`]
        """
        self._steps = steps

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreSpaceMemoryStrategy.

        **参数解释：** 创建时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The created_at of this CoreSpaceMemoryStrategy.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreSpaceMemoryStrategy.

        **参数解释：** 创建时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param created_at: The created_at of this CoreSpaceMemoryStrategy.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreSpaceMemoryStrategy.

        **参数解释：** 更新时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The updated_at of this CoreSpaceMemoryStrategy.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreSpaceMemoryStrategy.

        **参数解释：** 更新时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param updated_at: The updated_at of this CoreSpaceMemoryStrategy.
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
        if not isinstance(other, CoreSpaceMemoryStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
