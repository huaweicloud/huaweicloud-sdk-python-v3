# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryStatisticsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commit_count': 'int',
        'storage_size': 'float',
        'repository_size': 'float',
        'lfs_objects_size': 'float',
        'tenant_repo_size_limit': 'int'
    }

    attribute_map = {
        'commit_count': 'commit_count',
        'storage_size': 'storage_size',
        'repository_size': 'repository_size',
        'lfs_objects_size': 'lfs_objects_size',
        'tenant_repo_size_limit': 'tenant_repo_size_limit'
    }

    def __init__(self, commit_count=None, storage_size=None, repository_size=None, lfs_objects_size=None, tenant_repo_size_limit=None):
        r"""RepositoryStatisticsDto

        The model defined in huaweicloud sdk

        :param commit_count: **参数解释：** 提交数量。 **约束限制：** 不涉及。
        :type commit_count: int
        :param storage_size: **参数解释：** 存储大小。 **约束限制：** 不涉及。
        :type storage_size: float
        :param repository_size: **参数解释：** 仓库大小。 **约束限制：** 不涉及。
        :type repository_size: float
        :param lfs_objects_size: **参数解释：** LFS对象大小。 **约束限制：** 不涉及。
        :type lfs_objects_size: float
        :param tenant_repo_size_limit: **参数解释：** 租户仓库大小限制。 **约束限制：** 不涉及。
        :type tenant_repo_size_limit: int
        """
        
        

        self._commit_count = None
        self._storage_size = None
        self._repository_size = None
        self._lfs_objects_size = None
        self._tenant_repo_size_limit = None
        self.discriminator = None

        if commit_count is not None:
            self.commit_count = commit_count
        if storage_size is not None:
            self.storage_size = storage_size
        if repository_size is not None:
            self.repository_size = repository_size
        if lfs_objects_size is not None:
            self.lfs_objects_size = lfs_objects_size
        if tenant_repo_size_limit is not None:
            self.tenant_repo_size_limit = tenant_repo_size_limit

    @property
    def commit_count(self):
        r"""Gets the commit_count of this RepositoryStatisticsDto.

        **参数解释：** 提交数量。 **约束限制：** 不涉及。

        :return: The commit_count of this RepositoryStatisticsDto.
        :rtype: int
        """
        return self._commit_count

    @commit_count.setter
    def commit_count(self, commit_count):
        r"""Sets the commit_count of this RepositoryStatisticsDto.

        **参数解释：** 提交数量。 **约束限制：** 不涉及。

        :param commit_count: The commit_count of this RepositoryStatisticsDto.
        :type commit_count: int
        """
        self._commit_count = commit_count

    @property
    def storage_size(self):
        r"""Gets the storage_size of this RepositoryStatisticsDto.

        **参数解释：** 存储大小。 **约束限制：** 不涉及。

        :return: The storage_size of this RepositoryStatisticsDto.
        :rtype: float
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        r"""Sets the storage_size of this RepositoryStatisticsDto.

        **参数解释：** 存储大小。 **约束限制：** 不涉及。

        :param storage_size: The storage_size of this RepositoryStatisticsDto.
        :type storage_size: float
        """
        self._storage_size = storage_size

    @property
    def repository_size(self):
        r"""Gets the repository_size of this RepositoryStatisticsDto.

        **参数解释：** 仓库大小。 **约束限制：** 不涉及。

        :return: The repository_size of this RepositoryStatisticsDto.
        :rtype: float
        """
        return self._repository_size

    @repository_size.setter
    def repository_size(self, repository_size):
        r"""Sets the repository_size of this RepositoryStatisticsDto.

        **参数解释：** 仓库大小。 **约束限制：** 不涉及。

        :param repository_size: The repository_size of this RepositoryStatisticsDto.
        :type repository_size: float
        """
        self._repository_size = repository_size

    @property
    def lfs_objects_size(self):
        r"""Gets the lfs_objects_size of this RepositoryStatisticsDto.

        **参数解释：** LFS对象大小。 **约束限制：** 不涉及。

        :return: The lfs_objects_size of this RepositoryStatisticsDto.
        :rtype: float
        """
        return self._lfs_objects_size

    @lfs_objects_size.setter
    def lfs_objects_size(self, lfs_objects_size):
        r"""Sets the lfs_objects_size of this RepositoryStatisticsDto.

        **参数解释：** LFS对象大小。 **约束限制：** 不涉及。

        :param lfs_objects_size: The lfs_objects_size of this RepositoryStatisticsDto.
        :type lfs_objects_size: float
        """
        self._lfs_objects_size = lfs_objects_size

    @property
    def tenant_repo_size_limit(self):
        r"""Gets the tenant_repo_size_limit of this RepositoryStatisticsDto.

        **参数解释：** 租户仓库大小限制。 **约束限制：** 不涉及。

        :return: The tenant_repo_size_limit of this RepositoryStatisticsDto.
        :rtype: int
        """
        return self._tenant_repo_size_limit

    @tenant_repo_size_limit.setter
    def tenant_repo_size_limit(self, tenant_repo_size_limit):
        r"""Sets the tenant_repo_size_limit of this RepositoryStatisticsDto.

        **参数解释：** 租户仓库大小限制。 **约束限制：** 不涉及。

        :param tenant_repo_size_limit: The tenant_repo_size_limit of this RepositoryStatisticsDto.
        :type tenant_repo_size_limit: int
        """
        self._tenant_repo_size_limit = tenant_repo_size_limit

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
        if not isinstance(other, RepositoryStatisticsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
