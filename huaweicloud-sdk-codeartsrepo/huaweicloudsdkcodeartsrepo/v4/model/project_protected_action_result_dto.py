# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectProtectedActionResultDto:

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
        'levels': 'str',
        'level_names': 'str',
        'users': 'list[UserBasicDto]',
        'user_teams': 'list[UserTeamBasicDto]',
        'roles': 'list[RoleBasicDto]',
        'addition_switchers': 'list[ForceActionEnableDto]'
    }

    attribute_map = {
        'action': 'action',
        'enable': 'enable',
        'levels': 'levels',
        'level_names': 'level_names',
        'users': 'users',
        'user_teams': 'user_teams',
        'roles': 'roles',
        'addition_switchers': 'addition_switchers'
    }

    def __init__(self, action=None, enable=None, levels=None, level_names=None, users=None, user_teams=None, roles=None, addition_switchers=None):
        r"""ProjectProtectedActionResultDto

        The model defined in huaweicloud sdk

        :param action: **参数解释：** 动作。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type action: str
        :param enable: **参数解释：** 是否开启。
        :type enable: bool
        :param levels: **参数解释：** 权限点。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type levels: str
        :param level_names: **参数解释：** 权限名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type level_names: str
        :param users: **参数解释：** 成员列表。
        :type users: list[:class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`]
        :param user_teams: **参数解释：** 成员组列表。
        :type user_teams: list[:class:`huaweicloudsdkcodeartsrepo.v4.UserTeamBasicDto`]
        :param roles: **参数解释：** 角色列表。
        :type roles: list[:class:`huaweicloudsdkcodeartsrepo.v4.RoleBasicDto`]
        :param addition_switchers: **参数解释：** 操作选择列表。
        :type addition_switchers: list[:class:`huaweicloudsdkcodeartsrepo.v4.ForceActionEnableDto`]
        """
        
        

        self._action = None
        self._enable = None
        self._levels = None
        self._level_names = None
        self._users = None
        self._user_teams = None
        self._roles = None
        self._addition_switchers = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if enable is not None:
            self.enable = enable
        if levels is not None:
            self.levels = levels
        if level_names is not None:
            self.level_names = level_names
        if users is not None:
            self.users = users
        if user_teams is not None:
            self.user_teams = user_teams
        if roles is not None:
            self.roles = roles
        if addition_switchers is not None:
            self.addition_switchers = addition_switchers

    @property
    def action(self):
        r"""Gets the action of this ProjectProtectedActionResultDto.

        **参数解释：** 动作。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The action of this ProjectProtectedActionResultDto.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ProjectProtectedActionResultDto.

        **参数解释：** 动作。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param action: The action of this ProjectProtectedActionResultDto.
        :type action: str
        """
        self._action = action

    @property
    def enable(self):
        r"""Gets the enable of this ProjectProtectedActionResultDto.

        **参数解释：** 是否开启。

        :return: The enable of this ProjectProtectedActionResultDto.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ProjectProtectedActionResultDto.

        **参数解释：** 是否开启。

        :param enable: The enable of this ProjectProtectedActionResultDto.
        :type enable: bool
        """
        self._enable = enable

    @property
    def levels(self):
        r"""Gets the levels of this ProjectProtectedActionResultDto.

        **参数解释：** 权限点。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The levels of this ProjectProtectedActionResultDto.
        :rtype: str
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        r"""Sets the levels of this ProjectProtectedActionResultDto.

        **参数解释：** 权限点。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param levels: The levels of this ProjectProtectedActionResultDto.
        :type levels: str
        """
        self._levels = levels

    @property
    def level_names(self):
        r"""Gets the level_names of this ProjectProtectedActionResultDto.

        **参数解释：** 权限名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The level_names of this ProjectProtectedActionResultDto.
        :rtype: str
        """
        return self._level_names

    @level_names.setter
    def level_names(self, level_names):
        r"""Sets the level_names of this ProjectProtectedActionResultDto.

        **参数解释：** 权限名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param level_names: The level_names of this ProjectProtectedActionResultDto.
        :type level_names: str
        """
        self._level_names = level_names

    @property
    def users(self):
        r"""Gets the users of this ProjectProtectedActionResultDto.

        **参数解释：** 成员列表。

        :return: The users of this ProjectProtectedActionResultDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ProjectProtectedActionResultDto.

        **参数解释：** 成员列表。

        :param users: The users of this ProjectProtectedActionResultDto.
        :type users: list[:class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`]
        """
        self._users = users

    @property
    def user_teams(self):
        r"""Gets the user_teams of this ProjectProtectedActionResultDto.

        **参数解释：** 成员组列表。

        :return: The user_teams of this ProjectProtectedActionResultDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.UserTeamBasicDto`]
        """
        return self._user_teams

    @user_teams.setter
    def user_teams(self, user_teams):
        r"""Sets the user_teams of this ProjectProtectedActionResultDto.

        **参数解释：** 成员组列表。

        :param user_teams: The user_teams of this ProjectProtectedActionResultDto.
        :type user_teams: list[:class:`huaweicloudsdkcodeartsrepo.v4.UserTeamBasicDto`]
        """
        self._user_teams = user_teams

    @property
    def roles(self):
        r"""Gets the roles of this ProjectProtectedActionResultDto.

        **参数解释：** 角色列表。

        :return: The roles of this ProjectProtectedActionResultDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.RoleBasicDto`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this ProjectProtectedActionResultDto.

        **参数解释：** 角色列表。

        :param roles: The roles of this ProjectProtectedActionResultDto.
        :type roles: list[:class:`huaweicloudsdkcodeartsrepo.v4.RoleBasicDto`]
        """
        self._roles = roles

    @property
    def addition_switchers(self):
        r"""Gets the addition_switchers of this ProjectProtectedActionResultDto.

        **参数解释：** 操作选择列表。

        :return: The addition_switchers of this ProjectProtectedActionResultDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.ForceActionEnableDto`]
        """
        return self._addition_switchers

    @addition_switchers.setter
    def addition_switchers(self, addition_switchers):
        r"""Sets the addition_switchers of this ProjectProtectedActionResultDto.

        **参数解释：** 操作选择列表。

        :param addition_switchers: The addition_switchers of this ProjectProtectedActionResultDto.
        :type addition_switchers: list[:class:`huaweicloudsdkcodeartsrepo.v4.ForceActionEnableDto`]
        """
        self._addition_switchers = addition_switchers

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
        if not isinstance(other, ProjectProtectedActionResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
