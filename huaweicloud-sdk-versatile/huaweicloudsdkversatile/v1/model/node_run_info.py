# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeRunInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'node_id': 'str',
        'parent_node_id': 'str',
        'node_status': 'str',
        'parent_workflow_id': 'str',
        'loop_index': 'int',
        'loop_node_id': 'str',
        'status': 'Status',
        'node_name': 'str',
        'node_type': 'str',
        'error_message': 'str',
        'inputs': 'dict(str, object)',
        'outputs': 'dict(str, object)',
        'messages': 'list[Message]',
        'metadata': 'dict(str, object)',
        'start_time': 'int',
        'end_time': 'int',
        'startup_time': 'int',
        'prefill_time': 'int',
        'execution_id': 'str',
        'inner_error': 'NodeRunInfoInnerError',
        'memory': 'dict(str, object)'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'node_id': 'node_id',
        'parent_node_id': 'parent_node_id',
        'node_status': 'node_status',
        'parent_workflow_id': 'parent_workflow_id',
        'loop_index': 'loop_index',
        'loop_node_id': 'loop_node_id',
        'status': 'status',
        'node_name': 'node_name',
        'node_type': 'node_type',
        'error_message': 'error_message',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'messages': 'messages',
        'metadata': 'metadata',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'startup_time': 'startup_time',
        'prefill_time': 'prefill_time',
        'execution_id': 'execution_id',
        'inner_error': 'inner_error',
        'memory': 'memory'
    }

    def __init__(self, agent_id=None, node_id=None, parent_node_id=None, node_status=None, parent_workflow_id=None, loop_index=None, loop_node_id=None, status=None, node_name=None, node_type=None, error_message=None, inputs=None, outputs=None, messages=None, metadata=None, start_time=None, end_time=None, startup_time=None, prefill_time=None, execution_id=None, inner_error=None, memory=None):
        r"""NodeRunInfo

        The model defined in huaweicloud sdk

        :param agent_id: 工作流id
        :type agent_id: str
        :param node_id: 节点id
        :type node_id: str
        :param parent_node_id: 父节点id
        :type parent_node_id: str
        :param node_status: 工作流节点状态
        :type node_status: str
        :param parent_workflow_id: 父工作流节点id
        :type parent_workflow_id: str
        :param loop_index: 循环次数
        :type loop_index: int
        :param loop_node_id: 上层循环节点id
        :type loop_node_id: str
        :param status: 
        :type status: :class:`huaweicloudsdkversatile.v1.Status`
        :param node_name: 节点名称
        :type node_name: str
        :param node_type: 节点类型
        :type node_type: str
        :param error_message: 错误信息
        :type error_message: str
        :param inputs: 输入参数：debug才设置
        :type inputs: dict(str, object)
        :param outputs: 输出参数：debug才设置
        :type outputs: dict(str, object)
        :param messages: 消息节点或提问器节点的输出
        :type messages: list[:class:`huaweicloudsdkversatile.v1.Message`]
        :param metadata: 节点特有的输出，如：大模型原始回复debug才设置
        :type metadata: dict(str, object)
        :param start_time: 开始时间，13位时间戳 workflow_started,node_started必填
        :type start_time: int
        :param end_time: 结束时间，13位时间戳 workflow_finished,node_finished必填
        :type end_time: int
        :param startup_time: 真正启动的时间，13位时间戳
        :type startup_time: int
        :param prefill_time: 预热时间，如大模型节点表示首token时间
        :type prefill_time: int
        :param execution_id: execution id
        :type execution_id: str
        :param inner_error: 
        :type inner_error: :class:`huaweicloudsdkversatile.v1.NodeRunInfoInnerError`
        :param memory: 记忆变量
        :type memory: dict(str, object)
        """
        
        

        self._agent_id = None
        self._node_id = None
        self._parent_node_id = None
        self._node_status = None
        self._parent_workflow_id = None
        self._loop_index = None
        self._loop_node_id = None
        self._status = None
        self._node_name = None
        self._node_type = None
        self._error_message = None
        self._inputs = None
        self._outputs = None
        self._messages = None
        self._metadata = None
        self._start_time = None
        self._end_time = None
        self._startup_time = None
        self._prefill_time = None
        self._execution_id = None
        self._inner_error = None
        self._memory = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if node_id is not None:
            self.node_id = node_id
        if parent_node_id is not None:
            self.parent_node_id = parent_node_id
        if node_status is not None:
            self.node_status = node_status
        if parent_workflow_id is not None:
            self.parent_workflow_id = parent_workflow_id
        if loop_index is not None:
            self.loop_index = loop_index
        if loop_node_id is not None:
            self.loop_node_id = loop_node_id
        if status is not None:
            self.status = status
        if node_name is not None:
            self.node_name = node_name
        if node_type is not None:
            self.node_type = node_type
        if error_message is not None:
            self.error_message = error_message
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if messages is not None:
            self.messages = messages
        if metadata is not None:
            self.metadata = metadata
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if startup_time is not None:
            self.startup_time = startup_time
        if prefill_time is not None:
            self.prefill_time = prefill_time
        if execution_id is not None:
            self.execution_id = execution_id
        if inner_error is not None:
            self.inner_error = inner_error
        if memory is not None:
            self.memory = memory

    @property
    def agent_id(self):
        r"""Gets the agent_id of this NodeRunInfo.

        工作流id

        :return: The agent_id of this NodeRunInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this NodeRunInfo.

        工作流id

        :param agent_id: The agent_id of this NodeRunInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def node_id(self):
        r"""Gets the node_id of this NodeRunInfo.

        节点id

        :return: The node_id of this NodeRunInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this NodeRunInfo.

        节点id

        :param node_id: The node_id of this NodeRunInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def parent_node_id(self):
        r"""Gets the parent_node_id of this NodeRunInfo.

        父节点id

        :return: The parent_node_id of this NodeRunInfo.
        :rtype: str
        """
        return self._parent_node_id

    @parent_node_id.setter
    def parent_node_id(self, parent_node_id):
        r"""Sets the parent_node_id of this NodeRunInfo.

        父节点id

        :param parent_node_id: The parent_node_id of this NodeRunInfo.
        :type parent_node_id: str
        """
        self._parent_node_id = parent_node_id

    @property
    def node_status(self):
        r"""Gets the node_status of this NodeRunInfo.

        工作流节点状态

        :return: The node_status of this NodeRunInfo.
        :rtype: str
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        r"""Sets the node_status of this NodeRunInfo.

        工作流节点状态

        :param node_status: The node_status of this NodeRunInfo.
        :type node_status: str
        """
        self._node_status = node_status

    @property
    def parent_workflow_id(self):
        r"""Gets the parent_workflow_id of this NodeRunInfo.

        父工作流节点id

        :return: The parent_workflow_id of this NodeRunInfo.
        :rtype: str
        """
        return self._parent_workflow_id

    @parent_workflow_id.setter
    def parent_workflow_id(self, parent_workflow_id):
        r"""Sets the parent_workflow_id of this NodeRunInfo.

        父工作流节点id

        :param parent_workflow_id: The parent_workflow_id of this NodeRunInfo.
        :type parent_workflow_id: str
        """
        self._parent_workflow_id = parent_workflow_id

    @property
    def loop_index(self):
        r"""Gets the loop_index of this NodeRunInfo.

        循环次数

        :return: The loop_index of this NodeRunInfo.
        :rtype: int
        """
        return self._loop_index

    @loop_index.setter
    def loop_index(self, loop_index):
        r"""Sets the loop_index of this NodeRunInfo.

        循环次数

        :param loop_index: The loop_index of this NodeRunInfo.
        :type loop_index: int
        """
        self._loop_index = loop_index

    @property
    def loop_node_id(self):
        r"""Gets the loop_node_id of this NodeRunInfo.

        上层循环节点id

        :return: The loop_node_id of this NodeRunInfo.
        :rtype: str
        """
        return self._loop_node_id

    @loop_node_id.setter
    def loop_node_id(self, loop_node_id):
        r"""Sets the loop_node_id of this NodeRunInfo.

        上层循环节点id

        :param loop_node_id: The loop_node_id of this NodeRunInfo.
        :type loop_node_id: str
        """
        self._loop_node_id = loop_node_id

    @property
    def status(self):
        r"""Gets the status of this NodeRunInfo.

        :return: The status of this NodeRunInfo.
        :rtype: :class:`huaweicloudsdkversatile.v1.Status`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodeRunInfo.

        :param status: The status of this NodeRunInfo.
        :type status: :class:`huaweicloudsdkversatile.v1.Status`
        """
        self._status = status

    @property
    def node_name(self):
        r"""Gets the node_name of this NodeRunInfo.

        节点名称

        :return: The node_name of this NodeRunInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this NodeRunInfo.

        节点名称

        :param node_name: The node_name of this NodeRunInfo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_type(self):
        r"""Gets the node_type of this NodeRunInfo.

        节点类型

        :return: The node_type of this NodeRunInfo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this NodeRunInfo.

        节点类型

        :param node_type: The node_type of this NodeRunInfo.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def error_message(self):
        r"""Gets the error_message of this NodeRunInfo.

        错误信息

        :return: The error_message of this NodeRunInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this NodeRunInfo.

        错误信息

        :param error_message: The error_message of this NodeRunInfo.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def inputs(self):
        r"""Gets the inputs of this NodeRunInfo.

        输入参数：debug才设置

        :return: The inputs of this NodeRunInfo.
        :rtype: dict(str, object)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this NodeRunInfo.

        输入参数：debug才设置

        :param inputs: The inputs of this NodeRunInfo.
        :type inputs: dict(str, object)
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this NodeRunInfo.

        输出参数：debug才设置

        :return: The outputs of this NodeRunInfo.
        :rtype: dict(str, object)
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this NodeRunInfo.

        输出参数：debug才设置

        :param outputs: The outputs of this NodeRunInfo.
        :type outputs: dict(str, object)
        """
        self._outputs = outputs

    @property
    def messages(self):
        r"""Gets the messages of this NodeRunInfo.

        消息节点或提问器节点的输出

        :return: The messages of this NodeRunInfo.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        r"""Sets the messages of this NodeRunInfo.

        消息节点或提问器节点的输出

        :param messages: The messages of this NodeRunInfo.
        :type messages: list[:class:`huaweicloudsdkversatile.v1.Message`]
        """
        self._messages = messages

    @property
    def metadata(self):
        r"""Gets the metadata of this NodeRunInfo.

        节点特有的输出，如：大模型原始回复debug才设置

        :return: The metadata of this NodeRunInfo.
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this NodeRunInfo.

        节点特有的输出，如：大模型原始回复debug才设置

        :param metadata: The metadata of this NodeRunInfo.
        :type metadata: dict(str, object)
        """
        self._metadata = metadata

    @property
    def start_time(self):
        r"""Gets the start_time of this NodeRunInfo.

        开始时间，13位时间戳 workflow_started,node_started必填

        :return: The start_time of this NodeRunInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this NodeRunInfo.

        开始时间，13位时间戳 workflow_started,node_started必填

        :param start_time: The start_time of this NodeRunInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this NodeRunInfo.

        结束时间，13位时间戳 workflow_finished,node_finished必填

        :return: The end_time of this NodeRunInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this NodeRunInfo.

        结束时间，13位时间戳 workflow_finished,node_finished必填

        :param end_time: The end_time of this NodeRunInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def startup_time(self):
        r"""Gets the startup_time of this NodeRunInfo.

        真正启动的时间，13位时间戳

        :return: The startup_time of this NodeRunInfo.
        :rtype: int
        """
        return self._startup_time

    @startup_time.setter
    def startup_time(self, startup_time):
        r"""Sets the startup_time of this NodeRunInfo.

        真正启动的时间，13位时间戳

        :param startup_time: The startup_time of this NodeRunInfo.
        :type startup_time: int
        """
        self._startup_time = startup_time

    @property
    def prefill_time(self):
        r"""Gets the prefill_time of this NodeRunInfo.

        预热时间，如大模型节点表示首token时间

        :return: The prefill_time of this NodeRunInfo.
        :rtype: int
        """
        return self._prefill_time

    @prefill_time.setter
    def prefill_time(self, prefill_time):
        r"""Sets the prefill_time of this NodeRunInfo.

        预热时间，如大模型节点表示首token时间

        :param prefill_time: The prefill_time of this NodeRunInfo.
        :type prefill_time: int
        """
        self._prefill_time = prefill_time

    @property
    def execution_id(self):
        r"""Gets the execution_id of this NodeRunInfo.

        execution id

        :return: The execution_id of this NodeRunInfo.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this NodeRunInfo.

        execution id

        :param execution_id: The execution_id of this NodeRunInfo.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def inner_error(self):
        r"""Gets the inner_error of this NodeRunInfo.

        :return: The inner_error of this NodeRunInfo.
        :rtype: :class:`huaweicloudsdkversatile.v1.NodeRunInfoInnerError`
        """
        return self._inner_error

    @inner_error.setter
    def inner_error(self, inner_error):
        r"""Sets the inner_error of this NodeRunInfo.

        :param inner_error: The inner_error of this NodeRunInfo.
        :type inner_error: :class:`huaweicloudsdkversatile.v1.NodeRunInfoInnerError`
        """
        self._inner_error = inner_error

    @property
    def memory(self):
        r"""Gets the memory of this NodeRunInfo.

        记忆变量

        :return: The memory of this NodeRunInfo.
        :rtype: dict(str, object)
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this NodeRunInfo.

        记忆变量

        :param memory: The memory of this NodeRunInfo.
        :type memory: dict(str, object)
        """
        self._memory = memory

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
        if not isinstance(other, NodeRunInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
