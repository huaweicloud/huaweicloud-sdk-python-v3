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
        r"""ListWorkspacesResponse

        The model defined in huaweicloud sdk

        :param total: workspace总数
        :type total: int
        :param workspaces: workaspace列表
        :type workspaces: list[:class:`huaweicloudsdkdataartsfabric.v1.Workspace`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListWorkspacesResponse, self).__init__()

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
        r"""Gets the total of this ListWorkspacesResponse.

        workspace总数

        :return: The total of this ListWorkspacesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWorkspacesResponse.

        workspace总数

        :param total: The total of this ListWorkspacesResponse.
        :type total: int
        """
        self._total = total

    @property
    def workspaces(self):
        r"""Gets the workspaces of this ListWorkspacesResponse.

        workaspace列表

        :return: The workspaces of this ListWorkspacesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.Workspace`]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        r"""Sets the workspaces of this ListWorkspacesResponse.

        workaspace列表

        :param workspaces: The workspaces of this ListWorkspacesResponse.
        :type workspaces: list[:class:`huaweicloudsdkdataartsfabric.v1.Workspace`]
        """
        self._workspaces = workspaces

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListWorkspacesResponse.

        :return: The x_request_id of this ListWorkspacesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListWorkspacesResponse.

        :param x_request_id: The x_request_id of this ListWorkspacesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
