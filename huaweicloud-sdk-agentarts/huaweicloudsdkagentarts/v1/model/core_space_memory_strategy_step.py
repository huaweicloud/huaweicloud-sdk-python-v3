# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreSpaceMemoryStrategyStep:

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
        'step_order': 'int',
        'step_type': 'str',
        'isolation_level': 'str',
        'instruction': 'str',
        'output_schema': 'str',
        'enabled': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'step_order': 'step_order',
        'step_type': 'step_type',
        'isolation_level': 'isolation_level',
        'instruction': 'instruction',
        'output_schema': 'output_schema',
        'enabled': 'enabled',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, step_order=None, step_type=None, isolation_level=None, instruction=None, output_schema=None, enabled=None, created_at=None, updated_at=None):
        r"""CoreSpaceMemoryStrategyStep

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 步骤 ID。 **取值范围：** 不涉及。 
        :type id: str
        :param step_order: **参数解释：** 步骤执行顺序。 **取值范围：** 不涉及。 
        :type step_order: int
        :param step_type: **参数解释：** 步骤类型。 **取值范围：** - extraction: 提取 - consolidation: 合并 - reflection: 反思 
        :type step_type: str
        :param isolation_level: **参数解释：** 隔离级别。 **取值范围：** - actor: 按用户隔离 - session: 按会话隔离 - null: step_type&#x3D;extraction时，isolation_level&#x3D;null 
        :type isolation_level: str
        :param instruction: **参数解释：** 步骤指令。 **取值范围：** 不涉及。 
        :type instruction: str
        :param output_schema: **参数解释：** 输出格式模板。 **取值范围：** 不涉及。 
        :type output_schema: str
        :param enabled: **参数解释：** 是否启用。 **取值范围：** 不涉及。 
        :type enabled: bool
        :param created_at: **参数解释：** 创建时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 更新时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._step_order = None
        self._step_type = None
        self._isolation_level = None
        self._instruction = None
        self._output_schema = None
        self._enabled = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.step_order = step_order
        self.step_type = step_type
        if isolation_level is not None:
            self.isolation_level = isolation_level
        if instruction is not None:
            self.instruction = instruction
        if output_schema is not None:
            self.output_schema = output_schema
        self.enabled = enabled
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 步骤 ID。 **取值范围：** 不涉及。 

        :return: The id of this CoreSpaceMemoryStrategyStep.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 步骤 ID。 **取值范围：** 不涉及。 

        :param id: The id of this CoreSpaceMemoryStrategyStep.
        :type id: str
        """
        self._id = id

    @property
    def step_order(self):
        r"""Gets the step_order of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 步骤执行顺序。 **取值范围：** 不涉及。 

        :return: The step_order of this CoreSpaceMemoryStrategyStep.
        :rtype: int
        """
        return self._step_order

    @step_order.setter
    def step_order(self, step_order):
        r"""Sets the step_order of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 步骤执行顺序。 **取值范围：** 不涉及。 

        :param step_order: The step_order of this CoreSpaceMemoryStrategyStep.
        :type step_order: int
        """
        self._step_order = step_order

    @property
    def step_type(self):
        r"""Gets the step_type of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 步骤类型。 **取值范围：** - extraction: 提取 - consolidation: 合并 - reflection: 反思 

        :return: The step_type of this CoreSpaceMemoryStrategyStep.
        :rtype: str
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        r"""Sets the step_type of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 步骤类型。 **取值范围：** - extraction: 提取 - consolidation: 合并 - reflection: 反思 

        :param step_type: The step_type of this CoreSpaceMemoryStrategyStep.
        :type step_type: str
        """
        self._step_type = step_type

    @property
    def isolation_level(self):
        r"""Gets the isolation_level of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 隔离级别。 **取值范围：** - actor: 按用户隔离 - session: 按会话隔离 - null: step_type=extraction时，isolation_level=null 

        :return: The isolation_level of this CoreSpaceMemoryStrategyStep.
        :rtype: str
        """
        return self._isolation_level

    @isolation_level.setter
    def isolation_level(self, isolation_level):
        r"""Sets the isolation_level of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 隔离级别。 **取值范围：** - actor: 按用户隔离 - session: 按会话隔离 - null: step_type=extraction时，isolation_level=null 

        :param isolation_level: The isolation_level of this CoreSpaceMemoryStrategyStep.
        :type isolation_level: str
        """
        self._isolation_level = isolation_level

    @property
    def instruction(self):
        r"""Gets the instruction of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 步骤指令。 **取值范围：** 不涉及。 

        :return: The instruction of this CoreSpaceMemoryStrategyStep.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        r"""Sets the instruction of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 步骤指令。 **取值范围：** 不涉及。 

        :param instruction: The instruction of this CoreSpaceMemoryStrategyStep.
        :type instruction: str
        """
        self._instruction = instruction

    @property
    def output_schema(self):
        r"""Gets the output_schema of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 输出格式模板。 **取值范围：** 不涉及。 

        :return: The output_schema of this CoreSpaceMemoryStrategyStep.
        :rtype: str
        """
        return self._output_schema

    @output_schema.setter
    def output_schema(self, output_schema):
        r"""Sets the output_schema of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 输出格式模板。 **取值范围：** 不涉及。 

        :param output_schema: The output_schema of this CoreSpaceMemoryStrategyStep.
        :type output_schema: str
        """
        self._output_schema = output_schema

    @property
    def enabled(self):
        r"""Gets the enabled of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 是否启用。 **取值范围：** 不涉及。 

        :return: The enabled of this CoreSpaceMemoryStrategyStep.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 是否启用。 **取值范围：** 不涉及。 

        :param enabled: The enabled of this CoreSpaceMemoryStrategyStep.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 创建时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The created_at of this CoreSpaceMemoryStrategyStep.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 创建时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param created_at: The created_at of this CoreSpaceMemoryStrategyStep.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 更新时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :return: The updated_at of this CoreSpaceMemoryStrategyStep.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreSpaceMemoryStrategyStep.

        **参数解释：** 更新时间，格式为 ISO 8601（YYYY-MM-DDTHH:mm:ssZ）。 **取值范围：** 不涉及。 

        :param updated_at: The updated_at of this CoreSpaceMemoryStrategyStep.
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
        if not isinstance(other, CoreSpaceMemoryStrategyStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
