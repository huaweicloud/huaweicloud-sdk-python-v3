# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowExecution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'name': 'str',
        'execution_id': 'str',
        'description': 'str',
        'status': 'str',
        'workspace_id': 'str',
        'workflow_id': 'str',
        'workflow_name': 'str',
        'scene_id': 'str',
        'scene_name': 'str',
        'steps_execution': 'list[StepExecution]',
        'sub_graphs': 'list[WorkflowSubgraph]',
        'duration': 'str',
        'events': 'list[str]',
        'labels': 'list[str]',
        'data_requirements': 'list[DataRequirement]',
        'parameters': 'list[WorkflowParameter]',
        'policies': 'WorkflowDagPolicies'
    }

    attribute_map = {
        'created_at': 'created_at',
        'name': 'name',
        'execution_id': 'execution_id',
        'description': 'description',
        'status': 'status',
        'workspace_id': 'workspace_id',
        'workflow_id': 'workflow_id',
        'workflow_name': 'workflow_name',
        'scene_id': 'scene_id',
        'scene_name': 'scene_name',
        'steps_execution': 'steps_execution',
        'sub_graphs': 'sub_graphs',
        'duration': 'duration',
        'events': 'events',
        'labels': 'labels',
        'data_requirements': 'data_requirements',
        'parameters': 'parameters',
        'policies': 'policies'
    }

    def __init__(self, created_at=None, name=None, execution_id=None, description=None, status=None, workspace_id=None, workflow_id=None, workflow_name=None, scene_id=None, scene_name=None, steps_execution=None, sub_graphs=None, duration=None, events=None, labels=None, data_requirements=None, parameters=None, policies=None):
        r"""WorkflowExecution

        The model defined in huaweicloud sdk

        :param created_at: 创建时间。
        :type created_at: str
        :param name: 执行记录名称。
        :type name: str
        :param execution_id: 工作流执行ID。
        :type execution_id: str
        :param description: 执行记录描述。
        :type description: str
        :param status: 执行记录状态。
        :type status: str
        :param workspace_id: 工作空间ID。
        :type workspace_id: str
        :param workflow_id: Workflow工作流ID。
        :type workflow_id: str
        :param workflow_name: 工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。
        :type workflow_name: str
        :param scene_id: 自定义场景ID。
        :type scene_id: str
        :param scene_name: 自定义场景名称。
        :type scene_name: str
        :param steps_execution: 执行记录的step。
        :type steps_execution: list[:class:`huaweicloudsdkmodelarts.v1.StepExecution`]
        :param sub_graphs: 子图。
        :type sub_graphs: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowSubgraph`]
        :param duration: 执行的时长。
        :type duration: str
        :param events: 执行的事件。
        :type events: list[str]
        :param labels: 为执行记录设置的标签。
        :type labels: list[str]
        :param data_requirements: 节点steps使用到的数据。
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        :param parameters: 节点steps使用到的参数。
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        :param policies: 
        :type policies: :class:`huaweicloudsdkmodelarts.v1.WorkflowDagPolicies`
        """
        
        

        self._created_at = None
        self._name = None
        self._execution_id = None
        self._description = None
        self._status = None
        self._workspace_id = None
        self._workflow_id = None
        self._workflow_name = None
        self._scene_id = None
        self._scene_name = None
        self._steps_execution = None
        self._sub_graphs = None
        self._duration = None
        self._events = None
        self._labels = None
        self._data_requirements = None
        self._parameters = None
        self._policies = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if execution_id is not None:
            self.execution_id = execution_id
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if scene_id is not None:
            self.scene_id = scene_id
        if scene_name is not None:
            self.scene_name = scene_name
        if steps_execution is not None:
            self.steps_execution = steps_execution
        if sub_graphs is not None:
            self.sub_graphs = sub_graphs
        if duration is not None:
            self.duration = duration
        if events is not None:
            self.events = events
        if labels is not None:
            self.labels = labels
        if data_requirements is not None:
            self.data_requirements = data_requirements
        if parameters is not None:
            self.parameters = parameters
        if policies is not None:
            self.policies = policies

    @property
    def created_at(self):
        r"""Gets the created_at of this WorkflowExecution.

        创建时间。

        :return: The created_at of this WorkflowExecution.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this WorkflowExecution.

        创建时间。

        :param created_at: The created_at of this WorkflowExecution.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def name(self):
        r"""Gets the name of this WorkflowExecution.

        执行记录名称。

        :return: The name of this WorkflowExecution.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkflowExecution.

        执行记录名称。

        :param name: The name of this WorkflowExecution.
        :type name: str
        """
        self._name = name

    @property
    def execution_id(self):
        r"""Gets the execution_id of this WorkflowExecution.

        工作流执行ID。

        :return: The execution_id of this WorkflowExecution.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this WorkflowExecution.

        工作流执行ID。

        :param execution_id: The execution_id of this WorkflowExecution.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def description(self):
        r"""Gets the description of this WorkflowExecution.

        执行记录描述。

        :return: The description of this WorkflowExecution.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkflowExecution.

        执行记录描述。

        :param description: The description of this WorkflowExecution.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this WorkflowExecution.

        执行记录状态。

        :return: The status of this WorkflowExecution.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkflowExecution.

        执行记录状态。

        :param status: The status of this WorkflowExecution.
        :type status: str
        """
        self._status = status

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this WorkflowExecution.

        工作空间ID。

        :return: The workspace_id of this WorkflowExecution.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this WorkflowExecution.

        工作空间ID。

        :param workspace_id: The workspace_id of this WorkflowExecution.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this WorkflowExecution.

        Workflow工作流ID。

        :return: The workflow_id of this WorkflowExecution.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this WorkflowExecution.

        Workflow工作流ID。

        :param workflow_id: The workflow_id of this WorkflowExecution.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def workflow_name(self):
        r"""Gets the workflow_name of this WorkflowExecution.

        工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :return: The workflow_name of this WorkflowExecution.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        r"""Sets the workflow_name of this WorkflowExecution.

        工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :param workflow_name: The workflow_name of this WorkflowExecution.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def scene_id(self):
        r"""Gets the scene_id of this WorkflowExecution.

        自定义场景ID。

        :return: The scene_id of this WorkflowExecution.
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        r"""Sets the scene_id of this WorkflowExecution.

        自定义场景ID。

        :param scene_id: The scene_id of this WorkflowExecution.
        :type scene_id: str
        """
        self._scene_id = scene_id

    @property
    def scene_name(self):
        r"""Gets the scene_name of this WorkflowExecution.

        自定义场景名称。

        :return: The scene_name of this WorkflowExecution.
        :rtype: str
        """
        return self._scene_name

    @scene_name.setter
    def scene_name(self, scene_name):
        r"""Sets the scene_name of this WorkflowExecution.

        自定义场景名称。

        :param scene_name: The scene_name of this WorkflowExecution.
        :type scene_name: str
        """
        self._scene_name = scene_name

    @property
    def steps_execution(self):
        r"""Gets the steps_execution of this WorkflowExecution.

        执行记录的step。

        :return: The steps_execution of this WorkflowExecution.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.StepExecution`]
        """
        return self._steps_execution

    @steps_execution.setter
    def steps_execution(self, steps_execution):
        r"""Sets the steps_execution of this WorkflowExecution.

        执行记录的step。

        :param steps_execution: The steps_execution of this WorkflowExecution.
        :type steps_execution: list[:class:`huaweicloudsdkmodelarts.v1.StepExecution`]
        """
        self._steps_execution = steps_execution

    @property
    def sub_graphs(self):
        r"""Gets the sub_graphs of this WorkflowExecution.

        子图。

        :return: The sub_graphs of this WorkflowExecution.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowSubgraph`]
        """
        return self._sub_graphs

    @sub_graphs.setter
    def sub_graphs(self, sub_graphs):
        r"""Sets the sub_graphs of this WorkflowExecution.

        子图。

        :param sub_graphs: The sub_graphs of this WorkflowExecution.
        :type sub_graphs: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowSubgraph`]
        """
        self._sub_graphs = sub_graphs

    @property
    def duration(self):
        r"""Gets the duration of this WorkflowExecution.

        执行的时长。

        :return: The duration of this WorkflowExecution.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this WorkflowExecution.

        执行的时长。

        :param duration: The duration of this WorkflowExecution.
        :type duration: str
        """
        self._duration = duration

    @property
    def events(self):
        r"""Gets the events of this WorkflowExecution.

        执行的事件。

        :return: The events of this WorkflowExecution.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this WorkflowExecution.

        执行的事件。

        :param events: The events of this WorkflowExecution.
        :type events: list[str]
        """
        self._events = events

    @property
    def labels(self):
        r"""Gets the labels of this WorkflowExecution.

        为执行记录设置的标签。

        :return: The labels of this WorkflowExecution.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this WorkflowExecution.

        为执行记录设置的标签。

        :param labels: The labels of this WorkflowExecution.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def data_requirements(self):
        r"""Gets the data_requirements of this WorkflowExecution.

        节点steps使用到的数据。

        :return: The data_requirements of this WorkflowExecution.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        return self._data_requirements

    @data_requirements.setter
    def data_requirements(self, data_requirements):
        r"""Sets the data_requirements of this WorkflowExecution.

        节点steps使用到的数据。

        :param data_requirements: The data_requirements of this WorkflowExecution.
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        self._data_requirements = data_requirements

    @property
    def parameters(self):
        r"""Gets the parameters of this WorkflowExecution.

        节点steps使用到的参数。

        :return: The parameters of this WorkflowExecution.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this WorkflowExecution.

        节点steps使用到的参数。

        :param parameters: The parameters of this WorkflowExecution.
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        self._parameters = parameters

    @property
    def policies(self):
        r"""Gets the policies of this WorkflowExecution.

        :return: The policies of this WorkflowExecution.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowDagPolicies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this WorkflowExecution.

        :param policies: The policies of this WorkflowExecution.
        :type policies: :class:`huaweicloudsdkmodelarts.v1.WorkflowDagPolicies`
        """
        self._policies = policies

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
        if not isinstance(other, WorkflowExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
