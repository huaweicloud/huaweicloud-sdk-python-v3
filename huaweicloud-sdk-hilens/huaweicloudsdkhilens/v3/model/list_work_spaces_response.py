# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkSpacesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'workspaces': 'list[WorkspaceListElem]'
    }

    attribute_map = {
        'count': 'count',
        'workspaces': 'workspaces'
    }

    def __init__(self, count=None, workspaces=None):
        """ListWorkSpacesResponse

        The model defined in huaweicloud sdk

        :param count: 返回总条目数
        :type count: int
        :param workspaces: 工作空间列表
        :type workspaces: list[:class:`huaweicloudsdkhilens.v3.WorkspaceListElem`]
        """
        
        super(ListWorkSpacesResponse, self).__init__()

        self._count = None
        self._workspaces = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def count(self):
        """Gets the count of this ListWorkSpacesResponse.

        返回总条目数

        :return: The count of this ListWorkSpacesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListWorkSpacesResponse.

        返回总条目数

        :param count: The count of this ListWorkSpacesResponse.
        :type count: int
        """
        self._count = count

    @property
    def workspaces(self):
        """Gets the workspaces of this ListWorkSpacesResponse.

        工作空间列表

        :return: The workspaces of this ListWorkSpacesResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.WorkspaceListElem`]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this ListWorkSpacesResponse.

        工作空间列表

        :param workspaces: The workspaces of this ListWorkSpacesResponse.
        :type workspaces: list[:class:`huaweicloudsdkhilens.v3.WorkspaceListElem`]
        """
        self._workspaces = workspaces

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
        if not isinstance(other, ListWorkSpacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
