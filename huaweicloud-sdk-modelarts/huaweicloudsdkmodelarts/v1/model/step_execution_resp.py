# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepExecutionResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step_name': 'str',
        'execution_name': 'str',
        'name': 'str',
        'uuid': 'str',
        'execution_uuid': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'duration': 'int',
        'type': 'str',
        'instance_id': 'str',
        'status': 'str',
        'inputs': 'list[JobInputResp]',
        'outputs': 'list[JobOutputResp]',
        'step_uuid': 'str',
        'properties': 'dict(str, str)',
        'events': 'list[str]',
        'error_info': 'WorkflowErrorInfoResp',
        'policy': 'WorkflowStepExecutionPolicyResp',
        'conditions_execution': 'WorkflowConditionExecutionResp',
        'step_title': 'str',
        'conditions': 'list[StepConditionResp]'
    }

    attribute_map = {
        'step_name': 'step_name',
        'execution_name': 'execution_name',
        'name': 'name',
        'uuid': 'uuid',
        'execution_uuid': 'execution_uuid',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'duration': 'duration',
        'type': 'type',
        'instance_id': 'instance_id',
        'status': 'status',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'step_uuid': 'step_uuid',
        'properties': 'properties',
        'events': 'events',
        'error_info': 'error_info',
        'policy': 'policy',
        'conditions_execution': 'conditions_execution',
        'step_title': 'step_title',
        'conditions': 'conditions'
    }

    def __init__(self, step_name=None, execution_name=None, name=None, uuid=None, execution_uuid=None, created_at=None, updated_at=None, duration=None, type=None, instance_id=None, status=None, inputs=None, outputs=None, step_uuid=None, properties=None, events=None, error_info=None, policy=None, conditions_execution=None, step_title=None, conditions=None):
        r"""StepExecutionResp

        The model defined in huaweicloud sdk

        :param step_name: **参数解释**：节点的名称，在一个DAG中唯一。 **取值范围**：不涉及。
        :type step_name: str
        :param execution_name: **参数解释**：执行记录的名称。 **取值范围**：不涉及。
        :type execution_name: str
        :param name: **参数解释**：执行记录与节点的组合名称。 **取值范围**：不涉及。
        :type name: str
        :param uuid: **参数解释**：唯一标识uuid。创建节点执行时，后台自动生成。 **取值范围**：不涉及。
        :type uuid: str
        :param execution_uuid: **参数解释**：执行记录的UUID。 **取值范围**：不涉及。
        :type execution_uuid: str
        :param created_at: **参数解释**：Execution执行的创建时间。 **取值范围**：不涉及。
        :type created_at: str
        :param updated_at: **参数解释**：Execution执行的更新时间。 **取值范围**：不涉及。
        :type updated_at: str
        :param duration: **参数解释**：Execution执行的运行时长。 **取值范围**：不涉及。
        :type duration: int
        :param type: **参数解释**：节点的类型。 **取值范围**：枚举值如下: - job：训练 - labeling：标注 - release_dataset：数据集发布 - model：模型发布 - service：服务部署 - mrs_job：MRS作业 - dataset_import：数据集导入 - create_dataset：创建数据集
        :type type: str
        :param instance_id: **参数解释**：实例ID。 **取值范围**：不涉及。
        :type instance_id: str
        :param status: **参数解释**：节点的状态。 **取值范围**：枚举值如下： - init：初始化 - wait_inputs：等待输入 - pending：等待 - creating：创建中 - created：创建成功 - create_failed：创建失败 - running：运行中 - stopping：停止中 - stopped：停止 - timeout：超时 - completed：完成 - failed：失败 - hold：暂停 - skipped：跳过
        :type status: str
        :param inputs: **参数解释**：节点的输入项。
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.JobInputResp`]
        :param outputs: **参数解释**：节点的输出项。
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.JobOutputResp`]
        :param step_uuid: **参数解释**：节点的UUID，唯一性标识。 **取值范围**：不涉及。
        :type step_uuid: str
        :param properties: **参数解释**：节点的属性。
        :type properties: dict(str, str)
        :param events: **参数解释**：节点发生的事件。
        :type events: list[str]
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmodelarts.v1.WorkflowErrorInfoResp`
        :param policy: 
        :type policy: :class:`huaweicloudsdkmodelarts.v1.WorkflowStepExecutionPolicyResp`
        :param conditions_execution: 
        :type conditions_execution: :class:`huaweicloudsdkmodelarts.v1.WorkflowConditionExecutionResp`
        :param step_title: **参数解释**：节点标题。 **取值范围**：不涉及。
        :type step_title: str
        :param conditions: **参数解释**：条件节点执行条件。
        :type conditions: list[:class:`huaweicloudsdkmodelarts.v1.StepConditionResp`]
        """
        
        

        self._step_name = None
        self._execution_name = None
        self._name = None
        self._uuid = None
        self._execution_uuid = None
        self._created_at = None
        self._updated_at = None
        self._duration = None
        self._type = None
        self._instance_id = None
        self._status = None
        self._inputs = None
        self._outputs = None
        self._step_uuid = None
        self._properties = None
        self._events = None
        self._error_info = None
        self._policy = None
        self._conditions_execution = None
        self._step_title = None
        self._conditions = None
        self.discriminator = None

        if step_name is not None:
            self.step_name = step_name
        if execution_name is not None:
            self.execution_name = execution_name
        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if execution_uuid is not None:
            self.execution_uuid = execution_uuid
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if duration is not None:
            self.duration = duration
        if type is not None:
            self.type = type
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if step_uuid is not None:
            self.step_uuid = step_uuid
        if properties is not None:
            self.properties = properties
        if events is not None:
            self.events = events
        if error_info is not None:
            self.error_info = error_info
        if policy is not None:
            self.policy = policy
        if conditions_execution is not None:
            self.conditions_execution = conditions_execution
        if step_title is not None:
            self.step_title = step_title
        if conditions is not None:
            self.conditions = conditions

    @property
    def step_name(self):
        r"""Gets the step_name of this StepExecutionResp.

        **参数解释**：节点的名称，在一个DAG中唯一。 **取值范围**：不涉及。

        :return: The step_name of this StepExecutionResp.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        r"""Sets the step_name of this StepExecutionResp.

        **参数解释**：节点的名称，在一个DAG中唯一。 **取值范围**：不涉及。

        :param step_name: The step_name of this StepExecutionResp.
        :type step_name: str
        """
        self._step_name = step_name

    @property
    def execution_name(self):
        r"""Gets the execution_name of this StepExecutionResp.

        **参数解释**：执行记录的名称。 **取值范围**：不涉及。

        :return: The execution_name of this StepExecutionResp.
        :rtype: str
        """
        return self._execution_name

    @execution_name.setter
    def execution_name(self, execution_name):
        r"""Sets the execution_name of this StepExecutionResp.

        **参数解释**：执行记录的名称。 **取值范围**：不涉及。

        :param execution_name: The execution_name of this StepExecutionResp.
        :type execution_name: str
        """
        self._execution_name = execution_name

    @property
    def name(self):
        r"""Gets the name of this StepExecutionResp.

        **参数解释**：执行记录与节点的组合名称。 **取值范围**：不涉及。

        :return: The name of this StepExecutionResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StepExecutionResp.

        **参数解释**：执行记录与节点的组合名称。 **取值范围**：不涉及。

        :param name: The name of this StepExecutionResp.
        :type name: str
        """
        self._name = name

    @property
    def uuid(self):
        r"""Gets the uuid of this StepExecutionResp.

        **参数解释**：唯一标识uuid。创建节点执行时，后台自动生成。 **取值范围**：不涉及。

        :return: The uuid of this StepExecutionResp.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this StepExecutionResp.

        **参数解释**：唯一标识uuid。创建节点执行时，后台自动生成。 **取值范围**：不涉及。

        :param uuid: The uuid of this StepExecutionResp.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def execution_uuid(self):
        r"""Gets the execution_uuid of this StepExecutionResp.

        **参数解释**：执行记录的UUID。 **取值范围**：不涉及。

        :return: The execution_uuid of this StepExecutionResp.
        :rtype: str
        """
        return self._execution_uuid

    @execution_uuid.setter
    def execution_uuid(self, execution_uuid):
        r"""Sets the execution_uuid of this StepExecutionResp.

        **参数解释**：执行记录的UUID。 **取值范围**：不涉及。

        :param execution_uuid: The execution_uuid of this StepExecutionResp.
        :type execution_uuid: str
        """
        self._execution_uuid = execution_uuid

    @property
    def created_at(self):
        r"""Gets the created_at of this StepExecutionResp.

        **参数解释**：Execution执行的创建时间。 **取值范围**：不涉及。

        :return: The created_at of this StepExecutionResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this StepExecutionResp.

        **参数解释**：Execution执行的创建时间。 **取值范围**：不涉及。

        :param created_at: The created_at of this StepExecutionResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this StepExecutionResp.

        **参数解释**：Execution执行的更新时间。 **取值范围**：不涉及。

        :return: The updated_at of this StepExecutionResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this StepExecutionResp.

        **参数解释**：Execution执行的更新时间。 **取值范围**：不涉及。

        :param updated_at: The updated_at of this StepExecutionResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def duration(self):
        r"""Gets the duration of this StepExecutionResp.

        **参数解释**：Execution执行的运行时长。 **取值范围**：不涉及。

        :return: The duration of this StepExecutionResp.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this StepExecutionResp.

        **参数解释**：Execution执行的运行时长。 **取值范围**：不涉及。

        :param duration: The duration of this StepExecutionResp.
        :type duration: int
        """
        self._duration = duration

    @property
    def type(self):
        r"""Gets the type of this StepExecutionResp.

        **参数解释**：节点的类型。 **取值范围**：枚举值如下: - job：训练 - labeling：标注 - release_dataset：数据集发布 - model：模型发布 - service：服务部署 - mrs_job：MRS作业 - dataset_import：数据集导入 - create_dataset：创建数据集

        :return: The type of this StepExecutionResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StepExecutionResp.

        **参数解释**：节点的类型。 **取值范围**：枚举值如下: - job：训练 - labeling：标注 - release_dataset：数据集发布 - model：模型发布 - service：服务部署 - mrs_job：MRS作业 - dataset_import：数据集导入 - create_dataset：创建数据集

        :param type: The type of this StepExecutionResp.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this StepExecutionResp.

        **参数解释**：实例ID。 **取值范围**：不涉及。

        :return: The instance_id of this StepExecutionResp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this StepExecutionResp.

        **参数解释**：实例ID。 **取值范围**：不涉及。

        :param instance_id: The instance_id of this StepExecutionResp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this StepExecutionResp.

        **参数解释**：节点的状态。 **取值范围**：枚举值如下： - init：初始化 - wait_inputs：等待输入 - pending：等待 - creating：创建中 - created：创建成功 - create_failed：创建失败 - running：运行中 - stopping：停止中 - stopped：停止 - timeout：超时 - completed：完成 - failed：失败 - hold：暂停 - skipped：跳过

        :return: The status of this StepExecutionResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StepExecutionResp.

        **参数解释**：节点的状态。 **取值范围**：枚举值如下： - init：初始化 - wait_inputs：等待输入 - pending：等待 - creating：创建中 - created：创建成功 - create_failed：创建失败 - running：运行中 - stopping：停止中 - stopped：停止 - timeout：超时 - completed：完成 - failed：失败 - hold：暂停 - skipped：跳过

        :param status: The status of this StepExecutionResp.
        :type status: str
        """
        self._status = status

    @property
    def inputs(self):
        r"""Gets the inputs of this StepExecutionResp.

        **参数解释**：节点的输入项。

        :return: The inputs of this StepExecutionResp.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobInputResp`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this StepExecutionResp.

        **参数解释**：节点的输入项。

        :param inputs: The inputs of this StepExecutionResp.
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.JobInputResp`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this StepExecutionResp.

        **参数解释**：节点的输出项。

        :return: The outputs of this StepExecutionResp.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobOutputResp`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this StepExecutionResp.

        **参数解释**：节点的输出项。

        :param outputs: The outputs of this StepExecutionResp.
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.JobOutputResp`]
        """
        self._outputs = outputs

    @property
    def step_uuid(self):
        r"""Gets the step_uuid of this StepExecutionResp.

        **参数解释**：节点的UUID，唯一性标识。 **取值范围**：不涉及。

        :return: The step_uuid of this StepExecutionResp.
        :rtype: str
        """
        return self._step_uuid

    @step_uuid.setter
    def step_uuid(self, step_uuid):
        r"""Sets the step_uuid of this StepExecutionResp.

        **参数解释**：节点的UUID，唯一性标识。 **取值范围**：不涉及。

        :param step_uuid: The step_uuid of this StepExecutionResp.
        :type step_uuid: str
        """
        self._step_uuid = step_uuid

    @property
    def properties(self):
        r"""Gets the properties of this StepExecutionResp.

        **参数解释**：节点的属性。

        :return: The properties of this StepExecutionResp.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this StepExecutionResp.

        **参数解释**：节点的属性。

        :param properties: The properties of this StepExecutionResp.
        :type properties: dict(str, str)
        """
        self._properties = properties

    @property
    def events(self):
        r"""Gets the events of this StepExecutionResp.

        **参数解释**：节点发生的事件。

        :return: The events of this StepExecutionResp.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this StepExecutionResp.

        **参数解释**：节点发生的事件。

        :param events: The events of this StepExecutionResp.
        :type events: list[str]
        """
        self._events = events

    @property
    def error_info(self):
        r"""Gets the error_info of this StepExecutionResp.

        :return: The error_info of this StepExecutionResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowErrorInfoResp`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this StepExecutionResp.

        :param error_info: The error_info of this StepExecutionResp.
        :type error_info: :class:`huaweicloudsdkmodelarts.v1.WorkflowErrorInfoResp`
        """
        self._error_info = error_info

    @property
    def policy(self):
        r"""Gets the policy of this StepExecutionResp.

        :return: The policy of this StepExecutionResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowStepExecutionPolicyResp`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this StepExecutionResp.

        :param policy: The policy of this StepExecutionResp.
        :type policy: :class:`huaweicloudsdkmodelarts.v1.WorkflowStepExecutionPolicyResp`
        """
        self._policy = policy

    @property
    def conditions_execution(self):
        r"""Gets the conditions_execution of this StepExecutionResp.

        :return: The conditions_execution of this StepExecutionResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowConditionExecutionResp`
        """
        return self._conditions_execution

    @conditions_execution.setter
    def conditions_execution(self, conditions_execution):
        r"""Sets the conditions_execution of this StepExecutionResp.

        :param conditions_execution: The conditions_execution of this StepExecutionResp.
        :type conditions_execution: :class:`huaweicloudsdkmodelarts.v1.WorkflowConditionExecutionResp`
        """
        self._conditions_execution = conditions_execution

    @property
    def step_title(self):
        r"""Gets the step_title of this StepExecutionResp.

        **参数解释**：节点标题。 **取值范围**：不涉及。

        :return: The step_title of this StepExecutionResp.
        :rtype: str
        """
        return self._step_title

    @step_title.setter
    def step_title(self, step_title):
        r"""Sets the step_title of this StepExecutionResp.

        **参数解释**：节点标题。 **取值范围**：不涉及。

        :param step_title: The step_title of this StepExecutionResp.
        :type step_title: str
        """
        self._step_title = step_title

    @property
    def conditions(self):
        r"""Gets the conditions of this StepExecutionResp.

        **参数解释**：条件节点执行条件。

        :return: The conditions of this StepExecutionResp.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.StepConditionResp`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this StepExecutionResp.

        **参数解释**：条件节点执行条件。

        :param conditions: The conditions of this StepExecutionResp.
        :type conditions: list[:class:`huaweicloudsdkmodelarts.v1.StepConditionResp`]
        """
        self._conditions = conditions

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
        if not isinstance(other, StepExecutionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
