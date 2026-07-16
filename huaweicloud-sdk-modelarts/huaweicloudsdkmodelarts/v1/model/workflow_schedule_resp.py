# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowScheduleResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'content': 'dict(str, str)',
        'action': 'str',
        'workflow_id': 'str',
        'user_id': 'str',
        'enable': 'bool',
        'uuid': 'str',
        'policies': 'WorkflowSchedulePoliciesResp',
        'created_at': 'str'
    }

    attribute_map = {
        'type': 'type',
        'content': 'content',
        'action': 'action',
        'workflow_id': 'workflow_id',
        'user_id': 'user_id',
        'enable': 'enable',
        'uuid': 'uuid',
        'policies': 'policies',
        'created_at': 'created_at'
    }

    def __init__(self, type=None, content=None, action=None, workflow_id=None, user_id=None, enable=None, uuid=None, policies=None, created_at=None):
        r"""WorkflowScheduleResp

        The model defined in huaweicloud sdk

        :param type: **参数解释**：类型，仅支持time（时间）。 **取值范围**：不涉及。
        :type type: str
        :param content: **参数解释**：内容。
        :type content: dict(str, str)
        :param action: **参数解释**：动作，仅支持run。 **取值范围**：不涉及。
        :type action: str
        :param workflow_id: **参数解释**：Workflow工作流ID。 **取值范围**：不涉及。
        :type workflow_id: str
        :param user_id: **参数解释**：用户ID。 **取值范围**：不涉及。
        :type user_id: str
        :param enable: **参数解释**：定时调度信息，使能标记。 **取值范围**： - true：生效 - false：不生效
        :type enable: bool
        :param uuid: **参数解释**：ID标记。 **取值范围**：不涉及。
        :type uuid: str
        :param policies: 
        :type policies: :class:`huaweicloudsdkmodelarts.v1.WorkflowSchedulePoliciesResp`
        :param created_at: **参数解释**：创建时间。 **取值范围**：不涉及。
        :type created_at: str
        """
        
        

        self._type = None
        self._content = None
        self._action = None
        self._workflow_id = None
        self._user_id = None
        self._enable = None
        self._uuid = None
        self._policies = None
        self._created_at = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if content is not None:
            self.content = content
        if action is not None:
            self.action = action
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if user_id is not None:
            self.user_id = user_id
        if enable is not None:
            self.enable = enable
        if uuid is not None:
            self.uuid = uuid
        if policies is not None:
            self.policies = policies
        if created_at is not None:
            self.created_at = created_at

    @property
    def type(self):
        r"""Gets the type of this WorkflowScheduleResp.

        **参数解释**：类型，仅支持time（时间）。 **取值范围**：不涉及。

        :return: The type of this WorkflowScheduleResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkflowScheduleResp.

        **参数解释**：类型，仅支持time（时间）。 **取值范围**：不涉及。

        :param type: The type of this WorkflowScheduleResp.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this WorkflowScheduleResp.

        **参数解释**：内容。

        :return: The content of this WorkflowScheduleResp.
        :rtype: dict(str, str)
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this WorkflowScheduleResp.

        **参数解释**：内容。

        :param content: The content of this WorkflowScheduleResp.
        :type content: dict(str, str)
        """
        self._content = content

    @property
    def action(self):
        r"""Gets the action of this WorkflowScheduleResp.

        **参数解释**：动作，仅支持run。 **取值范围**：不涉及。

        :return: The action of this WorkflowScheduleResp.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this WorkflowScheduleResp.

        **参数解释**：动作，仅支持run。 **取值范围**：不涉及。

        :param action: The action of this WorkflowScheduleResp.
        :type action: str
        """
        self._action = action

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this WorkflowScheduleResp.

        **参数解释**：Workflow工作流ID。 **取值范围**：不涉及。

        :return: The workflow_id of this WorkflowScheduleResp.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this WorkflowScheduleResp.

        **参数解释**：Workflow工作流ID。 **取值范围**：不涉及。

        :param workflow_id: The workflow_id of this WorkflowScheduleResp.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def user_id(self):
        r"""Gets the user_id of this WorkflowScheduleResp.

        **参数解释**：用户ID。 **取值范围**：不涉及。

        :return: The user_id of this WorkflowScheduleResp.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this WorkflowScheduleResp.

        **参数解释**：用户ID。 **取值范围**：不涉及。

        :param user_id: The user_id of this WorkflowScheduleResp.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def enable(self):
        r"""Gets the enable of this WorkflowScheduleResp.

        **参数解释**：定时调度信息，使能标记。 **取值范围**： - true：生效 - false：不生效

        :return: The enable of this WorkflowScheduleResp.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this WorkflowScheduleResp.

        **参数解释**：定时调度信息，使能标记。 **取值范围**： - true：生效 - false：不生效

        :param enable: The enable of this WorkflowScheduleResp.
        :type enable: bool
        """
        self._enable = enable

    @property
    def uuid(self):
        r"""Gets the uuid of this WorkflowScheduleResp.

        **参数解释**：ID标记。 **取值范围**：不涉及。

        :return: The uuid of this WorkflowScheduleResp.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this WorkflowScheduleResp.

        **参数解释**：ID标记。 **取值范围**：不涉及。

        :param uuid: The uuid of this WorkflowScheduleResp.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def policies(self):
        r"""Gets the policies of this WorkflowScheduleResp.

        :return: The policies of this WorkflowScheduleResp.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowSchedulePoliciesResp`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this WorkflowScheduleResp.

        :param policies: The policies of this WorkflowScheduleResp.
        :type policies: :class:`huaweicloudsdkmodelarts.v1.WorkflowSchedulePoliciesResp`
        """
        self._policies = policies

    @property
    def created_at(self):
        r"""Gets the created_at of this WorkflowScheduleResp.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :return: The created_at of this WorkflowScheduleResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this WorkflowScheduleResp.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :param created_at: The created_at of this WorkflowScheduleResp.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, WorkflowScheduleResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
