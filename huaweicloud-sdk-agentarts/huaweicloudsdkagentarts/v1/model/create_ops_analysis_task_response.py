# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsAnalysisTaskResponse(SdkResponse):

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
        'agent': 'OpsAnalysisTaskAgent',
        'agency_name': 'str',
        'status': 'str',
        'created_at': 'int',
        'updated_at': 'int',
        'next_fire_time': 'int',
        'tags': 'list[OpsTasksTagForTMS]',
        'progress': 'OpsTaskProgress',
        'execution_strategy': 'OpsExecutionStrategy',
        'status_count': 'OpsAnalysisTaskInstanceStatusCount',
        'sample_strategy': 'OpsSampleStrategy',
        'failures': 'list[OpsFailureCategory]',
        'input_tokens': 'int',
        'output_tokens': 'int',
        'total_session_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'agent': 'agent',
        'agency_name': 'agency_name',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'next_fire_time': 'next_fire_time',
        'tags': 'tags',
        'progress': 'progress',
        'execution_strategy': 'execution_strategy',
        'status_count': 'status_count',
        'sample_strategy': 'sample_strategy',
        'failures': 'failures',
        'input_tokens': 'input_tokens',
        'output_tokens': 'output_tokens',
        'total_session_count': 'total_session_count'
    }

    def __init__(self, id=None, name=None, description=None, agent=None, agency_name=None, status=None, created_at=None, updated_at=None, next_fire_time=None, tags=None, progress=None, execution_strategy=None, status_count=None, sample_strategy=None, failures=None, input_tokens=None, output_tokens=None, total_session_count=None):
        r"""CreateOpsAnalysisTaskResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 智能体优化任务ID。  **取值范围：** UUID格式字符串。
        :type id: str
        :param name: **参数解释：** 任务名称，用于标识和区分不同的分析任务。  **取值范围：** 长度1-64个字符，支持中文、字母、数字、中划线及下划线。
        :type name: str
        :param description: **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **取值范围：** 长度0-1024个字符。
        :type description: str
        :param agent: 
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskAgent`
        :param agency_name: **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 合法的委托名称字符串。
        :type agency_name: str
        :param status: **参数解释：** 任务状态。  **取值范围：** draft：草稿态，scheduled：待运行，running：运行中，paused：已暂停，completed：已完成，fail：失败，stopping：停止中，stopped：已停止。
        :type status: str
        :param created_at: **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。
        :type created_at: int
        :param updated_at: **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。
        :type updated_at: int
        :param next_fire_time: **参数解释：** 计划下次执行时间。对于待运行、运行中的周期任务，显示下一个task instance时间。对于其他状态的周期任务为null。对待运行的单次任务显示计划运行时间。无后续调度时为 null。  **取值范围：** 13位毫秒级时间戳或 null。
        :type next_fire_time: int
        :param tags: **参数解释：** 资源标签列表，用于资源分类。  **取值范围：** 数组长度0-20。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        :param progress: 
        :type progress: :class:`huaweicloudsdkagentarts.v1.OpsTaskProgress`
        :param execution_strategy: 
        :type execution_strategy: :class:`huaweicloudsdkagentarts.v1.OpsExecutionStrategy`
        :param status_count: 
        :type status_count: :class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskInstanceStatusCount`
        :param sample_strategy: 
        :type sample_strategy: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        :param failures: **参数解释：** 故障列表。  **取值范围：** 长度为0-100的数组。
        :type failures: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureCategory`]
        :param input_tokens: **参数解释：** 输入的 Token 数。 **取值范围：** 无。任务未执行过时为 null。
        :type input_tokens: int
        :param output_tokens: **参数解释：** 模型输出的 Token 数。 **取值范围：** 无。任务未执行过时为 null。
        :type output_tokens: int
        :param total_session_count: **参数解释：** 分析覆盖的session总数。 **取值范围：** 无。
        :type total_session_count: int
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._agent = None
        self._agency_name = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._next_fire_time = None
        self._tags = None
        self._progress = None
        self._execution_strategy = None
        self._status_count = None
        self._sample_strategy = None
        self._failures = None
        self._input_tokens = None
        self._output_tokens = None
        self._total_session_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if agent is not None:
            self.agent = agent
        if agency_name is not None:
            self.agency_name = agency_name
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if next_fire_time is not None:
            self.next_fire_time = next_fire_time
        if tags is not None:
            self.tags = tags
        if progress is not None:
            self.progress = progress
        if execution_strategy is not None:
            self.execution_strategy = execution_strategy
        if status_count is not None:
            self.status_count = status_count
        if sample_strategy is not None:
            self.sample_strategy = sample_strategy
        if failures is not None:
            self.failures = failures
        if input_tokens is not None:
            self.input_tokens = input_tokens
        if output_tokens is not None:
            self.output_tokens = output_tokens
        if total_session_count is not None:
            self.total_session_count = total_session_count

    @property
    def id(self):
        r"""Gets the id of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 智能体优化任务ID。  **取值范围：** UUID格式字符串。

        :return: The id of this CreateOpsAnalysisTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 智能体优化任务ID。  **取值范围：** UUID格式字符串。

        :param id: The id of this CreateOpsAnalysisTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 任务名称，用于标识和区分不同的分析任务。  **取值范围：** 长度1-64个字符，支持中文、字母、数字、中划线及下划线。

        :return: The name of this CreateOpsAnalysisTaskResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 任务名称，用于标识和区分不同的分析任务。  **取值范围：** 长度1-64个字符，支持中文、字母、数字、中划线及下划线。

        :param name: The name of this CreateOpsAnalysisTaskResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **取值范围：** 长度0-1024个字符。

        :return: The description of this CreateOpsAnalysisTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 任务的详细描述，用于记录任务目的或备注信息。  **取值范围：** 长度0-1024个字符。

        :param description: The description of this CreateOpsAnalysisTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def agent(self):
        r"""Gets the agent of this CreateOpsAnalysisTaskResponse.

        :return: The agent of this CreateOpsAnalysisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskAgent`
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        r"""Sets the agent of this CreateOpsAnalysisTaskResponse.

        :param agent: The agent of this CreateOpsAnalysisTaskResponse.
        :type agent: :class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskAgent`
        """
        self._agent = agent

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 合法的委托名称字符串。

        :return: The agency_name of this CreateOpsAnalysisTaskResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 委托名称，赋予服务访问用户资源的权限。  **取值范围：** 合法的委托名称字符串。

        :param agency_name: The agency_name of this CreateOpsAnalysisTaskResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def status(self):
        r"""Gets the status of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 任务状态。  **取值范围：** draft：草稿态，scheduled：待运行，running：运行中，paused：已暂停，completed：已完成，fail：失败，stopping：停止中，stopped：已停止。

        :return: The status of this CreateOpsAnalysisTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 任务状态。  **取值范围：** draft：草稿态，scheduled：待运行，running：运行中，paused：已暂停，completed：已完成，fail：失败，stopping：停止中，stopped：已停止。

        :param status: The status of this CreateOpsAnalysisTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :return: The created_at of this CreateOpsAnalysisTaskResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 创建时间，单位：毫秒（13位时间戳）。  **取值范围：** 13位毫秒级时间戳。

        :param created_at: The created_at of this CreateOpsAnalysisTaskResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。

        :return: The updated_at of this CreateOpsAnalysisTaskResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 更新时间（单位：毫秒）  **取值范围：** 13位毫秒级时间戳。

        :param updated_at: The updated_at of this CreateOpsAnalysisTaskResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def next_fire_time(self):
        r"""Gets the next_fire_time of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 计划下次执行时间。对于待运行、运行中的周期任务，显示下一个task instance时间。对于其他状态的周期任务为null。对待运行的单次任务显示计划运行时间。无后续调度时为 null。  **取值范围：** 13位毫秒级时间戳或 null。

        :return: The next_fire_time of this CreateOpsAnalysisTaskResponse.
        :rtype: int
        """
        return self._next_fire_time

    @next_fire_time.setter
    def next_fire_time(self, next_fire_time):
        r"""Sets the next_fire_time of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 计划下次执行时间。对于待运行、运行中的周期任务，显示下一个task instance时间。对于其他状态的周期任务为null。对待运行的单次任务显示计划运行时间。无后续调度时为 null。  **取值范围：** 13位毫秒级时间戳或 null。

        :param next_fire_time: The next_fire_time of this CreateOpsAnalysisTaskResponse.
        :type next_fire_time: int
        """
        self._next_fire_time = next_fire_time

    @property
    def tags(self):
        r"""Gets the tags of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 资源标签列表，用于资源分类。  **取值范围：** 数组长度0-20。

        :return: The tags of this CreateOpsAnalysisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 资源标签列表，用于资源分类。  **取值范围：** 数组长度0-20。

        :param tags: The tags of this CreateOpsAnalysisTaskResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTasksTagForTMS`]
        """
        self._tags = tags

    @property
    def progress(self):
        r"""Gets the progress of this CreateOpsAnalysisTaskResponse.

        :return: The progress of this CreateOpsAnalysisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsTaskProgress`
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this CreateOpsAnalysisTaskResponse.

        :param progress: The progress of this CreateOpsAnalysisTaskResponse.
        :type progress: :class:`huaweicloudsdkagentarts.v1.OpsTaskProgress`
        """
        self._progress = progress

    @property
    def execution_strategy(self):
        r"""Gets the execution_strategy of this CreateOpsAnalysisTaskResponse.

        :return: The execution_strategy of this CreateOpsAnalysisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsExecutionStrategy`
        """
        return self._execution_strategy

    @execution_strategy.setter
    def execution_strategy(self, execution_strategy):
        r"""Sets the execution_strategy of this CreateOpsAnalysisTaskResponse.

        :param execution_strategy: The execution_strategy of this CreateOpsAnalysisTaskResponse.
        :type execution_strategy: :class:`huaweicloudsdkagentarts.v1.OpsExecutionStrategy`
        """
        self._execution_strategy = execution_strategy

    @property
    def status_count(self):
        r"""Gets the status_count of this CreateOpsAnalysisTaskResponse.

        :return: The status_count of this CreateOpsAnalysisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskInstanceStatusCount`
        """
        return self._status_count

    @status_count.setter
    def status_count(self, status_count):
        r"""Sets the status_count of this CreateOpsAnalysisTaskResponse.

        :param status_count: The status_count of this CreateOpsAnalysisTaskResponse.
        :type status_count: :class:`huaweicloudsdkagentarts.v1.OpsAnalysisTaskInstanceStatusCount`
        """
        self._status_count = status_count

    @property
    def sample_strategy(self):
        r"""Gets the sample_strategy of this CreateOpsAnalysisTaskResponse.

        :return: The sample_strategy of this CreateOpsAnalysisTaskResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        """
        return self._sample_strategy

    @sample_strategy.setter
    def sample_strategy(self, sample_strategy):
        r"""Sets the sample_strategy of this CreateOpsAnalysisTaskResponse.

        :param sample_strategy: The sample_strategy of this CreateOpsAnalysisTaskResponse.
        :type sample_strategy: :class:`huaweicloudsdkagentarts.v1.OpsSampleStrategy`
        """
        self._sample_strategy = sample_strategy

    @property
    def failures(self):
        r"""Gets the failures of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 故障列表。  **取值范围：** 长度为0-100的数组。

        :return: The failures of this CreateOpsAnalysisTaskResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureCategory`]
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        r"""Sets the failures of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 故障列表。  **取值范围：** 长度为0-100的数组。

        :param failures: The failures of this CreateOpsAnalysisTaskResponse.
        :type failures: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureCategory`]
        """
        self._failures = failures

    @property
    def input_tokens(self):
        r"""Gets the input_tokens of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 输入的 Token 数。 **取值范围：** 无。任务未执行过时为 null。

        :return: The input_tokens of this CreateOpsAnalysisTaskResponse.
        :rtype: int
        """
        return self._input_tokens

    @input_tokens.setter
    def input_tokens(self, input_tokens):
        r"""Sets the input_tokens of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 输入的 Token 数。 **取值范围：** 无。任务未执行过时为 null。

        :param input_tokens: The input_tokens of this CreateOpsAnalysisTaskResponse.
        :type input_tokens: int
        """
        self._input_tokens = input_tokens

    @property
    def output_tokens(self):
        r"""Gets the output_tokens of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 模型输出的 Token 数。 **取值范围：** 无。任务未执行过时为 null。

        :return: The output_tokens of this CreateOpsAnalysisTaskResponse.
        :rtype: int
        """
        return self._output_tokens

    @output_tokens.setter
    def output_tokens(self, output_tokens):
        r"""Sets the output_tokens of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 模型输出的 Token 数。 **取值范围：** 无。任务未执行过时为 null。

        :param output_tokens: The output_tokens of this CreateOpsAnalysisTaskResponse.
        :type output_tokens: int
        """
        self._output_tokens = output_tokens

    @property
    def total_session_count(self):
        r"""Gets the total_session_count of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 分析覆盖的session总数。 **取值范围：** 无。

        :return: The total_session_count of this CreateOpsAnalysisTaskResponse.
        :rtype: int
        """
        return self._total_session_count

    @total_session_count.setter
    def total_session_count(self, total_session_count):
        r"""Sets the total_session_count of this CreateOpsAnalysisTaskResponse.

        **参数解释：** 分析覆盖的session总数。 **取值范围：** 无。

        :param total_session_count: The total_session_count of this CreateOpsAnalysisTaskResponse.
        :type total_session_count: int
        """
        self._total_session_count = total_session_count

    def to_dict(self):
        import warnings
        warnings.warn("CreateOpsAnalysisTaskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateOpsAnalysisTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
