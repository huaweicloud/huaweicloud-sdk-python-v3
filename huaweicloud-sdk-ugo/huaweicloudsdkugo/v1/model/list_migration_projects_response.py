# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMigrationProjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migration_projects': 'list[MigrationProject]',
        'total_count': 'int'
    }

    attribute_map = {
        'migration_projects': 'migration_projects',
        'total_count': 'total_count'
    }

    def __init__(self, migration_projects=None, total_count=None):
        """ListMigrationProjectsResponse

        The model defined in huaweicloud sdk

        :param migration_projects: 当前页的迁移项目列表。
        :type migration_projects: list[:class:`huaweicloudsdkugo.v1.MigrationProject`]
        :param total_count: 迁移项目总数。
        :type total_count: int
        """
        
        super(ListMigrationProjectsResponse, self).__init__()

        self._migration_projects = None
        self._total_count = None
        self.discriminator = None

        if migration_projects is not None:
            self.migration_projects = migration_projects
        if total_count is not None:
            self.total_count = total_count

    @property
    def migration_projects(self):
        """Gets the migration_projects of this ListMigrationProjectsResponse.

        当前页的迁移项目列表。

        :return: The migration_projects of this ListMigrationProjectsResponse.
        :rtype: list[:class:`huaweicloudsdkugo.v1.MigrationProject`]
        """
        return self._migration_projects

    @migration_projects.setter
    def migration_projects(self, migration_projects):
        """Sets the migration_projects of this ListMigrationProjectsResponse.

        当前页的迁移项目列表。

        :param migration_projects: The migration_projects of this ListMigrationProjectsResponse.
        :type migration_projects: list[:class:`huaweicloudsdkugo.v1.MigrationProject`]
        """
        self._migration_projects = migration_projects

    @property
    def total_count(self):
        """Gets the total_count of this ListMigrationProjectsResponse.

        迁移项目总数。

        :return: The total_count of this ListMigrationProjectsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListMigrationProjectsResponse.

        迁移项目总数。

        :param total_count: The total_count of this ListMigrationProjectsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListMigrationProjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
