# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserMigrationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_migrate_user': 'bool',
        'is_set_password': 'bool',
        'password': 'str',
        'user_list': 'list[UserMigrationList]',
        'role_list': 'list[UserMigrationRole]'
    }

    attribute_map = {
        'is_migrate_user': 'is_migrate_user',
        'is_set_password': 'is_set_password',
        'password': 'password',
        'user_list': 'user_list',
        'role_list': 'role_list'
    }

    def __init__(self, is_migrate_user=None, is_set_password=None, password=None, user_list=None, role_list=None):
        """UserMigrationInfo

        The model defined in huaweicloud sdk

        :param is_migrate_user: 是否迁移用户。
        :type is_migrate_user: bool
        :param is_set_password: 是否统一重置密码。取值： - true：重置密码为统一密码。 - false：不统一重置密码。 当前支持的场景：  - 实时迁移场景：MySQL迁移。
        :type is_set_password: bool
        :param password: 重置后的统一密码。统一重置密码为true时必填。 约束：密码不能为空。
        :type password: str
        :param user_list: 
        :type user_list: list[:class:`huaweicloudsdkdrs.v5.UserMigrationList`]
        :param role_list: 
        :type role_list: list[:class:`huaweicloudsdkdrs.v5.UserMigrationRole`]
        """
        
        

        self._is_migrate_user = None
        self._is_set_password = None
        self._password = None
        self._user_list = None
        self._role_list = None
        self.discriminator = None

        self.is_migrate_user = is_migrate_user
        self.is_set_password = is_set_password
        if password is not None:
            self.password = password
        if user_list is not None:
            self.user_list = user_list
        if role_list is not None:
            self.role_list = role_list

    @property
    def is_migrate_user(self):
        """Gets the is_migrate_user of this UserMigrationInfo.

        是否迁移用户。

        :return: The is_migrate_user of this UserMigrationInfo.
        :rtype: bool
        """
        return self._is_migrate_user

    @is_migrate_user.setter
    def is_migrate_user(self, is_migrate_user):
        """Sets the is_migrate_user of this UserMigrationInfo.

        是否迁移用户。

        :param is_migrate_user: The is_migrate_user of this UserMigrationInfo.
        :type is_migrate_user: bool
        """
        self._is_migrate_user = is_migrate_user

    @property
    def is_set_password(self):
        """Gets the is_set_password of this UserMigrationInfo.

        是否统一重置密码。取值： - true：重置密码为统一密码。 - false：不统一重置密码。 当前支持的场景：  - 实时迁移场景：MySQL迁移。

        :return: The is_set_password of this UserMigrationInfo.
        :rtype: bool
        """
        return self._is_set_password

    @is_set_password.setter
    def is_set_password(self, is_set_password):
        """Sets the is_set_password of this UserMigrationInfo.

        是否统一重置密码。取值： - true：重置密码为统一密码。 - false：不统一重置密码。 当前支持的场景：  - 实时迁移场景：MySQL迁移。

        :param is_set_password: The is_set_password of this UserMigrationInfo.
        :type is_set_password: bool
        """
        self._is_set_password = is_set_password

    @property
    def password(self):
        """Gets the password of this UserMigrationInfo.

        重置后的统一密码。统一重置密码为true时必填。 约束：密码不能为空。

        :return: The password of this UserMigrationInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserMigrationInfo.

        重置后的统一密码。统一重置密码为true时必填。 约束：密码不能为空。

        :param password: The password of this UserMigrationInfo.
        :type password: str
        """
        self._password = password

    @property
    def user_list(self):
        """Gets the user_list of this UserMigrationInfo.

        :return: The user_list of this UserMigrationInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.UserMigrationList`]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        """Sets the user_list of this UserMigrationInfo.

        :param user_list: The user_list of this UserMigrationInfo.
        :type user_list: list[:class:`huaweicloudsdkdrs.v5.UserMigrationList`]
        """
        self._user_list = user_list

    @property
    def role_list(self):
        """Gets the role_list of this UserMigrationInfo.

        :return: The role_list of this UserMigrationInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.UserMigrationRole`]
        """
        return self._role_list

    @role_list.setter
    def role_list(self, role_list):
        """Sets the role_list of this UserMigrationInfo.

        :param role_list: The role_list of this UserMigrationInfo.
        :type role_list: list[:class:`huaweicloudsdkdrs.v5.UserMigrationRole`]
        """
        self._role_list = role_list

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
        if not isinstance(other, UserMigrationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
