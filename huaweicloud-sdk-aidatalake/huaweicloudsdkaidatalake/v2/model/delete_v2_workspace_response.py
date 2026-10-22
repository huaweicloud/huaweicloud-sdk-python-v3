# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteV2WorkspaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, workspace_id=None, x_request_id=None):
        r"""DeleteV2WorkspaceResponse

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 
        :type workspace_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._workspace_id = None
        self._x_request_id = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this DeleteV2WorkspaceResponse.

        **参数解释**：工作空间ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 

        :return: The workspace_id of this DeleteV2WorkspaceResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this DeleteV2WorkspaceResponse.

        **参数解释**：工作空间ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 

        :param workspace_id: The workspace_id of this DeleteV2WorkspaceResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DeleteV2WorkspaceResponse.

        :return: The x_request_id of this DeleteV2WorkspaceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DeleteV2WorkspaceResponse.

        :param x_request_id: The x_request_id of this DeleteV2WorkspaceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("DeleteV2WorkspaceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteV2WorkspaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
