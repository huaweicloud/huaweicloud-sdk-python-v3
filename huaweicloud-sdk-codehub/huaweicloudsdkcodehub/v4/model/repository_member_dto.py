# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryMemberDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'int',
        'user_iam_id': 'str',
        'user_name': 'str',
        'user_nick_name': 'str',
        'tenant_name': 'str',
        'tenant_id': 'str',
        'is_repo_creator': 'int',
        'is_group_creator': 'int',
        'is_project_admin': 'int',
        'project_role_name': 'str',
        'repository_role_name': 'str',
        'repository_role_id': 'str',
        'member_source': 'str',
        'member_group_source': 'str',
        'member_source_id': 'str',
        'service_license_status': 'int',
        'action_enabled': 'bool'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_iam_id': 'user_iam_id',
        'user_name': 'user_name',
        'user_nick_name': 'user_nick_name',
        'tenant_name': 'tenant_name',
        'tenant_id': 'tenant_id',
        'is_repo_creator': 'is_repo_creator',
        'is_group_creator': 'is_group_creator',
        'is_project_admin': 'is_Project_admin',
        'project_role_name': 'project_role_name',
        'repository_role_name': 'repository_role_name',
        'repository_role_id': 'repository_role_Id',
        'member_source': 'member_source',
        'member_group_source': 'member_group_source',
        'member_source_id': 'member_source_id',
        'service_license_status': 'service_license_status',
        'action_enabled': 'action_enabled'
    }

    def __init__(self, user_id=None, user_iam_id=None, user_name=None, user_nick_name=None, tenant_name=None, tenant_id=None, is_repo_creator=None, is_group_creator=None, is_project_admin=None, project_role_name=None, repository_role_name=None, repository_role_id=None, member_source=None, member_group_source=None, member_source_id=None, service_license_status=None, action_enabled=None):
        r"""RepositoryMemberDto

        The model defined in huaweicloud sdk

        :param user_id: 用户id
        :type user_id: int
        :param user_iam_id: 用户iamId
        :type user_iam_id: str
        :param user_name: 用户名称
        :type user_name: str
        :param user_nick_name: 用户昵称
        :type user_nick_name: str
        :param tenant_name: 租户名称
        :type tenant_name: str
        :param tenant_id: 租户id
        :type tenant_id: str
        :param is_repo_creator: 是否为仓库所有者
        :type is_repo_creator: int
        :param is_group_creator: 是否为父代码组所有者
        :type is_group_creator: int
        :param is_project_admin: 是否为项目管理员
        :type is_project_admin: int
        :param project_role_name: 项目角色名称
        :type project_role_name: str
        :param repository_role_name: 仓库角色名称
        :type repository_role_name: str
        :param repository_role_id: 仓库角色id
        :type repository_role_id: str
        :param member_source: 成员如果来自成员组，成员组名称
        :type member_source: str
        :param member_group_source: 成员如果来自上层代码组，代码组名称
        :type member_group_source: str
        :param member_source_id: 成员来源id —— 代码组id或者成员组id
        :type member_source_id: str
        :param service_license_status: 成员服务级权限状态： 1-使用中、0-已停用
        :type service_license_status: int
        :param action_enabled: 是否有对应权限： true-有权限、false-无权限
        :type action_enabled: bool
        """
        
        

        self._user_id = None
        self._user_iam_id = None
        self._user_name = None
        self._user_nick_name = None
        self._tenant_name = None
        self._tenant_id = None
        self._is_repo_creator = None
        self._is_group_creator = None
        self._is_project_admin = None
        self._project_role_name = None
        self._repository_role_name = None
        self._repository_role_id = None
        self._member_source = None
        self._member_group_source = None
        self._member_source_id = None
        self._service_license_status = None
        self._action_enabled = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_iam_id is not None:
            self.user_iam_id = user_iam_id
        if user_name is not None:
            self.user_name = user_name
        if user_nick_name is not None:
            self.user_nick_name = user_nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if is_repo_creator is not None:
            self.is_repo_creator = is_repo_creator
        if is_group_creator is not None:
            self.is_group_creator = is_group_creator
        if is_project_admin is not None:
            self.is_project_admin = is_project_admin
        if project_role_name is not None:
            self.project_role_name = project_role_name
        if repository_role_name is not None:
            self.repository_role_name = repository_role_name
        if repository_role_id is not None:
            self.repository_role_id = repository_role_id
        if member_source is not None:
            self.member_source = member_source
        if member_group_source is not None:
            self.member_group_source = member_group_source
        if member_source_id is not None:
            self.member_source_id = member_source_id
        if service_license_status is not None:
            self.service_license_status = service_license_status
        if action_enabled is not None:
            self.action_enabled = action_enabled

    @property
    def user_id(self):
        r"""Gets the user_id of this RepositoryMemberDto.

        用户id

        :return: The user_id of this RepositoryMemberDto.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this RepositoryMemberDto.

        用户id

        :param user_id: The user_id of this RepositoryMemberDto.
        :type user_id: int
        """
        self._user_id = user_id

    @property
    def user_iam_id(self):
        r"""Gets the user_iam_id of this RepositoryMemberDto.

        用户iamId

        :return: The user_iam_id of this RepositoryMemberDto.
        :rtype: str
        """
        return self._user_iam_id

    @user_iam_id.setter
    def user_iam_id(self, user_iam_id):
        r"""Sets the user_iam_id of this RepositoryMemberDto.

        用户iamId

        :param user_iam_id: The user_iam_id of this RepositoryMemberDto.
        :type user_iam_id: str
        """
        self._user_iam_id = user_iam_id

    @property
    def user_name(self):
        r"""Gets the user_name of this RepositoryMemberDto.

        用户名称

        :return: The user_name of this RepositoryMemberDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RepositoryMemberDto.

        用户名称

        :param user_name: The user_name of this RepositoryMemberDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_nick_name(self):
        r"""Gets the user_nick_name of this RepositoryMemberDto.

        用户昵称

        :return: The user_nick_name of this RepositoryMemberDto.
        :rtype: str
        """
        return self._user_nick_name

    @user_nick_name.setter
    def user_nick_name(self, user_nick_name):
        r"""Sets the user_nick_name of this RepositoryMemberDto.

        用户昵称

        :param user_nick_name: The user_nick_name of this RepositoryMemberDto.
        :type user_nick_name: str
        """
        self._user_nick_name = user_nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this RepositoryMemberDto.

        租户名称

        :return: The tenant_name of this RepositoryMemberDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this RepositoryMemberDto.

        租户名称

        :param tenant_name: The tenant_name of this RepositoryMemberDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this RepositoryMemberDto.

        租户id

        :return: The tenant_id of this RepositoryMemberDto.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this RepositoryMemberDto.

        租户id

        :param tenant_id: The tenant_id of this RepositoryMemberDto.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def is_repo_creator(self):
        r"""Gets the is_repo_creator of this RepositoryMemberDto.

        是否为仓库所有者

        :return: The is_repo_creator of this RepositoryMemberDto.
        :rtype: int
        """
        return self._is_repo_creator

    @is_repo_creator.setter
    def is_repo_creator(self, is_repo_creator):
        r"""Sets the is_repo_creator of this RepositoryMemberDto.

        是否为仓库所有者

        :param is_repo_creator: The is_repo_creator of this RepositoryMemberDto.
        :type is_repo_creator: int
        """
        self._is_repo_creator = is_repo_creator

    @property
    def is_group_creator(self):
        r"""Gets the is_group_creator of this RepositoryMemberDto.

        是否为父代码组所有者

        :return: The is_group_creator of this RepositoryMemberDto.
        :rtype: int
        """
        return self._is_group_creator

    @is_group_creator.setter
    def is_group_creator(self, is_group_creator):
        r"""Sets the is_group_creator of this RepositoryMemberDto.

        是否为父代码组所有者

        :param is_group_creator: The is_group_creator of this RepositoryMemberDto.
        :type is_group_creator: int
        """
        self._is_group_creator = is_group_creator

    @property
    def is_project_admin(self):
        r"""Gets the is_project_admin of this RepositoryMemberDto.

        是否为项目管理员

        :return: The is_project_admin of this RepositoryMemberDto.
        :rtype: int
        """
        return self._is_project_admin

    @is_project_admin.setter
    def is_project_admin(self, is_project_admin):
        r"""Sets the is_project_admin of this RepositoryMemberDto.

        是否为项目管理员

        :param is_project_admin: The is_project_admin of this RepositoryMemberDto.
        :type is_project_admin: int
        """
        self._is_project_admin = is_project_admin

    @property
    def project_role_name(self):
        r"""Gets the project_role_name of this RepositoryMemberDto.

        项目角色名称

        :return: The project_role_name of this RepositoryMemberDto.
        :rtype: str
        """
        return self._project_role_name

    @project_role_name.setter
    def project_role_name(self, project_role_name):
        r"""Sets the project_role_name of this RepositoryMemberDto.

        项目角色名称

        :param project_role_name: The project_role_name of this RepositoryMemberDto.
        :type project_role_name: str
        """
        self._project_role_name = project_role_name

    @property
    def repository_role_name(self):
        r"""Gets the repository_role_name of this RepositoryMemberDto.

        仓库角色名称

        :return: The repository_role_name of this RepositoryMemberDto.
        :rtype: str
        """
        return self._repository_role_name

    @repository_role_name.setter
    def repository_role_name(self, repository_role_name):
        r"""Sets the repository_role_name of this RepositoryMemberDto.

        仓库角色名称

        :param repository_role_name: The repository_role_name of this RepositoryMemberDto.
        :type repository_role_name: str
        """
        self._repository_role_name = repository_role_name

    @property
    def repository_role_id(self):
        r"""Gets the repository_role_id of this RepositoryMemberDto.

        仓库角色id

        :return: The repository_role_id of this RepositoryMemberDto.
        :rtype: str
        """
        return self._repository_role_id

    @repository_role_id.setter
    def repository_role_id(self, repository_role_id):
        r"""Sets the repository_role_id of this RepositoryMemberDto.

        仓库角色id

        :param repository_role_id: The repository_role_id of this RepositoryMemberDto.
        :type repository_role_id: str
        """
        self._repository_role_id = repository_role_id

    @property
    def member_source(self):
        r"""Gets the member_source of this RepositoryMemberDto.

        成员如果来自成员组，成员组名称

        :return: The member_source of this RepositoryMemberDto.
        :rtype: str
        """
        return self._member_source

    @member_source.setter
    def member_source(self, member_source):
        r"""Sets the member_source of this RepositoryMemberDto.

        成员如果来自成员组，成员组名称

        :param member_source: The member_source of this RepositoryMemberDto.
        :type member_source: str
        """
        self._member_source = member_source

    @property
    def member_group_source(self):
        r"""Gets the member_group_source of this RepositoryMemberDto.

        成员如果来自上层代码组，代码组名称

        :return: The member_group_source of this RepositoryMemberDto.
        :rtype: str
        """
        return self._member_group_source

    @member_group_source.setter
    def member_group_source(self, member_group_source):
        r"""Sets the member_group_source of this RepositoryMemberDto.

        成员如果来自上层代码组，代码组名称

        :param member_group_source: The member_group_source of this RepositoryMemberDto.
        :type member_group_source: str
        """
        self._member_group_source = member_group_source

    @property
    def member_source_id(self):
        r"""Gets the member_source_id of this RepositoryMemberDto.

        成员来源id —— 代码组id或者成员组id

        :return: The member_source_id of this RepositoryMemberDto.
        :rtype: str
        """
        return self._member_source_id

    @member_source_id.setter
    def member_source_id(self, member_source_id):
        r"""Sets the member_source_id of this RepositoryMemberDto.

        成员来源id —— 代码组id或者成员组id

        :param member_source_id: The member_source_id of this RepositoryMemberDto.
        :type member_source_id: str
        """
        self._member_source_id = member_source_id

    @property
    def service_license_status(self):
        r"""Gets the service_license_status of this RepositoryMemberDto.

        成员服务级权限状态： 1-使用中、0-已停用

        :return: The service_license_status of this RepositoryMemberDto.
        :rtype: int
        """
        return self._service_license_status

    @service_license_status.setter
    def service_license_status(self, service_license_status):
        r"""Sets the service_license_status of this RepositoryMemberDto.

        成员服务级权限状态： 1-使用中、0-已停用

        :param service_license_status: The service_license_status of this RepositoryMemberDto.
        :type service_license_status: int
        """
        self._service_license_status = service_license_status

    @property
    def action_enabled(self):
        r"""Gets the action_enabled of this RepositoryMemberDto.

        是否有对应权限： true-有权限、false-无权限

        :return: The action_enabled of this RepositoryMemberDto.
        :rtype: bool
        """
        return self._action_enabled

    @action_enabled.setter
    def action_enabled(self, action_enabled):
        r"""Sets the action_enabled of this RepositoryMemberDto.

        是否有对应权限： true-有权限、false-无权限

        :param action_enabled: The action_enabled of this RepositoryMemberDto.
        :type action_enabled: bool
        """
        self._action_enabled = action_enabled

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
        if not isinstance(other, RepositoryMemberDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
