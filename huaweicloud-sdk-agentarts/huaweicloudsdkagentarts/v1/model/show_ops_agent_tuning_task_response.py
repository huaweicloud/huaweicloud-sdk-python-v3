# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsAgentTuningTaskResponse(SdkResponse):

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
        'type': 'str',
        'agent': 'OpsAgentTuningTaskAgent',
        'agency_name': 'str',
        'analysis_task_id': 'str',
        'status': 'str',
        'fail_reason': 'str',
        'created_at': 'int',
        'updated_at': 'int',
        'executed_time': 'int',
        'tags': 'list[OpsTasksTagForTMS]',
        'tuning_target': 'OpsTuningTarget',
        'tuning_output': 'OpsTuningOutput',
        'sample_duration': 'OpsSampleDuration',
        'sample_strategy': 'OpsSampleStrategy',
        'input_tokens': 'int',
        'output_tokens': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'agent': 'agent',
        'agency_name': 'agency_name',
        'analysis_task_id': 'analysis_task_id',
        'status': 'status',
        'fail_reason': 'fail_reason',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'executed_time': 'executed_time',
        'tags': 'tags',
        'tuning_target': 'tuning_target',
        'tuning_output': 'tuning_output',
        'sample_duration': 'sample_duration',
        'sample_strategy': 'sample_strategy',
        'input_tokens': 'input_tokens',
        'output_tokens': 'output_tokens'
    }

    def __init__(self, id=None, name=None, description=None, type=None, agent=None, agency_name=None, analysis_task_id=None, status=None, fail_reason=None, created_at=None, updated_at=None, executed_time=None, tags=None, tuning_target=None, tuning_output=None, sample_duration=None, sample_strategy=None, input_tokens=None, output_tokens=None):
        r"""ShowOpsAgentTuningTaskResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 智能体优化任务ID。  **取值范围：** UUID格式字符串。
        :type id: str
        :param name: **参数解释：** 任务名称。  **取值范围：** 长度1-64个字符的字符串。
        :type name: str
        :param description: **参数解释：** 任务描述。  **取值范围：** 长度0-255个字符的字符串。
        :type description: str
        :param type: **参数解释：**  任务类型，用于根据类型筛选任务。  **取值范围：**  tool：工具，skill：技能。
        :type type: str
        :param agent: 
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsAgentTuningTaskAgent`
        :param agency_name: **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 有效的IAM委托名称字符串。
        :type agency_name: str
        :param analysis_task_id: **参数解释：** 分析任务ID，通过分析任务一键优化创建出来的智能体优化任务该字段不为空。  **取值范围：** 有效分析任务ID。
        :type analysis_task_id: str
        :param status: **参数解释：** 任务状态。  **取值范围：** draft：草稿态，running：运行中，stopping：停止中，stopped：已停止，success：成功，fail：失败。
        :type status: str
        :param fail_reason: **参数解释：** 失败的错误信息。  **取值范围：** 无。
        :type fail_reason: str
        :param created_at: **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。
        :type created_at: int
        :param updated_at: **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。
        :type updated_at: int
        :param executed_time: **参数解释：** 运行时长，单位：分钟。  **取值范围：** 大于等于0的整数（单位：分钟）
        :type executed_time: int
        :param tags: **参数解释：** 资源标签列表。  **取值范围：** 符合OpsTasksTagForTMS定义的对象数组。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        :param tuning_target: 
        :type tuning_target: :class:`huaweicloudsdkagentarts.v1.OpsTuningTarget`
        :param tuning_output: 
        :type tuning_output: :class:`huaweicloudsdkagentarts.v1.OpsTuningOutput`
        :param sample_duration: 
        :type sample_duration: :class:`huaweicloudsdkagentarts.v1.OpsSampleDuration`
        :param sample_strategy: 
        :type sample_strategy: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        :param input_tokens: **参数解释：** 输入的 Token 数。  **取值范围：** 无。
        :type input_tokens: int
        :param output_tokens: **参数解释：** 模型输出的 Token 数。  **取值范围：** 无。
        :type output_tokens: int
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._agent = None
        self._agency_name = None
        self._analysis_task_id = None
        self._status = None
        self._fail_reason = None
        self._created_at = None
        self._updated_at = None
        self._executed_time = None
        self._tags = None
        self._tuning_target = None
        self._tuning_output = None
        self._sample_duration = None
        self._sample_strategy = None
        self._input_tokens = None
        self._output_tokens = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if agent is not None:
            self.agent = agent
        if agency_name is not None:
            self.agency_name = agency_name
        if analysis_task_id is not None:
            self.analysis_task_id = analysis_task_id
        if status is not None:
            self.status = status
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if executed_time is not None:
            self.executed_time = executed_time
        if tags is not None:
            self.tags = tags
        if tuning_target is not None:
            self.tuning_target = tuning_target
        if tuning_output is not None:
            self.tuning_output = tuning_output
        if sample_duration is not None:
            self.sample_duration = sample_duration
        if sample_strategy is not None:
            self.sample_strategy = sample_strategy
        if input_tokens is not None:
            self.input_tokens = input_tokens
        if output_tokens is not None:
            self.output_tokens = output_tokens

    @property
    def id(self):
        r"""Gets the id of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 智能体优化任务ID。  **取值范围：** UUID格式字符串。

        :return: The id of this ShowOpsAgentTuningTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 智能体优化任务ID。  **取值范围：** UUID格式字符串。

        :param id: The id of this ShowOpsAgentTuningTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 任务名称。  **取值范围：** 长度1-64个字符的字符串。

        :return: The name of this ShowOpsAgentTuningTaskResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 任务名称。  **取值范围：** 长度1-64个字符的字符串。

        :param name: The name of this ShowOpsAgentTuningTaskResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 任务描述。  **取值范围：** 长度0-255个字符的字符串。

        :return: The description of this ShowOpsAgentTuningTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 任务描述。  **取值范围：** 长度0-255个字符的字符串。

        :param description: The description of this ShowOpsAgentTuningTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this ShowOpsAgentTuningTaskResponse.

        **参数解释：**  任务类型，用于根据类型筛选任务。  **取值范围：**  tool：工具，skill：技能。

        :return: The type of this ShowOpsAgentTuningTaskResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowOpsAgentTuningTaskResponse.

        **参数解释：**  任务类型，用于根据类型筛选任务。  **取值范围：**  tool：工具，skill：技能。

        :param type: The type of this ShowOpsAgentTuningTaskResponse.
        :type type: str
        """
        self._type = type

    @property
    def agent(self):
        r"""Gets the agent of this ShowOpsAgentTuningTaskResponse.

        :return: The agent of this ShowOpsAgentTuningTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsAgentTuningTaskAgent`
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        r"""Sets the agent of this ShowOpsAgentTuningTaskResponse.

        :param agent: The agent of this ShowOpsAgentTuningTaskResponse.
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsAgentTuningTaskAgent`
        """
        self._agent = agent

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 有效的IAM委托名称字符串。

        :return: The agency_name of this ShowOpsAgentTuningTaskResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 有效的IAM委托名称字符串。

        :param agency_name: The agency_name of this ShowOpsAgentTuningTaskResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def analysis_task_id(self):
        r"""Gets the analysis_task_id of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 分析任务ID，通过分析任务一键优化创建出来的智能体优化任务该字段不为空。  **取值范围：** 有效分析任务ID。

        :return: The analysis_task_id of this ShowOpsAgentTuningTaskResponse.
        :rtype: str
        """
        return self._analysis_task_id

    @analysis_task_id.setter
    def analysis_task_id(self, analysis_task_id):
        r"""Sets the analysis_task_id of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 分析任务ID，通过分析任务一键优化创建出来的智能体优化任务该字段不为空。  **取值范围：** 有效分析任务ID。

        :param analysis_task_id: The analysis_task_id of this ShowOpsAgentTuningTaskResponse.
        :type analysis_task_id: str
        """
        self._analysis_task_id = analysis_task_id

    @property
    def status(self):
        r"""Gets the status of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 任务状态。  **取值范围：** draft：草稿态，running：运行中，stopping：停止中，stopped：已停止，success：成功，fail：失败。

        :return: The status of this ShowOpsAgentTuningTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 任务状态。  **取值范围：** draft：草稿态，running：运行中，stopping：停止中，stopped：已停止，success：成功，fail：失败。

        :param status: The status of this ShowOpsAgentTuningTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 失败的错误信息。  **取值范围：** 无。

        :return: The fail_reason of this ShowOpsAgentTuningTaskResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 失败的错误信息。  **取值范围：** 无。

        :param fail_reason: The fail_reason of this ShowOpsAgentTuningTaskResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :return: The created_at of this ShowOpsAgentTuningTaskResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :param created_at: The created_at of this ShowOpsAgentTuningTaskResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。

        :return: The updated_at of this ShowOpsAgentTuningTaskResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。

        :param updated_at: The updated_at of this ShowOpsAgentTuningTaskResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def executed_time(self):
        r"""Gets the executed_time of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 运行时长，单位：分钟。  **取值范围：** 大于等于0的整数（单位：分钟）

        :return: The executed_time of this ShowOpsAgentTuningTaskResponse.
        :rtype: int
        """
        return self._executed_time

    @executed_time.setter
    def executed_time(self, executed_time):
        r"""Sets the executed_time of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 运行时长，单位：分钟。  **取值范围：** 大于等于0的整数（单位：分钟）

        :param executed_time: The executed_time of this ShowOpsAgentTuningTaskResponse.
        :type executed_time: int
        """
        self._executed_time = executed_time

    @property
    def tags(self):
        r"""Gets the tags of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 资源标签列表。  **取值范围：** 符合OpsTasksTagForTMS定义的对象数组。

        :return: The tags of this ShowOpsAgentTuningTaskResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 资源标签列表。  **取值范围：** 符合OpsTasksTagForTMS定义的对象数组。

        :param tags: The tags of this ShowOpsAgentTuningTaskResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        self._tags = tags

    @property
    def tuning_target(self):
        r"""Gets the tuning_target of this ShowOpsAgentTuningTaskResponse.

        :return: The tuning_target of this ShowOpsAgentTuningTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningTarget`
        """
        return self._tuning_target

    @tuning_target.setter
    def tuning_target(self, tuning_target):
        r"""Sets the tuning_target of this ShowOpsAgentTuningTaskResponse.

        :param tuning_target: The tuning_target of this ShowOpsAgentTuningTaskResponse.
        :type tuning_target: :class:`huaweicloudsdkagentarts.v1.OpsTuningTarget`
        """
        self._tuning_target = tuning_target

    @property
    def tuning_output(self):
        r"""Gets the tuning_output of this ShowOpsAgentTuningTaskResponse.

        :return: The tuning_output of this ShowOpsAgentTuningTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTuningOutput`
        """
        return self._tuning_output

    @tuning_output.setter
    def tuning_output(self, tuning_output):
        r"""Sets the tuning_output of this ShowOpsAgentTuningTaskResponse.

        :param tuning_output: The tuning_output of this ShowOpsAgentTuningTaskResponse.
        :type tuning_output: :class:`huaweicloudsdkagentarts.v1.OpsTuningOutput`
        """
        self._tuning_output = tuning_output

    @property
    def sample_duration(self):
        r"""Gets the sample_duration of this ShowOpsAgentTuningTaskResponse.

        :return: The sample_duration of this ShowOpsAgentTuningTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsSampleDuration`
        """
        return self._sample_duration

    @sample_duration.setter
    def sample_duration(self, sample_duration):
        r"""Sets the sample_duration of this ShowOpsAgentTuningTaskResponse.

        :param sample_duration: The sample_duration of this ShowOpsAgentTuningTaskResponse.
        :type sample_duration: :class:`huaweicloudsdkagentarts.v1.OpsSampleDuration`
        """
        self._sample_duration = sample_duration

    @property
    def sample_strategy(self):
        r"""Gets the sample_strategy of this ShowOpsAgentTuningTaskResponse.

        :return: The sample_strategy of this ShowOpsAgentTuningTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        """
        return self._sample_strategy

    @sample_strategy.setter
    def sample_strategy(self, sample_strategy):
        r"""Sets the sample_strategy of this ShowOpsAgentTuningTaskResponse.

        :param sample_strategy: The sample_strategy of this ShowOpsAgentTuningTaskResponse.
        :type sample_strategy: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        """
        self._sample_strategy = sample_strategy

    @property
    def input_tokens(self):
        r"""Gets the input_tokens of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 输入的 Token 数。  **取值范围：** 无。

        :return: The input_tokens of this ShowOpsAgentTuningTaskResponse.
        :rtype: int
        """
        return self._input_tokens

    @input_tokens.setter
    def input_tokens(self, input_tokens):
        r"""Sets the input_tokens of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 输入的 Token 数。  **取值范围：** 无。

        :param input_tokens: The input_tokens of this ShowOpsAgentTuningTaskResponse.
        :type input_tokens: int
        """
        self._input_tokens = input_tokens

    @property
    def output_tokens(self):
        r"""Gets the output_tokens of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 模型输出的 Token 数。  **取值范围：** 无。

        :return: The output_tokens of this ShowOpsAgentTuningTaskResponse.
        :rtype: int
        """
        return self._output_tokens

    @output_tokens.setter
    def output_tokens(self, output_tokens):
        r"""Sets the output_tokens of this ShowOpsAgentTuningTaskResponse.

        **参数解释：** 模型输出的 Token 数。  **取值范围：** 无。

        :param output_tokens: The output_tokens of this ShowOpsAgentTuningTaskResponse.
        :type output_tokens: int
        """
        self._output_tokens = output_tokens

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsAgentTuningTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsAgentTuningTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
