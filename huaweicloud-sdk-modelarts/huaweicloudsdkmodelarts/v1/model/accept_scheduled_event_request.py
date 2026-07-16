# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AcceptScheduledEventRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'workspace_id': 'str',
        'body': 'EventUpdate'
    }

    attribute_map = {
        'event_id': 'event_id',
        'workspace_id': 'workspaceId',
        'body': 'body'
    }

    def __init__(self, event_id=None, workspace_id=None, body=None):
        r"""AcceptScheduledEventRequest

        The model defined in huaweicloud sdk

        :param event_id: **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 **约束限制**：不涉及。 **取值范围**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63 **默认取值**：不涉及。
        :type event_id: str
        :param workspace_id: **参数解释**：工作空间ID，默认值为0，取值于查询workspaces列表的接口的id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type workspace_id: str
        :param body: Body of the AcceptScheduledEventRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.EventUpdate`
        """
        
        

        self._event_id = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.event_id = event_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def event_id(self):
        r"""Gets the event_id of this AcceptScheduledEventRequest.

        **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 **约束限制**：不涉及。 **取值范围**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63 **默认取值**：不涉及。

        :return: The event_id of this AcceptScheduledEventRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this AcceptScheduledEventRequest.

        **参数解释**：计划事件ID，取值查询计划事件列表接口的event_id字段。 **约束限制**：不涉及。 **取值范围**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，长度小于63 **默认取值**：不涉及。

        :param event_id: The event_id of this AcceptScheduledEventRequest.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AcceptScheduledEventRequest.

        **参数解释**：工作空间ID，默认值为0，取值于查询workspaces列表的接口的id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The workspace_id of this AcceptScheduledEventRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AcceptScheduledEventRequest.

        **参数解释**：工作空间ID，默认值为0，取值于查询workspaces列表的接口的id字段。 **约束限制**：系统自动生成，只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度小于63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this AcceptScheduledEventRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this AcceptScheduledEventRequest.

        :return: The body of this AcceptScheduledEventRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.EventUpdate`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AcceptScheduledEventRequest.

        :param body: The body of this AcceptScheduledEventRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.EventUpdate`
        """
        self._body = body

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
        if not isinstance(other, AcceptScheduledEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
