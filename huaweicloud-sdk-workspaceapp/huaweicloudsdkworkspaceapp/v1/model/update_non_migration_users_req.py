# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNonMigrationUsersReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_type': 'UpdateUserEnum',
        'non_migrate_users': 'list[UserInfo]'
    }

    attribute_map = {
        'update_type': 'update_type',
        'non_migrate_users': 'non_migrate_users'
    }

    def __init__(self, update_type=None, non_migrate_users=None):
        r"""UpdateNonMigrationUsersReq

        The model defined in huaweicloud sdk

        :param update_type: 
        :type update_type: :class:`huaweicloudsdkworkspaceapp.v1.UpdateUserEnum`
        :param non_migrate_users: 热点时不迁移用户id列表。
        :type non_migrate_users: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        
        

        self._update_type = None
        self._non_migrate_users = None
        self.discriminator = None

        self.update_type = update_type
        self.non_migrate_users = non_migrate_users

    @property
    def update_type(self):
        r"""Gets the update_type of this UpdateNonMigrationUsersReq.

        :return: The update_type of this UpdateNonMigrationUsersReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpdateUserEnum`
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        r"""Sets the update_type of this UpdateNonMigrationUsersReq.

        :param update_type: The update_type of this UpdateNonMigrationUsersReq.
        :type update_type: :class:`huaweicloudsdkworkspaceapp.v1.UpdateUserEnum`
        """
        self._update_type = update_type

    @property
    def non_migrate_users(self):
        r"""Gets the non_migrate_users of this UpdateNonMigrationUsersReq.

        热点时不迁移用户id列表。

        :return: The non_migrate_users of this UpdateNonMigrationUsersReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        return self._non_migrate_users

    @non_migrate_users.setter
    def non_migrate_users(self, non_migrate_users):
        r"""Sets the non_migrate_users of this UpdateNonMigrationUsersReq.

        热点时不迁移用户id列表。

        :param non_migrate_users: The non_migrate_users of this UpdateNonMigrationUsersReq.
        :type non_migrate_users: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        self._non_migrate_users = non_migrate_users

    def to_dict(self):
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
        if not isinstance(other, UpdateNonMigrationUsersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
