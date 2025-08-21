# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryProtectedActionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'enable': 'bool',
        'users': 'list[RepositoryUserDto]',
        'user_teams': 'list[UserTeamBasicDto]',
        'roles': 'list[BasicRoleDto]'
    }

    attribute_map = {
        'action': 'action',
        'enable': 'enable',
        'users': 'users',
        'user_teams': 'user_teams',
        'roles': 'roles'
    }

    def __init__(self, action=None, enable=None, users=None, user_teams=None, roles=None):
        r"""RepositoryProtectedActionDto

        The model defined in huaweicloud sdk

        :param action: **参数解释：** 事件名称。 **取值范围：** 不涉及。
        :type action: str
        :param enable: **参数解释：** 是否启用。 **取值范围：** - true，开启规则限制。 - false，未开启规则限制。
        :type enable: bool
        :param users: **参数解释：** 白名单用户列表。 **取值范围：** 不涉及。
        :type users: list[:class:`huaweicloudsdkcodehub.v4.RepositoryUserDto`]
        :param user_teams: **参数解释：** 白名单用户组列表。 **取值范围：** 不涉及。
        :type user_teams: list[:class:`huaweicloudsdkcodehub.v4.UserTeamBasicDto`]
        :param roles: **参数解释：** 白名单角色列表。 **取值范围：** 不涉及。
        :type roles: list[:class:`huaweicloudsdkcodehub.v4.BasicRoleDto`]
        """
        
        

        self._action = None
        self._enable = None
        self._users = None
        self._user_teams = None
        self._roles = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if enable is not None:
            self.enable = enable
        if users is not None:
            self.users = users
        if user_teams is not None:
            self.user_teams = user_teams
        if roles is not None:
            self.roles = roles

    @property
    def action(self):
        r"""Gets the action of this RepositoryProtectedActionDto.

        **参数解释：** 事件名称。 **取值范围：** 不涉及。

        :return: The action of this RepositoryProtectedActionDto.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this RepositoryProtectedActionDto.

        **参数解释：** 事件名称。 **取值范围：** 不涉及。

        :param action: The action of this RepositoryProtectedActionDto.
        :type action: str
        """
        self._action = action

    @property
    def enable(self):
        r"""Gets the enable of this RepositoryProtectedActionDto.

        **参数解释：** 是否启用。 **取值范围：** - true，开启规则限制。 - false，未开启规则限制。

        :return: The enable of this RepositoryProtectedActionDto.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this RepositoryProtectedActionDto.

        **参数解释：** 是否启用。 **取值范围：** - true，开启规则限制。 - false，未开启规则限制。

        :param enable: The enable of this RepositoryProtectedActionDto.
        :type enable: bool
        """
        self._enable = enable

    @property
    def users(self):
        r"""Gets the users of this RepositoryProtectedActionDto.

        **参数解释：** 白名单用户列表。 **取值范围：** 不涉及。

        :return: The users of this RepositoryProtectedActionDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.RepositoryUserDto`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this RepositoryProtectedActionDto.

        **参数解释：** 白名单用户列表。 **取值范围：** 不涉及。

        :param users: The users of this RepositoryProtectedActionDto.
        :type users: list[:class:`huaweicloudsdkcodehub.v4.RepositoryUserDto`]
        """
        self._users = users

    @property
    def user_teams(self):
        r"""Gets the user_teams of this RepositoryProtectedActionDto.

        **参数解释：** 白名单用户组列表。 **取值范围：** 不涉及。

        :return: The user_teams of this RepositoryProtectedActionDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserTeamBasicDto`]
        """
        return self._user_teams

    @user_teams.setter
    def user_teams(self, user_teams):
        r"""Sets the user_teams of this RepositoryProtectedActionDto.

        **参数解释：** 白名单用户组列表。 **取值范围：** 不涉及。

        :param user_teams: The user_teams of this RepositoryProtectedActionDto.
        :type user_teams: list[:class:`huaweicloudsdkcodehub.v4.UserTeamBasicDto`]
        """
        self._user_teams = user_teams

    @property
    def roles(self):
        r"""Gets the roles of this RepositoryProtectedActionDto.

        **参数解释：** 白名单角色列表。 **取值范围：** 不涉及。

        :return: The roles of this RepositoryProtectedActionDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.BasicRoleDto`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this RepositoryProtectedActionDto.

        **参数解释：** 白名单角色列表。 **取值范围：** 不涉及。

        :param roles: The roles of this RepositoryProtectedActionDto.
        :type roles: list[:class:`huaweicloudsdkcodehub.v4.BasicRoleDto`]
        """
        self._roles = roles

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
        if not isinstance(other, RepositoryProtectedActionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
