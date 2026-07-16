# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkspaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'count': 'int',
        'workspaces': 'list[WorkspaceResponse]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'count': 'count',
        'workspaces': 'workspaces'
    }

    def __init__(self, total_count=None, count=None, workspaces=None):
        r"""ListWorkspaceResponse

        The model defined in huaweicloud sdk

        :param total_count: 工作空间的总数。
        :type total_count: int
        :param count: 此次请求返回的工作空间个数。
        :type count: int
        :param workspaces: workspace属性列表。
        :type workspaces: list[:class:`huaweicloudsdkmodelarts.v1.WorkspaceResponse`]
        """
        
        super().__init__()

        self._total_count = None
        self._count = None
        self._workspaces = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if count is not None:
            self.count = count
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def total_count(self):
        r"""Gets the total_count of this ListWorkspaceResponse.

        工作空间的总数。

        :return: The total_count of this ListWorkspaceResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListWorkspaceResponse.

        工作空间的总数。

        :param total_count: The total_count of this ListWorkspaceResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def count(self):
        r"""Gets the count of this ListWorkspaceResponse.

        此次请求返回的工作空间个数。

        :return: The count of this ListWorkspaceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListWorkspaceResponse.

        此次请求返回的工作空间个数。

        :param count: The count of this ListWorkspaceResponse.
        :type count: int
        """
        self._count = count

    @property
    def workspaces(self):
        r"""Gets the workspaces of this ListWorkspaceResponse.

        workspace属性列表。

        :return: The workspaces of this ListWorkspaceResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkspaceResponse`]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        r"""Sets the workspaces of this ListWorkspaceResponse.

        workspace属性列表。

        :param workspaces: The workspaces of this ListWorkspaceResponse.
        :type workspaces: list[:class:`huaweicloudsdkmodelarts.v1.WorkspaceResponse`]
        """
        self._workspaces = workspaces

    def to_dict(self):
        import warnings
        warnings.warn("ListWorkspaceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListWorkspaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
