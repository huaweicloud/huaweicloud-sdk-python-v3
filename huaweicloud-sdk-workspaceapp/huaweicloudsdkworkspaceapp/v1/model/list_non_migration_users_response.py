# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNonMigrationUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'non_migrate_users': 'list[UserInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'non_migrate_users': 'non_migrate_users'
    }

    def __init__(self, total_count=None, non_migrate_users=None):
        r"""ListNonMigrationUsersResponse

        The model defined in huaweicloud sdk

        :param total_count: 热点时不迁移用户id总数量。
        :type total_count: int
        :param non_migrate_users: 热点时不迁移用户id列表。
        :type non_migrate_users: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        
        super().__init__()

        self._total_count = None
        self._non_migrate_users = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if non_migrate_users is not None:
            self.non_migrate_users = non_migrate_users

    @property
    def total_count(self):
        r"""Gets the total_count of this ListNonMigrationUsersResponse.

        热点时不迁移用户id总数量。

        :return: The total_count of this ListNonMigrationUsersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListNonMigrationUsersResponse.

        热点时不迁移用户id总数量。

        :param total_count: The total_count of this ListNonMigrationUsersResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def non_migrate_users(self):
        r"""Gets the non_migrate_users of this ListNonMigrationUsersResponse.

        热点时不迁移用户id列表。

        :return: The non_migrate_users of this ListNonMigrationUsersResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        return self._non_migrate_users

    @non_migrate_users.setter
    def non_migrate_users(self, non_migrate_users):
        r"""Sets the non_migrate_users of this ListNonMigrationUsersResponse.

        热点时不迁移用户id列表。

        :param non_migrate_users: The non_migrate_users of this ListNonMigrationUsersResponse.
        :type non_migrate_users: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        self._non_migrate_users = non_migrate_users

    def to_dict(self):
        import warnings
        warnings.warn("ListNonMigrationUsersResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListNonMigrationUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
