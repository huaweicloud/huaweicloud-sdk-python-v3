# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyAopWorkflowVersionInfo:

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
        'status': 'str',
        'taskconfig': 'str',
        'taskflow': 'str',
        'taskflow_type': 'str',
        'aop_type': 'str',
        'input': 'str',
        'output': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'taskconfig': 'taskconfig',
        'taskflow': 'taskflow',
        'taskflow_type': 'taskflow_type',
        'aop_type': 'aop_type',
        'input': 'input',
        'output': 'output'
    }

    def __init__(self, name=None, description=None, status=None, taskconfig=None, taskflow=None, taskflow_type=None, aop_type=None, input=None, output=None):
        r"""ModifyAopWorkflowVersionInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type name: str
        :param description: **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type description: str
        :param status: **参数解释**: 更新流程的动作 - pending_submit 更新流程基础信息 - pending_approval 提交审核 - not_activated 取消激活 - activated 激活流程  **约束限制**: 不涉及         **取值范围**: - pending_submit - pending_approval - not_activated - activated  **默认值**:  pending_submit
        :type status: str
        :param taskconfig: **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type taskconfig: str
        :param taskflow: **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type taskflow: str
        :param taskflow_type: **参数解释**: 流程的类型 **约束限制**: 不涉及         **取值范围**: - JSON  **默认值**:  不涉及
        :type taskflow_type: str
        :param aop_type: **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及
        :type aop_type: str
        :param input: **参数解释**: 流程的输入 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type input: str
        :param output: **参数解释**: 流程的输出 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type output: str
        """
        
        

        self._name = None
        self._description = None
        self._status = None
        self._taskconfig = None
        self._taskflow = None
        self._taskflow_type = None
        self._aop_type = None
        self._input = None
        self._output = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if taskconfig is not None:
            self.taskconfig = taskconfig
        if taskflow is not None:
            self.taskflow = taskflow
        if taskflow_type is not None:
            self.taskflow_type = taskflow_type
        if aop_type is not None:
            self.aop_type = aop_type
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output

    @property
    def name(self):
        r"""Gets the name of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The name of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param name: The name of this ModifyAopWorkflowVersionInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The description of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param description: The description of this ModifyAopWorkflowVersionInfo.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 更新流程的动作 - pending_submit 更新流程基础信息 - pending_approval 提交审核 - not_activated 取消激活 - activated 激活流程  **约束限制**: 不涉及         **取值范围**: - pending_submit - pending_approval - not_activated - activated  **默认值**:  pending_submit

        :return: The status of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 更新流程的动作 - pending_submit 更新流程基础信息 - pending_approval 提交审核 - not_activated 取消激活 - activated 激活流程  **约束限制**: 不涉及         **取值范围**: - pending_submit - pending_approval - not_activated - activated  **默认值**:  pending_submit

        :param status: The status of this ModifyAopWorkflowVersionInfo.
        :type status: str
        """
        self._status = status

    @property
    def taskconfig(self):
        r"""Gets the taskconfig of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The taskconfig of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._taskconfig

    @taskconfig.setter
    def taskconfig(self, taskconfig):
        r"""Sets the taskconfig of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param taskconfig: The taskconfig of this ModifyAopWorkflowVersionInfo.
        :type taskconfig: str
        """
        self._taskconfig = taskconfig

    @property
    def taskflow(self):
        r"""Gets the taskflow of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The taskflow of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._taskflow

    @taskflow.setter
    def taskflow(self, taskflow):
        r"""Sets the taskflow of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param taskflow: The taskflow of this ModifyAopWorkflowVersionInfo.
        :type taskflow: str
        """
        self._taskflow = taskflow

    @property
    def taskflow_type(self):
        r"""Gets the taskflow_type of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的类型 **约束限制**: 不涉及         **取值范围**: - JSON  **默认值**:  不涉及

        :return: The taskflow_type of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._taskflow_type

    @taskflow_type.setter
    def taskflow_type(self, taskflow_type):
        r"""Sets the taskflow_type of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的类型 **约束限制**: 不涉及         **取值范围**: - JSON  **默认值**:  不涉及

        :param taskflow_type: The taskflow_type of this ModifyAopWorkflowVersionInfo.
        :type taskflow_type: str
        """
        self._taskflow_type = taskflow_type

    @property
    def aop_type(self):
        r"""Gets the aop_type of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及

        :return: The aop_type of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._aop_type

    @aop_type.setter
    def aop_type(self, aop_type):
        r"""Sets the aop_type of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及

        :param aop_type: The aop_type of this ModifyAopWorkflowVersionInfo.
        :type aop_type: str
        """
        self._aop_type = aop_type

    @property
    def input(self):
        r"""Gets the input of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的输入 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The input of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的输入 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param input: The input of this ModifyAopWorkflowVersionInfo.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的输出 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The output of this ModifyAopWorkflowVersionInfo.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ModifyAopWorkflowVersionInfo.

        **参数解释**: 流程的输出 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param output: The output of this ModifyAopWorkflowVersionInfo.
        :type output: str
        """
        self._output = output

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
        if not isinstance(other, ModifyAopWorkflowVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
