# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectResponse(SdkResponse):

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
        'projects': 'list[ProjectRsp]'
    }

    attribute_map = {
        'count': 'count',
        'projects': 'projects'
    }

    def __init__(self, count=None, projects=None):
        r"""ListProjectResponse

        The model defined in huaweicloud sdk

        :param count: 个数
        :type count: int
        :param projects: 项目详情列表
        :type projects: list[:class:`huaweicloudsdkeihealth.v1.ProjectRsp`]
        """
        
        super(ListProjectResponse, self).__init__()

        self._count = None
        self._projects = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if projects is not None:
            self.projects = projects

    @property
    def count(self):
        r"""Gets the count of this ListProjectResponse.

        个数

        :return: The count of this ListProjectResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListProjectResponse.

        个数

        :param count: The count of this ListProjectResponse.
        :type count: int
        """
        self._count = count

    @property
    def projects(self):
        r"""Gets the projects of this ListProjectResponse.

        项目详情列表

        :return: The projects of this ListProjectResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ProjectRsp`]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        r"""Sets the projects of this ListProjectResponse.

        项目详情列表

        :param projects: The projects of this ListProjectResponse.
        :type projects: list[:class:`huaweicloudsdkeihealth.v1.ProjectRsp`]
        """
        self._projects = projects

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
        if not isinstance(other, ListProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
