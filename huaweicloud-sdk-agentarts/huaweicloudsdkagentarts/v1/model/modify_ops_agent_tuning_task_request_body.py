# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyOpsAgentTuningTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'agent': 'OpsAgentTuningTaskAgent',
        'tuning_target': 'OpsTuningTarget',
        'sample_duration': 'OpsSampleDuration',
        'sample_strategy': 'OpsSampleStrategy',
        'agency_name': 'str',
        'tags': 'list[OpsTasksTagForTMS]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'agent': 'agent',
        'tuning_target': 'tuning_target',
        'sample_duration': 'sample_duration',
        'sample_strategy': 'sample_strategy',
        'agency_name': 'agency_name',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, type=None, agent=None, tuning_target=None, sample_duration=None, sample_strategy=None, agency_name=None, tags=None):
        r"""ModifyOpsAgentTuningTaskRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 任务名称，用于标识和区分不同的智能体优化任务。  **约束限制：** 不涉及  **取值范围：** 长度2-64个字符，支持中文、字母、数字、中划线及下划线。  **默认取值：** 无
        :type name: str
        :param description: **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **约束限制：** 不涉及  **取值范围：** 长度0-1024个字符。  **默认取值：** 无
        :type description: str
        :param type: **参数解释：**  任务类型，用于根据类型筛选任务。  **约束限制：**  不涉及 。  **取值范围：**  tool：工具，skill：技能。   **默认取值：**  无。
        :type type: str
        :param agent: 
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsAgentTuningTaskAgent`
        :param tuning_target: 
        :type tuning_target: :class:`huaweicloudsdkagentarts.v1.OpsTuningTarget`
        :param sample_duration: 
        :type sample_duration: :class:`huaweicloudsdkagentarts.v1.OpsSampleDuration`
        :param sample_strategy: 
        :type sample_strategy: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        :param agency_name: **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **约束限制：** 必须是IAM中已创建的有效委托。  **取值范围：** 合法的委托名称字符串。  **默认取值：** 无
        :type agency_name: str
        :param tags: **参数解释：** 资源标签列表，用于资源分类。  **约束限制：** 不涉及  **取值范围：** 数组长度0-20。  **默认取值：** 空数组
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._agent = None
        self._tuning_target = None
        self._sample_duration = None
        self._sample_strategy = None
        self._agency_name = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        self.agent = agent
        self.tuning_target = tuning_target
        self.sample_duration = sample_duration
        self.sample_strategy = sample_strategy
        self.agency_name = agency_name
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：** 任务名称，用于标识和区分不同的智能体优化任务。  **约束限制：** 不涉及  **取值范围：** 长度2-64个字符，支持中文、字母、数字、中划线及下划线。  **默认取值：** 无

        :return: The name of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：** 任务名称，用于标识和区分不同的智能体优化任务。  **约束限制：** 不涉及  **取值范围：** 长度2-64个字符，支持中文、字母、数字、中划线及下划线。  **默认取值：** 无

        :param name: The name of this ModifyOpsAgentTuningTaskRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **约束限制：** 不涉及  **取值范围：** 长度0-1024个字符。  **默认取值：** 无

        :return: The description of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **约束限制：** 不涉及  **取值范围：** 长度0-1024个字符。  **默认取值：** 无

        :param description: The description of this ModifyOpsAgentTuningTaskRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：**  任务类型，用于根据类型筛选任务。  **约束限制：**  不涉及 。  **取值范围：**  tool：工具，skill：技能。   **默认取值：**  无。

        :return: The type of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：**  任务类型，用于根据类型筛选任务。  **约束限制：**  不涉及 。  **取值范围：**  tool：工具，skill：技能。   **默认取值：**  无。

        :param type: The type of this ModifyOpsAgentTuningTaskRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def agent(self):
        r"""Gets the agent of this ModifyOpsAgentTuningTaskRequestBody.

        :return: The agent of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsAgentTuningTaskAgent`
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        r"""Sets the agent of this ModifyOpsAgentTuningTaskRequestBody.

        :param agent: The agent of this ModifyOpsAgentTuningTaskRequestBody.
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsAgentTuningTaskAgent`
        """
        self._agent = agent

    @property
    def tuning_target(self):
        r"""Gets the tuning_target of this ModifyOpsAgentTuningTaskRequestBody.

        :return: The tuning_target of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningTarget`
        """
        return self._tuning_target

    @tuning_target.setter
    def tuning_target(self, tuning_target):
        r"""Sets the tuning_target of this ModifyOpsAgentTuningTaskRequestBody.

        :param tuning_target: The tuning_target of this ModifyOpsAgentTuningTaskRequestBody.
        :type tuning_target: :class:`huaweicloudsdkagentarts.v1.OpsTuningTarget`
        """
        self._tuning_target = tuning_target

    @property
    def sample_duration(self):
        r"""Gets the sample_duration of this ModifyOpsAgentTuningTaskRequestBody.

        :return: The sample_duration of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsSampleDuration`
        """
        return self._sample_duration

    @sample_duration.setter
    def sample_duration(self, sample_duration):
        r"""Sets the sample_duration of this ModifyOpsAgentTuningTaskRequestBody.

        :param sample_duration: The sample_duration of this ModifyOpsAgentTuningTaskRequestBody.
        :type sample_duration: :class:`huaweicloudsdkagentarts.v1.OpsSampleDuration`
        """
        self._sample_duration = sample_duration

    @property
    def sample_strategy(self):
        r"""Gets the sample_strategy of this ModifyOpsAgentTuningTaskRequestBody.

        :return: The sample_strategy of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        """
        return self._sample_strategy

    @sample_strategy.setter
    def sample_strategy(self, sample_strategy):
        r"""Sets the sample_strategy of this ModifyOpsAgentTuningTaskRequestBody.

        :param sample_strategy: The sample_strategy of this ModifyOpsAgentTuningTaskRequestBody.
        :type sample_strategy: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        """
        self._sample_strategy = sample_strategy

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **约束限制：** 必须是IAM中已创建的有效委托。  **取值范围：** 合法的委托名称字符串。  **默认取值：** 无

        :return: The agency_name of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **约束限制：** 必须是IAM中已创建的有效委托。  **取值范围：** 合法的委托名称字符串。  **默认取值：** 无

        :param agency_name: The agency_name of this ModifyOpsAgentTuningTaskRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def tags(self):
        r"""Gets the tags of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：** 资源标签列表，用于资源分类。  **约束限制：** 不涉及  **取值范围：** 数组长度0-20。  **默认取值：** 空数组

        :return: The tags of this ModifyOpsAgentTuningTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ModifyOpsAgentTuningTaskRequestBody.

        **参数解释：** 资源标签列表，用于资源分类。  **约束限制：** 不涉及  **取值范围：** 数组长度0-20。  **默认取值：** 空数组

        :param tags: The tags of this ModifyOpsAgentTuningTaskRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        self._tags = tags

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
        if not isinstance(other, ModifyOpsAgentTuningTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
