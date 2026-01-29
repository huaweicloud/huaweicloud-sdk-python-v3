# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AopInstanceUpdateDataPojo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command_type': 'str',
        'task_id': 'str',
        'input_dataobject': 'str'
    }

    attribute_map = {
        'command_type': 'command_type',
        'task_id': 'task_id',
        'input_dataobject': 'input_dataobject'
    }

    def __init__(self, command_type=None, task_id=None, input_dataobject=None):
        r"""AopInstanceUpdateDataPojo

        The model defined in huaweicloud sdk

        :param command_type: **参数解释**: 更新流程实例的指令 - ActionInstanceTerminateCommand 终止流程实例 - ActionInstanceRetryCommand 重试流程实例 - ActionInstanceDebugCommand 更新流程实例的调试结果  **约束限制**: 当command_type&#x3D;ActionInstanceDebugCommand时task_id和inputdataobject是必填参数         **取值范围**: - ActionInstanceTerminateCommand - ActionInstanceRetryCommand - ActionInstanceDebugCommand  **默认值**:  不涉及
        :type command_type: str
        :param task_id: **参数解释**:         更新流程调试实例节点ID **约束限制**: 当command_type&#x3D;ActionInstanceDebugCommand时参数为必填参数        **取值范围**: 不涉及 **默认值**:  不涉及
        :type task_id: str
        :param input_dataobject: **参数解释**: 更新流程调试实例节点参数 **约束限制**: 当command_type&#x3D;ActionInstanceDebugCommand时参数为必填参 **取值范围**: 不涉及 **默认值**:  不涉及
        :type input_dataobject: str
        """
        
        

        self._command_type = None
        self._task_id = None
        self._input_dataobject = None
        self.discriminator = None

        self.command_type = command_type
        if task_id is not None:
            self.task_id = task_id
        if input_dataobject is not None:
            self.input_dataobject = input_dataobject

    @property
    def command_type(self):
        r"""Gets the command_type of this AopInstanceUpdateDataPojo.

        **参数解释**: 更新流程实例的指令 - ActionInstanceTerminateCommand 终止流程实例 - ActionInstanceRetryCommand 重试流程实例 - ActionInstanceDebugCommand 更新流程实例的调试结果  **约束限制**: 当command_type=ActionInstanceDebugCommand时task_id和inputdataobject是必填参数         **取值范围**: - ActionInstanceTerminateCommand - ActionInstanceRetryCommand - ActionInstanceDebugCommand  **默认值**:  不涉及

        :return: The command_type of this AopInstanceUpdateDataPojo.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        r"""Sets the command_type of this AopInstanceUpdateDataPojo.

        **参数解释**: 更新流程实例的指令 - ActionInstanceTerminateCommand 终止流程实例 - ActionInstanceRetryCommand 重试流程实例 - ActionInstanceDebugCommand 更新流程实例的调试结果  **约束限制**: 当command_type=ActionInstanceDebugCommand时task_id和inputdataobject是必填参数         **取值范围**: - ActionInstanceTerminateCommand - ActionInstanceRetryCommand - ActionInstanceDebugCommand  **默认值**:  不涉及

        :param command_type: The command_type of this AopInstanceUpdateDataPojo.
        :type command_type: str
        """
        self._command_type = command_type

    @property
    def task_id(self):
        r"""Gets the task_id of this AopInstanceUpdateDataPojo.

        **参数解释**:         更新流程调试实例节点ID **约束限制**: 当command_type=ActionInstanceDebugCommand时参数为必填参数        **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The task_id of this AopInstanceUpdateDataPojo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this AopInstanceUpdateDataPojo.

        **参数解释**:         更新流程调试实例节点ID **约束限制**: 当command_type=ActionInstanceDebugCommand时参数为必填参数        **取值范围**: 不涉及 **默认值**:  不涉及

        :param task_id: The task_id of this AopInstanceUpdateDataPojo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def input_dataobject(self):
        r"""Gets the input_dataobject of this AopInstanceUpdateDataPojo.

        **参数解释**: 更新流程调试实例节点参数 **约束限制**: 当command_type=ActionInstanceDebugCommand时参数为必填参 **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The input_dataobject of this AopInstanceUpdateDataPojo.
        :rtype: str
        """
        return self._input_dataobject

    @input_dataobject.setter
    def input_dataobject(self, input_dataobject):
        r"""Sets the input_dataobject of this AopInstanceUpdateDataPojo.

        **参数解释**: 更新流程调试实例节点参数 **约束限制**: 当command_type=ActionInstanceDebugCommand时参数为必填参 **取值范围**: 不涉及 **默认值**:  不涉及

        :param input_dataobject: The input_dataobject of this AopInstanceUpdateDataPojo.
        :type input_dataobject: str
        """
        self._input_dataobject = input_dataobject

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
        if not isinstance(other, AopInstanceUpdateDataPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
