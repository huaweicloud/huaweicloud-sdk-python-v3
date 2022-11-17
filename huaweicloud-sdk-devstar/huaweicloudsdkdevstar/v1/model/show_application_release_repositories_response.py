# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApplicationReleaseRepositoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'release_repositories': 'list[ReleaseRepository]',
        'count': 'int'
    }

    attribute_map = {
        'release_repositories': 'release_repositories',
        'count': 'count'
    }

    def __init__(self, release_repositories=None, count=None):
        """ShowApplicationReleaseRepositoriesResponse

        The model defined in huaweicloud sdk

        :param release_repositories: 软件包列表
        :type release_repositories: list[:class:`huaweicloudsdkdevstar.v1.ReleaseRepository`]
        :param count: 软件包总条数
        :type count: int
        """
        
        super(ShowApplicationReleaseRepositoriesResponse, self).__init__()

        self._release_repositories = None
        self._count = None
        self.discriminator = None

        if release_repositories is not None:
            self.release_repositories = release_repositories
        if count is not None:
            self.count = count

    @property
    def release_repositories(self):
        """Gets the release_repositories of this ShowApplicationReleaseRepositoriesResponse.

        软件包列表

        :return: The release_repositories of this ShowApplicationReleaseRepositoriesResponse.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.ReleaseRepository`]
        """
        return self._release_repositories

    @release_repositories.setter
    def release_repositories(self, release_repositories):
        """Sets the release_repositories of this ShowApplicationReleaseRepositoriesResponse.

        软件包列表

        :param release_repositories: The release_repositories of this ShowApplicationReleaseRepositoriesResponse.
        :type release_repositories: list[:class:`huaweicloudsdkdevstar.v1.ReleaseRepository`]
        """
        self._release_repositories = release_repositories

    @property
    def count(self):
        """Gets the count of this ShowApplicationReleaseRepositoriesResponse.

        软件包总条数

        :return: The count of this ShowApplicationReleaseRepositoriesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowApplicationReleaseRepositoriesResponse.

        软件包总条数

        :param count: The count of this ShowApplicationReleaseRepositoriesResponse.
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
        if not isinstance(other, ShowApplicationReleaseRepositoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
