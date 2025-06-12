# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkspacesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspaces': 'list[CreateWorkspaceResponseBody]',
        'count': 'float'
    }

    attribute_map = {
        'workspaces': 'workspaces',
        'count': 'count'
    }

    def __init__(self, workspaces=None, count=None):
        r"""ListWorkspacesResponse

        The model defined in huaweicloud sdk

        :param workspaces: list of informations of workspaces
        :type workspaces: list[:class:`huaweicloudsdksecmaster.v2.CreateWorkspaceResponseBody`]
        :param count: 数据总量
        :type count: float
        """
        
        super(ListWorkspacesResponse, self).__init__()

        self._workspaces = None
        self._count = None
        self.discriminator = None

        if workspaces is not None:
            self.workspaces = workspaces
        if count is not None:
            self.count = count

    @property
    def workspaces(self):
        r"""Gets the workspaces of this ListWorkspacesResponse.

        list of informations of workspaces

        :return: The workspaces of this ListWorkspacesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CreateWorkspaceResponseBody`]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        r"""Sets the workspaces of this ListWorkspacesResponse.

        list of informations of workspaces

        :param workspaces: The workspaces of this ListWorkspacesResponse.
        :type workspaces: list[:class:`huaweicloudsdksecmaster.v2.CreateWorkspaceResponseBody`]
        """
        self._workspaces = workspaces

    @property
    def count(self):
        r"""Gets the count of this ListWorkspacesResponse.

        数据总量

        :return: The count of this ListWorkspacesResponse.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListWorkspacesResponse.

        数据总量

        :param count: The count of this ListWorkspacesResponse.
        :type count: float
        """
        self._count = count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListWorkspacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
