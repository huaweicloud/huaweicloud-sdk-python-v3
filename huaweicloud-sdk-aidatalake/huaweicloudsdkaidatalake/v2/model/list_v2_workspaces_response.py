# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2WorkspacesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'workspaces': 'list[Workspace]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'workspaces': 'workspaces',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total=None, workspaces=None, x_request_id=None):
        r"""ListV2WorkspacesResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：总记录数。 **取值范围**：不涉及。 
        :type total: int
        :param workspaces: **参数解释**：工作空间列表，每个元素为一个Workspace对象，包含工作空间ID、名称、描述、创建时间等信息。 
        :type workspaces: list[:class:`huaweicloudsdkaidatalake.v2.Workspace`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._total = None
        self._workspaces = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if workspaces is not None:
            self.workspaces = workspaces
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ListV2WorkspacesResponse.

        **参数解释**：总记录数。 **取值范围**：不涉及。 

        :return: The total of this ListV2WorkspacesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2WorkspacesResponse.

        **参数解释**：总记录数。 **取值范围**：不涉及。 

        :param total: The total of this ListV2WorkspacesResponse.
        :type total: int
        """
        self._total = total

    @property
    def workspaces(self):
        r"""Gets the workspaces of this ListV2WorkspacesResponse.

        **参数解释**：工作空间列表，每个元素为一个Workspace对象，包含工作空间ID、名称、描述、创建时间等信息。 

        :return: The workspaces of this ListV2WorkspacesResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.Workspace`]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        r"""Sets the workspaces of this ListV2WorkspacesResponse.

        **参数解释**：工作空间列表，每个元素为一个Workspace对象，包含工作空间ID、名称、描述、创建时间等信息。 

        :param workspaces: The workspaces of this ListV2WorkspacesResponse.
        :type workspaces: list[:class:`huaweicloudsdkaidatalake.v2.Workspace`]
        """
        self._workspaces = workspaces

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListV2WorkspacesResponse.

        :return: The x_request_id of this ListV2WorkspacesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListV2WorkspacesResponse.

        :param x_request_id: The x_request_id of this ListV2WorkspacesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListV2WorkspacesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2WorkspacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
