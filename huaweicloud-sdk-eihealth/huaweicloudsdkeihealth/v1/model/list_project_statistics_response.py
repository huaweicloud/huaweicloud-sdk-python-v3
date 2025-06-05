# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'projects': 'list[ProjectStatistic]',
        'count': 'int'
    }

    attribute_map = {
        'projects': 'projects',
        'count': 'count'
    }

    def __init__(self, projects=None, count=None):
        r"""ListProjectStatisticsResponse

        The model defined in huaweicloud sdk

        :param projects: 空间统计信息。
        :type projects: list[:class:`huaweicloudsdkeihealth.v1.ProjectStatistic`]
        :param count: 空间总数。
        :type count: int
        """
        
        super(ListProjectStatisticsResponse, self).__init__()

        self._projects = None
        self._count = None
        self.discriminator = None

        if projects is not None:
            self.projects = projects
        if count is not None:
            self.count = count

    @property
    def projects(self):
        r"""Gets the projects of this ListProjectStatisticsResponse.

        空间统计信息。

        :return: The projects of this ListProjectStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ProjectStatistic`]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        r"""Sets the projects of this ListProjectStatisticsResponse.

        空间统计信息。

        :param projects: The projects of this ListProjectStatisticsResponse.
        :type projects: list[:class:`huaweicloudsdkeihealth.v1.ProjectStatistic`]
        """
        self._projects = projects

    @property
    def count(self):
        r"""Gets the count of this ListProjectStatisticsResponse.

        空间总数。

        :return: The count of this ListProjectStatisticsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListProjectStatisticsResponse.

        空间总数。

        :param count: The count of this ListProjectStatisticsResponse.
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
        if not isinstance(other, ListProjectStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
