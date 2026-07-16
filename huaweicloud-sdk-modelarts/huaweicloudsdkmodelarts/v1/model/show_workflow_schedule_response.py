# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowScheduleResponse(SdkResponse):

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
        'content': 'dict(str, object)',
        'action': 'str',
        'workflow_id': 'str',
        'user_id': 'str',
        'enable': 'bool',
        'uuid': 'str',
        'policies': 'WorkflowSchedulePolicies',
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
        r"""ShowWorkflowScheduleResponse

        The model defined in huaweicloud sdk

        :param type: 类型，仅支持time（时间）。
        :type type: str
        :param content: 内容。
        :type content: dict(str, object)
        :param action: 动作，仅支持run。
        :type action: str
        :param workflow_id: Workflow工作流ID。
        :type workflow_id: str
        :param user_id: 用户ID。
        :type user_id: str
        :param enable: 定时调度信息，使能标记。
        :type enable: bool
        :param uuid: ID标记。
        :type uuid: str
        :param policies: 
        :type policies: :class:`huaweicloudsdkmodelarts.v1.WorkflowSchedulePolicies`
        :param created_at: 创建时间。
        :type created_at: str
        """
        
        super().__init__()

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
        r"""Gets the type of this ShowWorkflowScheduleResponse.

        类型，仅支持time（时间）。

        :return: The type of this ShowWorkflowScheduleResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowWorkflowScheduleResponse.

        类型，仅支持time（时间）。

        :param type: The type of this ShowWorkflowScheduleResponse.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this ShowWorkflowScheduleResponse.

        内容。

        :return: The content of this ShowWorkflowScheduleResponse.
        :rtype: dict(str, object)
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowWorkflowScheduleResponse.

        内容。

        :param content: The content of this ShowWorkflowScheduleResponse.
        :type content: dict(str, object)
        """
        self._content = content

    @property
    def action(self):
        r"""Gets the action of this ShowWorkflowScheduleResponse.

        动作，仅支持run。

        :return: The action of this ShowWorkflowScheduleResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ShowWorkflowScheduleResponse.

        动作，仅支持run。

        :param action: The action of this ShowWorkflowScheduleResponse.
        :type action: str
        """
        self._action = action

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ShowWorkflowScheduleResponse.

        Workflow工作流ID。

        :return: The workflow_id of this ShowWorkflowScheduleResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ShowWorkflowScheduleResponse.

        Workflow工作流ID。

        :param workflow_id: The workflow_id of this ShowWorkflowScheduleResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowWorkflowScheduleResponse.

        用户ID。

        :return: The user_id of this ShowWorkflowScheduleResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowWorkflowScheduleResponse.

        用户ID。

        :param user_id: The user_id of this ShowWorkflowScheduleResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def enable(self):
        r"""Gets the enable of this ShowWorkflowScheduleResponse.

        定时调度信息，使能标记。

        :return: The enable of this ShowWorkflowScheduleResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ShowWorkflowScheduleResponse.

        定时调度信息，使能标记。

        :param enable: The enable of this ShowWorkflowScheduleResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def uuid(self):
        r"""Gets the uuid of this ShowWorkflowScheduleResponse.

        ID标记。

        :return: The uuid of this ShowWorkflowScheduleResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this ShowWorkflowScheduleResponse.

        ID标记。

        :param uuid: The uuid of this ShowWorkflowScheduleResponse.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def policies(self):
        r"""Gets the policies of this ShowWorkflowScheduleResponse.

        :return: The policies of this ShowWorkflowScheduleResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowSchedulePolicies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ShowWorkflowScheduleResponse.

        :param policies: The policies of this ShowWorkflowScheduleResponse.
        :type policies: :class:`huaweicloudsdkmodelarts.v1.WorkflowSchedulePolicies`
        """
        self._policies = policies

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowWorkflowScheduleResponse.

        创建时间。

        :return: The created_at of this ShowWorkflowScheduleResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowWorkflowScheduleResponse.

        创建时间。

        :param created_at: The created_at of this ShowWorkflowScheduleResponse.
        :type created_at: str
        """
        self._created_at = created_at

    def to_dict(self):
        import warnings
        warnings.warn("ShowWorkflowScheduleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowWorkflowScheduleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
