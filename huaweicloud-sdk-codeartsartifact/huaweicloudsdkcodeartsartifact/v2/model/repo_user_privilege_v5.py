# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoUserPrivilegeV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'domain_id': 'str',
        'user_name': 'str',
        'repo_id': 'str',
        'privilege': 'str',
        'role_id': 'str',
        'role_name': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'domain_id': 'domain_id',
        'user_name': 'user_name',
        'repo_id': 'repo_id',
        'privilege': 'privilege',
        'role_id': 'role_id',
        'role_name': 'role_name'
    }

    def __init__(self, user_id=None, domain_id=None, user_name=None, repo_id=None, privilege=None, role_id=None, role_name=None):
        r"""RepoUserPrivilegeV5

        The model defined in huaweicloud sdk

        :param user_id: **参数解释**: 用户id。 **取值范围**: 不涉及。 
        :type user_id: str
        :param domain_id: **参数解释**: 租户id。 **取值范围**: 不涉及。 
        :type domain_id: str
        :param user_name: **参数解释**: 用户名。 **取值范围**: 不涉及。 
        :type user_name: str
        :param repo_id: **参数解释**: 仓库id。 **取值范围**: 不涉及。 
        :type repo_id: str
        :param privilege: **参数解释**: 权限信息。 **取值范围**: 不涉及。 
        :type privilege: str
        :param role_id: **参数解释**: 角色id。 **取值范围**: 不涉及。 
        :type role_id: str
        :param role_name: **参数解释**: 角色名称。 **取值范围**: 不涉及。 
        :type role_name: str
        """
        
        

        self._user_id = None
        self._domain_id = None
        self._user_name = None
        self._repo_id = None
        self._privilege = None
        self._role_id = None
        self._role_name = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if domain_id is not None:
            self.domain_id = domain_id
        if user_name is not None:
            self.user_name = user_name
        if repo_id is not None:
            self.repo_id = repo_id
        if privilege is not None:
            self.privilege = privilege
        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name

    @property
    def user_id(self):
        r"""Gets the user_id of this RepoUserPrivilegeV5.

        **参数解释**: 用户id。 **取值范围**: 不涉及。 

        :return: The user_id of this RepoUserPrivilegeV5.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this RepoUserPrivilegeV5.

        **参数解释**: 用户id。 **取值范围**: 不涉及。 

        :param user_id: The user_id of this RepoUserPrivilegeV5.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this RepoUserPrivilegeV5.

        **参数解释**: 租户id。 **取值范围**: 不涉及。 

        :return: The domain_id of this RepoUserPrivilegeV5.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this RepoUserPrivilegeV5.

        **参数解释**: 租户id。 **取值范围**: 不涉及。 

        :param domain_id: The domain_id of this RepoUserPrivilegeV5.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def user_name(self):
        r"""Gets the user_name of this RepoUserPrivilegeV5.

        **参数解释**: 用户名。 **取值范围**: 不涉及。 

        :return: The user_name of this RepoUserPrivilegeV5.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RepoUserPrivilegeV5.

        **参数解释**: 用户名。 **取值范围**: 不涉及。 

        :param user_name: The user_name of this RepoUserPrivilegeV5.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def repo_id(self):
        r"""Gets the repo_id of this RepoUserPrivilegeV5.

        **参数解释**: 仓库id。 **取值范围**: 不涉及。 

        :return: The repo_id of this RepoUserPrivilegeV5.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this RepoUserPrivilegeV5.

        **参数解释**: 仓库id。 **取值范围**: 不涉及。 

        :param repo_id: The repo_id of this RepoUserPrivilegeV5.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def privilege(self):
        r"""Gets the privilege of this RepoUserPrivilegeV5.

        **参数解释**: 权限信息。 **取值范围**: 不涉及。 

        :return: The privilege of this RepoUserPrivilegeV5.
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        r"""Sets the privilege of this RepoUserPrivilegeV5.

        **参数解释**: 权限信息。 **取值范围**: 不涉及。 

        :param privilege: The privilege of this RepoUserPrivilegeV5.
        :type privilege: str
        """
        self._privilege = privilege

    @property
    def role_id(self):
        r"""Gets the role_id of this RepoUserPrivilegeV5.

        **参数解释**: 角色id。 **取值范围**: 不涉及。 

        :return: The role_id of this RepoUserPrivilegeV5.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this RepoUserPrivilegeV5.

        **参数解释**: 角色id。 **取值范围**: 不涉及。 

        :param role_id: The role_id of this RepoUserPrivilegeV5.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this RepoUserPrivilegeV5.

        **参数解释**: 角色名称。 **取值范围**: 不涉及。 

        :return: The role_name of this RepoUserPrivilegeV5.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this RepoUserPrivilegeV5.

        **参数解释**: 角色名称。 **取值范围**: 不涉及。 

        :param role_name: The role_name of this RepoUserPrivilegeV5.
        :type role_name: str
        """
        self._role_name = role_name

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
        if not isinstance(other, RepoUserPrivilegeV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
