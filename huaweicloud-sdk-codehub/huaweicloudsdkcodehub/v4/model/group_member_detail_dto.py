# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupMemberDetailDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'source_id': 'int',
        'user_id': 'int',
        'user_from': 'str',
        'role_id': 'str',
        'role_name': 'str',
        'cn_role_name': 'str',
        'req_role_id': 'str',
        'req_role_name': 'str',
        'user_group_id': 'str',
        'group_name': 'str',
        'user_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'nick_name': 'str',
        'is_group_creator': 'bool',
        'is_project_admin': 'bool',
        'path': 'str',
        'role_chinese_name': 'str',
        'can_remove': 'bool',
        'access_level': 'int',
        'service_license_status': 'int',
        'iam_id': 'str',
        'current_group_member': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'source_id': 'source_id',
        'user_id': 'user_id',
        'user_from': 'user_from',
        'role_id': 'role_id',
        'role_name': 'role_name',
        'cn_role_name': 'cn_role_name',
        'req_role_id': 'req_role_id',
        'req_role_name': 'req_role_name',
        'user_group_id': 'user_group_id',
        'group_name': 'group_name',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'nick_name': 'nick_name',
        'is_group_creator': 'is_group_creator',
        'is_project_admin': 'is_project_admin',
        'path': 'path',
        'role_chinese_name': 'role_chinese_name',
        'can_remove': 'can_remove',
        'access_level': 'access_level',
        'service_license_status': 'service_license_status',
        'iam_id': 'iam_id',
        'current_group_member': 'current_group_member'
    }

    def __init__(self, id=None, source_id=None, user_id=None, user_from=None, role_id=None, role_name=None, cn_role_name=None, req_role_id=None, req_role_name=None, user_group_id=None, group_name=None, user_name=None, domain_id=None, domain_name=None, nick_name=None, is_group_creator=None, is_project_admin=None, path=None, role_chinese_name=None, can_remove=None, access_level=None, service_license_status=None, iam_id=None, current_group_member=None):
        r"""GroupMemberDetailDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 唯一标识id。
        :type id: int
        :param source_id: **参数解释：** 资源id。
        :type source_id: int
        :param user_id: **参数解释：** 用户id。
        :type user_id: int
        :param user_from: **参数解释：** 用户来源。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type user_from: str
        :param role_id: **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_id: str
        :param role_name: **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_name: str
        :param cn_role_name: **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type cn_role_name: str
        :param req_role_id: **参数解释：** 项目角色id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type req_role_id: str
        :param req_role_name: **参数解释：** 项目角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type req_role_name: str
        :param user_group_id: **参数解释：** 成员组id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type user_group_id: str
        :param group_name: **参数解释：** 代码组名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type group_name: str
        :param user_name: **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type user_name: str
        :param domain_id: **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type domain_id: str
        :param domain_name: **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type domain_name: str
        :param nick_name: **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type nick_name: str
        :param is_group_creator: **参数解释：** 是否为代码组创建者。
        :type is_group_creator: bool
        :param is_project_admin: **参数解释：** 是否为项目管理员。
        :type is_project_admin: bool
        :param path: **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type path: str
        :param role_chinese_name: **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_chinese_name: str
        :param can_remove: **参数解释：** 是否可移除。
        :type can_remove: bool
        :param access_level: **参数解释：** 角色。
        :type access_level: int
        :param service_license_status: **参数解释：** 服务license状态。
        :type service_license_status: int
        :param iam_id: **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type iam_id: str
        :param current_group_member: **参数解释：** 是否为当前代码组成员。
        :type current_group_member: bool
        """
        
        

        self._id = None
        self._source_id = None
        self._user_id = None
        self._user_from = None
        self._role_id = None
        self._role_name = None
        self._cn_role_name = None
        self._req_role_id = None
        self._req_role_name = None
        self._user_group_id = None
        self._group_name = None
        self._user_name = None
        self._domain_id = None
        self._domain_name = None
        self._nick_name = None
        self._is_group_creator = None
        self._is_project_admin = None
        self._path = None
        self._role_chinese_name = None
        self._can_remove = None
        self._access_level = None
        self._service_license_status = None
        self._iam_id = None
        self._current_group_member = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source_id is not None:
            self.source_id = source_id
        if user_id is not None:
            self.user_id = user_id
        if user_from is not None:
            self.user_from = user_from
        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name
        if cn_role_name is not None:
            self.cn_role_name = cn_role_name
        if req_role_id is not None:
            self.req_role_id = req_role_id
        if req_role_name is not None:
            self.req_role_name = req_role_name
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if group_name is not None:
            self.group_name = group_name
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if nick_name is not None:
            self.nick_name = nick_name
        if is_group_creator is not None:
            self.is_group_creator = is_group_creator
        if is_project_admin is not None:
            self.is_project_admin = is_project_admin
        if path is not None:
            self.path = path
        if role_chinese_name is not None:
            self.role_chinese_name = role_chinese_name
        if can_remove is not None:
            self.can_remove = can_remove
        if access_level is not None:
            self.access_level = access_level
        if service_license_status is not None:
            self.service_license_status = service_license_status
        if iam_id is not None:
            self.iam_id = iam_id
        if current_group_member is not None:
            self.current_group_member = current_group_member

    @property
    def id(self):
        r"""Gets the id of this GroupMemberDetailDto.

        **参数解释：** 唯一标识id。

        :return: The id of this GroupMemberDetailDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupMemberDetailDto.

        **参数解释：** 唯一标识id。

        :param id: The id of this GroupMemberDetailDto.
        :type id: int
        """
        self._id = id

    @property
    def source_id(self):
        r"""Gets the source_id of this GroupMemberDetailDto.

        **参数解释：** 资源id。

        :return: The source_id of this GroupMemberDetailDto.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this GroupMemberDetailDto.

        **参数解释：** 资源id。

        :param source_id: The source_id of this GroupMemberDetailDto.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def user_id(self):
        r"""Gets the user_id of this GroupMemberDetailDto.

        **参数解释：** 用户id。

        :return: The user_id of this GroupMemberDetailDto.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this GroupMemberDetailDto.

        **参数解释：** 用户id。

        :param user_id: The user_id of this GroupMemberDetailDto.
        :type user_id: int
        """
        self._user_id = user_id

    @property
    def user_from(self):
        r"""Gets the user_from of this GroupMemberDetailDto.

        **参数解释：** 用户来源。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The user_from of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._user_from

    @user_from.setter
    def user_from(self, user_from):
        r"""Sets the user_from of this GroupMemberDetailDto.

        **参数解释：** 用户来源。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param user_from: The user_from of this GroupMemberDetailDto.
        :type user_from: str
        """
        self._user_from = user_from

    @property
    def role_id(self):
        r"""Gets the role_id of this GroupMemberDetailDto.

        **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_id of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this GroupMemberDetailDto.

        **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_id: The role_id of this GroupMemberDetailDto.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this GroupMemberDetailDto.

        **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_name of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this GroupMemberDetailDto.

        **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_name: The role_name of this GroupMemberDetailDto.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def cn_role_name(self):
        r"""Gets the cn_role_name of this GroupMemberDetailDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The cn_role_name of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._cn_role_name

    @cn_role_name.setter
    def cn_role_name(self, cn_role_name):
        r"""Sets the cn_role_name of this GroupMemberDetailDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param cn_role_name: The cn_role_name of this GroupMemberDetailDto.
        :type cn_role_name: str
        """
        self._cn_role_name = cn_role_name

    @property
    def req_role_id(self):
        r"""Gets the req_role_id of this GroupMemberDetailDto.

        **参数解释：** 项目角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The req_role_id of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._req_role_id

    @req_role_id.setter
    def req_role_id(self, req_role_id):
        r"""Sets the req_role_id of this GroupMemberDetailDto.

        **参数解释：** 项目角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param req_role_id: The req_role_id of this GroupMemberDetailDto.
        :type req_role_id: str
        """
        self._req_role_id = req_role_id

    @property
    def req_role_name(self):
        r"""Gets the req_role_name of this GroupMemberDetailDto.

        **参数解释：** 项目角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The req_role_name of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._req_role_name

    @req_role_name.setter
    def req_role_name(self, req_role_name):
        r"""Sets the req_role_name of this GroupMemberDetailDto.

        **参数解释：** 项目角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param req_role_name: The req_role_name of this GroupMemberDetailDto.
        :type req_role_name: str
        """
        self._req_role_name = req_role_name

    @property
    def user_group_id(self):
        r"""Gets the user_group_id of this GroupMemberDetailDto.

        **参数解释：** 成员组id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The user_group_id of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        r"""Sets the user_group_id of this GroupMemberDetailDto.

        **参数解释：** 成员组id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param user_group_id: The user_group_id of this GroupMemberDetailDto.
        :type user_group_id: str
        """
        self._user_group_id = user_group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this GroupMemberDetailDto.

        **参数解释：** 代码组名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The group_name of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this GroupMemberDetailDto.

        **参数解释：** 代码组名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param group_name: The group_name of this GroupMemberDetailDto.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def user_name(self):
        r"""Gets the user_name of this GroupMemberDetailDto.

        **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The user_name of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this GroupMemberDetailDto.

        **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param user_name: The user_name of this GroupMemberDetailDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this GroupMemberDetailDto.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The domain_id of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this GroupMemberDetailDto.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param domain_id: The domain_id of this GroupMemberDetailDto.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this GroupMemberDetailDto.

        **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The domain_name of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this GroupMemberDetailDto.

        **参数解释：** 租户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param domain_name: The domain_name of this GroupMemberDetailDto.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this GroupMemberDetailDto.

        **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The nick_name of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this GroupMemberDetailDto.

        **参数解释：** 用户昵称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param nick_name: The nick_name of this GroupMemberDetailDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def is_group_creator(self):
        r"""Gets the is_group_creator of this GroupMemberDetailDto.

        **参数解释：** 是否为代码组创建者。

        :return: The is_group_creator of this GroupMemberDetailDto.
        :rtype: bool
        """
        return self._is_group_creator

    @is_group_creator.setter
    def is_group_creator(self, is_group_creator):
        r"""Sets the is_group_creator of this GroupMemberDetailDto.

        **参数解释：** 是否为代码组创建者。

        :param is_group_creator: The is_group_creator of this GroupMemberDetailDto.
        :type is_group_creator: bool
        """
        self._is_group_creator = is_group_creator

    @property
    def is_project_admin(self):
        r"""Gets the is_project_admin of this GroupMemberDetailDto.

        **参数解释：** 是否为项目管理员。

        :return: The is_project_admin of this GroupMemberDetailDto.
        :rtype: bool
        """
        return self._is_project_admin

    @is_project_admin.setter
    def is_project_admin(self, is_project_admin):
        r"""Sets the is_project_admin of this GroupMemberDetailDto.

        **参数解释：** 是否为项目管理员。

        :param is_project_admin: The is_project_admin of this GroupMemberDetailDto.
        :type is_project_admin: bool
        """
        self._is_project_admin = is_project_admin

    @property
    def path(self):
        r"""Gets the path of this GroupMemberDetailDto.

        **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The path of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this GroupMemberDetailDto.

        **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param path: The path of this GroupMemberDetailDto.
        :type path: str
        """
        self._path = path

    @property
    def role_chinese_name(self):
        r"""Gets the role_chinese_name of this GroupMemberDetailDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_chinese_name of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._role_chinese_name

    @role_chinese_name.setter
    def role_chinese_name(self, role_chinese_name):
        r"""Sets the role_chinese_name of this GroupMemberDetailDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_chinese_name: The role_chinese_name of this GroupMemberDetailDto.
        :type role_chinese_name: str
        """
        self._role_chinese_name = role_chinese_name

    @property
    def can_remove(self):
        r"""Gets the can_remove of this GroupMemberDetailDto.

        **参数解释：** 是否可移除。

        :return: The can_remove of this GroupMemberDetailDto.
        :rtype: bool
        """
        return self._can_remove

    @can_remove.setter
    def can_remove(self, can_remove):
        r"""Sets the can_remove of this GroupMemberDetailDto.

        **参数解释：** 是否可移除。

        :param can_remove: The can_remove of this GroupMemberDetailDto.
        :type can_remove: bool
        """
        self._can_remove = can_remove

    @property
    def access_level(self):
        r"""Gets the access_level of this GroupMemberDetailDto.

        **参数解释：** 角色。

        :return: The access_level of this GroupMemberDetailDto.
        :rtype: int
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        r"""Sets the access_level of this GroupMemberDetailDto.

        **参数解释：** 角色。

        :param access_level: The access_level of this GroupMemberDetailDto.
        :type access_level: int
        """
        self._access_level = access_level

    @property
    def service_license_status(self):
        r"""Gets the service_license_status of this GroupMemberDetailDto.

        **参数解释：** 服务license状态。

        :return: The service_license_status of this GroupMemberDetailDto.
        :rtype: int
        """
        return self._service_license_status

    @service_license_status.setter
    def service_license_status(self, service_license_status):
        r"""Sets the service_license_status of this GroupMemberDetailDto.

        **参数解释：** 服务license状态。

        :param service_license_status: The service_license_status of this GroupMemberDetailDto.
        :type service_license_status: int
        """
        self._service_license_status = service_license_status

    @property
    def iam_id(self):
        r"""Gets the iam_id of this GroupMemberDetailDto.

        **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The iam_id of this GroupMemberDetailDto.
        :rtype: str
        """
        return self._iam_id

    @iam_id.setter
    def iam_id(self, iam_id):
        r"""Sets the iam_id of this GroupMemberDetailDto.

        **参数解释：** 用户iam_id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param iam_id: The iam_id of this GroupMemberDetailDto.
        :type iam_id: str
        """
        self._iam_id = iam_id

    @property
    def current_group_member(self):
        r"""Gets the current_group_member of this GroupMemberDetailDto.

        **参数解释：** 是否为当前代码组成员。

        :return: The current_group_member of this GroupMemberDetailDto.
        :rtype: bool
        """
        return self._current_group_member

    @current_group_member.setter
    def current_group_member(self, current_group_member):
        r"""Sets the current_group_member of this GroupMemberDetailDto.

        **参数解释：** 是否为当前代码组成员。

        :param current_group_member: The current_group_member of this GroupMemberDetailDto.
        :type current_group_member: bool
        """
        self._current_group_member = current_group_member

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
        if not isinstance(other, GroupMemberDetailDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
