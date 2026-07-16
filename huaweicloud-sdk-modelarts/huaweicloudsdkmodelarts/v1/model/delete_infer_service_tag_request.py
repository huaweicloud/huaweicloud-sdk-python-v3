# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInferServiceTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'workspace_id': 'str',
        'body': 'DeleteInferTmsTagsRequest'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, resource_id=None, workspace_id=None, body=None):
        r"""DeleteInferServiceTagRequest

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释：** 待创建标签的资源ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type resource_id: str
        :param workspace_id: **参数解释：** 工作空间ID，workspaceId将会被设置为null。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type workspace_id: str
        :param body: Body of the DeleteInferServiceTagRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.DeleteInferTmsTagsRequest`
        """
        
        

        self._resource_id = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.resource_id = resource_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def resource_id(self):
        r"""Gets the resource_id of this DeleteInferServiceTagRequest.

        **参数解释：** 待创建标签的资源ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The resource_id of this DeleteInferServiceTagRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this DeleteInferServiceTagRequest.

        **参数解释：** 待创建标签的资源ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param resource_id: The resource_id of this DeleteInferServiceTagRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteInferServiceTagRequest.

        **参数解释：** 工作空间ID，workspaceId将会被设置为null。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The workspace_id of this DeleteInferServiceTagRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteInferServiceTagRequest.

        **参数解释：** 工作空间ID，workspaceId将会被设置为null。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param workspace_id: The workspace_id of this DeleteInferServiceTagRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this DeleteInferServiceTagRequest.

        :return: The body of this DeleteInferServiceTagRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeleteInferTmsTagsRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DeleteInferServiceTagRequest.

        :param body: The body of this DeleteInferServiceTagRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.DeleteInferTmsTagsRequest`
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
        if not isinstance(other, DeleteInferServiceTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
