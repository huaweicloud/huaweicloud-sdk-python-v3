# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrderIdRequest:

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
        'action_type': 'str',
        'workspace_id': 'str',
        'body': 'CreateOrderRequestBody'
    }

    attribute_map = {
        'name': 'name',
        'action_type': 'actionType',
        'workspace_id': 'workspaceId',
        'body': 'body'
    }

    def __init__(self, name=None, action_type=None, workspace_id=None, body=None):
        r"""CreateOrderIdRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释**：资源池ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param action_type: **参数解释**：订单操作类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - toPeriod：按需转包周期，默认值 **默认取值**：不涉及。
        :type action_type: str
        :param workspace_id: **参数解释**：工作空间ID，默认是0。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type workspace_id: str
        :param body: Body of the CreateOrderIdRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.CreateOrderRequestBody`
        """
        
        

        self._name = None
        self._action_type = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.name = name
        if action_type is not None:
            self.action_type = action_type
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def name(self):
        r"""Gets the name of this CreateOrderIdRequest.

        **参数解释**：资源池ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this CreateOrderIdRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOrderIdRequest.

        **参数解释**：资源池ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this CreateOrderIdRequest.
        :type name: str
        """
        self._name = name

    @property
    def action_type(self):
        r"""Gets the action_type of this CreateOrderIdRequest.

        **参数解释**：订单操作类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - toPeriod：按需转包周期，默认值 **默认取值**：不涉及。

        :return: The action_type of this CreateOrderIdRequest.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this CreateOrderIdRequest.

        **参数解释**：订单操作类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - toPeriod：按需转包周期，默认值 **默认取值**：不涉及。

        :param action_type: The action_type of this CreateOrderIdRequest.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateOrderIdRequest.

        **参数解释**：工作空间ID，默认是0。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The workspace_id of this CreateOrderIdRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateOrderIdRequest.

        **参数解释**：工作空间ID，默认是0。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this CreateOrderIdRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this CreateOrderIdRequest.

        :return: The body of this CreateOrderIdRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateOrderRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateOrderIdRequest.

        :param body: The body of this CreateOrderIdRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.CreateOrderRequestBody`
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
        if not isinstance(other, CreateOrderIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
