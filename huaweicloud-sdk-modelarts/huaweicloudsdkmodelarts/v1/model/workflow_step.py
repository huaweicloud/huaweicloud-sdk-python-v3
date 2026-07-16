# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowStep:

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
        'type': 'str',
        'inputs': 'list[JobInput]',
        'outputs': 'list[JobOutput]',
        'created_at': 'str',
        'title': 'str',
        'description': 'str',
        'properties': 'dict(str, object)',
        'depend_steps': 'list[str]',
        'conditions': 'list[StepCondition]',
        'if_then_steps': 'list[str]',
        'else_then_steps': 'list[str]',
        'policy': 'WorkflowStepPolicy'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'created_at': 'created_at',
        'title': 'title',
        'description': 'description',
        'properties': 'properties',
        'depend_steps': 'depend_steps',
        'conditions': 'conditions',
        'if_then_steps': 'if_then_steps',
        'else_then_steps': 'else_then_steps',
        'policy': 'policy'
    }

    def __init__(self, name=None, type=None, inputs=None, outputs=None, created_at=None, title=None, description=None, properties=None, depend_steps=None, conditions=None, if_then_steps=None, else_then_steps=None, policy=None):
        r"""WorkflowStep

        The model defined in huaweicloud sdk

        :param name: Workflow工作流节点的名称，在一个DAG中唯一，1到64位只包含中英文，数字，空格，下划线（_）和中划线（-），并且以中英文开头。
        :type name: str
        :param type: 节点的类型，枚举值如下: - job 训练 - labeling 标注 - release_dataset 数据集发布 - model 模型发布 - service 服务部署 - mrs_job MRS作业 - dataset_import 数据集导入 - create_dataset 创建数据集
        :type type: str
        :param inputs: 节点的输入项。
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.JobInput`]
        :param outputs: 节点的输出项。
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.JobOutput`]
        :param created_at: 节点的创建时间。
        :type created_at: str
        :param title: 工作流节点标题。
        :type title: str
        :param description: 节点的描述信息。
        :type description: str
        :param properties: 节点属性。
        :type properties: dict(str, object)
        :param depend_steps: 运行依赖的前置节点。
        :type depend_steps: list[str]
        :param conditions: 节点执行条件。
        :type conditions: list[:class:`huaweicloudsdkmodelarts.v1.StepCondition`]
        :param if_then_steps: 条件节点分支。
        :type if_then_steps: list[str]
        :param else_then_steps: 条件节点另一分支。
        :type else_then_steps: list[str]
        :param policy: 
        :type policy: :class:`huaweicloudsdkmodelarts.v1.WorkflowStepPolicy`
        """
        
        

        self._name = None
        self._type = None
        self._inputs = None
        self._outputs = None
        self._created_at = None
        self._title = None
        self._description = None
        self._properties = None
        self._depend_steps = None
        self._conditions = None
        self._if_then_steps = None
        self._else_then_steps = None
        self._policy = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if created_at is not None:
            self.created_at = created_at
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties
        if depend_steps is not None:
            self.depend_steps = depend_steps
        if conditions is not None:
            self.conditions = conditions
        if if_then_steps is not None:
            self.if_then_steps = if_then_steps
        if else_then_steps is not None:
            self.else_then_steps = else_then_steps
        if policy is not None:
            self.policy = policy

    @property
    def name(self):
        r"""Gets the name of this WorkflowStep.

        Workflow工作流节点的名称，在一个DAG中唯一，1到64位只包含中英文，数字，空格，下划线（_）和中划线（-），并且以中英文开头。

        :return: The name of this WorkflowStep.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkflowStep.

        Workflow工作流节点的名称，在一个DAG中唯一，1到64位只包含中英文，数字，空格，下划线（_）和中划线（-），并且以中英文开头。

        :param name: The name of this WorkflowStep.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this WorkflowStep.

        节点的类型，枚举值如下: - job 训练 - labeling 标注 - release_dataset 数据集发布 - model 模型发布 - service 服务部署 - mrs_job MRS作业 - dataset_import 数据集导入 - create_dataset 创建数据集

        :return: The type of this WorkflowStep.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkflowStep.

        节点的类型，枚举值如下: - job 训练 - labeling 标注 - release_dataset 数据集发布 - model 模型发布 - service 服务部署 - mrs_job MRS作业 - dataset_import 数据集导入 - create_dataset 创建数据集

        :param type: The type of this WorkflowStep.
        :type type: str
        """
        self._type = type

    @property
    def inputs(self):
        r"""Gets the inputs of this WorkflowStep.

        节点的输入项。

        :return: The inputs of this WorkflowStep.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobInput`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this WorkflowStep.

        节点的输入项。

        :param inputs: The inputs of this WorkflowStep.
        :type inputs: list[:class:`huaweicloudsdkmodelarts.v1.JobInput`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this WorkflowStep.

        节点的输出项。

        :return: The outputs of this WorkflowStep.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobOutput`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this WorkflowStep.

        节点的输出项。

        :param outputs: The outputs of this WorkflowStep.
        :type outputs: list[:class:`huaweicloudsdkmodelarts.v1.JobOutput`]
        """
        self._outputs = outputs

    @property
    def created_at(self):
        r"""Gets the created_at of this WorkflowStep.

        节点的创建时间。

        :return: The created_at of this WorkflowStep.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this WorkflowStep.

        节点的创建时间。

        :param created_at: The created_at of this WorkflowStep.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def title(self):
        r"""Gets the title of this WorkflowStep.

        工作流节点标题。

        :return: The title of this WorkflowStep.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this WorkflowStep.

        工作流节点标题。

        :param title: The title of this WorkflowStep.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this WorkflowStep.

        节点的描述信息。

        :return: The description of this WorkflowStep.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkflowStep.

        节点的描述信息。

        :param description: The description of this WorkflowStep.
        :type description: str
        """
        self._description = description

    @property
    def properties(self):
        r"""Gets the properties of this WorkflowStep.

        节点属性。

        :return: The properties of this WorkflowStep.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this WorkflowStep.

        节点属性。

        :param properties: The properties of this WorkflowStep.
        :type properties: dict(str, object)
        """
        self._properties = properties

    @property
    def depend_steps(self):
        r"""Gets the depend_steps of this WorkflowStep.

        运行依赖的前置节点。

        :return: The depend_steps of this WorkflowStep.
        :rtype: list[str]
        """
        return self._depend_steps

    @depend_steps.setter
    def depend_steps(self, depend_steps):
        r"""Sets the depend_steps of this WorkflowStep.

        运行依赖的前置节点。

        :param depend_steps: The depend_steps of this WorkflowStep.
        :type depend_steps: list[str]
        """
        self._depend_steps = depend_steps

    @property
    def conditions(self):
        r"""Gets the conditions of this WorkflowStep.

        节点执行条件。

        :return: The conditions of this WorkflowStep.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.StepCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this WorkflowStep.

        节点执行条件。

        :param conditions: The conditions of this WorkflowStep.
        :type conditions: list[:class:`huaweicloudsdkmodelarts.v1.StepCondition`]
        """
        self._conditions = conditions

    @property
    def if_then_steps(self):
        r"""Gets the if_then_steps of this WorkflowStep.

        条件节点分支。

        :return: The if_then_steps of this WorkflowStep.
        :rtype: list[str]
        """
        return self._if_then_steps

    @if_then_steps.setter
    def if_then_steps(self, if_then_steps):
        r"""Sets the if_then_steps of this WorkflowStep.

        条件节点分支。

        :param if_then_steps: The if_then_steps of this WorkflowStep.
        :type if_then_steps: list[str]
        """
        self._if_then_steps = if_then_steps

    @property
    def else_then_steps(self):
        r"""Gets the else_then_steps of this WorkflowStep.

        条件节点另一分支。

        :return: The else_then_steps of this WorkflowStep.
        :rtype: list[str]
        """
        return self._else_then_steps

    @else_then_steps.setter
    def else_then_steps(self, else_then_steps):
        r"""Sets the else_then_steps of this WorkflowStep.

        条件节点另一分支。

        :param else_then_steps: The else_then_steps of this WorkflowStep.
        :type else_then_steps: list[str]
        """
        self._else_then_steps = else_then_steps

    @property
    def policy(self):
        r"""Gets the policy of this WorkflowStep.

        :return: The policy of this WorkflowStep.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowStepPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this WorkflowStep.

        :param policy: The policy of this WorkflowStep.
        :type policy: :class:`huaweicloudsdkmodelarts.v1.WorkflowStepPolicy`
        """
        self._policy = policy

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
        if not isinstance(other, WorkflowStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
