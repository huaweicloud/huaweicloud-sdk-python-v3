# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AopInstanceEventData:

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
        'action_type': 'str',
        'action_id': 'str',
        'action_instance_id': 'str',
        'playbook_context': 'PlaybookcontextRef'
    }

    attribute_map = {
        'command_type': 'command_type',
        'action_type': 'action_type',
        'action_id': 'action_id',
        'action_instance_id': 'action_instance_id',
        'playbook_context': 'playbook_context'
    }

    def __init__(self, command_type=None, action_type=None, action_id=None, action_instance_id=None, playbook_context=None):
        r"""AopInstanceEventData

        The model defined in huaweicloud sdk

        :param command_type: **参数解释**: 操作流程实例的指令 - ActionInstanceRunCommand 运行流程实例  **约束限制**: 不涉及         **取值范围**: - ActionInstanceRunCommand  **默认值**:  不涉及
        :type command_type: str
        :param action_type: **参数解释**: action的类型 - workflow 流程  **约束限制**: 不涉及         **取值范围**: - workflow  **默认值**:  不涉及
        :type action_type: str
        :param action_id: **参数解释**: 流程的ID **约束限制**: 不涉及
        :type action_id: str
        :param action_instance_id: **参数解释**: 流程实例的ID **约束限制**: 不涉及
        :type action_instance_id: str
        :param playbook_context: 
        :type playbook_context: :class:`huaweicloudsdksecmaster.v1.PlaybookcontextRef`
        """
        
        

        self._command_type = None
        self._action_type = None
        self._action_id = None
        self._action_instance_id = None
        self._playbook_context = None
        self.discriminator = None

        self.command_type = command_type
        self.action_type = action_type
        if action_id is not None:
            self.action_id = action_id
        if action_instance_id is not None:
            self.action_instance_id = action_instance_id
        if playbook_context is not None:
            self.playbook_context = playbook_context

    @property
    def command_type(self):
        r"""Gets the command_type of this AopInstanceEventData.

        **参数解释**: 操作流程实例的指令 - ActionInstanceRunCommand 运行流程实例  **约束限制**: 不涉及         **取值范围**: - ActionInstanceRunCommand  **默认值**:  不涉及

        :return: The command_type of this AopInstanceEventData.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        r"""Sets the command_type of this AopInstanceEventData.

        **参数解释**: 操作流程实例的指令 - ActionInstanceRunCommand 运行流程实例  **约束限制**: 不涉及         **取值范围**: - ActionInstanceRunCommand  **默认值**:  不涉及

        :param command_type: The command_type of this AopInstanceEventData.
        :type command_type: str
        """
        self._command_type = command_type

    @property
    def action_type(self):
        r"""Gets the action_type of this AopInstanceEventData.

        **参数解释**: action的类型 - workflow 流程  **约束限制**: 不涉及         **取值范围**: - workflow  **默认值**:  不涉及

        :return: The action_type of this AopInstanceEventData.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this AopInstanceEventData.

        **参数解释**: action的类型 - workflow 流程  **约束限制**: 不涉及         **取值范围**: - workflow  **默认值**:  不涉及

        :param action_type: The action_type of this AopInstanceEventData.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def action_id(self):
        r"""Gets the action_id of this AopInstanceEventData.

        **参数解释**: 流程的ID **约束限制**: 不涉及

        :return: The action_id of this AopInstanceEventData.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this AopInstanceEventData.

        **参数解释**: 流程的ID **约束限制**: 不涉及

        :param action_id: The action_id of this AopInstanceEventData.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def action_instance_id(self):
        r"""Gets the action_instance_id of this AopInstanceEventData.

        **参数解释**: 流程实例的ID **约束限制**: 不涉及

        :return: The action_instance_id of this AopInstanceEventData.
        :rtype: str
        """
        return self._action_instance_id

    @action_instance_id.setter
    def action_instance_id(self, action_instance_id):
        r"""Sets the action_instance_id of this AopInstanceEventData.

        **参数解释**: 流程实例的ID **约束限制**: 不涉及

        :param action_instance_id: The action_instance_id of this AopInstanceEventData.
        :type action_instance_id: str
        """
        self._action_instance_id = action_instance_id

    @property
    def playbook_context(self):
        r"""Gets the playbook_context of this AopInstanceEventData.

        :return: The playbook_context of this AopInstanceEventData.
        :rtype: :class:`huaweicloudsdksecmaster.v1.PlaybookcontextRef`
        """
        return self._playbook_context

    @playbook_context.setter
    def playbook_context(self, playbook_context):
        r"""Sets the playbook_context of this AopInstanceEventData.

        :param playbook_context: The playbook_context of this AopInstanceEventData.
        :type playbook_context: :class:`huaweicloudsdksecmaster.v1.PlaybookcontextRef`
        """
        self._playbook_context = playbook_context

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
        if not isinstance(other, AopInstanceEventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
