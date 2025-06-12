# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoriesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latest': 'str',
        'repositories': 'list[str]'
    }

    attribute_map = {
        'latest': 'latest',
        'repositories': 'repositories'
    }

    def __init__(self, latest=None, repositories=None):
        r"""RepositoriesResult

        The model defined in huaweicloud sdk

        :param latest: 最后一次仓库名称
        :type latest: str
        :param repositories: 本次任务的构建步骤详情，返回的步骤为页面可见步骤
        :type repositories: list[str]
        """
        
        

        self._latest = None
        self._repositories = None
        self.discriminator = None

        if latest is not None:
            self.latest = latest
        if repositories is not None:
            self.repositories = repositories

    @property
    def latest(self):
        r"""Gets the latest of this RepositoriesResult.

        最后一次仓库名称

        :return: The latest of this RepositoriesResult.
        :rtype: str
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        r"""Sets the latest of this RepositoriesResult.

        最后一次仓库名称

        :param latest: The latest of this RepositoriesResult.
        :type latest: str
        """
        self._latest = latest

    @property
    def repositories(self):
        r"""Gets the repositories of this RepositoriesResult.

        本次任务的构建步骤详情，返回的步骤为页面可见步骤

        :return: The repositories of this RepositoriesResult.
        :rtype: list[str]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        r"""Sets the repositories of this RepositoriesResult.

        本次任务的构建步骤详情，返回的步骤为页面可见步骤

        :param repositories: The repositories of this RepositoriesResult.
        :type repositories: list[str]
        """
        self._repositories = repositories

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
        if not isinstance(other, RepositoriesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
