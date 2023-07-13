# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectsV4Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'projects': 'list[ProjectV3]',
        'count': 'int'
    }

    attribute_map = {
        'projects': 'projects',
        'count': 'count'
    }

    def __init__(self, projects=None, count=None):
        """ListProjectsV4Response

        The model defined in huaweicloud sdk

        :param projects: 项目列表
        :type projects: list[:class:`huaweicloudsdkdevstar.v1.ProjectV3`]
        :param count: 总数
        :type count: int
        """
        
        super(ListProjectsV4Response, self).__init__()

        self._projects = None
        self._count = None
        self.discriminator = None

        if projects is not None:
            self.projects = projects
        if count is not None:
            self.count = count

    @property
    def projects(self):
        """Gets the projects of this ListProjectsV4Response.

        项目列表

        :return: The projects of this ListProjectsV4Response.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.ProjectV3`]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ListProjectsV4Response.

        项目列表

        :param projects: The projects of this ListProjectsV4Response.
        :type projects: list[:class:`huaweicloudsdkdevstar.v1.ProjectV3`]
        """
        self._projects = projects

    @property
    def count(self):
        """Gets the count of this ListProjectsV4Response.

        总数

        :return: The count of this ListProjectsV4Response.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListProjectsV4Response.

        总数

        :param count: The count of this ListProjectsV4Response.
        :type count: int
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
        if not isinstance(other, ListProjectsV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
