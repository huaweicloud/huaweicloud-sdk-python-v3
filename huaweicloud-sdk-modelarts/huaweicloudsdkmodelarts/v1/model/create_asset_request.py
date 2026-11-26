# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAssetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_storage_token')

    openapi_types = {
        'workspace_id': 'str',
        'x_storage_token': 'str',
        'body': 'CreateAssetReq'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'x_storage_token': 'X-Storage-Token',
        'body': 'body'
    }

    def __init__(self, workspace_id=None, x_storage_token=None, body=None):
        r"""CreateAssetRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。
        :type workspace_id: str
        :param x_storage_token: **参数解释**： OBS属主租户token。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type x_storage_token: str
        :param body: Body of the CreateAssetRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.CreateAssetReq`
        """
        
        

        self._workspace_id = None
        self._x_storage_token = None
        self._body = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if x_storage_token is not None:
            self.x_storage_token = x_storage_token
        if body is not None:
            self.body = body

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateAssetRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :return: The workspace_id of this CreateAssetRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateAssetRequest.

        工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。

        :param workspace_id: The workspace_id of this CreateAssetRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def x_storage_token(self):
        r"""Gets the x_storage_token of this CreateAssetRequest.

        **参数解释**： OBS属主租户token。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The x_storage_token of this CreateAssetRequest.
        :rtype: str
        """
        return self._x_storage_token

    @x_storage_token.setter
    def x_storage_token(self, x_storage_token):
        r"""Sets the x_storage_token of this CreateAssetRequest.

        **参数解释**： OBS属主租户token。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param x_storage_token: The x_storage_token of this CreateAssetRequest.
        :type x_storage_token: str
        """
        self._x_storage_token = x_storage_token

    @property
    def body(self):
        r"""Gets the body of this CreateAssetRequest.

        :return: The body of this CreateAssetRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreateAssetReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAssetRequest.

        :param body: The body of this CreateAssetRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.CreateAssetReq`
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
        if not isinstance(other, CreateAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
